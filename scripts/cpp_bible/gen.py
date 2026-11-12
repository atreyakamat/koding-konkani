#!/usr/bin/env python3
"""Build C++ Bible modules (docs/cpp-bible/mNN.md) from episode data.

Usage: python scripts/cpp_bible/gen.py m00 m01 ...

Each data module (scripts/cpp_bible/mNN.py) defines MODULE and EPISODES.
This script compiles and runs every sample with g++, pastes the real output and the real
compiler message into the Markdown, writes the illustration data as JSON, works out scene
lengths from the narration, builds the Shorts from the scene narration, and lints the
narration against docs/cpp-bible/STE.md. Then run scripts/check_cpp.py and
scripts/preflight_cpp.py: they re-check the Markdown independently.
"""
from __future__ import annotations

import importlib
import json
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import check_cpp as cc  # noqa: E402
import ste_lint  # noqa: E402

OUT = HERE.parent.parent / "docs" / "cpp-bible"
PROBLEMS: list[str] = []
BASE_TAGS = ["c++", "c++ for beginners", "c++ tutorial", "koding konkani", "class 11 computer science",
             "first year engineering", "coding in goa", "learn c++"]
ORDS = ["One", "Two", "Three", "Four", "Five"]
WPS = 1.8  # narrator words per second in scenes


def esc(t: str) -> str:
    return re.sub(r"\[(HL \d+|TRACK [^\]]*)\]", r"\\[\1\\]", t)


def mmss(s: int) -> str:
    return f"{s // 60}:{s % 60:02d}"


def words(t: str) -> int:
    return ste_lint.count_words(ste_lint.clean(t))


def need(narr: str, minimum: int) -> int:
    return max(minimum, math.ceil(words(narr) / WPS) + 2)


def dd(s: str) -> str:
    return s.strip("\n") + "\n"


def fence(src: str, lang: str = "cpp") -> str:
    return f"```{lang}\n{src.rstrip(chr(10))}\n```"


def paragraphs(narr: str, per: int = 4) -> list[str]:
    """Hand paragraphs stay. Any paragraph with more than 'per' sentences is split into even chunks (STE: max 6)."""
    out: list[str] = []
    for para in [p.strip() for p in narr.split("\n") if p.strip()]:
        ss = ste_lint.SENTENCE_END.split(para)
        if len(ss) <= per + 1:
            out.append(para)
            continue
        k = math.ceil(len(ss) / per)
        size = math.ceil(len(ss) / k)
        out.extend(" ".join(ss[i:i + size]) for i in range(0, len(ss), size))
    return out


def resolve_hl(ep: int, narr: str, src: str) -> str:
    """Turn [HL: some code text] cues into [HL n]. The line is the first one, at or after the previous
    cue's line, that contains the text. The text may contain balanced square brackets.
    This avoids hand-counted line numbers."""
    lines = src.rstrip("\n").split("\n")
    last = 0
    out: list[str] = []
    i = 0
    while i < len(narr):
        if narr.startswith("[HL:", i):
            j, depth = i + 4, 0
            while j < len(narr):
                if narr[j] == "[":
                    depth += 1
                elif narr[j] == "]":
                    if depth == 0:
                        break
                    depth -= 1
                j += 1
            else:
                raise SystemExit(f"EP {ep}: unclosed [HL: cue")
            needle = narr[i + 4:j].strip()
            hit = None
            for start in (last, 0):
                for k in range(start, len(lines)):
                    if needle in lines[k]:
                        hit = k
                        break
                if hit is not None:
                    break
            if hit is None:
                raise SystemExit(f"EP {ep}: [HL: {needle}] not found in the code")
            last = hit
            out.append(f"[HL {hit + 1}]")
            i = j + 1
        else:
            out.append(narr[i])
            i += 1
    return "".join(out)


def say_file(name: str) -> str:
    stem, ext = name.rsplit(".", 1)
    if not stem.isalpha():
        raise SystemExit(f"file name {name!r} must use letters only (the narrator spells it out)")
    return f"{stem} dot {ext}"


def sents(t: str) -> list[str]:
    return ste_lint.sentences(t)


