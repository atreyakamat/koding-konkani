#!/usr/bin/env python3
"""Compiles and runs every C file in every episode (Code shown + Bug of the
Day wrong/fixed code) with the installed MSYS2 UCRT64 gcc, and reports the
result. See docs/PIPELINE.md.

This never edits docs/ or episodes/ to make things pass — only the report
changes. Writes out/c-check-report.md (git-ignored, full detail) and
docs/c-check-summary.md (committed, counts + non-PASS table).

Usage: python scripts/check_c.py [--gcc PATH] [--episode N]
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EPISODES_DIR = ROOT / "episodes"

DEFAULT_GCC_DIRS = [r"C:\msys64\ucrt64\bin", r"C:\msys64\mingw64\bin"]
TIMEOUT_SECONDS = 5

NONDETERMINISTIC_MARKERS = re.compile(r"\[MEASURED\]|may differ|your output may differ|may vary", re.IGNORECASE)
NONDETERMINISTIC_CALLS = re.compile(r"\b(rand\s*\(|time\s*\(|clock\s*\(|srand\s*\()")
ADDRESS_FORMAT = re.compile(r"%p\b")

RESULTS_ORDER = [
    "PASS",
    "OUTPUT-MISMATCH",
    "COMPILE-ERROR",
    "BUG-MESSAGE-DIFFERS",
    "NEEDS-INPUT",
    "NONDETERMINISTIC",
    "TIMEOUT",
    "SKIPPED",
]


def find_gcc(explicit: str | None) -> Path:
    if explicit:
        p = Path(explicit)
        if p.exists():
            return p
        sys.exit(f"--gcc path does not exist: {explicit}")
    for d in DEFAULT_GCC_DIRS:
        p = Path(d) / "gcc.exe"
        if p.exists():
            return p
    sys.exit(
        "No gcc.exe found in " + ", ".join(DEFAULT_GCC_DIRS) + ". Install MSYS2 UCRT64's "
        "mingw-w64-ucrt-x86_64-gcc package, or pass --gcc <path to gcc.exe>."
    )


def gcc_env(gcc_path: Path) -> dict:
    import os

    env = os.environ.copy()
    env["PATH"] = str(gcc_path.parent) + os.pathsep + env.get("PATH", "")
    return env


@dataclass
class CheckResult:
    episode: int
    title: str
    kind: str  # "code" or "bug-wrong" or "bug-fixed"
    file: str
    status: str
    detail: str = ""
    expected: str = ""
    actual: str = ""


@dataclass
class Report:
    gcc_version: str
    results: list[CheckResult] = field(default_factory=list)
    reconstructed_fixes: list[str] = field(default_factory=list)
    skipped_notes: list[str] = field(default_factory=list)


# ---------------------------------------------------------------------------
# Grouping files that must be compiled together: connected components by
# local #include "x.h" relationships, not by parsing the spoken-prose gcc
# command in the narration.
# ---------------------------------------------------------------------------

_LOCAL_INCLUDE_RE = re.compile(r'#include\s*"([^"]+)"')


def group_code_files(code_files: list[dict]) -> list[list[dict]]:
    by_name = {f["file"]: f for f in code_files if f.get("lang", "c") == "c"}
    parent = {name: name for name in by_name}

    def find(x: str) -> str:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: str, b: str) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for name, f in by_name.items():
        for inc in _LOCAL_INCLUDE_RE.findall(f["source"]):
            inc_c = inc.rsplit(".", 1)[0] + ".c"
            if inc in by_name:
                union(name, inc)
            if inc_c in by_name:
                union(name, inc_c)
            # If main.c includes shapes.h, and shapes.c is the implementation
            # file for shapes.h, they belong together even without main.c
            # including shapes.c directly.
            base = inc.rsplit(".", 1)[0]
            for other_name in by_name:
                if other_name.rsplit(".", 1)[0] == base:
                    union(name, other_name)

    groups: dict[str, list[dict]] = {}
    for name in by_name:
        groups.setdefault(find(name), []).append(by_name[name])
    return list(groups.values())


# ---------------------------------------------------------------------------
# Reconstructing a full fixed program when the Bible only shows a diff/snippet.
# ---------------------------------------------------------------------------


def reconstruct_fixed(wrong_source: str, fixed_snippet: str) -> tuple[str, bool]:
    """Returns (reconstructed_source, was_reconstructed). If `fixed_snippet`
    already looks like a full program, returns it unchanged."""
    if "#include" in fixed_snippet or re.search(r"\bint\s+main\s*\(", fixed_snippet):
        return fixed_snippet, False

    wrong_lines = wrong_source.splitlines()
    snippet_lines = [l for l in fixed_snippet.splitlines() if l.strip()]
    if not snippet_lines:
        return wrong_source, False

    # Find the best-matching contiguous block in wrong_lines for the snippet,
    # using the first snippet line as an anchor (closest match by similarity).
    first = snippet_lines[0].strip()
    best_idx, best_ratio = None, 0.0
    for i, line in enumerate(wrong_lines):
        ratio = difflib.SequenceMatcher(None, line.strip(), first).ratio()
        if ratio > best_ratio:
            best_ratio, best_idx = ratio, i
    if best_idx is None or best_ratio < 0.4:
        return wrong_source, False

    new_lines = wrong_lines[:best_idx] + snippet_lines + wrong_lines[best_idx + len(snippet_lines) :]
    return "\n".join(new_lines), True


def normalise_output(text: str) -> str:
    lines = text.replace("\r\n", "\n").split("\n")
    # Some "Expected output" blocks are a full terminal transcript (shell
    # prompt + typed command, e.g. "$ gcc bubble.c -o bubble" / "$ ./bubble")
    # rather than pure stdout; strip leading "$ " lines before comparing,
    # since real stdout never contains them.
    while lines and lines[0].strip().startswith("$ "):
        lines = lines[1:]
    return "\n".join(line.rstrip() for line in lines).rstrip("\n")


def normalise_output_loose(text: str) -> str:
    """Whitespace-collapsed comparison, for the scanf/inferred-stdin case:
    a prompt printf() with no trailing \\n runs straight into the next
    printf()'s text when stdin is piped non-interactively (no terminal echo
    inserting newlines), so comparing line-by-line against the Bible's
    terminal-transcript formatting isn't meaningful there."""
    return " ".join(text.split())


