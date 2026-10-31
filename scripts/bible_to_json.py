#!/usr/bin/env python3
"""Convert docs/bible/m00.md .. m13.md into episodes/ep001.json .. ep086.json.

See docs/PIPELINE.md for the pipeline this is part of. Design notes and the
known Bible-format inconsistencies this parser works around are documented in
the PR description for the feat/episode-data branch; the short version:

- The Bible is markdown exported from a doc: backslash-escaped punctuation
  outside code blocks (\\[ \\] \\* \\_ \\\\ \\| etc.), verbatim inside them.
- Two "Code shown" multi-file formats exist ("File 1: `x.c`" and
  "File 1, x.c:"); both are accepted.
- A handful of sections don't fit the strict schema (module 12's "Move
  trace", the two renamed "Step trace" variants, "How the timings are
  measured"); these are left unparsed and noted as warnings, not guessed at.
- Two scenes use "Challenge + Outro" as a combined Template value; mapped to
  "outro" with a reported warning rather than inventing an 11th enum value.

This script never edits docs/ or episodes/ to make validation pass — it
reports every anomaly it finds instead. Run twice to confirm it's idempotent.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIBLE_DIR = ROOT / "docs" / "bible"
EPISODES_DIR = ROOT / "episodes"
SFX_DIR = ROOT / "audio" / "sfx"

EM_DASH = "\u2014"
EN_DASH = "\u2013"
MID_DOT = "\u00b7"

# ---------------------------------------------------------------------------
# Warnings collection: every anomaly gets reported here instead of fixed.
# ---------------------------------------------------------------------------


@dataclass
class Warnings:
    items: list[str] = field(default_factory=list)

    def add(self, episode: str, message: str) -> None:
        self.items.append(f"EP{episode}: {message}")


# ---------------------------------------------------------------------------
# Escaping: un-escape backslash-escaped punctuation in prose/tables, but
# never touch text inside fenced ``` code blocks.
# ---------------------------------------------------------------------------

_ESCAPABLE = r"\\`*_{}\[\]()#+\-.!|<>~^$%&@:;,/?'\"="
_ESCAPE_RE = re.compile(r"\\([" + _ESCAPABLE + r"])")
_FENCE_RE = re.compile(r"```[a-zA-Z]*\n.*?\n```", re.DOTALL)


def unescape_prose(text: str) -> str:
    """Un-escapes backslash-escaped markdown punctuation."""
    return _ESCAPE_RE.sub(r"\1", text)


def split_code_fences(text: str) -> list[tuple[bool, str]]:
    """Splits text into (is_code, chunk) pieces at ``` fences. Fence chunks
    include their backtick lines; prose chunks are everything between."""
    pieces: list[tuple[bool, str]] = []
    pos = 0
    for m in _FENCE_RE.finditer(text):
        if m.start() > pos:
            pieces.append((False, text[pos : m.start()]))
        pieces.append((True, m.group(0)))
        pos = m.end()
    if pos < len(text):
        pieces.append((False, text[pos:]))
    return pieces


def unescape_outside_code(text: str) -> str:
    """Un-escapes prose/table text but leaves fenced code blocks verbatim."""
    return "".join(
        chunk if is_code else unescape_prose(chunk) for is_code, chunk in split_code_fences(text)
    )


# ---------------------------------------------------------------------------
# Splitting a module file into episodes, and an episode into named sections.
# ---------------------------------------------------------------------------

_EPISODE_HEADER_RE = re.compile(
    r"^## EP (\d+)\s*[" + EM_DASH + r"\-]{1,2}\s*(.+?)\s*$", re.MULTILINE
)
_SECTION_HEADER_RE = re.compile(r"^### (.+?)\s*$", re.MULTILINE)


@dataclass
class RawEpisode:
    ep: int
    title: str
    preamble: str
    sections: dict[str, str]  # section heading text -> body (first match wins per heading text)
    source_file: str


def split_module_into_episodes(text: str, source_file: str, warnings: Warnings) -> list[RawEpisode]:
    headers = list(_EPISODE_HEADER_RE.finditer(text))
    episodes: list[RawEpisode] = []
    for i, m in enumerate(headers):
        ep = int(m.group(1))
        title = m.group(2).strip()
        if m.group(0).count(EM_DASH) == 0:
            warnings.add(f"{ep:02d}", f"episode header in {source_file} does not use an em dash: {m.group(0)!r}")
        body_start = m.end()
        body_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[body_start:body_end]
        preamble, sections = split_episode_body(body)
        episodes.append(
            RawEpisode(ep=ep, title=title, preamble=preamble, sections=sections, source_file=source_file)
        )
    return episodes


def split_episode_body(body: str) -> tuple[str, dict[str, str]]:
    """Splits one episode's body into (preamble, {section_heading: section_body})."""
    headers = list(_SECTION_HEADER_RE.finditer(body))
    preamble = body[: headers[0].start()] if headers else body
    sections: dict[str, str] = {}
    for i, m in enumerate(headers):
        heading = m.group(1).strip()
        start = m.end()
        end = headers[i + 1].start() if i + 1 < len(headers) else len(body)
        section_body = body[start:end]
        if heading in sections:
            # Duplicate heading text (shouldn't happen per-episode); keep both, concatenated.
            sections[heading] += "\n" + section_body
        else:
            sections[heading] = section_body
    return preamble, sections


def find_section(sections: dict[str, str], prefix: str) -> tuple[str, str] | None:
    """Finds a section whose heading starts with `prefix` (handles renamed
    variants like 'Step trace: scorecard on...'). Returns (heading, body)."""
    for heading, body in sections.items():
        if heading == prefix or heading.startswith(prefix + ":") or heading.startswith(prefix + " "):
            return heading, body
    return None


# ---------------------------------------------------------------------------
# Preamble: the bold "**Module X . Name . m:ss . Background + Accent .
# Prerequisite: ...**" line, and "**Learning goals:** ...".
# ---------------------------------------------------------------------------

_MODULE_LINE_RE = re.compile(
    r"\*\*Module (\d+)\s*"
    + MID_DOT
    + r"\s*(.+?)\s*"
    + MID_DOT
    + r"\s*(\d+):(\d{2})\s*"
    + MID_DOT
    + r"\s*(.+?)\s*"
    + MID_DOT
    + r"\s*Prerequisite:\s*(.+?)\*\*"
)
_LEARNING_GOALS_RE = re.compile(r"\*\*Learning goals:\*\*\s*(.+?)(?:\n\n|\Z)", re.DOTALL)


@dataclass
class Preamble:
    module: int
    module_name: str
    length_sec: int
    colours_text: str
    prerequisite: str
    learning_goals: list[str]


def parse_preamble(preamble_text: str, ep: str, warnings: Warnings) -> Preamble | None:
    text = unescape_outside_code(preamble_text)
    m = _MODULE_LINE_RE.search(text)
    if not m:
        warnings.add(ep, f"could not parse Module line: {preamble_text[:120]!r}")
        return None
    module = int(m.group(1))
    module_name = m.group(2)
    length_sec = int(m.group(3)) * 60 + int(m.group(4))
    colours_text = m.group(5)
    prerequisite = m.group(6)

    goals_match = _LEARNING_GOALS_RE.search(text)
    if not goals_match:
        warnings.add(ep, "could not find Learning goals line")
        learning_goals: list[str] = []
    else:
        raw = goals_match.group(1).strip().rstrip(".")
        learning_goals = [g.strip() for g in raw.split(";") if g.strip()]

    return Preamble(
        module=module,
        module_name=module_name,
        length_sec=length_sec,
        colours_text=colours_text,
        prerequisite=prerequisite,
        learning_goals=learning_goals,
    )


# ---------------------------------------------------------------------------
# ### YouTube: - **Title:** / **Description:** / **Tags:** / **Thumbnail:**
# ---------------------------------------------------------------------------

_YOUTUBE_BULLET_RE = re.compile(
    r"^-\s+\*\*(Title|Description|Tags|Thumbnail):\*\*\s*(.+?)\s*$", re.MULTILINE
)
_CHAPTER_RE = re.compile(r"(\d{1,2}:\d{2})\s+(.+?)(?=\s*" + MID_DOT + r"\s*\d{1,2}:\d{2}|\s*$)")
_QUOTED_RE = re.compile(r'"([^"]+)"')


def parse_youtube(section_text: str, ep: str, warnings: Warnings) -> dict:
    text = unescape_outside_code(section_text)
    bullets = {m.group(1): m.group(2) for m in _YOUTUBE_BULLET_RE.finditer(text)}

    for required in ("Title", "Description", "Tags", "Thumbnail"):
        if required not in bullets:
            warnings.add(ep, f"### YouTube missing bullet: {required}")

    title = bullets.get("Title", "")
    description = bullets.get("Description", "")
    tags_raw = bullets.get("Tags", "")
    tags = [t.strip() for t in tags_raw.split(",") if t.strip()]

    chapters = [{"t": m.group(1), "label": m.group(2).strip()} for m in _CHAPTER_RE.finditer(description)]
    if not chapters:
        warnings.add(ep, "no chapter timestamps found in Description")

    thumbnail_raw = bullets.get("Thumbnail", "")
    quoted = _QUOTED_RE.findall(thumbnail_raw)
    thumb_text = quoted[0] if quoted else ""
    if not quoted:
        warnings.add(ep, "Thumbnail bullet has no quoted text for thumbnail.text")
    pose_match = re.search(r"Xecxec[^;.]*", thumbnail_raw)
    thumb_pose = pose_match.group(0).strip() if pose_match else ""
    if not pose_match:
        warnings.add(ep, "Thumbnail bullet mentions no Xecxec pose")

    return {
        "title": title,
        "description": description,
        "chapters": chapters,
        "tags": tags,
        "thumbnail": {"text": thumb_text, "visual": thumbnail_raw, "pose": thumb_pose},
    }


# ---------------------------------------------------------------------------
# Generic markdown table parser: header row, separator row, data rows.
# Handles `\|` as a literal pipe inside a cell.
# ---------------------------------------------------------------------------

_SEPARATOR_CELL_RE = re.compile(r"^:?-+:?$")


def split_table_row(line: str) -> list[str]:
    """Splits one `| a | b |` row into cells, honouring `\\|` as a literal pipe."""
    body = line.strip()
    if body.startswith("|"):
        body = body[1:]
    if body.endswith("|"):
        body = body[:-1]
    # Split on unescaped pipes only.
    cells: list[str] = []
    current = ""
    i = 0
    while i < len(body):
        if body[i] == "\\" and i + 1 < len(body) and body[i + 1] == "|":
            current += "|"
            i += 2
            continue
        if body[i] == "|":
            cells.append(current.strip())
            current = ""
            i += 1
            continue
        current += body[i]
        i += 1
    cells.append(current.strip())
    return cells


def parse_markdown_table(text: str) -> list[dict[str, str]]:
    """Parses the first markdown table in `text` into a list of {header: cell} dicts."""
    lines = [line for line in text.splitlines() if line.strip().startswith("|")]
    if len(lines) < 2:
        return []
    header = split_table_row(lines[0])
    separator_cells = split_table_row(lines[1])
    data_start = 1
    if all(_SEPARATOR_CELL_RE.match(c) for c in separator_cells if c):
        data_start = 2
    rows: list[dict[str, str]] = []
    for line in lines[data_start:]:
        cells = split_table_row(line)
        row = {header[i]: (cells[i] if i < len(cells) else "") for i in range(len(header))}
        rows.append(row)
    return rows


# ---------------------------------------------------------------------------
# ### Scene list
# ---------------------------------------------------------------------------


def parse_timecode(text: str) -> int | None:
    m = re.match(r"^(\d+):(\d{2})$", text.strip())
    if not m:
        return None
    return int(m.group(1)) * 60 + int(m.group(2))


SFX_NAMES = sorted(p.stem for p in SFX_DIR.glob("*.wav") if not p.stem.startswith("placeholder-"))
_SFX_PATTERNS = [(name, re.compile(re.escape(name).replace(r"\-", r"[\s-]"), re.IGNORECASE)) for name in SFX_NAMES]

_COMBINED_TEMPLATE_MAP = {
    # Non-canonical Template cell values -> Bible-style template name (not the
    # final slug — assemble_episode() does that mapping uniformly), reported not silent.
    "Challenge + Outro": "Outro",
}


def extract_sfx(animation_text: str) -> list[str]:
    found = []
    for name, pattern in _SFX_PATTERNS:
        if pattern.search(animation_text):
            found.append(name)
    return found


def parse_scene_list(section_text: str, ep: str, warnings: Warnings) -> list[dict]:
    text = unescape_outside_code(section_text)
    rows = parse_markdown_table(text)
    scenes = []
    for row in rows:
        try:
            scene_id = int(row.get("#", "").strip())
        except ValueError:
            warnings.add(ep, f"Scene list row has non-numeric # column: {row!r}")
            continue
        start_text = row.get("Start", "")
        length_text = row.get("Length", "")
        start_sec = parse_timecode(start_text)
        length_sec = parse_timecode(length_text)
        if start_sec is None:
            warnings.add(ep, f"scene {scene_id}: could not parse Start {start_text!r}")
            start_sec = 0
        if length_sec is None:
            warnings.add(ep, f"scene {scene_id}: could not parse Length {length_text!r}")
            length_sec = 0

        template_raw = row.get("Template", "").strip()
        template = None
        if template_raw in _COMBINED_TEMPLATE_MAP:
            warnings.add(
                ep,
                f"scene {scene_id}: non-standard combined Template {template_raw!r}, "
                f"mapped to {_COMBINED_TEMPLATE_MAP[template_raw]!r}",
            )
            template_raw = _COMBINED_TEMPLATE_MAP[template_raw]
        template = template_raw

        on_screen = row.get("On screen", "")
        animation = row.get("Animation & SFX", "")
        sfx = extract_sfx(animation)

        scenes.append(
            {
                "id": scene_id,
                "template_raw": template,
                "startSec": start_sec,
                "lengthSec": length_sec,
                "onScreen": on_screen,
                "animation": animation,
                "sfx": sfx,
            }
        )
    return scenes


# ---------------------------------------------------------------------------
# ### Narration script: paragraphs "**[N . Name]** text", cues like [HL 4]
# and [TRACK age=19] stay inline (they're already unescaped by this point).
# ---------------------------------------------------------------------------

_NARRATION_PARA_RE = re.compile(
    r"\*\*\[(\d+)\s*" + MID_DOT + r"\s*(.+?)\]\*\*\s*(.+?)(?=\n\n\*\*\[|\Z)", re.DOTALL
)


def parse_narration(section_text: str, ep: str, scene_ids: list[int], warnings: Warnings) -> dict[int, str]:
    text = unescape_outside_code(section_text)
    by_scene: dict[int, str] = {}
    matched_ids = set()
    for m in _NARRATION_PARA_RE.finditer(text):
        n = int(m.group(1))
        narration = " ".join(m.group(3).split())
        if n in by_scene:
            warnings.add(ep, f"duplicate narration paragraph for scene {n}")
        by_scene[n] = narration
        matched_ids.add(n)

    for scene_id in scene_ids:
        if scene_id not in matched_ids:
            warnings.add(ep, f"scene {scene_id} has no matching narration paragraph")
    for n in matched_ids:
        if n not in scene_ids:
            warnings.add(ep, f"narration paragraph [{n}] does not match any scene id")

    return by_scene


# ---------------------------------------------------------------------------
# ### Code shown: one block, or several files announced as
# "File 1: `name.c`" / "File 1, name.c:" (optionally "(scene N)"), each
# followed by its ```c block and an optional output block.
# ---------------------------------------------------------------------------

