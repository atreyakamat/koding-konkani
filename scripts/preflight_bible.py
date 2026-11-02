#!/usr/bin/env python3
"""Pre-flight check of the Episode Bible for episodes >= a start number.

Reads docs/bible/m*.md and writes docs/ep19-preflight.md: one row per episode with
facts a renderer needs and flags for things that broke earlier renders.
Read-only on the Bible. No network. Run: python scripts/preflight_bible.py [--from 19]
"""
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIBLE = ROOT / "docs" / "bible"
OUT = ROOT / "docs" / "ep19-preflight.md"

MAX_CODE_COLS = 52  # wider lines wrap or clip in the Short code panel
MAX_CODE_ROWS = 22  # more rows force scrolling in CodeExplain
MAX_MINUTES = 9.0  # STYLE.md: report, never speed the voice up
WORDS_PER_MIN = 130

EP_RE = re.compile(r"^## EP (\d+) — (.+)$", re.M)
HL_RE = re.compile(r"\[HL (\d+)\]|\\\[HL (\d+)\\\]")


@dataclass
class Row:
    ep: int
    title: str
    module: str = ""
    scenes: int = 0
    templates: dict[str, int] = field(default_factory=dict)
    narr_tags: int = 0
    words: int = 0
    code_blocks: int = 0
    max_rows: int = 0
    max_cols: int = 0
    max_hl: int = 0
    shorts: int = 0
    has_trace: bool = False
    has_expected: bool = False
    flags: list[str] = field(default_factory=list)


def split_sections(body: str) -> dict[str, str]:
    parts = re.split(r"^### (.+)$", body, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def analyse(ep: int, title: str, body: str, module: str) -> Row:
    row = Row(ep, title, module)
    secs = split_sections(body)

    scene_sec = next((v for k, v in secs.items() if k.startswith("Scene list")), "")
    for line in scene_sec.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0].isdigit():
            row.scenes += 1
            row.templates[cells[3]] = row.templates.get(cells[3], 0) + 1

    narr = next((v for k, v in secs.items() if k.startswith("Narration")), "")
    row.narr_tags = len(re.findall(r"^\*\*\\\[\d+ ·", narr, flags=re.M))
    plain = re.sub(r"\\?\[[^\]]*\\?\]", " ", narr)
    row.words = len(re.findall(r"[A-Za-z0-9']+", plain))
    hls = [int(a or b) for a, b in HL_RE.findall(narr)]
    row.max_hl = max(hls, default=0)

    code = secs.get("Code shown", "")
    blocks = re.findall(r"```c\n(.*?)```", code, flags=re.S)
    row.code_blocks = len(blocks)
    for blk in blocks:
        lines = blk.rstrip("\n").split("\n")
        row.max_rows = max(row.max_rows, len(lines))
        row.max_cols = max(row.max_cols, max((len(l.expandtabs(4)) for l in lines), default=0))
    row.has_expected = "```text" in code

    row.has_trace = any(k.startswith("Step trace") for k in secs)
    row.shorts = len(re.findall(r"^\*\*S[1-5] ·", body, flags=re.M))

    # flags: each one names the fix so a small model can act on it
    if row.scenes and row.narr_tags != row.scenes:
        row.flags.append(f"FIX: narration tags {row.narr_tags} != scene rows {row.scenes}: align them")
    if row.shorts != 5:
        row.flags.append(f"FIX: {row.shorts} Shorts, expected 5")
    if blocks and row.max_hl > max(len(b.rstrip().split("\n")) for b in blocks):
        row.flags.append(f"FIX: [HL {row.max_hl}] is beyond the longest code block: fix the cue")
    if row.max_cols > MAX_CODE_COLS:
        row.flags.append(f"WATCH: code line {row.max_cols} cols > {MAX_CODE_COLS}: Shorts must wrap")
    if row.max_rows > MAX_CODE_ROWS:
        row.flags.append(f"WATCH: code {row.max_rows} rows > {MAX_CODE_ROWS}: split or scroll whole rows")
    if row.words / WORDS_PER_MIN > MAX_MINUTES:
        row.flags.append(f"FIX: narration ~{row.words / WORDS_PER_MIN:.1f} min > {MAX_MINUTES}: trim text")
    if any("Terminal" in t for t in row.templates) and not row.has_expected:
        row.flags.append("FIX: Terminal scene but no expected output block")
    if any("Algorithm" in t for t in row.templates) and not row.has_trace:
        row.flags.append("FIX: Algorithm bars scene but no Step trace table (add one, or use Memory boxes)")
    if "**" in title or "`" in title:
        row.flags.append("FIX: markdown in title")
    return row


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="start", type=int, default=19)
    start = ap.parse_args().start

    rows: list[Row] = []
    for f in sorted(BIBLE.glob("m*.md")):
        text = f.read_text(encoding="utf-8")
        mod = re.search(r"^# (Module \d+)", text, flags=re.M)
        matches = list(EP_RE.finditer(text))
        for i, m in enumerate(matches):
            ep = int(m.group(1))
            if ep < start:
                continue
            end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
            rows.append(analyse(ep, m.group(2), text[m.end():end], mod.group(1) if mod else f.stem))

    lines = [
        f"# Pre-flight: EP {start} onwards",
        "",
        "Generated by `python scripts/preflight_bible.py`. Do not edit by hand.",
        "FIX = repair the Bible or episode JSON BEFORE rendering that episode. WATCH = look at the rendered result.",
        "",
        "| EP | Module | Scenes | Code rows x cols | Shorts | Trace | Flags |",
        "| --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        flags = "; ".join(r.flags) or "ok"
        lines.append(
            f"| {r.ep} | {r.module} | {r.scenes} | {r.max_rows}x{r.max_cols} | {r.shorts} "
            f"| {'yes' if r.has_trace else '-'} | {flags} |"
        )
    flagged = sum(1 for r in rows if any(f.startswith("FIX") for f in r.flags))
    lines += ["", f"{len(rows)} episodes checked, {flagged} with FIX flags. WATCH = renderer must handle it (wrap, scroll); not a Bible error."]
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{len(rows)} episodes, {flagged} with FIX flags -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