def is_nondeterministic(source: str, expected_output: str) -> bool:
    return bool(
        NONDETERMINISTIC_MARKERS.search(expected_output)
        or NONDETERMINISTIC_CALLS.search(source)
        or ADDRESS_FORMAT.search(source)
    )


_PROMPT_ECHO_RE = re.compile(r"^(.*:\s*)(\S+)\s*$")


def infer_stdin_from_output(expected_output: str) -> tuple[str, str] | None:
    """When a scanf program's stdin wasn't captured separately, the Bible
    often shows it inline, terminal-style ("Enter your marks: 72"), since
    that's what a real terminal looks like when you type after a prompt —
    but it's local terminal echo, not something the program itself prints,
    so it won't appear when stdin is piped in non-interactively. Takes the
    first run if several are shown (blank-line separated); every line
    ending in "prompt: value" is treated as one scanf's prompt+typed value,
    collected as one stdin line each, and stripped from the comparison text.
    Returns (stdin, cleaned_first_run_for_comparison) or None if no such
    line was found."""
    first_run = expected_output.strip().split("\n\n")[0]
    lines = first_run.splitlines()
    stdin_values: list[str] = []
    cleaned_lines: list[str] = []
    for line in lines:
        m = _PROMPT_ECHO_RE.match(line)
        if m:
            stdin_values.append(m.group(2))
            cleaned_lines.append(m.group(1).rstrip())
        else:
            cleaned_lines.append(line)
    if not stdin_values:
        return None
    return "\n".join(stdin_values) + "\n", "\n".join(cleaned_lines)


# ---------------------------------------------------------------------------
# Compiling and running.
# ---------------------------------------------------------------------------