_FENCE_CONTENT_RE = re.compile(r"```([a-zA-Z]*)\n(.*?)\n```", re.DOTALL)
_FILE_ANNOUNCE_RE = re.compile(
    r"\*{0,2}File (\d+)[,:]\s*`?([\w./]+\.\w+)`?\*{0,2}"
    r"\s*(?:\((?:scene[s]?\s*([\d,\- ]+)|[^)]*)\))?\s*:?\s*$",
    re.MULTILINE,
)
# Bare-filename announcement, e.g. a paragraph that is just "sort.h" (EP82's format).
_BARE_FILENAME_RE = re.compile(r"^\s*`?([\w./]+\.\w+)`?\s*$")
# Last-resort: any filename-shaped token in a short free-text label (EP06's format).
_LOOSE_FILENAME_RE = re.compile(r"\b([A-Za-z_][\w]*\.(?:c|h|cpp|txt))\b")
_INPUT_NOTE_RE = re.compile(r"(?:run with input|Input:|stdin:)\s*([^.\n)]+)", re.IGNORECASE)


def fence_content(fence_chunk: str) -> tuple[str, str]:
    m = _FENCE_CONTENT_RE.match(fence_chunk.strip())
    if not m:
        return "", fence_chunk
    return m.group(1), m.group(2)


