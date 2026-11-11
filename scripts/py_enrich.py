#!/usr/bin/env python3
"""Adds the Remotion-ready fields to episodes-python/epNNN.json (run after bible_to_json.py --lang python).

Why: the scene components were built for the C course and guess their props from free text. Python scenes
get explicit data instead, so nothing is guessed:
  scene.props   explicit component props (lines, command, terminal lines, bug panel, illustration ...)
  scene.memory  memory-boxes frames (names tied to objects), built from the Bible's "Memory boxes" block
  episode.course = "python"

Usage: python3 scripts/py_enrich.py          (rewrites episodes-python/*.json; idempotent)
"""
from __future__ import annotations

import ast
import difflib
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EP_DIR = ROOT / "episodes-python"
BIBLE = ROOT / "docs" / "python-bible"
ILL_DIR = BIBLE / "illustrations"

MAX_TERMINAL_ROWS = 6
NUMBER_WORDS = ["One", "Two", "Three", "Four", "Five"]


# ---------------------------------------------------------------- text helpers
def strip_md(t: str) -> str:
    t = re.sub(r"\\([\\`*_{}\[\]()#+\-.!|<>~^$%&@:;,/?'\"=])", r"\1", t)
    return t.replace("`", "").strip()


def sentences(t: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.?!])\s+", re.sub(r"\[(?:HL|TRACK)[^\]]*\]", "", t).strip()) if s.strip()]


def clip(t: str, n: int) -> str:
    t = t.strip()
    if len(t) <= n:
        return t
    cut = re.split(r"[,:;]\s", t)[0]
    if 12 <= len(cut) <= n:
        return cut
    return t[: n - 1].rstrip() + "…"


# ---------------------------------------------------------------- code files
def pick_file(ep: dict, name: str) -> dict | None:
    for k in ep["codeFiles"]:
        if k["file"] == name:
            return k
    return None


def transcript(k: dict) -> list[str]:
    """Terminal text for one program: expected output with the typed input placed after each prompt."""
    out = k.get("output", "")
    stdin = [l for l in (k.get("stdin") or "").split("\n") if l != ""]
    if not stdin:
        return out.split("\n") if out else []
    prompts = re.findall(r"input\(\s*(?P<q>[\"'])(?P<p>.*?)(?P=q)\s*\)", k["source"])
    text = out
    pos = 0
    for (q, p), typed in zip(prompts, stdin):
        i = text.find(p, pos) if p else pos
        if i < 0:
            break
        end = i + len(p)
        text = text[:end] + typed + "\n" + text[end:]
        pos = end + len(typed) + 1
    return text.rstrip("\n").split("\n")


# ---------------------------------------------------------------- scenes
def concept_lines(scene: dict) -> tuple[list[str], dict | None]:
    m = re.match(r'^"?(?P<title>[^":]{2,60})"?:\s*three numbered lines \((?P<pts>.*?)\)(?: and an analogy card:\s*(?P<body>.*))?$', scene["onScreen"])
    if not m:
        # Module 0 (hand-written): the text names the analogy but does not list the lines. Use the narration.
        a = re.search(r"three numbered lines and (?:an? )?(?P<what>.+?)(?: on the right)?$", scene["onScreen"])
        analogy = {"title": "Think of it like this", "body": a.group("what").strip().capitalize()} if a else None
        return diagram_lines(scene), analogy
    pts = re.split(r";\s*(?=\d\.\s)", m.group("pts"))
    lines = [re.sub(r"^\d\.\s*", "", p).strip() for p in pts]
    analogy = None
    if m.group("body"):
        analogy = {"title": "Think of it like this", "body": m.group("body").strip()}
    return lines, analogy


def cap(t: str) -> str:
    return t[:1].upper() + t[1:]


def recap_lines(scene: dict, shown: list[str] | None) -> list[str]:
    """Recap card text: the Bible's "On-screen recap" list when it has one, else the first sentence of each
    numbered item of the narration (module 0, written by hand)."""
    if shown:
        return [cap(x) for x in shown[:4]]
    text = re.sub(r"\[(?:HL|TRACK)[^\]]*\]", "", scene["narration"])
    parts = re.split(r"\b(?:One|Two|Three|Four|Five):\s*", text)[1:]
    items = [re.split(r"(?<=[.?!])\s+", p.strip())[0].strip() for p in parts]
    if not items:
        raise ValueError("recap narration has no numbered items")
    return [cap(x) for x in items[:4]]


def diagram_lines(scene: dict) -> list[str]:
    """Up to three short lines for a diagram slide: whole sentences of the narration that fit one or two rows;
    when fewer than two qualify, their comma-separated clauses. Nothing is cut mid-sentence."""
    sents = [s for s in sentences(scene["narration"]) if len(s.split()) >= 3]
    short = [s for s in sents if len(s) <= 52]
    if len(short) < 2:
        for s in sents:
            for c in re.split(r",\s+", s):
                c = c.strip().rstrip(".") + "."
                if 12 <= len(c) <= 52 and c not in short:
                    short.append(c)
    if not short:
        short = [clip(sents[0], 52)] if sents else ["Watch the picture."]
    return short[:3]


