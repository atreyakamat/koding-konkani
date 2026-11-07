#!/usr/bin/env python3
"""Fills the data gaps that stop EP52-83 from rendering (see docs/RUNBOOK-ep51-86.md).

  * 40 blank memory-boxes scenes (EP52-83): writes the `memory` frames from docs/fix4/boxes-draft-ep52-83.json
    (made by docs/fix4/gen_boxes_52_83.py from each scene's own narration, on-screen text and code; EP61/64/71
    byte offsets and sizes were taken from a gcc probe).
  * EP77 scene 4 (Tower of Hanoi): adds the missing bars `trace` (3 bars = discs, bar height = peg A/B/C).
  * EP81 scene 4: adds the missing bars `trace` (replays the EP74 bubble-sort trace).
  * EP81: replaces every "[MEASURED]" placeholder with the real times of one run of showdown.c
    (and of the buggy variant for the Bug of the Day), so the narrator never says "measured".

Only those fields change. Line endings of each episode file are kept. Safe to run twice.
Usage (from the repo root):  python scripts/apply_boxes_52_83.py [--dry]
"""
import copy, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DRY = "--dry" in sys.argv
boxes = json.loads((ROOT / "docs" / "fix4" / "boxes-draft-ep52-83.json").read_text(encoding="utf-8"))


def load(n):
    p = ROOT / "episodes" / f"ep{n:03d}.json"
    raw = p.read_bytes().decode("utf-8")
    return p, json.loads(raw), ("\r\n" if "\r\n" in raw else "\n")


def save(p, d, nl):
    out = json.dumps(d, indent=2, ensure_ascii=False).replace("\n", nl) + nl
    if not DRY:
        p.write_bytes(out.encode("utf-8"))


eps = {}
touched = set()
def ep(n):
    if n not in eps: eps[n] = load(n)
    return eps[n][1]


for key, mem in boxes.items():
    e_n, sc = map(int, key.split("."))
    scene = next(s for s in ep(e_n)["scenes"] if s["id"] == sc)
    assert scene["template"] == "memory-boxes", f"EP{e_n} s{sc} is {scene['template']}"
    scene["memory"] = mem
    touched.add(e_n)


def hanoi_trace():
    """Bars = discs 1..3, bar height = peg (A=1, B=2, C=3), the moved disc is highlighted. Moves follow the
    7-move output of EP77's hanoi.c and the narration for n = 1, 2, 3."""
    A, B, C = 1, 2, 3
    t = []
    def phase(n, moves):
        arr = [A, A, A]
        t.append({"step": f"n={n} start", "array": list(arr)})
        for k, (d, peg) in enumerate(moves, 1):
            arr[d] = peg
            st = {"step": f"n={n} move {k}", "array": list(arr), "compare": [d, d]}
            if k == len(moves): st["sorted"] = list(range(n))
            t.append(st)
    phase(1, [(0, C)])
    phase(2, [(0, B), (1, C), (0, C)])
    phase(3, [(0, C), (1, B), (0, B), (2, C), (0, A), (1, C), (0, C)])
    return t


s = next(s for s in ep(77)["scenes"] if s["id"] == 4)
assert s["template"] == "algorithm-bars"
touched.add(77)
s["trace"] = hanoi_trace()
s["onScreen"] = "Three bars = discs 1, 2, 3; bar height = peg (A = 1, B = 2, C = 3); the disc being moved lights up. Solve n = 1, 2, 3"

tr = []
for sc in ep(74)["scenes"]:
    if sc["template"] == "algorithm-bars" and sc.get("trace"): tr += copy.deepcopy(sc["trace"])
s = next(s for s in ep(81)["scenes"] if s["id"] == 4)
assert s["template"] == "algorithm-bars" and tr
touched.add(81)
s["trace"] = tr
s["onScreen"] = "One bar row replays bubble sort on {5, 2, 9, 1, 6, 3}; the scorecard below shows the counts for all six sorts"

# ---- EP81 "[MEASURED]": one real run of showdown.c (gcc 13.3, no -O, N = 10000, srand(42)), 2026-11-08.
GOOD = """Bubble        133.66 ms  sorted
Selection      41.18 ms  sorted
Insertion      26.88 ms  sorted
Merge           1.03 ms  sorted
Quick           0.71 ms  sorted
Counting        0.10 ms  sorted"""
PLACEHOLDER_OUT = re.compile(r"Bubble     \[MEASURED\] ms  sorted\nSelection  \[MEASURED\] ms  sorted\nInsertion  \[MEASURED\] ms  sorted\n"
                             r"Merge      \[MEASURED\] ms  sorted\nQuick      \[MEASURED\] ms  sorted\nCounting   \[MEASURED\] ms  sorted")
REPL = [
    ("[TRACK ms=[MEASURED]]", "[TRACK ms=133.66]"),
    ("Bubble sort: [MEASURED] milliseconds. Selection sort: [MEASURED]. Insertion sort: [MEASURED]. Merge sort: [MEASURED]. Quick sort: [MEASURED]. Counting sort: [MEASURED].",
     "Bubble sort: about 134 milliseconds. Selection sort: about 41. Insertion sort: about 27. Merge sort: about 1. Quick sort: under one millisecond. Counting sort: even faster, about a tenth of one."),
    ("These are our laptop's numbers; yours will be different", "These come from one test run on our computer; yours will be different"),
    ("Results table with [MEASURED] values;", "Results table with the six times (Bubble 133.66 ms down to Counting 0.10 ms);"),
    ("numbers are [MEASURED]", "numbers are the real times from the run"),
    ("Wrong behaviour (describe with [MEASURED] values from a recorded run of the buggy file): only Bubble gets random data. Insertion then sorts already-sorted data, its best case, and its time drops to almost nothing; Quick sorts already-sorted data with a last-element pivot, its worst case, and its time jumps up to bubble-sort territory.",
     "Wrong behaviour, from a recorded run of the buggy file: only Bubble gets random data (116.50 ms). Insertion then sorts already-sorted data, its best case, and drops to 0.02 ms; Quick sorts already-sorted data with a last-element pivot, its worst case, and jumps to 78.45 ms, bubble-sort territory."),
    ("confirm with your own [MEASURED] run", "confirm with your own run"),
]

def fix(x):
    if isinstance(x, str):
        x = PLACEHOLDER_OUT.sub(GOOD, x)
        for a, b in REPL: x = x.replace(a, b)
        return x
    if isinstance(x, list): return [fix(i) for i in x]
    if isinstance(x, dict): return {k: fix(v) for k, v in x.items()}
    return x

eps[81] = (eps[81][0], fix(eps[81][1]), eps[81][2])
left = json.dumps(eps[81][1]).count("MEASURED")
assert left == 0, f"{left} [MEASURED] placeholders left in EP81"

for n in sorted(touched): save(*eps[n])
print(("DRY RUN: would patch" if DRY else "patched"), "episodes:", ", ".join(str(n) for n in sorted(touched)), f"| {len(boxes)} memory scenes")