@dataclass
class CodeFile:
    file: str
    source: str
    output: str | None = None
    stdin: str | None = None
    build_step: str | None = None
    lang: str = "c"


def parse_code_shown(section_text: str, ep: str, warnings: Warnings) -> list[CodeFile]:
    chunks = split_code_fences(section_text)
    files: list[CodeFile] = []
    pending_name: str | None = None
    pending_stdin: str | None = None
    pending_is_expected_output = False
    current: CodeFile | None = None
    unlabeled_index = 0

    for is_code, raw in chunks:
        if not is_code:
            prose = unescape_outside_code(raw)
            announce = _FILE_ANNOUNCE_RE.search(prose)
            if announce:
                pending_name = announce.group(2)
            else:
                bare = _BARE_FILENAME_RE.match(prose.strip())
                if bare:
                    pending_name = bare.group(1)
                elif len(prose.strip()) < 200:
                    # Free-text label format ("Clean version, fish_board.c (scenes 3-5, 8):")
                    # with no "File N" prefix — take the last filename-shaped token.
                    loose = _LOOSE_FILENAME_RE.findall(prose)
                    if loose:
                        pending_name = loose[-1]
            input_m = _INPUT_NOTE_RE.search(prose)
            if input_m:
                pending_stdin = input_m.group(1).strip().rstrip(",;")
            if re.search(r"expected output", prose, re.IGNORECASE):
                pending_is_expected_output = True
            continue

        lang, content = fence_content(raw)
        if lang in ("c", "cpp", ""):
            unlabeled_index += 1
            name = pending_name or f"file{unlabeled_index}.{lang or 'c'}"
            current = CodeFile(file=name, source=content, stdin=pending_stdin, lang=lang or "c")
            files.append(current)
            pending_name = None
            pending_stdin = None
            pending_is_expected_output = False
        elif lang in ("text", "console", "output"):
            # A filename announcement right before a text block (e.g.
            # "Contents of `diary.txt`:") describes that text block, not
            # some later code block — a stray pending_name must not survive
            # past it, or it'll wrongly attach to the next real .c file.
            is_file_contents_label = pending_name is not None
            if current is not None and not is_file_contents_label and (current.output is None or pending_is_expected_output):
                # The first text block after a file's code is assumed to be
                # its real output, UNLESS a later block is explicitly
                # labelled "Expected output:" (e.g. a GCC-warning aside
                # shown first, then the real output) — that label always wins.
                current.output = content
            pending_is_expected_output = False
            pending_name = None
            pending_stdin = None
            # A bare text/output block before any code (e.g. EP03's terminal
            # walkthrough of installing gcc) is a legitimate standalone
            # example, not an error — nothing to attach it to, so it's just
            # not captured as a CodeFile's output.
        elif lang == "bash":
            if current is not None:
                current.build_step = content
            pending_name = None
            pending_stdin = None
            # Same as above: a standalone shell command (e.g. "pacman -S ...")
            # with no preceding code block is expected in setup-style episodes.
        else:
            warnings.add(ep, f"Code shown: unrecognised fence language {lang!r}")

    if not files:
        warnings.add(ep, "### Code shown has no code blocks (expected for a setup/non-coding episode; verify by hand)")
    for f in files:
        # A file without main() is a support TU (e.g. shapes.c implementing
        # shapes.h) and is never expected to show its own output.
        if f.output is None and "main(" in f.source:
            warnings.add(ep, f"{f.file}: no Expected output block found")

    return files