def terminal_lines(ep: dict, scene: dict) -> list[dict]:
    m = re.search(r"python\s+([\w./-]+\.py)", scene["onScreen"])
    if not m:
        raise ValueError(f"EP{ep['ep']}: terminal scene has no 'python file.py' command")
    name = m.group(1)
    k = pick_file(ep, name)
    if not k:
        raise ValueError(f"EP{ep['ep']}: terminal runs {name} but no such code file")
    rows = transcript(k)
    lines = [{"text": f"python {name}", "kind": "input"}]
    body = rows[: MAX_TERMINAL_ROWS - 1] if len(rows) > MAX_TERMINAL_ROWS - 1 else rows
    lines += [{"text": r if r else " ", "kind": "output"} for r in body]
    if len(rows) > len(body):
        lines.append({"text": "…", "kind": "output"})
    return lines


CODE_HINT = re.compile(r"[=()\[\]:#]|^\s*(import|from|def|class|for|while|if|print)\b", re.M)


def looks_code(t: str) -> bool:
    t = t.strip()
    if "\n" in t:
        return True
    words = t.split()
    if t.endswith(".") and len(words) > 4 and not re.search(r"[=()]", t):
        return False
    return bool(CODE_HINT.search(t))


def first_diff(wrong: str, fixed: str) -> tuple[int | None, int | None]:
    a, b = wrong.split("\n"), fixed.split("\n")
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag == "equal":
            continue
        w = i1 + 1 if i2 > i1 else min(i1 + 1, len(a))
        f = j1 + 1 if j2 > j1 else min(j1 + 1, len(b))
        return w, f
    return None, None


def bug_props(ep: dict, scene: dict, files: list[dict]) -> dict:
    bug = ep["bug"]
    err = bug["error"].strip()
    parts = re.split(r"\n\s*\nPython output \(", err, maxsplit=1)
    if len(parts) == 2:
        head, rest = parts
        typed = head.strip()
        body = rest.split("):", 1)[1].strip() if "):" in rest else rest
        kind_text = rest.split("):", 1)[0]
    else:
        m = re.match(r"Python output \((.*?)\):\s*(.*)$", err, re.S)
        typed = ""
        kind_text = m.group(1) if m else ""
        body = m.group(2).strip() if m else err
    wrong, fixed = bug["wrong"], bug["fixed"]
    culprit: dict = {}
    override: dict
    fname = files[0]["file"] if files else "program.py"
    cmd = f"python {fname}"
    if "never finishes" in body:
        override = {"lines": [], "hang": True, "caption": "no output: the program waits for ever"}
        w, f = first_diff(wrong, fixed)
    elif re.search(r"Traceback|File \".*\", line \d+", body):
        tb = [l.rstrip() for l in body.split("\n") if l.strip()]
        if tb and tb[0].startswith("Traceback"):
            tb = tb[1:]
        # Keep the location line, the code echo and the exception line (at most 4 rows).
        override = {"lines": tb[-4:] if len(tb) > 4 else tb}
        lm = re.search(r'File ".*?", line (\d+)', body)
        w = int(lm.group(1)) if lm else None
        _, f = first_diff(wrong, fixed)
    else:
        rows = [l for l in body.split("\n")]
        override = {"lines": rows[:3], "caption": "wrong output" if "wrong" in kind_text else ""}
        w, f = first_diff(wrong, fixed)
    if w:
        culprit["wrong"] = w
    if f:
        culprit["fixed"] = f
    p: dict = {
        "wrongCode": strip_md(wrong) if not looks_code(wrong) else wrong,
        "fixedCode": strip_md(fixed) if not looks_code(fixed) else fixed,
        "error": "\n".join(override["lines"]),
        "errorOverride": override,
        "why": strip_md(bug["why"]),
        "wrongIsCode": looks_code(wrong),
        "fixedIsCode": looks_code(fixed),
        "lang": "python",
        "command": cmd,
    }
    if culprit:
        p["culprit"] = culprit
    return p


# ---------------------------------------------------------------- memory
def recap_blocks() -> dict[int, list[str]]:
    out: dict[int, list[str]] = {}
    for f in sorted(glob.glob(str(BIBLE / "m*.md"))):
        t = Path(f).read_text(encoding="utf-8")
        for m in re.finditer(r"^## EP (\d+) —.*?(?=^## EP |\Z)", t, re.S | re.M):
            mm = re.search(r"### On-screen recap\n(.*?)(?=^### )", m.group(0), re.S | re.M)
            if mm:
                items = re.findall(r"^\d+\.\s+(.+)$", mm.group(1), re.M)
                if items:
                    out[int(m.group(1))] = items
    return out


def memory_blocks() -> dict[int, list[str]]:
    mem: dict[int, list[str]] = {}
    for f in sorted(glob.glob(str(BIBLE / "m*.md"))):
        t = Path(f).read_text(encoding="utf-8")
        for m in re.finditer(r"^## EP (\d+) —.*?(?=^## EP |\Z)", t, re.S | re.M):
            mm = re.search(r"### Memory boxes.*?```text\n(.*?)\n```", m.group(0), re.S)
            if mm:
                mem[int(m.group(1))] = mm.group(1).split("\n")
    return mem


