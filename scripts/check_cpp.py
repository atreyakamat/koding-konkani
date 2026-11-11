#!/usr/bin/env python3
"""Compile and run every C++ sample in docs/cpp-bible/m*.md and compare with the Bible.

For each episode it checks:
  * every "Code shown" file compiles with no warnings and prints the "Expected output";
  * the Bug of the Day wrong code behaves as the Bible says (compile error, warning,
    wrong output or run-time failure) and the compiler message lines match;
  * the Bug of the Day fixed code compiles with no warnings.

It reads only the Markdown, so it is independent of the generator.
It never edits docs/. It writes docs/cpp-bible/check-report.md.

Usage: python scripts/check_cpp.py [--cxx g++] [--std c++20] [--episode N] [--module m03]
Run it on the Windows PC with MSYS2 GCC 16 before you render. LC_ALL=C keeps quotes plain.
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIBLE = ROOT / "docs" / "cpp-bible"
TIMEOUT = 10
FLAGS = ["-Wall", "-Wextra", "-pthread"]
FENCE = re.compile(r"^```(\w*)\n(.*?)\n```[ \t]*$", re.S | re.M)
DIAG = re.compile(r"^(?P<file>[\w.\-]+):(?P<line>\d+):(?P<col>\d+): (?P<kind>error|warning): (?P<msg>.*)$")


@dataclass
class Run:
    compile_rc: int
    compile_out: str
    run_rc: int | None
    stdout: str
    stderr: str
    timed_out: bool


def norm(s: str) -> str:
    s = s.replace("‘", "'").replace("’", "'").replace("\r\n", "\n")
    return "\n".join(line.rstrip() for line in s.rstrip("\n").split("\n")) if s.strip() else ""


def compile_run(src: str, fname: str, stdin: str = "", files: dict[str, str] | None = None,
                cxx: str = "g++", std: str = "c++20", run: bool = True) -> Run:
    tmp = Path(tempfile.mkdtemp(prefix="cppbible-"))
    try:
        (tmp / fname).write_text(src, encoding="utf-8", newline="\n")
        for fn, body in (files or {}).items():
            (tmp / fn).write_text(body, encoding="utf-8", newline="\n")
        env = dict(os.environ, LC_ALL="C", LANG="C")
        exe = "prog.exe" if os.name == "nt" else "prog"
        c = subprocess.run([cxx, f"-std={std}", *FLAGS, fname, "-o", exe], cwd=tmp, env=env,
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        if c.returncode != 0 or not run:
            return Run(c.returncode, norm(c.stderr), None, "", "", False)
        try:
            r = subprocess.run([str(tmp / exe)], cwd=tmp, env=env, input=stdin, capture_output=True,
                               text=True, encoding="utf-8", errors="replace", timeout=TIMEOUT)
            return Run(0, norm(c.stderr), r.returncode, norm(r.stdout), norm(r.stderr), False)
        except subprocess.TimeoutExpired:
            return Run(0, norm(c.stderr), None, "", "", True)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def diag_lines(text: str) -> list[str]:
    """Only the 'file:line:col: error|warning: message' lines, as 'kind: message'."""
    out = []
    for line in text.split("\n"):
        m = DIAG.match(line)
        if m:
            out.append(f"{m['kind']}: {m['msg']}")
    return out


# ---------------------------------------------------------------- Markdown parsing
def parse_episodes(md: str) -> list[tuple[int, str, str]]:
    parts = re.split(r"^## EP (\d+) — (.+)$", md, flags=re.M)
    return [(int(parts[i]), parts[i + 1].strip(), parts[i + 2]) for i in range(1, len(parts) - 2, 3)]


def sections(body: str) -> dict[str, str]:
    parts = re.split(r"^### (.+)$", body, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


def fences_with_context(sec: str) -> list[tuple[str, str, str]]:
    """(preceding text, lang, content) for every fenced block in a section."""
    out, pos = [], 0
    for m in FENCE.finditer(sec):
        out.append((sec[pos:m.start()], m.group(1), m.group(2)))
        pos = m.end()
    return out


def code_files(sec: str) -> list[dict]:
    items = fences_with_context(sec)
    res: list[dict] = []
    pending_stdin = ""
    for ctx, lang, body in items:
        c = ctx.strip()
        if "Typed input" in c:
            pending_stdin = body + "\n"
        elif lang == "cpp":
            m = re.search(r"File \d+: (\S+)", c)
            res.append({"file": m.group(1) if m else "main.cpp", "src": body + "\n",
                        "stdin": pending_stdin, "expected": None})
            pending_stdin = ""
        elif "Expected output" in c and res:
            res[-1]["expected"] = body
    return res


def bug_info(sec: str) -> dict:
    items = fences_with_context(sec)
    info: dict = {"kind": "compile", "file": "bug.cpp", "wrong": None, "shown": "", "fixed": None, "stdin": ""}
    m = re.search(r"\*\*Bug kind:\*\* (\w+) · \*\*Bug file:\*\* (\S+)", sec)
    if m:
        info["kind"], info["file"] = m.group(1), m.group(2)
    for ctx, lang, body in items:
        c = ctx.strip()
        if "Typed input" in c:
            info["stdin"] = body + "\n"
        elif lang == "cpp" and "Wrong code" in c:
            info["wrong"] = body + "\n"
        elif lang == "cpp" and "Fixed code" in c:
            info["fixed"] = body + "\n"
        elif lang == "text" and info["wrong"] is not None and info["fixed"] is None:
            info["shown"] = body
    return info


@dataclass
class Result:
    ep: int
    title: str
    what: str
    status: str
    detail: str = ""


def check_episode(ep: int, title: str, body: str, cxx: str, std: str) -> list[Result]:
    res: list[Result] = []
    secs = sections(body)
    files = code_files(secs.get("Code shown", ""))
    if not files:
        res.append(Result(ep, title, "code", "NO-CODE", "no cpp fence in Code shown"))
    for f in files:
        r = compile_run(f["src"], f["file"], f["stdin"], cxx=cxx, std=std)
        what = f"code {f['file']}"
        if r.compile_rc != 0:
            res.append(Result(ep, title, what, "COMPILE-ERROR", "\n".join(diag_lines(r.compile_out)[:3])))
        elif r.compile_out:
            res.append(Result(ep, title, what, "WARNING", "\n".join(diag_lines(r.compile_out)[:3]) or r.compile_out[:200]))
        elif r.timed_out:
            res.append(Result(ep, title, what, "TIMEOUT"))
        elif r.run_rc != 0:
            res.append(Result(ep, title, what, "RUN-FAILED", f"rc={r.run_rc} {r.stderr[:200]}"))
        elif f["expected"] is None:
            res.append(Result(ep, title, what, "NO-EXPECTED"))
        elif norm(f["expected"]) != r.stdout:
            res.append(Result(ep, title, what, "OUTPUT-MISMATCH", f"expected:\n{f['expected']}\nactual:\n{r.stdout}"))
        else:
            res.append(Result(ep, title, what, "PASS"))
    bug = bug_info(secs.get("Bug of the Day", ""))
    if bug["wrong"] is None or bug["fixed"] is None:
        res.append(Result(ep, title, "bug", "NO-BUG", "wrong or fixed code missing"))
        return res
    wr = compile_run(bug["wrong"], bug["file"], bug["stdin"], cxx=cxx, std=std)
    kind = bug["kind"]
    what = f"bug-wrong[{kind}] {bug['file']}"
    shown_diag = diag_lines(norm(bug["shown"]))
    if kind == "compile":
        if wr.compile_rc == 0:
            res.append(Result(ep, title, what, "BUG-DID-NOT-FAIL"))
        else:
            actual = diag_lines(wr.compile_out)
            ok = bool(shown_diag) and all(s in actual for s in shown_diag)
            res.append(Result(ep, title, what, "PASS" if ok else "BUG-MESSAGE-DIFFERS",
                              "" if ok else f"shown: {shown_diag}\nactual: {actual}"))
    elif kind == "warn":
        actual = diag_lines(wr.compile_out)
        if wr.compile_rc != 0 or not actual:
            res.append(Result(ep, title, what, "BUG-NO-WARNING", wr.compile_out[:200]))
        else:
            ok = bool(shown_diag) and all(s in actual for s in shown_diag)
            res.append(Result(ep, title, what, "PASS" if ok else "BUG-MESSAGE-DIFFERS",
                              "" if ok else f"shown: {shown_diag}\nactual: {actual}"))
    elif kind == "output":
        if wr.compile_rc != 0 or wr.compile_out or wr.run_rc != 0:
            res.append(Result(ep, title, what, "BUG-NOT-CLEAN", (wr.compile_out or wr.stderr)[:200]))
        else:
            res.append(Result(ep, title, what, "PASS" if norm(bug["shown"]) == wr.stdout else "OUTPUT-MISMATCH",
                              f"shown:\n{bug['shown']}\nactual:\n{wr.stdout}"))
    elif kind == "runtime":
        if wr.compile_rc != 0:
            res.append(Result(ep, title, what, "COMPILE-ERROR", wr.compile_out[:200]))
        elif wr.timed_out or wr.run_rc == 0:
            res.append(Result(ep, title, what, "BUG-DID-NOT-FAIL"))
        else:
            first = norm(bug["shown"]).split("\n")[0]
            ok = bool(first) and first in wr.stderr
            res.append(Result(ep, title, what, "PASS" if ok else "BUG-MESSAGE-DIFFERS",
                              "" if ok else f"shown first line: {first}\nactual stderr: {wr.stderr[:300]}"))
    else:
        res.append(Result(ep, title, what, "BAD-KIND", kind))
    fr = compile_run(bug["fixed"], bug["file"], bug["stdin"], cxx=cxx, std=std)
    what = f"bug-fixed {bug['file']}"
    if fr.compile_rc != 0:
        res.append(Result(ep, title, what, "COMPILE-ERROR", "\n".join(diag_lines(fr.compile_out)[:3])))
    elif fr.compile_out:
        res.append(Result(ep, title, what, "WARNING", "\n".join(diag_lines(fr.compile_out)[:3])))
    elif fr.run_rc != 0 or fr.timed_out:
        res.append(Result(ep, title, what, "RUN-FAILED", fr.stderr[:200]))
    else:
        res.append(Result(ep, title, what, "PASS"))
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cxx", default="g++")
    ap.add_argument("--std", default="c++20")
    ap.add_argument("--episode", type=int)
    ap.add_argument("--module")
    ap.add_argument("--report", default=str(BIBLE / "check-report.md"))
    a = ap.parse_args()
    ver = subprocess.run([a.cxx, "--version"], capture_output=True, text=True).stdout.split("\n")[0]
    paths = sorted(BIBLE.glob(f"{a.module or 'm*'}.md"))
    results: list[Result] = []
    eps = 0
    for p in paths:
        for ep, title, body in parse_episodes(p.read_text(encoding="utf-8")):
            if a.episode and ep != a.episode:
                continue
            eps += 1
            rs = check_episode(ep, title, body, a.cxx, a.std)
            results.extend(rs)
            bad = [r for r in rs if r.status != "PASS"]
            print(f"EP {ep:02d} {title}: {'ok' if not bad else 'PROBLEMS'}")
            for r in bad:
                print(f"   {r.status} {r.what}: {r.detail[:300]}")
    fails = [r for r in results if r.status != "PASS"]
    lines = [f"# C++ Bible check report", "", f"Compiler: `{ver}` · flags `-std={a.std} {' '.join(FLAGS)}` · LC_ALL=C",
             f"Episodes: {eps} · checks: {len(results)} · passed: {len(results) - len(fails)} · not passed: {len(fails)}", ""]
    if fails:
        lines += ["| EP | Check | Status | Detail |", "| --- | --- | --- | --- |"]
        for r in fails:
            lines.append(f"| {r.ep} | {r.what} | {r.status} | {r.detail[:150].replace(chr(10), ' / ')} |")
    else:
        lines.append("All checks passed.")
    if not a.episode and not a.module:
        Path(a.report).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\n{eps} episodes, {len(results)} checks, {len(fails)} not passed ({ver})")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
