#!/usr/bin/env python3
"""Check the Python Bible: run every sample and compare it with the text.

Usage: python scripts/check_py.py docs/python-bible/m00.md [more.md ...]

Per episode it checks:
  * every "Code shown" file runs (with its input files and typed input) and
    prints exactly the "Expected output";
  * the Bug of the Day behaves as stated: "error" fails with exactly the
    traceback shown, "output" runs and prints the wrong result, "hang" keeps
    running (the shown lines are the start of its output); the fixed code runs;
  * Memory boxes data is re-derived from the real objects (shared objects are
    grouped, no addresses);
  * scene lengths add up to the header and scene starts follow each other;
  * [HL n] cues point at a real line and [TRACK name=value] cues name a value
    the variable really holds while the code runs;
  * the Bug narration names the error that Python raises;
  * every Short is 35-45 s (script words at 120 a minute + 4 s lead-in and end badge) and its length label is right;
  * no emoji or unusual symbols.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

EP_SPLIT = re.compile(r"^## EP (\d+) — (.+)$", re.M)
ADDR = re.compile(r"0x[0-9a-fA-F]{6,}")
FILE_LINE = re.compile(r'File "([^"]+)"')

TRACER = r'''
import sys, json
src = open(sys.argv[1], encoding="utf-8").read()
want = json.loads(sys.argv[2])
rec = {}
def simple(v):
    return isinstance(v, (int, float, str, bool, type(None), list, tuple, dict, set, frozenset))
def add(frame):
    if frame.f_code.co_filename != sys.argv[1]:
        return
    for k, v in list(frame.f_locals.items()):
        if k.startswith("__") or not simple(v):
            continue
        s = rec.setdefault(k, set())
        s.add(repr(v))
        s.add(str(v))
def tr(frame, ev, arg):
    if ev in ("line", "return", "call"):
        add(frame)
    return tr
g = {"__name__": "__main__", "__file__": sys.argv[1]}
sys.settrace(tr)
try:
    exec(compile(src, sys.argv[1], "exec"), g)
finally:
    sys.settrace(None)
mem = {}
for n in want:
    if n in g:
        v = g[n]
        mem[n] = [repr(v), type(v).__name__, id(v)]
sys.stderr.write("@@TRACE" + json.dumps({"rec": {k: sorted(v) for k, v in rec.items()}, "mem": mem}))
'''


def _env(extra: str = "") -> dict[str, str]:
    return {"PYTHONPATH": extra, "PYTHONIOENCODING": "utf-8", "PYTHONHASHSEED": "0", "PYTHONUNBUFFERED": "1", "PYTHONWARNINGS": "ignore",
            "PATH": os.environ.get("PATH", "")}


def _setup(d: str, files: dict[str, str]) -> None:
    for n, body in files.items():
        Path(d, n).write_text(body, encoding="utf-8")


def norm(s: str) -> str:
    s = s.replace("\r\n", "\n").rstrip("\n")
    s = FILE_LINE.sub(lambda m: f'File "{os.path.basename(m.group(1))}"', s)
    return ADDR.sub("0x...", s)


def run(src: str, name: str, stdin: str = "", files: dict[str, str] | None = None,
        timeout: float = 10) -> tuple[int, str, str, bool]:
    """Run one program. Returns (returncode, stdout, stderr, timed_out)."""
    with tempfile.TemporaryDirectory() as d:
        _setup(d, files or {})
        Path(d, name).write_text(src, encoding="utf-8")
        try:
            r = subprocess.run([sys.executable, "-s", "-P", name], cwd=d, input=stdin, capture_output=True,
                               text=True, timeout=timeout, env=_env(d if files else ""))
            return r.returncode, r.stdout, r.stderr, False
        except subprocess.TimeoutExpired as e:
            out = e.stdout.decode() if isinstance(e.stdout, bytes) else (e.stdout or "")
            return -1, out, "", True


def trace(src: str, name: str, names: list[str], stdin: str = "",
          files: dict[str, str] | None = None) -> dict:
    with tempfile.TemporaryDirectory() as d:
        _setup(d, files or {})
        Path(d, name).write_text(src, encoding="utf-8")
        Path(d, "_tracer.py").write_text("import os\n" + TRACER, encoding="utf-8")
        r = subprocess.run([sys.executable, "-s", "-P", "_tracer.py", name, json.dumps(names)], cwd=d,
                           input=stdin, capture_output=True, text=True, timeout=30, env=_env(d if files else ""))
        m = re.search(r"@@TRACE(.*)$", r.stderr, re.S)
        if not m:
            raise RuntimeError(f"trace failed for {name}: {r.stderr[-300:]}")
        return json.loads(m.group(1))


IMMUTABLE = ("int", "str", "float", "bool", "NoneType", "tuple", "frozenset")


def mem_block(src: str, name: str, names: list[str], stdin: str = "",
              files: dict[str, str] | None = None) -> str:
    t = trace(src, name, names, stdin, files)["mem"]
    groups: list[tuple[list[str], str, str]] = []
    seen: dict[int, int] = {}
    for n in names:
        if n not in t:
            raise RuntimeError(f"memory name {n!r} not found in {name}")
        rep, typ, oid = t[n]
        if oid in seen and typ not in IMMUTABLE:
            groups[seen[oid]][0].append(n)
        else:
            seen[oid] = len(groups)
            groups.append(([n], rep, typ))
    w = max(len(", ".join(g[0])) for g in groups)
    return "\n".join(f"{', '.join(g[0]).ljust(w)}  ->  {g[1]}   ({g[2]})" for g in groups)


def to_sec(t: str) -> int:
    m, s = t.split(":")
    return int(m) * 60 + int(s)


def words(text: str) -> int:
    text = re.sub(r"\\?\[(HL|TRACK)[^\]]*\\?\]", " ", text)
    return len(re.findall(r"[A-Za-z0-9'’.-]+", text))


def blocks(chunk: str) -> list[tuple[str, str, str]]:
    """(label, lang, body) for each fence; label = last non-empty line before it."""
    out = []
    lines = chunk.split("\n")
    i = 0
    label = ""
    while i < len(lines):
        ln = lines[i]
        if ln.startswith("```"):
            lang = ln[3:].strip()
            j = i + 1
            body = []
            while j < len(lines) and not lines[j].startswith("```"):
                body.append(lines[j])
                j += 1
            out.append((label, lang, "\n".join(body)))
            label = ""
            i = j + 1
            continue
        if ln.strip():
            label = ln.strip()
        i += 1
    return out


def section(body: str, title: str) -> str:
    m = re.search(rf"^### {re.escape(title)}.*?$(.*?)(?=^### |\Z)", body, re.S | re.M)
    return m.group(1) if m else ""


def spoken_variants(err: str) -> list[str]:
    words_ = re.sub(r"(?<!^)(?=[A-Z])", " ", err).lower()
    v = [words_, err.lower()]
    alias = {
        "ZeroDivisionError": ["division by zero", "divide by zero", "zero division error"],
        "UnboundLocalError": ["unbound local"],
        "ModuleNotFoundError": ["module not found"],
        "FileNotFoundError": ["file not found"],
        "JSONDecodeError": ["json decode error"],
    }
    return v + alias.get(err, [])


def parse_files(chunk: str) -> tuple[dict[str, str], str]:
    files, stdin = {}, ""
    for label, lang, body in blocks(chunk):
        m = re.match(r"\*\*Input file (\S+?):\*\*", label)
        if m:
            files[m.group(1)] = body + "\n"
        elif label.startswith("**Typed input:**"):
            stdin = body + "\n"
    return files, stdin


def check_episode(ep: str, title: str, body: str) -> list[str]:
    errs: list[str] = []
    tag = f"EP {ep}"

    # ---- code shown
    code = section(body, "Code shown")
    parts = re.split(r"^(File \d+: \S+\.py.*)$", code, flags=re.M)
    progs: list[dict] = []
    for i in range(1, len(parts), 2):
        head, chunk = parts[i], parts[i + 1]
        name = re.match(r"File \d+: (\S+\.py)", head).group(1)
        bl = blocks(chunk)
        pys = [b for b in bl if b[1] == "python"]
        exp = [b for b in bl if b[0].startswith("**Expected output")]
        files, stdin = parse_files(chunk)
        if len(pys) != 1 or len(exp) != 1:
            errs.append(f"{tag}: {name} needs one python fence and one expected-output fence")
            continue
        src, want = pys[0][2] + "\n", exp[0][2]
        rc, out, err, to = run(src, name, stdin, files)
        if rc != 0 or norm(out) != norm(want):
            errs.append(f"{tag}: {name} output mismatch\n  expected: {want!r}\n  got:      {norm(out) if rc == 0 else norm(err)!r}")
        progs.append({"name": name, "src": src, "stdin": stdin, "files": files})
    if not progs:
        errs.append(f"{tag}: no runnable code in 'Code shown'")

    # ---- memory boxes
    mem = section(body, "Memory boxes")
    if mem.strip():
        m = re.search(r"\*\*Memory from:\*\* File (\d+)\s*·\s*names: (.+)", mem)
        bl = blocks(mem)
        if not m or not bl:
            errs.append(f"{tag}: Memory boxes block malformed")
        else:
            k = int(m.group(1)) - 1
            names = [n.strip() for n in m.group(2).split(",")]
            try:
                got = mem_block(progs[k]["src"], progs[k]["name"], names, progs[k]["stdin"], progs[k]["files"])
                if got != bl[0][2]:
                    errs.append(f"{tag}: memory boxes differ from the real objects\n  expected: {bl[0][2]!r}\n  got:      {got!r}")
            except Exception as e:  # noqa: BLE001
                errs.append(f"{tag}: memory boxes could not be derived: {e}")
            if re.search(r"0x[0-9a-f]+", bl[0][2]):
                errs.append(f"{tag}: memory boxes must not show addresses")

    # ---- bug
    bug = section(body, "Bug of the Day")
    kind = (re.search(r"\*\*Bug kind:\*\* (\w+)", bug) or [None, "error"])[1]
    trimm = re.search(r"\*\*Trace trimmed:\*\* last (\d+) lines", bug)
    bl = blocks(bug)
    pys = [b for b in bl if b[1] == "python"]
    outs = [b for b in bl if b[1] == "text" and not b[0].startswith(("**Input file", "**Typed input", "**Fixed input file"))]
    bfiles, bstdin = parse_files(bug)
    name = progs[0]["name"] if progs else "main.py"
    bf_m = re.search(r"\*\*Bug file:\*\* (\S+)", bug)
    if bf_m:
        name = bf_m.group(1)
    spoken_err = ""
    if len(pys) != 2 or len(outs) != 1:
        errs.append(f"{tag}: Bug of the Day needs wrong code, one output, fixed code")
    else:
        rc, out, err, to = run(pys[0][2] + "\n", name, bstdin, bfiles, timeout=3 if kind == "hang" else 10)
        want = outs[0][2]
        if kind == "error":
            if rc == 0 or to:
                errs.append(f"{tag}: bug code did not fail")
            else:
                got = norm(err)
                if trimm:
                    got = "\n".join(got.split("\n")[-int(trimm.group(1)):])
                if got != want.rstrip("\n"):
                    errs.append(f"{tag}: traceback mismatch\n  expected: {want!r}\n  got:      {got!r}")
                spoken_err = norm(err).split("\n")[-1].split(":")[0].strip().split(".")[-1]
        elif kind == "output":
            if rc != 0 or norm(out) != want.rstrip("\n"):
                errs.append(f"{tag}: bug output mismatch\n  expected: {want!r}\n  got:      {norm(out)!r}")
        elif kind == "hang":
            if not to:
                errs.append(f"{tag}: bug code was expected to hang")
            else:
                first = [ln for ln in want.split("\n") if not ln.startswith("(")]
                if not norm(out).startswith("\n".join(first)):
                    errs.append(f"{tag}: hang output does not start with the shown lines")
        else:
            errs.append(f"{tag}: unknown bug kind {kind}")
        ffiles = dict(bfiles)
        for label, lang, fbody in blocks(bug):
            m = re.match(r"\*\*Fixed input file (\S+?):\*\*", label)
            if m:
                ffiles[m.group(1)] = fbody + "\n"
        rc, out, err, to = run(pys[1][2] + "\n", name, bstdin, ffiles)
        if rc != 0 or to:
            errs.append(f"{tag}: fixed code fails: {err[-200:]!r}")

    narr = section(body, "Narration script")
    scenes = {int(n): txt for n, txt in re.findall(r"\*\*\\\[(\d+) · [^\]]*?\\\]\*\* (.*?)(?=\n\n\*\*\\\[|\Z)", narr, re.S)}
    if kind == "error" and spoken_err:
        t8 = re.sub(r"[^a-z ]", "", scenes.get(8, "").lower())
        if not any(v in t8 for v in spoken_variants(spoken_err)):
            errs.append(f"{tag}: bug narration never names the error ({spoken_err})")

    # ---- cues
    for sc, fi in ((3, 0), (5, 1 if len(progs) > 1 else 0)):
        if sc not in scenes or fi >= len(progs):
            continue
        n_lines = len(progs[fi]["src"].rstrip("\n").split("\n"))
        for n in {int(x) for x in re.findall(r"\\\[HL (\d+)\\\]", scenes[sc])}:
            if n > n_lines:
                errs.append(f"{tag}: scene {sc} [HL {n}] is past the last line ({n_lines})")
        tracks = re.findall(r"\\\[TRACK (\w+)=(.*?)\\\]", scenes[sc])
        if tracks:
            p = progs[fi]
            try:
                rec = trace(p["src"], p["name"], [], p["stdin"], p["files"])["rec"]
            except Exception as e:  # noqa: BLE001
                errs.append(f"{tag}: trace failed: {e}")
                rec = {}
            for nm, val in tracks:
                vals = rec.get(nm)
                if vals is None:
                    errs.append(f"{tag}: scene {sc} [TRACK {nm}] names a variable the code never sets")
                elif val not in vals and val.strip("'\"") not in vals:
                    errs.append(f"{tag}: scene {sc} [TRACK {nm}={val}] is never true; values seen: {vals[:6]}")

    # ---- timing
    head = re.search(r"\*\*Module \d+ · .*? · (\d+:\d\d) ·", body)
    rows = re.findall(r"^\| (\d+) \| (\d+:\d\d) \| (\d+:\d\d) \|", body, re.M)
    if head and rows:
        total = sum(to_sec(r[2]) for r in rows)
        if total != to_sec(head.group(1)):
            errs.append(f"{tag}: scene lengths sum to {total}s, header says {head.group(1)}")
        t = 0
        for n, start, length in rows:
            if to_sec(start) != t:
                errs.append(f"{tag}: scene {n} starts {start}, expected {t // 60}:{t % 60:02d}")
            t += to_sec(length)

    # ---- shorts: 35-45 s at 120 words a minute
    for sid, mins, secs, script in re.findall(
            r"^\*\*(S\d) · .*? — (\d+):(\d\d) · .*?\n- \*\*Hook.*?\n- \*\*Script:\*\* (.*?)\n", body, re.M | re.S):
        n = words(script)
        length = int(mins) * 60 + int(secs)
        if not 35 <= length <= 45 or abs(-(-n // 2) + 4 - length) > 0:
            errs.append(f"{tag}: {sid} has {n} words (= {-(-n // 2) + 4}s with 4 s of lead-in and badge) but is labelled {mins}:{secs}; need 35-45 s")

    # ---- style
    for ch in set(body):
        if ord(ch) > 0x2FFF or 0x1F300 <= ord(ch) <= 0x1FAFF:
            errs.append(f"{tag}: suspicious symbol {ch!r}")
    return errs


def main(paths: list[str]) -> int:
    all_errs: list[str] = []
    count = 0
    for p in paths:
        text = Path(p).read_text(encoding="utf-8")
        parts = EP_SPLIT.split(text)
        for i in range(1, len(parts), 3):
            count += 1
            all_errs += check_episode(parts[i], parts[i + 1], parts[i + 2])
    for e in all_errs:
        print("FAIL", e)
    print(f"{count} episodes checked, {len(all_errs)} problems")
    return 1 if all_errs else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]) if len(sys.argv) > 1 else 2)
