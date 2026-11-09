#!/usr/bin/env python3
"""Build Python Bible modules (docs/python-bible/mNN.md) from episode data.

Usage: python scripts/python_bible/gen.py m01 [m02 ...]

Each data module (scripts/python_bible/mNN.py) defines MODULE and EPISODES. This
script runs every code sample with Python, pastes the real output or traceback
into the Markdown, derives the Memory boxes data from the real objects, works
out scene lengths from the narration (120 words a minute) and writes the
Bible in the same layout as the C Bible. Then run scripts/check_py.py on the
result: it re-runs everything independently.
"""
from __future__ import annotations

import importlib
import math
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import check_py as cp  # noqa: E402

PROBLEMS: list[str] = []
OUT = HERE.parent.parent / "docs" / "python-bible"
BASE_TAGS = ["python", "python for beginners", "python tutorial", "koding konkani",
             "class 11 computer science", "coding in goa", "learn python"]


def esc(t: str) -> str:
    return re.sub(r"\[(HL \d+|TRACK [^\]]*)\]", r"\\[\1\\]", t)


def mmss(s: int) -> str:
    return f"{s // 60}:{s % 60:02d}"


def sentence_words(t: str) -> int:
    return cp.words(t)


def need(sec_words: str, minimum: int, pad: int = 4) -> int:
    return max(minimum, math.ceil(cp.words(sec_words) / 2) + pad)


def dd(s: str) -> str:
    return s.strip("\n") + "\n"


def code_fence(src: str, lang: str = "python") -> str:
    return f"```{lang}\n{src.rstrip(chr(10))}\n```"


def pretty_run(prog: dict, expect_ok: bool = True) -> str:
    rc, out, err, to = cp.run(prog["src"], prog["file"], prog.get("stdin", ""), prog.get("files"))
    if rc != 0 or to:
        raise SystemExit(f"{prog['file']} failed: {cp.norm(err)}")
    return cp.norm(out)