def diag_block(compile_out: str, kind: str, limit: int = 6) -> str:
    """The first g++ diagnostic of the given kind with its source lines, as g++ prints it."""
    lines = compile_out.split("\n")
    for i, line in enumerate(lines):
        m = cc.DIAG.match(line)
        if m and m["kind"] == kind:
            start = i - 1 if i > 0 and re.match(r"^[\w.\-]+: In ", lines[i - 1]) else i
            end = i + 1
            while end < len(lines) and end - start < limit and not cc.DIAG.match(lines[end]) \
                    and not re.match(r"^[\w.\-]+: In |^In file included", lines[end]) and lines[end].strip():
                end += 1
            return "\n".join(lines[start:end])
    raise SystemExit(f"no {kind} found in compiler output:\n{compile_out}")


def pretty_json(d: dict) -> str:
    """One key per line; lists of objects one object per line; short lists inline."""
    parts = []
    for k, v in d.items():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            inner = ",\n".join("  " + json.dumps(x, ensure_ascii=False) for x in v)
            parts.append(f' "{k}": [\n{inner}\n ]')
        else:
            parts.append(f' "{k}": ' + json.dumps(v, ensure_ascii=False))
    return "{\n" + ",\n".join(parts) + "\n}"


def lint(ep: int, label: str, text: str, exempt: bool = False) -> None:
    if exempt:
        for lv, code, msg in ste_lint.lint_text(text):
            if code in ("TTS-CHAR",):
                PROBLEMS.append(f"EP {ep} [{label}] {code}: {msg}")
        return
    for lv, code, msg in ste_lint.lint_text(text):
        if lv == "ERROR":
            PROBLEMS.append(f"EP {ep} [{label}] {code}: {msg}")
        else:
            print(f"  warn EP {ep} [{label}] {code}: {msg}")


def run_prog(ep: int, p: dict, cxx: str) -> str:
    r = cc.compile_run(p["src"], p["file"], p.get("stdin", ""), cxx=cxx)
    if r.compile_rc != 0:
        raise SystemExit(f"EP {ep} {p['file']} does not compile:\n{r.compile_out}")
    if r.compile_out:
        raise SystemExit(f"EP {ep} {p['file']} has warnings:\n{r.compile_out}")
    if r.run_rc != 0 or r.timed_out:
        raise SystemExit(f"EP {ep} {p['file']} failed to run: rc={r.run_rc} {r.stderr}")
    return r.stdout


def apply_ext(ep: dict, ext: dict) -> dict:
    """Add the longer narration from ext_mNN.py to the end of the matching texts. Nothing else changes."""
    e = ext.get(ep["n"])
    if not e:
        return ep
    # The Shorts are built from the short original text, so keep it: a Short must not end on a half tip.
    base = {"concept": ep["concept"], "A": ep["A"]["narr"], "ill": ep["ill"]["narr"], "B": ep["B"]["narr"],
            "term": ep["term"], "bug": ep["bug"]["narr"], "challenge": ep["challenge"]}
    ep = {**ep, "A": dict(ep["A"]), "B": dict(ep["B"]), "ill": dict(ep["ill"]), "bug": dict(ep["bug"]), "_base": base}
    if "intro" in e:
        ep["intro"] = ep["intro"] + " " + e["intro"]
    if "concept" in e:
        ep["concept"] = ep["concept"] + "\n" + e["concept"]
    if "A" in e:
        ep["A"]["narr"] = ep["A"]["narr"].rstrip() + " " + e["A"]
    if "ill" in e:
        ep["ill"]["narr"] = ep["ill"]["narr"].rstrip() + " " + e["ill"]
    if "B" in e:
        ep["B"]["narr"] = ep["B"]["narr"].rstrip() + " " + e["B"]
    if "term" in e:
        ep["term"] = ep["term"] + " " + e["term"]
    if "bug" in e:
        ep["bug"]["narr"] = ep["bug"]["narr"].rstrip() + " " + e["bug"]
    if "hint" in e:
        ep["challenge"] = ep["challenge"] + " " + e["hint"]
    return ep