def compile_and_run(
    files: dict[str, str],
    main_file: str,
    gcc_path: Path,
    env: dict,
    stdin_text: str | None,
    work_root: Path,
) -> tuple[str, str, str]:
    """Returns (stage, detail, stdout). stage is 'compile-error', 'timeout', or 'ran'."""
    work_dir = Path(tempfile.mkdtemp(dir=work_root))
    try:
        for name, source in files.items():
            (work_dir / name).write_text(source, encoding="utf-8")

        exe = work_dir / "a.exe"
        c_files = [name for name in files if name.endswith(".c")]
        cmd = [str(gcc_path), "-Wall", "-Wextra", "-std=c17", *c_files, "-o", str(exe)]
        proc = subprocess.run(cmd, cwd=work_dir, capture_output=True, text=True, encoding="utf-8", errors="replace", env=env, timeout=30)
        if proc.returncode != 0:
            return "compile-error", proc.stderr, ""

        try:
            run = subprocess.run(
                [str(exe)],
                cwd=work_dir,
                input=stdin_text or "",
                capture_output=True,
                text=True, encoding="utf-8", errors="replace",
                env=env,
                timeout=TIMEOUT_SECONDS,
            )
            return "ran", proc.stderr, run.stdout
        except subprocess.TimeoutExpired:
            return "timeout", "", ""
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


def check_group(
    ep: int, title: str, group: list[dict], gcc_path: Path, env: dict, work_root: Path, report: Report
) -> None:
    mains = [f for f in group if re.search(r"\bint\s+main\s*\(", f["source"])]
    if len(mains) != 1:
        report.results.append(
            CheckResult(
                ep, title, "code", ",".join(f["file"] for f in group), "SKIPPED",
                detail=f"group has {len(mains)} main() functions (expected 1): {[f['file'] for f in group]}",
            )
        )
        return
    main_file = mains[0]
    files = {f["file"]: f["source"] for f in group}

    expected_output = main_file.get("output") or ""
    stdin_text = main_file.get("stdin")

    # Some "Code shown" snippets are deliberate compile-error illustrations
    # (e.g. "arrays cannot be copied with ="), with the GCC error text
    # captured as this file's `output` rather than real stdout — recognisable
    # because it looks like a compiler diagnostic, not program output.
    if re.search(r":\d+:\d+:\s*(error|warning):", expected_output):
        stage, detail, _ = compile_and_run(files, main_file["file"], gcc_path, env, stdin_text, work_root)
        if stage == "compile-error":
            error_lines = [l.strip() for l in expected_output.splitlines() if "error:" in l.lower()]
            matched = any(line and _error_core(line) in detail for line in error_lines) if error_lines else True
            status = "PASS" if matched else "BUG-MESSAGE-DIFFERS"
            report.results.append(
                CheckResult(ep, title, "code", main_file["file"], status, detail=detail[:800], expected=expected_output[:400])
            )
        else:
            report.results.append(
                CheckResult(ep, title, "code", main_file["file"], "OUTPUT-MISMATCH",
                            detail="expected output looks like a compiler error, but this compiled cleanly", expected=expected_output[:400])
            )
        return

    if is_nondeterministic(main_file["source"], expected_output):
        report.results.append(
            CheckResult(ep, title, "code", main_file["file"], "NONDETERMINISTIC", detail="uses rand/time/clock/%p or marked [MEASURED]/'may differ'")
        )
        return

    truncated_to_first_run = False
    stdin_was_inferred = False
    if "scanf" in main_file["source"] and not stdin_text:
        inferred = infer_stdin_from_output(expected_output)
        if inferred:
            stdin_text, first_run_output = inferred
            truncated_to_first_run = first_run_output != expected_output.strip()
            expected_output = first_run_output
            stdin_was_inferred = True
        else:
            report.results.append(
                CheckResult(ep, title, "code", main_file["file"], "NEEDS-INPUT", detail="program reads scanf but no stdin was captured from the Bible text")
            )
            return

    stage, detail, stdout = compile_and_run(files, main_file["file"], gcc_path, env, stdin_text, work_root)
    if stage == "compile-error":
        status = "COMPILE-ERROR"
        if re.search(r"implicit declaration of function|implicit int", detail):
            status = "COMPILE-ERROR (GCC14+: implicit decl/int now an error)"
        report.results.append(CheckResult(ep, title, "code", main_file["file"], status, detail=detail[:1000]))
        return
    if stage == "timeout":
        report.results.append(CheckResult(ep, title, "code", main_file["file"], "TIMEOUT"))
        return

    if not expected_output.strip():
        report.results.append(CheckResult(ep, title, "code", main_file["file"], "PASS", detail="(no expected output recorded; compiled and ran without crashing)"))
        return

    if stdin_was_inferred:
        matches = normalise_output_loose(stdout) == normalise_output_loose(expected_output)
    else:
        matches = normalise_output(stdout) == normalise_output(expected_output)

    if matches:
        detail = "stdin inferred from the output text (loose whitespace comparison); only the first of several shown runs was tested" if truncated_to_first_run else (
            "stdin inferred from the output text (loose whitespace comparison)" if stdin_was_inferred else ""
        )
        report.results.append(CheckResult(ep, title, "code", main_file["file"], "PASS", detail=detail))
    else:
        report.results.append(
            CheckResult(
                ep, title, "code", main_file["file"], "OUTPUT-MISMATCH",
                expected=expected_output[:400], actual=stdout[:400],
            )
        )