# ---------------------------------------------------------------------------
# ### Bug of the Day: wrong code, the GCC/behaviour explanation (a text
# block, prose, or both), the fix, and a Why sentence. The exact shape varies
# a lot across episodes (plain compile errors, prose-only "it compiles but
# misbehaves" bugs, even non-code "wrong idea" bugs), so this scans content
# rather than assuming a fixed block sequence.
# ---------------------------------------------------------------------------

_FIXED_MARKER_RE = re.compile(r"\bfix(?:ed)?\b", re.IGNORECASE)
# The actual "Fixed:" label starting a paragraph/sentence (not just the word
# "fix" appearing inside a longer explanation) — used to split a prose chunk
# that contains both error-description text and this marker together.
_FIXED_LABEL_SPLIT_RE = re.compile(
    r"(?:^|\n\n)\s*\*{0,2}Fix(?:ed)?(?: code| inner loop| it)?\*{0,2}[^.\n]{0,60}:\s*", re.IGNORECASE
)
_WHY_RE = re.compile(r"\*{0,2}Why:\*{0,2}\s*(.+?)\s*(?:\n\n|\Z)", re.DOTALL)


@dataclass
class Bug:
    wrong: str
    error: str
    fixed: str
    why: str
    fixed_output: str | None = None
    wrong_lang: str = "c"
    fixed_has_full_program: bool = True