def build_episode(mod: dict, ep: dict, nxt: dict | None, cxx: str) -> str:
    n = ep["n"]
    A, B, bug, ill = ep["A"], ep["B"], ep["bug"], ep["ill"]
    A["src"], B["src"] = dd(A["src"]), dd(B["src"])
    A["narr"], B["narr"] = resolve_hl(n, A["narr"], A["src"]), resolve_hl(n, B["narr"], B["src"])
    sc: list[dict] = []

    def add(template, label, on, narr, minimum, anim, fixed=None, exempt=False):
        sc.append({"t": template, "label": label, "on": on, "narr": narr.strip(), "min": minimum,
                   "anim": anim, "fixed": fixed, "exempt": exempt})

    add("Title card", "Title", f"EP {n:02d} · {ep['thumb']}", ep["intro"], 15,
        "Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting")
    pts = "; ".join(f"{i + 1}. {p}" for i, p in enumerate(ep["c_pts"]))
    add("Concept slide", ep["title"], f"\"{ep['title']}\": numbered lines ({pts}) and an analogy card: {ep['analogy']}",
        ep["concept"], 30, "Lines spring in one by one with a pop; the analogy card slides in from the right")
    add("Code explain", A["label"], f"{A['file']}: {A['on']}", A["narr"], 40,
        "Code types in with key-tick; butter \\[HL n\\] highlight sweeps line by line with marker-swipe; explanation card on the right")
    kind = ill["data"]["kind"]
    tpl = {"memory": "Memory boxes", "trace": "Algorithm bars"}.get(kind, "Concept slide")
    ill_anim = {"memory": "Boxes pop in one by one with size and address tags; arrows draw on as the narrator mentions them; regions are labelled; pop per box",
                "trace": "Bars compare in butter, swap in tomato and slide past each other, sorted bars turn mint; pass, compare and swap counters tick",
                "flow": "Steps drop in left to right with a pop; connecting arrows draw on; the active step glows butter",
                "graph": "Nodes pop in one by one; edges draw on as the narrator mentions them",
                "table": "Table rows slide in one by one; the row the narrator mentions glows butter",
                "callstack": "Frames stack up with a thud and leave with a whoosh, one step per narrated sentence"}[kind]
    add(tpl, ill["label"], ill["on"], ill["narr"], 30, ill_anim)
    add("Code explain", B["label"], f"{B['file']}: {B['on']}", B["narr"], 40,
        "Second program or a twist on the first; \\[HL n\\] and \\[TRACK name=value\\] cues drive the variable tracker; output panel fills line by line with a ding per line")
    runfile = B["file"]
    add("Terminal", "Run it", f"Terminal: g++ -std=c++20 {runfile} -o {runfile.rsplit('.', 1)[0]} then ./{runfile.rsplit('.', 1)[0]}",
        f"Save the file as {say_file(runfile)}. Compile it with g plus plus. Then run the program. {ep['term']}", 20,
        "Dark-blue terminal: the compile command types with key-tick, the run command types, output prints in mint with a ding")
    ords = ep["recap"]
    recap_narr = "Let us recap.\n" + " ".join(f"{ORDS[i]}. {r}" for i, r in enumerate(ords)) + "\nPause the video. Say these ideas out loud, one time, slowly."
    add("Concept slide", "Recap", f"Recap: {len(ords)} ideas on one card", recap_narr, 30,
        "Recap lines tick in one by one with a pop; Xecxec nods after each tick")
    banim = {"compile": "Butter banner drops in with a buzzer; wrong code shakes; the g++ error lines appear in tomato; the fix slides in and the terminal turns mint with a ding",
             "warn": "Butter banner drops in with a buzzer; the g++ warning appears in tomato; the fix slides in and the warning goes away with a ding",
             "output": "Butter banner drops in with a buzzer; the program runs and the wrong output appears in tomato; the fix slides in and the output turns mint with a ding",
             "runtime": "Butter banner drops in with a buzzer; the program crashes and the run-time error appears in tomato; the fix slides in and the output turns mint with a ding"}[bug.get("kind", "compile")]
    add("Bug of the Day", bug["title"], f"BUG OF THE DAY: {bug['title']}", bug["narr"], 40, banim)
    add("Pun card", "Pun", ep["pun"], ep["pun"], 8, "Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw", fixed=8, exempt=True)
    add("Challenge", "Challenge", f"Task card: {ep['task']}", f"Your challenge: {ep['challenge']} Write your answer in the comments.", 20,
        "Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen")
    nxt_line = f"Next: EP {nxt['n']:02d} · {nxt['title']}" if nxt else ep["next_line"]
    nxt_say = f"Next time: {nxt['spoken']}." if nxt else ep["next_say"]
    add("Outro", "Next episode", nxt_line, f"{nxt_say} Keep coding, says Xecxec!", 15,
        "Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in")

    t = 0
    for s in sc:
        s["len"] = s["fixed"] or need(s["narr"], s["min"])
        s["start"] = t
        t += s["len"]
    total = t
    if not 270 <= total <= 540:
        print(f"  note: EP {n} is {mmss(total)}")
    for i, s in enumerate(sc, 1):
        lint(n, f"scene {i} {s['label']}", "\n\n".join(paragraphs(s["narr"])), s["exempt"])

    chap_idx = [(1, "Intro"), (2, sc[1]["label"]), (3, sc[2]["label"]), (4, ill["label"]), (5, "Second program"),
                (7, "Recap"), (8, "Bug of the Day"), (10, "Challenge"), (11, "Next episode")]
    chapters = " · ".join(f"{mmss(sc[i - 1]['start'])} {lab}" for i, lab in chap_idx)
    g = ep["goals"]
    desc = f"In this episode you will {g[0]}, {g[1]} and {g[2]}, with Xecxec the crab. {chapters}"
    tags = BASE_TAGS + ep["tags"]

    L: list[str] = []
    L.append(f"## EP {n:02d} — {ep['title']}\n")
    prereq = f"EP {n - 1:02d}" if n > 1 else "none"
    L.append(f"**Module {mod['id']} · {mod['name']} · {mmss(total)} · {mod['colours']} · Prerequisite: {prereq}**\n")
    L.append("**Learning goals:** " + "; ".join(g) + ".\n")
    L.append("### YouTube\n")
    L.append(f"- **Title:** {ep.get('yt', ep['title'] + ' in C++')} | C++ Programming EP {n:02d}")
    L.append(f"- **Description:** {desc}")
    L.append(f"- **Tags:** {', '.join(tags)}")
    L.append(f"- **Thumbnail:** big text \"{ep['thumb']}\" in tomato on {mod['bg']}; Xecxec next to {ep['vis']}; thin black border and drop shadow.\n")
    L.append("### Scene list\n")
    L.append("| # | Start | Length | Template | On screen | Animation & SFX |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for i, s in enumerate(sc, 1):
        L.append(f"| {i} | {mmss(s['start'])} | {mmss(s['len'])} | {s['t']} | {esc(s['on'])} | {s['anim']} |")
    L.append("\n### Narration script\n")
    for i, s in enumerate(sc, 1):
        paras = paragraphs(s["narr"])
        L.append(f"**\\[{i} · {s['label']}\\]** " + "\n\n".join(esc(p) for p in paras) + "\n")

    L.append("### Code shown\n")
    outs: dict[str, str] = {}
    for k, p in enumerate((A, B), 1):
        scn = "scene 3" if k == 1 else "scene 5, 6"
        L.append(f"File {k}: {p['file']} ({scn})\n")
        if p.get("stdin"):
            L.append(f"**Typed input:** (the terminal scene shows these characters, then Enter)\n\n```text\n{p['stdin'].rstrip(chr(10))}\n```\n")
        L.append(fence(p["src"]) + "\n")
        out = run_prog(n, p, cxx)
        outs[p["file"]] = out
        L.append("**Expected output:**\n")
        L.append(fence(out, "text") + "\n")
        hl = [int(x) for x in re.findall(r"\[HL (\d+)\]", p["narr"])]
        nlines = len(p["src"].rstrip("\n").split("\n"))
        if any(h < 1 or h > nlines for h in hl):
            PROBLEMS.append(f"EP {n}: [HL] out of range in {p['file']} (lines 1-{nlines}): {hl}")
        if not hl:
            PROBLEMS.append(f"EP {n}: no [HL] cue in the narration for {p['file']}")
    L.append("### Illustrations\n")
    data = dict(ill["data"])
    data = {"scene": 4, **data}
    if not data.get("caption"):
        data["caption"] = ill["on"]
    L.append(f"**Scene 4 · {ill['label']}** (kind: {kind})\n")
    L.append("```json\n" + pretty_json(data) + "\n```\n")

    L.append("### Bug of the Day\n")
    bkind = bug.get("kind", "compile")
    bname = bug.get("file", A["file"])
    wrong = dd(bug["wrong"])
    bstdin = bug.get("stdin", "")
    wr = cc.compile_run(wrong, bname, bstdin, cxx=cxx)
    L.append(f"**Bug kind:** {bkind} · **Bug file:** {bname}\n")
    if bstdin:
        L.append(f"**Typed input:** (the terminal scene shows these characters, then Enter)\n\n```text\n{bstdin.rstrip(chr(10))}\n```\n")
    L.append(f"Wrong code ({bug['wrong_note']}):\n")
    L.append(fence(wrong) + "\n")
    if bkind == "compile":
        if wr.compile_rc == 0:
            raise SystemExit(f"EP {n}: bug code compiled")
        shown, label = diag_block(wr.compile_out, "error"), "Compiler output (exactly as g++ prints it):"
    elif bkind == "warn":
        if wr.compile_rc != 0:
            raise SystemExit(f"EP {n}: warn bug did not compile:\n{wr.compile_out}")
        shown, label = diag_block(wr.compile_out, "warning"), "Compiler output (a warning, the program still builds):"
    elif bkind == "output":
        if wr.compile_rc != 0 or wr.compile_out or wr.run_rc != 0:
            raise SystemExit(f"EP {n}: output bug not clean: {wr.compile_out}{wr.stderr}")
        shown, label = wr.stdout, "Program output (it runs, but the answer is wrong):"
    else:
        if wr.compile_rc != 0 or wr.run_rc in (0, None):
            raise SystemExit(f"EP {n}: runtime bug did not fail: {wr.compile_out} rc={wr.run_rc}")
        shown, label = wr.stderr, "Program error output (exactly as the program prints it):"
    L.append(label + "\n")
    L.append(fence(shown, "text") + "\n")
    fixed = dd(bug["fixed"])
    fr = cc.compile_run(fixed, bname, bstdin, cxx=cxx)
    if fr.compile_rc != 0 or fr.compile_out or fr.run_rc != 0:
        raise SystemExit(f"EP {n}: fixed code not clean:\n{fr.compile_out}{fr.stderr}")
    L.append(f"Fixed code ({bug['fixed_note']}):\n")
    L.append(fence(fixed) + "\n")
    if bug.get("show_fixed_out", True):
        L.append("**Fixed output:**\n")
        L.append(fence(fr.stdout, "text") + "\n")
    L.append(f"**Why:** {bug['why']}\n")
    lint(n, "bug why", bug["why"])

    L.append("### Pun & challenge\n")
    L.append(f"- **Pun:** \"{ep['pun']}\"")
    L.append(f"- **Challenge:** {ep['challenge']}")
    L.append(f"- **Challenge answer:** {ep['answer']}\n")
    lint(n, "challenge answer", ep["answer"])

    # ---- Shorts, built from the scene narration
    L.append(f"### Shorts for EP {n:02d}\n")
    base = ep.get("_base", {})
    narr = {i + 1: s["narr"] for i, s in enumerate(sc)}
    for idx, key in ((2, "concept"), (3, "A"), (4, "ill"), (5, "B"), (8, "bug")):
        if key in base:
            narr[idx] = resolve_hl(n, base[key], A["src"] if key == "A" else B["src"]) if key in ("A", "B") else base[key]
    short_term = base.get("term", ep["term"])
    short_challenge = base.get("challenge", ep["challenge"])
    recap_s = [f"{r}" for r in ords]
    plan = [
        ("S1", f"What you will learn: {ep['title']}", [ep["hook"]] + sents(narr[1]) + sents(narr[2]) + recap_s, [1, 2]),
        ("S2", f"{ep['title']} in one minute", sents(narr[2]) + sents(narr[3]) + recap_s, [2, 3]),
        ("S3", "Inside the second program", sents(narr[5]) + sents(short_term) + recap_s, [5, 6]),
        ("S4", f"Bug of the Day: {bug['title']}", [f"Can you spot the bug in {ep['spoken']}?"] + sents(narr[8]) + sents(bug["why"]) + recap_s, [8]),
        ("S5", "Pun and challenge", [f"Can you {ep['task']} in {ep['spoken']}?", ep["pun"]] + sents(short_challenge) + ["Write your answer in the comments."] + recap_s, [9, 10]),
    ]
    slug = re.sub(r"[^a-z0-9]", "", ep["title"].lower())
    used_hooks: set[str] = set()
    for sid, st, pool, frm in plan:
        while pool[0].strip() in used_hooks and len(pool) > 1:
            pool = pool[1:]  # never open two Shorts of one episode with the same sentence
        used_hooks.add(pool[0].strip())
        body: list[str] = []
        w = 0
        for s in pool:
            if w >= 58:
                break
            body.append(s.strip())
            w += words(s)
        script = " ".join(body) + " Keep coding, says Xecxec!"
        tw = words(script)
        length = math.ceil(tw / 2) + 4
        if not 35 <= length <= 45:
            PROBLEMS.append(f"EP {n} {sid}: {tw} words = {length}s; need 62-82 words")
        hook = body[0]
        if len(hook.split()) > 12:  # the hook is the first 1.5 seconds only
            hook = hook.split(",")[0] if len(hook.split(",")[0].split()) <= 12 else " ".join(hook.split()[:10])
        for lv, code, msg in ste_lint.lint_text(script):
            if code == "TTS-CHAR":  # sentences were linted in their scenes; the pun is exempt
                PROBLEMS.append(f"EP {n} {sid}: {code}: {msg}")
        on = {"S2": ep["title"], "S4": "Bug of the Day"}.get(sid, st.replace("What you will learn: ", "")).upper()
        extra = {"S1": "#beginners", "S2": "#coding", "S3": "#learntocode", "S4": "#bugfix", "S5": "#codingchallenge"}[sid]
        L.append(f"**{sid} · {st}** — {mmss(length)} · built from scene{'s' if len(frm) > 1 else ''} {', '.join(map(str, frm))}")
        L.append(f"- **Hook (first 1.5s):** \"{hook}\"")
        L.append(f"- **Script:** {script}")
        L.append(f"- **On-screen text:** {on}")
        L.append(f"- **Caption + hashtags:** {st}. #cpp #kodingkonkani #{slug} {extra}\n")
    return "\n".join(L)


def build_module(name: str, cxx: str = "g++") -> int:
    m = importlib.import_module(name)
    mod, eps = m.MODULE, m.EPISODES
    try:
        ext = importlib.import_module("ext_" + name).EXT
    except ModuleNotFoundError:
        ext = {}
    eps = [apply_ext(e, ext) for e in eps]
    nxt_mod = getattr(m, "NEXT_AFTER", None)
    out = [f"# C++ Module {mod['id']} — {mod['name']}\n",
           f"Episodes {mod['range']} · {mod['colours']} · Every sample compiled and run with g++ `-std=c++20 -Wall -Wextra`; "
           f"outputs and compiler messages are pasted from those runs. Narration follows STE.md.\n"]
    for i, ep in enumerate(eps):
        nxt = eps[i + 1] if i + 1 < len(eps) else None
        if nxt is None and nxt_mod:
            ep = dict(ep)
            ep["next_line"], ep["next_say"] = nxt_mod
        out.append(build_episode(mod, ep, nxt, cxx))
    path = OUT / f"{name}.md"
    OUT.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {path} ({len(eps)} episodes)")
    for p in PROBLEMS:
        print("PROBLEM", p)
    return 1 if PROBLEMS else 0


if __name__ == "__main__":
    rc = 0
    for a in sys.argv[1:]:
        PROBLEMS.clear()
        rc |= build_module(a)
    sys.exit(rc)