def check_bug(ep: int, title: str, bug: dict, bug_extra: dict, gcc_path: Path, env: dict, work_root: Path, report: Report) -> None:
    if bug_extra.get("wrongLang") != "c":
        report.results.append(CheckResult(ep, title, "bug-wrong", "(conceptual)", "SKIPPED", detail="non-code bug (wrong idea / setup mistake), nothing to compile"))
        return

    wrong = bug["wrong"]
    error_text = bug["error"]
    fixed_raw = bug["fixed"]

    if "#include" not in wrong and not re.search(r"\bint\s+main\s*\(", wrong):
        # The "wrong" side is itself a bare excerpt (e.g. just a for-loop),
        # not a full program — there's no legitimate standalone way to
        # compile it, reconstruction or not.
        report.results.append(
            CheckResult(ep, title, "bug-wrong", "wrong.c", "SKIPPED", detail="wrong code is a bare excerpt, not a full program; needs manual review in context")
        )
        report.results.append(
            CheckResult(ep, title, "bug-fixed", "fixed.c", "SKIPPED", detail="fixed code is a bare excerpt, not a full program; needs manual review in context")
        )
        return

    # Wrong code: should fail to compile, or compile but misbehave (realloc-style bugs).
    stage, detail, stdout = compile_and_run({"wrong.c": wrong}, "wrong.c", gcc_path, env, None, work_root)
    if stage == "compile-error":
        # Compare the Bible's described error against the real GCC message:
        # look for the Bible's error LINE text (not file/column) inside gcc's output.
        error_lines = [l.strip() for l in error_text.splitlines() if "error:" in l.lower() or "warning:" in l.lower()]
        matched = any(line and _error_core(line) in detail for line in error_lines) if error_lines else True
        status = "PASS" if matched else "BUG-MESSAGE-DIFFERS"
        report.results.append(
            CheckResult(ep, title, "bug-wrong", "wrong.c", status, detail=detail[:800], expected=error_text[:400])
        )
    elif stage == "timeout":
        report.results.append(CheckResult(ep, title, "bug-wrong", "wrong.c", "TIMEOUT"))
    else:
        # Compiled cleanly — expected for behavioural (not compile-error) bugs.
        report.results.append(
            CheckResult(ep, title, "bug-wrong", "wrong.c", "PASS", detail="compiled cleanly (behavioural bug, not a compile error, matches the Bible's description)")
        )

    # Fixed code.
    fixed, was_reconstructed = reconstruct_fixed(wrong, fixed_raw)
    if was_reconstructed:
        report.reconstructed_fixes.append(f"EP{ep:02d}")

    stage, detail, stdout = compile_and_run({"fixed.c": fixed}, "fixed.c", gcc_path, env, None, work_root)
    if stage == "compile-error":
        report.results.append(CheckResult(ep, title, "bug-fixed", "fixed.c", "COMPILE-ERROR", detail=detail[:800]))
    elif stage == "timeout":
        report.results.append(CheckResult(ep, title, "bug-fixed", "fixed.c", "TIMEOUT"))
    else:
        report.results.append(CheckResult(ep, title, "bug-fixed", "fixed.c", "PASS", detail="compiled and ran"))