def cells_for(rep: str, typ: str) -> list[dict]:
    """One cell per element for small lists, tuples, sets and dicts of simple values; else one cell."""
    def short(v: object) -> str:
        s = repr(v) if not isinstance(v, str) else repr(v)
        return s if len(s) <= 14 else s[:13] + "…"

    try:
        obj = ast.literal_eval(rep)
    except Exception:  # noqa: BLE001  (an object repr, Counter(...) and so on)
        obj = None
    simple = (int, float, str, bool, type(None))
    if isinstance(obj, (list, tuple, set)) and 1 <= len(obj) <= 8 and all(isinstance(v, simple) for v in obj):
        return [{"value": short(v), "index": i} for i, v in enumerate(obj)]
    if isinstance(obj, dict) and 1 <= len(obj) <= 6 and all(isinstance(v, simple) for v in obj.values()):
        return [{"value": short(v), "index": str(k)} for k, v in obj.items()]
    return [{"value": rep if len(rep) <= 30 else rep[:29] + "…", "address": typ}]


def memory_frames(lines: list[str]) -> dict:
    groups: list[dict] = []
    for ln in lines:
        m = re.match(r"^(?P<names>.+?)\s+->\s+(?P<rep>.+?)\s+\((?P<typ>[\w.]+)\)$", ln)
        if not m:
            raise ValueError(f"cannot parse memory line: {ln!r}")
        names = [n.strip() for n in m.group("names").split(",")]
        cells = cells_for(m.group("rep"), m.group("typ"))
        if len(cells) > 1:
            cells[0].setdefault("address", m.group("typ"))
        g: dict = {"name": names[0], "cells": cells}
        if len(names) > 1:
            g["tags"] = names[1:4]
        if len(cells) == 1:
            g["cells"][0]["name"] = names[0] if len(names) == 1 else ", ".join(names[:3])
            g.pop("name")
            g.pop("tags", None)
        groups.append(g)
    frames = [{"groups": groups[: i + 1]} for i in range(len(groups))]
    return {"frames": frames}


# ---------------------------------------------------------------- main
def enrich(ep: dict, mem: dict[int, list[str]], recaps: dict[int, list[str]], titles: dict[int, str]) -> None:
    ep["course"] = "python"
    n = ep["ep"]
    illustration = None
    ill_path = ILL_DIR / f"ep{n:03d}.json"
    if ill_path.exists():
        illustration = json.loads(ill_path.read_text(encoding="utf-8"))
    code_scenes = [s for s in ep["scenes"] if s["template"] == "code-explain"]
    for s in ep["scenes"]:
        s.pop("props", None)
        s.pop("memory", None)
        t = s["template"]
        if t == "concept-slide":
            if s["id"] == 2:
                lines, analogy = concept_lines(s)
                s["props"] = {"lines": lines, **({"analogy": analogy} if analogy else {})}
            elif s["id"] == 7:
                s["props"] = {"lines": recap_lines(s, recaps.get(n)), "analogy": None}
            else:
                props: dict = {"lines": diagram_lines(s), "analogy": None}
                if illustration:
                    props["illustration"] = illustration
                s["props"] = props
        elif t == "code-explain":
            code = s.get("code") or next(c for c in ep["codeFiles"] if c["file"].startswith(s["onScreen"].split(":")[0]))
            k = pick_file(ep, code["file"]) or {"file": code["file"], "source": code["source"], "output": code.get("output", "")}
            out = "\n".join(transcript(k)) if k.get("output") else None
            s["props"] = {"lang": "python", "command": f"python {code['file']}", **({"output": out} if out else {})}
        elif t == "terminal":
            s["props"] = {"lines": terminal_lines(ep, s)}
        elif t == "bug-of-the-day":
            s["props"] = bug_props(ep, s, ep["codeFiles"])
        elif t == "memory-boxes":
            if n not in mem:
                raise ValueError(f"EP{n}: memory scene but no Memory boxes block in the Bible")
            s["memory"] = memory_frames(mem[n])
        elif t == "outro":
            nxt = titles.get(n + 1)
            s["props"] = {"nextEp": n + 1, **({"nextTitle": nxt} if nxt else {"finaleLine": f"{len(titles)} episodes. You did it."})}
    del code_scenes


def main() -> int:
    files = sorted(EP_DIR.glob("ep*.json"))
    eps = [json.loads(f.read_text(encoding="utf-8")) for f in files]
    titles = {e["ep"]: e["title"] for e in eps}
    mem = memory_blocks()
    recaps = recap_blocks()
    bad = 0
    for f, ep in zip(files, eps):
        try:
            enrich(ep, mem, recaps, titles)
        except Exception as exc:  # noqa: BLE001
            print(f"EP{ep['ep']:02d}: {exc}")
            bad += 1
            continue
        f.write_text(json.dumps(ep, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"enriched {len(files) - bad} of {len(files)} episodes")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