def build_episode(mod: dict, ep: dict, nxt: dict | None) -> str:
    n = ep["n"]
    A, B = ep["A"], ep.get("B")
    A["src"] = dd(A["src"])
    if B:
        B["src"] = dd(B["src"])
    bug = ep["bug"]
    mem = ep.get("mem")
    has_mem = bool(mem)
    progs = [A] + ([B] if B else [])
    run_prog = ep.get("run", "B" if B else "A")
    runp = B if run_prog == "B" and B else A

    # --- scene definitions: (template, onscreen, narration, minimum, anim)
    sc: list[dict] = []

    def add(template: str, label: str, on: str, narr: str, minimum: int, anim: str, fixed: int | None = None):
        sc.append({"t": template, "label": label, "on": on, "narr": narr.strip(), "min": minimum,
                   "anim": anim, "fixed": fixed})

    add("Title card", "Title", f"EP {n:02d} · {ep['thumb']}", ep["intro"], 15,
        "Tomato title card: EP sticker thuds in, title stamps with a whoosh, Xecxec scuttles in and waves; thud, whoosh, claw-click, sting")
    pts = "; ".join(f"{i + 1}. {p}" for i, p in enumerate(ep["c_pts"]))
    add("Concept slide", ep["c_title"], f"\"{ep['c_title']}\": three numbered lines ({pts}) and an analogy card: {ep['analogy']}",
        ep["concept"], 30, "Lines spring in one by one with a pop; the analogy card slides in from the right")
    add("Code explain", A["label"], f"{A['file']}: {A['on']}",
        A["narr"], 40, "Code types in with key-tick; butter \\[HL n\\] highlight sweeps line by line with marker-swipe; explanation card on the right; faint indent guide lines")
    if has_mem:
        add("Memory boxes", mem["label"], f"{mem['on']}",
            mem["narr"], 30, "Name tags pop in with their arrows to the objects (value and type shown, no addresses); when Python reads a name the arrow glows and the object lights up")
    else:
        c2 = ep["c2"]
        add("Concept slide", c2["label"], c2["on"], c2["narr"], 30, c2["anim"])
    if B:
        add("Code explain", B["label"], f"{B['file']}: {B['on']}", B["narr"], 40,
            "Second program or a twist on the first; \\[HL n\\] and \\[TRACK name=value\\] cues drive the variable tracker; output panel fills line by line with a ding per line")
    else:
        add("Code explain", A["label2"], f"{A['file']} again with the output panel on the right", A["narr2"], 40,
            "Same code; the output panel fills line by line with a ding per output line; \\[TRACK\\] cards update")
    term_say = ep["term"]
    rn = runp["file"].replace(".", " dot ")
    add("Terminal", "Run it", f"Terminal: python {runp['file']}",
        f"Save the file as {rn}. In the terminal, type python, space, {rn}. {term_say}", 20,
        "Dark-blue terminal: the command types with key-tick, output prints in mint with a ding")
    rec = ep["recap"]
    ords = ["One", "Two", "Three", "Four"]
    recap_narr = "Let us recap. " + " ".join(f"{ords[i]}: {r}" for i, r in enumerate(rec)) + " Pause the video, and say these ideas out loud, once, slowly."
    add("Concept slide", "Recap", f"Recap: {len(rec)} ideas on one card", recap_narr, 30,
        "Recap lines tick in one by one with a pop; Xecxec nods after each tick")
    add("Bug of the Day", bug["title"], f"BUG OF THE DAY: {bug['title']}", bug["narr"], 40,
        "Butter banner drops in with a buzzer; wrong code shakes; the Python error lines appear in tomato; the fix slides in and the terminal turns mint with a ding")
    add("Pun card", "Pun", ep["pun"], ep["pun"], 8,
        "Full tomato screen, card flips in with a rimshot, Xecxec snaps his claw", fixed=8)
    add("Challenge", "Challenge", f"Task card: {ep['task']}", f"Your challenge: {ep['challenge']} Comment your answer below.", 20,
        "Task card pops in; checklist ticks with a pop; Xecxec holds a tiny pen")
    nxt_line = (f"Next: EP {nxt['n']:02d} · {nxt['title']}" if nxt else ep["next_line"])
    nxt_say = (f"Next time: {nxt['spoken']}." if nxt else ep["next_say"])
    add("Outro", "Next episode", nxt_line, f"{nxt_say} Keep coding, says Xecxec!", 15,
        "Next-episode card slides up with a whoosh; right side stays empty for end-screen elements; sign-off text types in")

    t = 0
    for s in sc:
        s["len"] = s["fixed"] or need(s["narr"], s["min"])
        s["start"] = t
        t += s["len"]
    total = t
    if not 270 <= total <= 480:
        print(f"  note: EP {n} is {mmss(total)}")

    # chapters
    chap_idx = [(1, "Intro"), (2, sc[1]["label"]), (3, sc[2]["label"]), (4, sc[3]["label"]),
                (5, "Second program" if B else "Run it in your head"), (7, "Recap"), (8, "Bug of the Day"),
                (10, "Challenge"), (11, "Next episode")]
    chapters = " · ".join(f"{mmss(sc[i - 1]['start'])} {lab}" for i, lab in chap_idx)
    g = ep["goals"]
    desc = (f"In this episode you will {g[0]}, {g[1]} and {g[2]}, with Xecxec the crab. {chapters}")
    tags = BASE_TAGS + ep["tags"]

    L: list[str] = []
    L.append(f"## EP {n:02d} — {ep['title']}\n")
    prereq = f"EP {n - 1:02d}" if n > 1 else "none"
    L.append(f"**Module {mod['id']} · {mod['name']} · {mmss(total)} · {mod['colours']} · Prerequisite: {prereq}**\n")
    L.append("**Learning goals:** " + "; ".join(g) + ".\n")
    L.append("### YouTube\n")
    L.append(f"- **Title:** {ep['yt']} | Python Programming EP {n:02d}")
    L.append(f"- **Description:** {desc}")
    L.append(f"- **Tags:** {', '.join(tags)}")
    L.append(f"- **Thumbnail:** big text \"{ep['thumb']}\" in tomato on peach; {ep['vis']}; thin black border and drop shadow.\n")
    L.append("### Scene list\n")
    L.append("| # | Start | Length | Template | On screen | Animation & SFX |")
    L.append("| --- | --- | --- | --- | --- | --- |")
    for i, s in enumerate(sc, 1):
        L.append(f"| {i} | {mmss(s['start'])} | {mmss(s['len'])} | {s['t']} | {esc(s['on'])} | {s['anim']} |")
    L.append("\n### Narration script\n")
    for i, s in enumerate(sc, 1):
        L.append(f"**\\[{i} · {s['label']}\\]** {esc(s['narr'])}\n")

    L.append("### Code shown\n")
    for k, p in enumerate(progs, 1):
        scenes = "scene 3" if k == 1 else "scene 5"
        if k == 1 and not B:
            scenes = "scenes 3, 5"
        L.append(f"File {k}: {p['file']} ({scenes})\n")
        for fn, body in (p.get("files") or {}).items():
            L.append(f"**Input file {fn}:**\n\n```text\n{body.rstrip(chr(10))}\n```\n")
        if p.get("stdin"):
            L.append(f"**Typed input:** (the terminal scene shows these characters after the prompt, then Enter)\n\n```text\n{p['stdin'].rstrip(chr(10))}\n```\n")
        L.append(code_fence(p["src"]) + "\n")
        L.append("**Expected output:**\n")
        L.append(code_fence(pretty_run(p), "text") + "\n")
    for lab, body in ep.get("ref", []):
        L.append(f"**{lab} (reference only, not run in checks):**\n\n```text\n{body.rstrip(chr(10))}\n```\n")
    if has_mem:
        k = 1 if mem.get("from", "A") == "A" else 2
        p = progs[k - 1]
        block = cp.mem_block(p["src"], p["file"], mem["names"], p.get("stdin", ""), p.get("files"))
        L.append("### Memory boxes\n")
        L.append(f"**Memory from:** File {k} · names: {', '.join(mem['names'])}\n")
        L.append("Names are labels tied by arrows to objects (value and type shown, no addresses). Used in scene 4.\n")
        L.append(code_fence(block, "text") + "\n")

    L.append("### Bug of the Day\n")
    kind = bug.get("kind", "error")
    L.append(f"**Bug kind:** {kind} · **Bug file:** {bug.get('file', A['file'])}\n")
    bname = bug.get("file", A["file"])
    wrong = dd(bug["wrong"])
    bfiles, bstdin = bug.get("files") or {}, bug.get("stdin", "")
    rc, out, err, to = cp.run(wrong, bname, bstdin, bfiles, timeout=3 if kind == "hang" else 10)
    if kind == "error":
        if rc == 0 or to:
            raise SystemExit(f"EP {n}: bug code did not fail")
        shown = cp.norm(err)
        if bug.get("trim"):
            shown = "\n".join(shown.split("\n")[-bug["trim"]:])
            tr = f"**Trace trimmed:** last {bug['trim']} lines\n"
        else:
            tr = ""
        label = "Python output (exactly as Python prints it):"
    elif kind == "output":
        if rc != 0:
            raise SystemExit(f"EP {n}: bug output code failed: {err}")
        shown, tr, label = cp.norm(out), "", "Python output (it runs, but the answer is wrong):"
    else:
        if not to:
            raise SystemExit(f"EP {n}: hang bug did not hang")
        lines = cp.norm(out).split("\n")[:5]
        shown = "\n".join(lines + ["(the program never finishes; press Ctrl+C to stop)"])
        tr, label = "", "Python output (the first lines; it never stops by itself):"
    L.append(f"Wrong code ({bug['wrong_note']}):\n")
    for fn, body in bfiles.items():
        L.append(f"**Input file {fn}:**\n\n```text\n{body.rstrip(chr(10))}\n```\n")
    if bstdin:
        L.append(f"**Typed input:** (the terminal scene shows these characters after the prompt, then Enter)\n\n```text\n{bstdin.rstrip(chr(10))}\n```\n")
    L.append(code_fence(wrong) + "\n")
    if tr:
        L.append(tr)
    L.append(label + "\n")
    L.append(code_fence(shown, "text") + "\n")
    for fn, body in (bug.get("fixed_files") or {}).items():
        L.append(f"**Fixed input file {fn}:**\n\n```text\n{body.rstrip(chr(10))}\n```\n")
    L.append(f"Fixed code ({bug['fixed_note']}):\n")
    L.append(code_fence(dd(bug["fixed"])) + "\n")
    L.append(f"**Why:** {bug['why']}\n")

    L.append("### Pun & challenge\n")
    L.append(f"- **Pun:** \"{ep['pun']}\"")
    L.append(f"- **Challenge:** {ep['challenge']}")
    L.append(f"- **Challenge answer:** {ep['answer']}\n")

    L.append(f"### Shorts for EP {n:02d}\n")
    froms = ep.get("from", [[3], [4 if has_mem else 2], [3, 5], [8], [9, 10]])
    hs = ep["hash"]
    extra = [["#beginners"], ["#coding"], ["#learntocode"], ["#bugfix"], ["#codingchallenge", "#programmingjokes"]]
    for i, (st, script, on, cap) in enumerate(ep["shorts"]):
        sid = f"S{i + 1}"
        script = script.strip()
        closers = ["Try it in your own file and watch what happens.", "Pause the video and type it out yourself.",
                   "Say it out loud once, and it will stick.", "Then run it, and compare with what you predicted."]
        base = script
        k = 0
        while cp.words(base + " Keep coding, says Xecxec!" + (f" Full video: EP {n:02d}." if sid == "S5" else "")) < 62 and k < len(closers):
            base += " " + closers[(i + k) % len(closers)]
            k += 1
        script = base
        if "Keep coding, says Xecxec!" not in script:
            script += " Keep coding, says Xecxec!"
        if sid == "S5" and not script.endswith(f"Full video: EP {n:02d}."):
            script += f" Full video: EP {n:02d}."
        w = cp.words(script)
        length = math.ceil(w / 2) + 4
        hook = re.split(r"(?<=[.?!])\s", script, maxsplit=1)[0]
        scn = ", ".join(str(x) for x in froms[i])
        word = "scene" if len(froms[i]) == 1 else "scenes"
        tagl = " ".join(["#python", "#kodingkonkani"] + hs[:2 if sid != "S5" else 1] + extra[i])
        if not 35 <= length <= 45:
            PROBLEMS.append(f"EP {n} {sid}: {w} words = {length}s; need about 62-82 words")
        L.append(f"**{sid} · {st}** — {mmss(length)} · built from {word} {scn}")
        L.append(f"- **Hook (first 1.5s):** \"{hook}\"")
        L.append(f"- **Script:** {script}")
        L.append(f"- **On-screen text:** {on}")
        L.append(f"- **Caption + hashtags:** {cap} {tagl}\n")
    return "\n".join(L)


def build_module(name: str) -> int:
    m = importlib.import_module(name)
    mod, eps = m.MODULE, m.EPISODES
    nxt_mod = getattr(m, "NEXT_AFTER", None)
    out = [f"# Python Module {mod['id']} — {mod['name']}\n",
           f"Episodes {mod['range']} · {mod['colours']} · Every sample run with Python 3.13 "
           f"(PYTHONHASHSEED=0 so set and dict printing is repeatable); outputs and tracebacks are pasted from those runs.\n"]
    for i, ep in enumerate(eps):
        nxt = eps[i + 1] if i + 1 < len(eps) else None
        if nxt is None and nxt_mod:
            ep = dict(ep)
            ep["next_line"], ep["next_say"] = nxt_mod
        out.append(build_episode(mod, ep, nxt))
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
        rc |= build_module(a)
    sys.exit(rc)
