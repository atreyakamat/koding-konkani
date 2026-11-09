"""Validate scripts/python_bible/illustrations.py and export docs/python-bible/illustrations/epNN.json.

Usage: python3 scripts/check_illustrations.py [--write]
Exit code 1 if any problem. Rules: docs/python-bible/ILLUSTRATIONS.md.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts" / "python_bible"))
from illustrations import ILL  # noqa: E402

COLS, ROWS = 12, 6
SHAPES = {"box", "card", "label", "token", "arrow"}
VERBS = {"show", "hide", "move", "draw", "glow", "dim", "shake", "stamp", "tick", "cross", "flip"}
COLOURS = {"tomato", "peach", "apricot", "butter", "cream", "pastelBlue", "mint", "lilac", "darkBlue", "ink", "white"}
SFX = {"buzzer", "chime", "claw-click", "ding", "key-tick", "marker-swipe", "pop", "rimshot", "stamp", "sting", "thud", "whoosh"}
ARROW_ONLY = {"draw"}
BOX_VERBS = VERBS - ARROW_ONLY


def contains(o: dict, i: dict) -> bool:
    return o["col"] <= i["col"] and o["row"] <= i["row"] and o["col"] + o["w"] >= i["col"] + i["w"] and o["row"] + o["h"] >= i["row"] + i["h"]


def check(ep: int, spec: dict) -> list[str]:
    bad: list[str] = []
    objs = spec.get("objects", [])
    steps = spec.get("steps", [])
    ids: dict[str, dict] = {}
    for o in objs:
        oid = o.get("id")
        if not oid or oid in ids:
            bad.append(f"duplicate or empty id {oid!r}")
            continue
        ids[oid] = o
        if o.get("shape") not in SHAPES:
            bad.append(f"{oid}: bad shape {o.get('shape')!r}")
        if o.get("colour") not in COLOURS:
            bad.append(f"{oid}: bad colour {o.get('colour')!r}")
        if o.get("shape") == "arrow":
            for k in ("from", "to"):
                if o.get(k) not in {x.get("id") for x in objs if x.get("shape") != "arrow"}:
                    bad.append(f"{oid}: arrow {k} {o.get(k)!r} is not a box id")
        else:
            c, r, w, h = (o.get(k) for k in ("col", "row", "w", "h"))
            if not all(isinstance(v, int) for v in (c, r, w, h)):
                bad.append(f"{oid}: col,row,w,h must be integers")
                continue
            if w < 1 or h < 1 or c < 0 or r < 0 or c + w > COLS or r + h > ROWS:
                bad.append(f"{oid}: outside the {COLS}x{ROWS} grid (col={c} row={r} w={w} h={h})")
            if not o.get("text"):
                bad.append(f"{oid}: empty text")
    # overlap between non-arrow objects that are on screen at the same time is allowed only
    # if they never show together; we flag identical positions as likely mistakes.
    boxes = [o for o in objs if o.get("shape") != "arrow" and all(isinstance(o.get(k), int) for k in ("col", "row", "w", "h"))]
    for i, a in enumerate(boxes):
        for b in boxes[i + 1:]:
            if a["col"] < b["col"] + b["w"] and b["col"] < a["col"] + a["w"] and a["row"] < b["row"] + b["h"] and b["row"] < a["row"] + a["h"]:
                # allowed: full nesting, outer box listed first
                if not contains(a, b):
                    bad.append(f"{a['id']} and {b['id']} overlap on the grid (only full nesting, outer box first, is allowed)")
    last = -1.0
    for n, s in enumerate(steps):
        where = f"step {n}"
        t = s.get("t")
        if not isinstance(t, (int, float)) or not 0 <= t <= 1:
            bad.append(f"{where}: t must be 0..1")
            continue
        if t < last:
            bad.append(f"{where}: t goes backwards ({t} < {last})")
        last = t
        do, tg = s.get("do"), s.get("target")
        if do not in VERBS:
            bad.append(f"{where}: bad verb {do!r}")
        if tg not in ids:
            bad.append(f"{where}: unknown target {tg!r}")
            continue
        is_arrow = ids[tg].get("shape") == "arrow"
        if do == "draw" and not is_arrow:
            bad.append(f"{where}: draw needs an arrow target ({tg})")
        if is_arrow and do not in {"draw", "show", "hide", "glow", "dim"}:
            bad.append(f"{where}: verb {do} not allowed on an arrow ({tg})")
        if do == "move":
            to = s.get("to")
            o = ids[tg]
            if not (isinstance(to, list) and len(to) == 2 and all(isinstance(v, int) for v in to)):
                bad.append(f"{where}: move needs to=[col,row]")
            elif not is_arrow and (to[0] < 0 or to[1] < 0 or to[0] + o["w"] > COLS or to[1] + o["h"] > ROWS):
                bad.append(f"{where}: move target outside grid")
        if s.get("sfx") and s["sfx"] not in SFX:
            bad.append(f"{where}: bad sfx {s['sfx']!r}")
        extra = set(s) - {"t", "do", "target", "sfx", "to"}
        if extra:
            bad.append(f"{where}: unknown keys {sorted(extra)}")
    shown = {s["target"] for s in steps if s.get("do") in {"show", "draw"} and s.get("target") in ids}
    for oid in ids:
        if oid not in shown:
            bad.append(f"{oid}: never shown or drawn")
    for o in objs:
        if o.get("shape") == "arrow":
            drawn = [s["t"] for s in steps if s.get("target") == o["id"] and s.get("do") in {"show", "draw"}]
            for end in (o.get("from"), o.get("to")):
                ends = [s["t"] for s in steps if s.get("target") == end and s.get("do") == "show"]
                if drawn and ends and min(drawn) < min(ends):
                    bad.append(f"{o['id']}: drawn before {end} is shown")
    return bad


def main() -> int:
    write = "--write" in sys.argv
    out = ROOT / "docs" / "python-bible" / "illustrations"
    total = 0
    for ep in sorted(ILL):
        problems = check(ep, ILL[ep])
        for p in problems:
            print(f"EP{ep:02d}: {p}")
        total += len(problems)
        if write and not problems:
            out.mkdir(parents=True, exist_ok=True)
            doc = {"ep": ep, "scene": 4, "grid": {"cols": COLS, "rows": ROWS}, **ILL[ep]}
            (out / f"ep{ep:03d}.json").write_text(json.dumps(doc, indent=2) + "\n", encoding="utf-8")
    print(f"{len(ILL)} illustrations, {total} problems")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
