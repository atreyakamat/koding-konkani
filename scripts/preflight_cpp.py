#!/usr/bin/env python3
"""Preflight check of the C++ Bible (docs/cpp-bible/m*.md) before Remotion renders it.

Read-only. No network. No compiler needed (use scripts/check_cpp.py for that).
It checks, for every episode:
  * the 11-scene table, times that add up, 9:00 maximum;
  * narration: one block per scene, STE lint (scripts/ste_lint.py), no digits or symbols;
  * cues: [HL n] only in code scenes and inside the code, [TRACK name=value] syntax;
  * illustration JSON: schema, sizes, addresses, arrows, bar traces (see ILLUSTRATIONS.md);
  * code files, expected output, bug section, 5 Shorts of 35-45 seconds.
It writes docs/cpp-bible/preflight.md and exits 1 on any ERROR.

Usage: python scripts/preflight_cpp.py [--module m03] [--episode N]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ste_lint  # noqa: E402

ROOT = HERE.parent
BIBLE = ROOT / "docs" / "cpp-bible"
MODULE_RANGES = {"m00": (1, 4), "m01": (5, 12), "m02": (13, 20), "m03": (21, 30), "m04": (31, 40), "m05": (41, 50),
                 "m06": (51, 60), "m07": (61, 68), "m08": (69, 76), "m09": (77, 84), "m10": (85, 90)}
SIZES = {"bool": 1, "char": 1, "short": 2, "int": 4, "unsigned": 4, "long": 8, "long long": 8, "size_t": 8,
         "float": 4, "double": 8, "std::string": 32, "string": 32}
TEMPLATE_FOR = {"memory": "Memory boxes", "trace": "Algorithm bars"}
SCENE_ORDER = ["Title card", "Concept slide", "Code explain", None, "Code explain", "Terminal", "Concept slide",
               "Bug of the Day", "Pun card", "Challenge", "Outro"]
FENCE = re.compile(r"^```(\w*)\n(.*?)\n```[ \t]*$", re.S | re.M)
UNESC = re.compile(r"\\([\[\]])")


def mm(s: str) -> int:
    a, b = s.split(":")
    return int(a) * 60 + int(b)


def secs(body: str) -> dict[str, str]:
    parts = re.split(r"^### (.+)$", body, flags=re.M)
    return {parts[i].strip(): parts[i + 1] for i in range(1, len(parts) - 1, 2)}


# ---------------------------------------------------------------- illustration schemas
def check_illustration(d: dict, errs: list[str]) -> None:
    k = d.get("kind")
    if k not in ("memory", "flow", "graph", "table", "callstack", "trace"):
        errs.append(f"illustration: unknown kind {k!r}")
        return
    if not isinstance(d.get("scene"), int):
        errs.append("illustration: missing scene number")
    if k == "memory":
        boxes, arrows = d.get("boxes", []), d.get("arrows", [])
        if not 1 <= len(boxes) <= 12:
            errs.append(f"memory: {len(boxes)} boxes (need 1-12 to fit the screen)")
        ids = [b.get("id") for b in boxes]
        if len(set(ids)) != len(ids):
            errs.append("memory: duplicate box id")
        occupied: dict[str, list[tuple[int, int, str]]] = {}
        for b in boxes:
            for key in ("id", "name", "type", "value", "bytes", "addr", "region"):
                if b.get(key) in (None, ""):
                    errs.append(f"memory: box {b.get('id')} lacks {key}")
            t = b.get("type", "")
            if t in SIZES and b.get("bytes") != SIZES[t]:
                errs.append(f"memory: {b['id']} type {t} must be {SIZES[t]} bytes, not {b.get('bytes')}")
            if t.endswith("*") and b.get("bytes") != 8:
                errs.append(f"memory: pointer {b['id']} must be 8 bytes")
            try:
                a = int(b["addr"], 16)
            except Exception:
                errs.append(f"memory: {b.get('id')} address {b.get('addr')!r} is not hex")
                continue
            if b.get("region") not in ("stack", "heap", "static"):
                errs.append(f"memory: {b['id']} region must be stack, heap or static")
            if a % min(b.get("bytes", 1), 8):
                errs.append(f"memory: {b['id']} address {b['addr']} is not aligned to its size")
            for (lo, hi, other) in occupied.get(b.get("region", ""), []):
                if a < hi and lo < a + b.get("bytes", 0):
                    errs.append(f"memory: {b['id']} overlaps {other}")
            occupied.setdefault(b.get("region", ""), []).append((a, a + b.get("bytes", 0), b["id"]))
        by = {b["id"]: b for b in boxes if "id" in b}
        for ar in arrows:
            if ar.get("from") not in by or ar.get("to") not in by:
                errs.append(f"memory: arrow {ar} uses a box that does not exist")
                continue
            src = by[ar["from"]]
            if src["type"].endswith("*") or src["type"].startswith("std::unique_ptr") or src["type"].startswith("std::shared_ptr"):
                if src["value"] != by[ar["to"]]["addr"] and ar.get("label") != "weak":
                    errs.append(f"memory: pointer {src['id']} holds {src['value']} but arrow goes to {by[ar['to']]['addr']}")
        for b in boxes:
            if b.get("type", "").endswith("*") and b.get("value") not in ("nullptr", "0x0000") and not any(
                    a.get("from") == b["id"] for a in arrows):
                errs.append(f"memory: pointer {b['id']} has an address but no arrow")
    elif k == "flow":
        st = d.get("steps", [])
        if not 2 <= len(st) <= 6:
            errs.append(f"flow: {len(st)} steps (need 2-6)")
        for s in st:
            if not s.get("label") or len(s["label"]) > 28 or len(s.get("detail", "")) > 70:
                errs.append(f"flow: step {s.get('id')} label or detail empty or too long")
    elif k == "graph":
        ns, es = d.get("nodes", []), d.get("edges", [])
        if d.get("layout") not in ("row", "column", "tree"):
            errs.append("graph: layout must be row, column or tree")
        if not 2 <= len(ns) <= 10:
            errs.append(f"graph: {len(ns)} nodes (need 2-10)")
        ids = [n.get("id") for n in ns]
        if len(set(ids)) != len(ids):
            errs.append("graph: duplicate node id")
        for e in es:
            if e.get("from") not in ids or e.get("to") not in ids:
                errs.append(f"graph: edge {e} uses a node that does not exist")
        if d.get("layout") == "tree":
            inc = Counter(e["to"] for e in es)
            if any(v > 1 for v in inc.values()):
                errs.append("graph: tree node with two parents")
    elif k == "table":
        h, rows = d.get("headers", []), d.get("rows", [])
        if not 1 <= len(h) <= 5 or not 1 <= len(rows) <= 8:
            errs.append("table: need 1-5 columns and 1-8 rows")
        for r in rows:
            if len(r) != len(h) or any(len(str(c)) > 40 for c in r):
                errs.append(f"table: bad row {r}")
    elif k == "callstack":
        st = d.get("steps", [])
        if len(st) < 2:
            errs.append("callstack: need at least 2 steps")
        for s in st:
            if not s.get("frames") or len(s["frames"]) > 8 or not all(isinstance(f, str) for f in s["frames"]):
                errs.append(f"callstack: step {s.get('step')} has bad frames")
    elif k == "trace":
        st = d.get("steps", [])
        if not 2 <= len(st) <= 90:
            errs.append(f"trace: {len(st)} steps")
            return
        n = len(st[0]["array"])
        if not 3 <= n <= 10:
            errs.append(f"trace: {n} bars (need 3-10)")
        base = sorted(st[0]["array"])
        for i, s in enumerate(st):
            if s.get("step") != i + 1:
                errs.append(f"trace: step numbers must run 1..N (got {s.get('step')} at {i + 1})")
            if sorted(s["array"]) != base:
                errs.append(f"trace: step {i + 1} changes the values")
            for key in ("compare", "swap"):
                if key in s and not all(0 <= x < n for x in s[key]):
                    errs.append(f"trace: step {i + 1} {key} index out of range")
            if "swap" in s and i + 1 < len(st):
                a = list(s["array"])
                x, y = s["swap"]
                a[x], a[y] = a[y], a[x]
                if a != st[i + 1]["array"]:
                    errs.append(f"trace: step {i + 1} swap does not give the next array")
        if st[-1]["array"] != sorted(st[-1]["array"]):
            errs.append("trace: last step is not sorted")
        if sorted(st[-1].get("sorted", [])) != list(range(n)):
            errs.append("trace: last step must mark every bar as sorted")
        c = d.get("counters", {})
        if c.get("swaps") != sum(1 for s in st if "swap" in s):
            errs.append("trace: swap counter is wrong")
        if c.get("compares") != sum(1 for s in st if "compare" in s and "swap" not in s):
            errs.append("trace: compare counter is wrong")


# ---------------------------------------------------------------- episode checks
def check_episode(ep: int, title: str, body: str, warns: list[str]) -> list[str]:
    errs: list[str] = []
    S = secs(body)
    head = body.split("###")[0]
    m = re.search(r"\*\*Module (\d+) · (.+?) · (\d+:\d\d) · ", head)
    total = mm(m.group(3)) if m else 0
    if not m:
        errs.append("header line missing")
    elif total > 540:
        errs.append(f"length {m.group(3)} is over 9:00")
    # scene table
    rows = [[c.strip() for c in l.strip().strip("|").split("|")] for l in S.get("Scene list", "").splitlines()
            if re.match(r"\|\s*\d+\s*\|", l)]
    if len(rows) != 11:
        errs.append(f"{len(rows)} scenes (need 11)")
    t = 0
    for i, r in enumerate(rows):
        if len(r) < 6:
            errs.append(f"scene row {i + 1} has {len(r)} cells")
            continue
        want = SCENE_ORDER[i] if i < len(SCENE_ORDER) else None
        if i == 3:
            pass
        elif r[3] != want:
            errs.append(f"scene {i + 1} is {r[3]!r}, expected {want!r}")
        if mm(r[1]) != t:
            errs.append(f"scene {i + 1} starts at {r[1]}, expected {t // 60}:{t % 60:02d}")
        t += mm(r[2])
        if not r[4] or not r[5]:
            errs.append(f"scene {i + 1} lacks on-screen text or animation")
    if m and rows and t != total:
        errs.append(f"scene lengths add to {t}s but header says {total}s")
    # illustration
    ill_scene_tpl = rows[3][3] if len(rows) > 3 and len(rows[3]) > 3 else ""
    try:
        ill_fences = []
        for lang, content in FENCE.findall(S.get("Illustrations", "")):
            if lang == "json":
                ill_fences.append(json.loads(content))
    except json.JSONDecodeError as e:
        errs.append(f"illustration JSON does not parse: {e}")
        ill_fences = []
    if len(ill_fences) != 1:
        errs.append(f"{len(ill_fences)} illustration blocks (need 1)")
    for d in ill_fences:
        check_illustration(d, errs)
        want = TEMPLATE_FOR.get(d.get("kind"), "Concept slide")
        if ill_scene_tpl != want:
            errs.append(f"scene 4 template {ill_scene_tpl!r} does not match illustration kind {d.get('kind')!r} ({want})")
        if d.get("scene") != 4:
            errs.append("illustration scene must be 4")
    # code files
    files = []
    pending = ""
    for pos, (lang, content) in enumerate(FENCE.findall(S.get("Code shown", ""))):
        if lang == "cpp":
            files.append(content)
    names = re.findall(r"^File \d+: (\S+)", S.get("Code shown", ""), flags=re.M)
    if len(files) != 2 or len(names) != 2:
        errs.append(f"{len(files)} code files (need 2)")
    for nme in names:
        if not nme.rsplit(".", 1)[0].isalpha():
            errs.append(f"file name {nme} must be letters only")
    if S.get("Code shown", "").count("**Expected output:**") != len(files):
        errs.append("every code file needs Expected output")
    # narration
    narr_blocks = re.findall(r"^\*\*\\\[(\d+) · (.+?)\\\]\*\* (.*?)(?=^\*\*\\\[\d+ · |\Z)", S.get("Narration script", ""), flags=re.M | re.S)
    if len(narr_blocks) != 11:
        errs.append(f"{len(narr_blocks)} narration blocks (need 11)")
    for num, label, text in narr_blocks:
        i = int(num)
        text = UNESC.sub(r"\1", text).strip()
        exempt = label == "Pun"
        for lv, code, msg in ste_lint.lint_text(text):
            if exempt and code != "TTS-CHAR":
                continue
            (errs if lv == "ERROR" else warns).append(f"scene {i} [{label}] {code}: {msg}")
        hl = [int(x) for x in re.findall(r"\[HL (\d+)\]", text)]
        if hl and i not in (3, 5):
            errs.append(f"scene {i}: [HL] cue outside a code scene")
        if i in (3, 5):
            src = files[0] if i == 3 and files else (files[1] if len(files) > 1 else "")
            n_lines = len(src.split("\n"))
            if not hl:
                errs.append(f"scene {i}: no [HL] cue")
            for h in hl:
                if not 1 <= h <= n_lines:
                    errs.append(f"scene {i}: [HL {h}] is outside the code (1-{n_lines})")
        for tr in re.findall(r"\[TRACK([^\]]*)\]", text):
            if not re.fullmatch(r" [A-Za-z_]\w*=[^\s\]]+", tr):
                errs.append(f"scene {i}: bad [TRACK{tr}] cue")
    # bug
    bs = S.get("Bug of the Day", "")
    for need in ("**Bug kind:**", "Wrong code", "Fixed code", "**Why:**"):
        if need not in bs:
            errs.append(f"bug section lacks {need}")
    pc = S.get("Pun & challenge", "")
    for need in ("**Pun:**", "**Challenge:**", "**Challenge answer:**"):
        if need not in pc:
            errs.append(f"pun and challenge section lacks {need}")
    # shorts
    sh = [s for s in S if s.startswith("Shorts for EP")]
    if not sh:
        errs.append("no Shorts section")
    else:
        txt = S[sh[0]]
        heads = re.findall(r"^\*\*(S\d) · (.+?)\*\* — (\d+:\d\d) · built from scenes? ([\d, ]+)$", txt, flags=re.M)
        if [h[0] for h in heads] != ["S1", "S2", "S3", "S4", "S5"]:
            errs.append(f"Shorts found: {[h[0] for h in heads]}")
        for h in heads:
            if not 35 <= mm(h[2]) <= 45:
                errs.append(f"{h[0]} is {h[2]} (need 0:35-0:45)")
            if any(not 1 <= int(x) <= 11 for x in re.findall(r"\d+", h[3])):
                errs.append(f"{h[0]} built from a scene that does not exist")
        scripts = re.findall(r"^- \*\*Script:\*\* (.+)$", txt, flags=re.M)
        if len(scripts) != 5:
            errs.append(f"{len(scripts)} Short scripts")
        for i, s in enumerate(scripts, 1):
            if not s.endswith("Keep coding, says Xecxec!"):
                errs.append(f"S{i} script lacks the sign-off")
            ps = [p for p in ste_lint.lint_paragraph(s) if p[1] == "TTS-CHAR"]
            for lv, code, msg in ps:
                errs.append(f"S{i} {code}: {msg}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--module")
    ap.add_argument("--episode", type=int)
    a = ap.parse_args()
    all_eps: dict[int, str] = {}
    rows: list[str] = []
    total_err = total_warn = 0
    for p in sorted(BIBLE.glob(f"{a.module or 'm*'}.md")):
        if not re.fullmatch(r"m\d\d", p.stem):
            continue
        md = p.read_text(encoding="utf-8")
        parts = re.split(r"^## EP (\d+) — (.+)$", md, flags=re.M)
        found = []
        for i in range(1, len(parts) - 2, 3):
            ep, title, body = int(parts[i]), parts[i + 1].strip(), parts[i + 2]
            if a.episode and ep != a.episode:
                continue
            found.append(ep)
            all_eps[ep] = title
            warns: list[str] = []
            errs = check_episode(ep, title, body, warns)
            mm_ = re.search(r"· (\d+:\d\d) ·", body)
            rows.append(f"| {ep} | {title} | {mm_.group(1) if mm_ else '?'} | {len(errs)} | {len(warns)} |")
            total_err += len(errs)
            total_warn += len(warns)
            print(f"EP {ep:02d} {title}: {'ok' if not errs else str(len(errs)) + ' ERRORS'}{' (' + str(len(warns)) + ' warnings)' if warns else ''}")
            for e in errs:
                print("   ERROR", e)
            for w in warns:
                print("   warn ", w)
        lo, hi = MODULE_RANGES.get(p.stem, (0, 0))
        if not a.episode and found != list(range(lo, hi + 1)):
            total_err += 1
            print(f"ERROR {p.name}: episodes {found[:3]}... do not match the module map {lo}-{hi}")
    if not a.module and not a.episode:
        if sorted(all_eps) != list(range(1, 91)):
            missing = sorted(set(range(1, 91)) - set(all_eps))
            print(f"NOTE: {len(all_eps)} episodes present; missing {missing[:10]}{'...' if len(missing) > 10 else ''}")
        lines = ["# C++ Bible preflight", "", f"Episodes checked: {len(all_eps)} / 90 · errors: {total_err} · warnings: {total_warn}", "",
                 "| EP | Title | Length | Errors | Warnings |", "| --- | --- | --- | --- | --- |", *rows]
        (BIBLE / "preflight.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"\nerrors: {total_err}, warnings: {total_warn}")
    return 1 if total_err else 0


if __name__ == "__main__":
    sys.exit(main())