def parse_bug(section_text: str, ep: str, warnings: Warnings) -> Bug | None:
    chunks = split_code_fences(section_text)

    why_match = _WHY_RE.search(unescape_outside_code(section_text))
    why = " ".join(why_match.group(1).split()) if why_match else ""
    why_was_labelled = bool(why)

    wrong: str | None = None
    wrong_lang = "c"
    error_parts: list[str] = []
    fixed: str | None = None
    fixed_output: str | None = None
    seen_fixed_marker = False
    seen_wrong_code = False
    last_prose = ""
    first_text_block: str | None = None

    for is_code, raw in chunks:
        if not is_code:
            prose = unescape_outside_code(raw)
            # Strip the Why sentence out of whatever prose chunk it's in, so
            # it doesn't also get folded into `error`.
            prose_sans_why = _WHY_RE.sub("", prose).strip()
            if prose_sans_why:
                last_prose = prose_sans_why

            label_split = _FIXED_LABEL_SPLIT_RE.split(prose_sans_why, maxsplit=1)
            if len(label_split) > 1:
                seen_fixed_marker = True
                before = label_split[0].strip()
                if before and seen_wrong_code and fixed is None:
                    error_parts.append(before)
            elif _FIXED_MARKER_RE.search(prose):
                seen_fixed_marker = True
            elif prose_sans_why and seen_wrong_code and fixed is None:
                error_parts.append(prose_sans_why)
            continue

        lang, content = fence_content(raw)
        if lang in ("c", "cpp"):
            if wrong is None:
                wrong = content
                wrong_lang = lang
                seen_wrong_code = True
            elif fixed is None:
                fixed = content
            else:
                warnings.add(ep, "Bug of the Day: more than 2 code blocks found; extra ones ignored")
        elif lang in ("text", "console", "bash"):
            if first_text_block is None:
                first_text_block = content
            if fixed is None:
                error_parts.append(content)
            elif fixed_output is None:
                fixed_output = content
            else:
                fixed_output += "\n" + content
        else:
            warnings.add(ep, f"Bug of the Day: unrecognised fence language {lang!r}")

    if not why_was_labelled:
        # Several episodes end with an unlabelled explanatory sentence
        # instead of a "**Why:**" line; fall back to the section's last
        # prose paragraph rather than leaving `why` empty.
        why = last_prose
        warnings.add(
            ep, "Bug of the Day: no 'Why:' label found; used the section's last prose paragraph instead"
        )

    if wrong is None:
        if first_text_block is not None:
            # Conceptual bug with no C code at all (e.g. a "wrong idea", or an
            # environment/PATH setup mistake) — the first text block is the
            # "wrong" side, shown verbatim rather than as compilable code.
            wrong = first_text_block
            wrong_lang = "text"
            warnings.add(ep, "Bug of the Day: no C code block; this is a conceptual/non-code bug")
        else:
            warnings.add(ep, "Bug of the Day: no wrong-code/wrong-idea block found at all")
            return None
    if fixed is None:
        warnings.add(ep, "Bug of the Day: no fixed code/text block found; using the last prose paragraph")
        fixed = last_prose
    if not seen_fixed_marker:
        warnings.add(ep, "Bug of the Day: no 'Fixed' marker text found before the fixed block")

    fixed_has_full_program = ("#include" in fixed) or ("int main" in fixed) or (wrong_lang != "c")
    if wrong_lang == "c" and fixed and not fixed_has_full_program:
        warnings.add(
            ep,
            "Bug of the Day: fixed block looks like a snippet, not a full program "
            "(check_c.py will reconstruct it by patching the wrong code)",
        )

    return Bug(
        wrong=wrong,
        error="\n\n".join(error_parts).strip(),
        fixed=fixed,
        why=why,
        fixed_output=fixed_output,
        wrong_lang=wrong_lang,
        fixed_has_full_program=fixed_has_full_program,
    )


# ---------------------------------------------------------------------------
# ### Pun & challenge: - **Pun:** / **Challenge:** / **Challenge answer:**
# ---------------------------------------------------------------------------

_PUN_BULLET_RE = re.compile(
    r"^-\s+\*\*(Pun|Challenge answer|Challenge)\*{0,2}[^:\n]*:\*{0,2}\s*(.*?)\s*$", re.MULTILINE
)


def parse_pun_challenge(section_text: str, ep: str, warnings: Warnings) -> dict:
    chunks = split_code_fences(section_text)
    prose_only = "".join(raw for is_code, raw in chunks if not is_code)
    text = unescape_outside_code(prose_only)
    bullets = {m.group(1): m.group(2) for m in _PUN_BULLET_RE.finditer(text)}

    answer = bullets.get("Challenge answer", "")
    if not answer:
        # EP14-style: "**Challenge answer** (...):" followed by a worked code
        # example instead of a sentence. Use the first code block after the
        # bullet, if any.
        for is_code, raw in chunks:
            if is_code:
                lang, content = fence_content(raw)
                if lang in ("c", "cpp"):
                    answer = f"(worked example)\n{content}"
                    warnings.add(ep, "Challenge answer is a code example, not a sentence; captured verbatim")
                    break

    for required in ("Pun", "Challenge"):
        if required not in bullets:
            warnings.add(ep, f"### Pun & challenge missing bullet: {required}")
    if not answer:
        warnings.add(ep, "### Pun & challenge missing bullet: Challenge answer")

    return {
        "pun": bullets.get("Pun", ""),
        "challenge": bullets.get("Challenge", ""),
        "challengeAnswer": answer,
    }


