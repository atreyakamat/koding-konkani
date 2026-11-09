#!/usr/bin/env python3
"""Check the Python Bible: run every sample and compare with the text.

Usage: python scripts/check_py.py docs/python-bible/m00.md [more.md ...]

Per episode it checks:
  * every "Code shown" python fence runs and prints the "Expected output" fence;
  * the Bug of the Day wrong code fails with exactly the traceback shown
    (file name normalised), and the fixed code runs without error;
  * scene lengths add up to the header length and scene starts follow each other;
  * [HL n] cues point at a real line of the code on screen;
  * no emoji and no em-dash-free rule breaks (non-ASCII symbols are reported).
"""
from __future__ import annotations

import re
import subprocess
import sys
import tempfile
from pathlib import Path

FENCE = re.compile(r"```(\w+)\n(.*?)```", re.S)
EP_SPLIT = re.compile(r"^## EP (\d+) — (.+)$", re.M)


def to_sec(t: str) -> int:
    m, s = t.split(":")
    return int(m) * 60 + int(s)


def run(source: str, name: str) -> tuple[int, str]:
    with tempfile.TemporaryDirectory() as d:
        p = Path(d, name)
        p.write_text(source, encoding="utf-8")
        r = subprocess.run(
            [sys.executable, "-I", name], cwd=d, capture_output=True,
            text=True, timeout=30, env={"PYTHONIOENCODING": "utf-8", "PYTHONWARNINGS": "ignore"},
        )
        return r.returncode, (r.stdout if r.returncode == 0 else r.stderr).rstrip("\n")


def section(body: str, title: str) -> str:
    m = re.search(rf"^### {re.escape(title)}.*?$(.*?)(?=^### |\Z)", body, re.S | re.M)
    return m.group(1) if m else ""


def check_episode(ep: str, title: str, body: str) -> list[str]:
    errs: list[str] = []
    tag = f"EP {ep}"

    code = section(body, "Code shown")
    files = re.findall(r"^File \d+: (\S+\.py)", code, re.M)
    fences = FENCE.findall(code)
    pys = [f[1] for f in fences if f[0] == "python"]
    outs = [f[1] for f in fences if f[0] == "text"]
    if len(pys) != len(outs) or not pys:
        errs.append(f"{tag}: code fences and expected outputs do not pair up ({len(pys)} vs {len(outs)})")
    else:
        for i, (src, exp) in enumerate(zip(pys, outs)):
            name = files[i] if i < len(files) else "main.py"
            rc, out = run(src, name)
            if rc != 0 or out != exp.rstrip("\n"):
                errs.append(f"{tag}: {name} output mismatch\n  expected: {exp!r}\n  got:      {out!r}")

    name = files[0] if files else "main.py"
    bug = section(body, "Bug of the Day")
    bf = FENCE.findall(bug)
    if len(bf) != 3:
        errs.append(f"{tag}: Bug of the Day needs wrong code, traceback, fixed code")
    else:
        rc, err = run(bf[0][1], name)
        if rc == 0:
            errs.append(f"{tag}: bug code did not fail")
        else:
            got = re.sub(r'File ".*?([^/\\"]+)"', rf'File "{name}"', err)
            if got != bf[1][1].rstrip("\n"):
                errs.append(f"{tag}: traceback mismatch\n  expected: {bf[1][1]!r}\n  got:      {got!r}")
        rc, err = run(bf[2][1], name)
        if rc != 0:
            errs.append(f"{tag}: fixed code fails: {err!r}")

    # timing
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

    # HL cues
    for n in {int(x) for x in re.findall(r"\\\[HL (\d+)\\\]", section(body, "Narration script"))}:
        if pys and n > max(len(s.splitlines()) for s in pys):
            errs.append(f"{tag}: [HL {n}] is past the last code line")

    # style
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