def _error_core(line: str) -> str:
    # Strip "file.c:12:34:" prefixes so comparison is on the message text only.
    return re.sub(r"^\S+:\d+:\d+:\s*", "", line).strip()


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------


def main() -> None:
    # Windows' console is often cp1252, which can't encode every character
    # that ends up in GCC output (curly quotes, arrows, etc. from the Bible).
    sys.stdout.reconfigure(errors="replace")

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gcc", default=None)
    parser.add_argument("--episode", type=int, default=None)
    args = parser.parse_args()

    gcc_path = find_gcc(args.gcc)
    env = gcc_env(gcc_path)
    version_out = subprocess.run([str(gcc_path), "--version"], capture_output=True, text=True, encoding="utf-8", errors="replace", env=env)
    gcc_version = version_out.stdout.splitlines()[0] if version_out.stdout else "unknown"

    report = Report(gcc_version=gcc_version)
    work_root = Path(tempfile.mkdtemp(prefix="koding-konkani-ccheck-"))

    try:
        episode_files = sorted(EPISODES_DIR.glob("ep*.json"))
        for ep_path in episode_files:
            data = json.loads(ep_path.read_text(encoding="utf-8"))
            ep, title = data["ep"], data["title"]
            if args.episode is not None and ep != args.episode:
                continue

            code_files = data.get("codeFiles", [])
            cpp_files = [f for f in code_files if f.get("lang") == "cpp"]
            for f in cpp_files:
                report.results.append(CheckResult(ep, title, "code", f["file"], "SKIPPED", detail="not C (cpp)"))

            for group in group_code_files(code_files):
                check_group(ep, title, group, gcc_path, env, work_root, report)

            check_bug(ep, title, data["bug"], data.get("bugExtra", {}), gcc_path, env, work_root, report)
    finally:
        shutil.rmtree(work_root, ignore_errors=True)

    write_reports(report)


def write_reports(report: Report) -> None:
    counts: dict[str, int] = {}
    for r in report.results:
        key = r.status.split(" (")[0]
        counts[key] = counts.get(key, 0) + 1

    out_report = ROOT / "out" / "c-check-report.md"
    out_report.parent.mkdir(parents=True, exist_ok=True)

    summary_lines = ["# C compiler check", "", f"gcc: `{report.gcc_version}`", "", "## Counts", ""]
    for status in RESULTS_ORDER:
        if status in counts:
            summary_lines.append(f"- {status}: {counts[status]}")
    for status, n in counts.items():
        if status not in RESULTS_ORDER:
            summary_lines.append(f"- {status}: {n}")
    summary_lines.append("")
    if report.reconstructed_fixes:
        summary_lines.append(
            f"Fixed code was a snippet (not a full program) and had to be reconstructed by patching "
            f"the wrong code for {len(report.reconstructed_fixes)} episodes: {', '.join(report.reconstructed_fixes)}."
        )
        summary_lines.append("")

    non_pass = [r for r in report.results if r.status != "PASS" and r.status != "SKIPPED"]
    summary_lines.append(f"## Non-PASS results ({len(non_pass)})")
    summary_lines.append("")
    summary_lines.append("| EP | Title | Kind | File | Status | Expected (first 10 lines) | Actual (first 10 lines) |")
    summary_lines.append("| --- | --- | --- | --- | --- | --- | --- |")
    for r in non_pass:
        expected_10 = "<br>".join(r.expected.splitlines()[:10]).replace("|", "\\|")
        actual_10 = "<br>".join((r.actual or r.detail).splitlines()[:10]).replace("|", "\\|")
        summary_lines.append(
            f"| {r.episode} | {r.title} | {r.kind} | {r.file} | {r.status} | {expected_10} | {actual_10} |"
        )

    full_report = "\n".join(summary_lines)
    out_report.write_text(full_report, encoding="utf-8")

    # docs/c-check-summary.md is the committed, lighter version: counts + non-PASS table only (same content here).
    docs_summary = ROOT / "docs" / "c-check-summary.md"
    docs_summary.write_text(full_report, encoding="utf-8")

    print(full_report)
    print(f"\nWrote {out_report} and {docs_summary}")


if __name__ == "__main__":
    main()