# ---------------------------------------------------------------------------
# ### Shorts for EP NN: "**S1 . Title** - m:ss . built from scene(s) ...",
# then bullets Hook / Script / On-screen text / Caption + hashtags.
# ---------------------------------------------------------------------------

_SHORT_HEADER_RE = re.compile(
    r"\*\*(S[1-5])\s*"
    + MID_DOT
    + r"\s*(.+?)\*\*\s*"
    + EM_DASH
    + r"\s*(\d+):(\d{2})\s*"
    + MID_DOT
    + r"\s*built from (.+?)\s*$",
    re.MULTILINE,
)
_SHORT_BULLET_RE = re.compile(
    r"^-\s+\*\*(Hook[^:]*|Script|On-screen text|Caption \+ hashtags):\*\*\s*(.+?)\s*$", re.MULTILINE
)
_SCENE_NUM_RE = re.compile(r"\d+")
_HASHTAG_RE = re.compile(r"#(\w+)")


def parse_from_scenes(built_from_text: str) -> list[int]:
    # "scenes 1-2", "scene 3", "scene 1 + pun card" -> all plain integers found.
    return [int(n) for n in _SCENE_NUM_RE.findall(built_from_text)]


def parse_shorts(section_text: str, ep: str, warnings: Warnings) -> list[dict]:
    text = unescape_outside_code(section_text)
    headers = list(_SHORT_HEADER_RE.finditer(text))
    shorts = []
    for i, m in enumerate(headers):
        short_id, title, mins, secs, built_from = m.groups()
        length_sec = int(mins) * 60 + int(secs)
        from_scenes = parse_from_scenes(built_from)
        if not from_scenes:
            warnings.add(ep, f"{short_id}: 'built from {built_from}' has no numeric scene reference")

        body_start = m.end()
        body_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        body = text[body_start:body_end]
        bullets = {bm.group(1).split(" (")[0]: bm.group(2) for bm in _SHORT_BULLET_RE.finditer(body)}

        for required in ("Hook", "Script", "On-screen text", "Caption + hashtags"):
            if required not in bullets:
                warnings.add(ep, f"{short_id}: missing bullet {required}")

        caption_raw = bullets.get("Caption + hashtags", "")
        hashtags = _HASHTAG_RE.findall(caption_raw)
        caption = _HASHTAG_RE.sub("", caption_raw).strip()

        shorts.append(
            {
                "id": short_id,
                "title": title.strip(),
                "hook": bullets.get("Hook", ""),
                "script": bullets.get("Script", ""),
                "onScreen": bullets.get("On-screen text", ""),
                "fromScenes": from_scenes,
                "lengthSec": length_sec,
                "caption": caption,
                "hashtags": hashtags,
            }
        )

    if len(shorts) != 5:
        warnings.add(ep, f"expected 5 Shorts, found {len(shorts)}")

    return shorts


# ---------------------------------------------------------------------------
# ### Step trace (module 12 only, sometimes renamed): only the simple
# pairwise-compare-and-swap sorts (bubble, selection, insertion) have a table
# that fits the strict {step, array, compare, swap, sorted} shape. Search,
# merge/quick/counting sort, recursion (Hanoi) and the "showdown"/"what the
# preprocessor sees" variants use their own table shapes and are left
# unparsed (reported, not force-fit).
# ---------------------------------------------------------------------------

_ARRAY_CELL_RE = re.compile(r"\[([\d,\s]+)\]")
_COMPARE_CELL_RE = re.compile(r"a\[(\d+)\].*?a\[(\d+)\]")


def parse_step_trace(section_text: str, ep: str, warnings: Warnings) -> list[dict] | None:
    text = unescape_outside_code(section_text)
    rows = parse_markdown_table(text)
    if not rows:
        return None

    headers = set(rows[0].keys())
    array_col = next((h for h in headers if "array" in h.lower()), None)
    compared_col = next((h for h in headers if h.lower().startswith("compar")), None)
    swapped_col = next((h for h in headers if "swap" in h.lower()), None)
    step_col = next((h for h in headers if h.lower() in ("step", "pass.step")), None)

    if not (array_col and compared_col and swapped_col and step_col):
        warnings.add(ep, "Step trace table does not have Step/Array/Compared/Swapped columns; not parsed into scene.trace")
        return None

    trace = []
    unmatched_compares = 0
    for row in rows:
        array_m = _ARRAY_CELL_RE.search(row.get(array_col, ""))
        if not array_m:
            continue  # e.g. the "start" row with no bracketed array, or a non-data row
        array = [int(n) for n in array_m.group(1).split(",")]

        compare_m = _COMPARE_CELL_RE.search(row.get(compared_col, ""))
        compare = [int(compare_m.group(1)), int(compare_m.group(2))] if compare_m else None
        if compare_m is None and row.get(compared_col, "").strip() not in ("", "-", EN_DASH, "—"):
            unmatched_compares += 1

        swap_text = row.get(swapped_col, "").strip()
        is_swap = compare is not None and swap_text not in ("", "-", "none", EN_DASH, "—") and "none" not in swap_text.lower()

        step_raw = row.get(step_col, "").strip()
        trace.append(
            {
                "step": step_raw,
                "array": array,
                **({"compare": compare} if compare else {}),
                **({"swap": compare} if is_swap else {}),
            }
        )

    if unmatched_compares > len(rows) / 2:
        warnings.add(
            ep,
            f"Step trace table has Step/Array/Compared/Swapped columns but {unmatched_compares} "
            "Compared cells don't match the 'a[i] ... a[j]' shape; trace may be incomplete",
        )

    return trace or None


# ---------------------------------------------------------------------------
# Template name mapping (mirrors src/lib/episode.ts's sceneTemplateFromBibleName).
# Kept here, not imported, since this script has no Node runtime available;
# scripts/validate_episodes.ts re-validates every emitted file against the
# real zod schema, so a drift between the two mappings would fail loudly there.
# ---------------------------------------------------------------------------

BIBLE_TEMPLATE_NAMES = {
    "Title card": "title-card",
    "Concept slide": "concept-slide",
    "Code explain": "code-explain",
    "Memory boxes": "memory-boxes",
    "Terminal": "terminal",
    "Algorithm bars": "algorithm-bars",
    "Bug of the Day": "bug-of-the-day",
    "Pun card": "pun-card",
    "Challenge": "challenge",
    "Outro": "outro",
}

# theme/modules.ts's moduleColours, by module index -> (bg name, accent name),
# for cross-checking against the Bible's own stated colour-pair text.
THEME_MODULE_COLOURS = [
    ("peach", "tomato"),
    ("pastelBlue", "tomato"),
    ("cream", "apricot"),
    ("mint", "darkBlue"),
    ("butter", "darkBlue"),
    ("lilac", "tomato"),
    ("peach", "darkBlue"),
    ("pastelBlue", "apricot"),
    ("lilac", "darkBlue"),
    ("cream", "tomato"),
    ("mint", "tomato"),
    ("apricot", "darkBlue"),
    ("darkBlue", "butter"),
    ("peach", "lilac"),
]
THEME_PALETTE_HEX = {
    "tomato": "#FF6F59",
    "peach": "#FFD8BE",
    "apricot": "#FFB88A",
    "butter": "#FFE58A",
    "cream": "#FFF4EC",
    "pastelBlue": "#BFD7FF",
    "mint": "#B8F2D0",
    "lilac": "#D9C9FF",
    "darkBlue": "#1E2A4A",
    "ink": "#111111",
    "white": "#FFFFFF",
}


def colours_text_to_names(colours_text: str) -> tuple[str, str] | None:
    """'Peach + Tomato' -> ('peach', 'tomato'), matching theme palette key casing."""
    parts = [p.strip() for p in colours_text.split("+")]
    if len(parts) != 2:
        return None

    def to_key(name: str) -> str | None:
        words = name.split()
        if not words:
            return None
        key = words[0].lower() + "".join(w.capitalize() for w in words[1:])
        return key if key in THEME_PALETTE_HEX else None

    bg, accent = to_key(parts[0]), to_key(parts[1])
    if bg is None or accent is None:
        return None
    return bg, accent


# ---------------------------------------------------------------------------
# Assembling one episode's JSON, and the file-level driver.
# ---------------------------------------------------------------------------


def assemble_episode(raw: RawEpisode, warnings: Warnings) -> dict | None:
    ep_label = f"{raw.ep:02d}"
    preamble = parse_preamble(raw.preamble, ep_label, warnings)
    if preamble is None:
        return None

    bg_name, accent_name = THEME_MODULE_COLOURS[preamble.module]
    colours_from_bible = colours_text_to_names(preamble.colours_text)
    if colours_from_bible is None:
        warnings.add(ep_label, f"could not parse colour-pair text {preamble.colours_text!r}")
    elif colours_from_bible != (bg_name, accent_name):
        warnings.add(
            ep_label,
            f"Bible says module {preamble.module} is {preamble.colours_text!r} but "
            f"theme/modules.ts says ({bg_name}, {accent_name})",
        )

    youtube = parse_youtube(raw.sections.get("YouTube", ""), ep_label, warnings)

    scenes_raw = parse_scene_list(raw.sections.get("Scene list", ""), ep_label, warnings)
    scene_ids = [s["id"] for s in scenes_raw]
    narration_by_scene = parse_narration(raw.sections.get("Narration script", ""), ep_label, scene_ids, warnings)

    code_files = parse_code_shown(raw.sections.get("Code shown", ""), ep_label, warnings)
    code_with_main = [c for c in code_files if "main(" in c.source and c.lang == "c"]
    sole_code_with_main = code_with_main[0] if len(code_with_main) == 1 else None

    step_trace_section = find_section(raw.sections, "Step trace")
    step_trace = None
    if step_trace_section:
        step_trace = parse_step_trace(step_trace_section[1], ep_label, warnings)
    for other_trace_heading in ("Move trace", "How the timings are measured"):
        other = find_section(raw.sections, other_trace_heading)
        if other:
            warnings.add(
                ep_label, f"has a {other[0]!r} section; informational only, not mapped to any schema field"
            )

    bug = parse_bug(raw.sections.get("Bug of the Day", ""), ep_label, warnings)

    pun_challenge = parse_pun_challenge(raw.sections.get("Pun & challenge", ""), ep_label, warnings)

    shorts_section = find_section(raw.sections, f"Shorts for EP {ep_label}")
    shorts = parse_shorts(shorts_section[1], ep_label, warnings) if shorts_section else []
    if shorts_section is None:
        warnings.add(ep_label, "no 'Shorts for EP NN' section found")

    scenes = []
    for s in scenes_raw:
        try:
            template = BIBLE_TEMPLATE_NAMES[s["template_raw"]]
        except KeyError:
            warnings.add(ep_label, f"scene {s['id']}: unknown template {s['template_raw']!r} (fail loud)")
            return None

        scene = {
            "id": s["id"],
            "template": template,
            "startSec": s["startSec"],
            "lengthSec": s["lengthSec"],
            "onScreen": s["onScreen"],
            "animation": s["animation"],
            "sfx": s["sfx"],
            "narration": narration_by_scene.get(s["id"], ""),
        }

        if template == "code-explain":
            matched = next((c for c in code_files if f"`{c.file}`" in s["onScreen"] or c.file in s["onScreen"]), None)
            code_file = matched or sole_code_with_main
            if code_file:
                scene["code"] = {"file": code_file.file, "source": code_file.source, **({"output": code_file.output} if code_file.output else {})}
        elif template == "algorithm-bars" and step_trace:
            scene["trace"] = step_trace

        scenes.append(scene)

    episode = {
        "ep": raw.ep,
        "title": raw.title,
        "module": preamble.module,
        "lengthSec": preamble.length_sec,
        "colours": {"bg": THEME_PALETTE_HEX[bg_name], "accent": THEME_PALETTE_HEX[accent_name]},
        "learningGoals": preamble.learning_goals,
        "youtube": youtube,
        "scenes": scenes,
        "bug": {
            "wrong": bug.wrong if bug else "",
            "error": bug.error if bug else "",
            "fixed": bug.fixed if bug else "",
            "why": bug.why if bug else "",
        },
        **pun_challenge,
        "shorts": shorts,
        # Extra, non-schema fields consumed directly by scripts/check_c.py.
        "codeFiles": [
            {
                "file": c.file,
                "source": c.source,
                **({"output": c.output} if c.output else {}),
                **({"stdin": c.stdin} if c.stdin else {}),
                **({"buildStep": c.build_step} if c.build_step else {}),
                "lang": c.lang,
            }
            for c in code_files
        ],
        "bugExtra": {
            "wrongLang": bug.wrong_lang if bug else "c",
            "fixedHasFullProgram": bug.fixed_has_full_program if bug else True,
            **({"fixedOutput": bug.fixed_output} if bug and bug.fixed_output else {}),
        },
    }
    return episode


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", default=str(ROOT / "out" / "bible-to-json-report.md"))
    args = parser.parse_args()

    warnings = Warnings()
    EPISODES_DIR.mkdir(parents=True, exist_ok=True)

    module_files = sorted(BIBLE_DIR.glob("m*.md"))
    summary_rows = []
    all_episode_nums = set()

    for module_file in module_files:
        text = module_file.read_text(encoding="utf-8")
        raw_episodes = split_module_into_episodes(text, module_file.name, warnings)
        for raw in raw_episodes:
            if raw.ep in all_episode_nums:
                warnings.add(f"{raw.ep:02d}", f"duplicate episode number (also seen before {module_file.name})")
            all_episode_nums.add(raw.ep)

            episode = assemble_episode(raw, warnings)
            ep_label = f"{raw.ep:02d}"
            if episode is None:
                summary_rows.append((raw.ep, raw.title, 0, 0, 0, "FAILED TO PARSE"))
                continue

            out_path = EPISODES_DIR / f"ep{raw.ep:03d}.json"
            out_path.write_text(json.dumps(episode, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

            n_scenes = len(episode["scenes"])
            n_files = len(episode["codeFiles"])
            n_shorts = len(episode["shorts"])
            flag = "" if n_shorts == 5 else "SHORTS!="

            scene_end = (episode["scenes"][-1]["startSec"] + episode["scenes"][-1]["lengthSec"]) if episode["scenes"] else 0
            if scene_end != episode["lengthSec"]:
                flag += f" LENGTH {scene_end}!={episode['lengthSec']}"
                warnings.add(ep_label, f"scene times sum to {scene_end}s but episode length is {episode['lengthSec']}s")

            summary_rows.append((raw.ep, raw.title, n_scenes, n_files, n_shorts, flag))

    missing = sorted(set(range(1, 87)) - all_episode_nums)
    if missing:
        warnings.add("--", f"missing episode numbers: {missing}")

    report_path = Path(args.report)
    report_path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["# bible_to_json.py report", "", f"Episodes parsed: {len(summary_rows)} / 86", ""]
    lines.append("| EP | Title | Scenes | Files | Shorts | Flags |")
    lines.append("| --- | --- | --- | --- | --- | --- |")
    for ep, title, n_scenes, n_files, n_shorts, flag in sorted(summary_rows):
        lines.append(f"| {ep} | {title} | {n_scenes} | {n_files} | {n_shorts} | {flag} |")
    lines.append("")
    lines.append(f"## Warnings ({len(warnings.items)})")
    lines.append("")
    for item in warnings.items:
        lines.append(f"- {item}")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"Wrote {len(summary_rows)} episodes to {EPISODES_DIR}")
    print(f"Warnings: {len(warnings.items)} (see {report_path})")


if __name__ == "__main__":
    main()
