#!/usr/bin/env python3
"""Aggregate out/epNNN/qa.json into out/render-all-report.md (or print progress with --status)."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
a, b = (int(x) for x in [v for v in sys.argv[1:] if not v.startswith("--")][:2] or (1, 86))
status_only = "--status" in sys.argv


def load(ep: int):
    p = ROOT / "out" / f"ep{ep:03d}" / "qa.json"
    if not p.exists():
        return None
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


rows, counts, black, secs_total, done_n = [], {"PASS": 0, "WARN": 0, "FAIL": 0, "PENDING": 0}, 0, 0.0, 0
skips = (ROOT / "out" / "episode-skips.log")
skipped = set()
if skips.exists():
    for line in skips.read_text(encoding="utf-8").splitlines():
        parts = line.split()
        if len(parts) > 2 and parts[2].startswith("SKIPPED") and parts[1].startswith("ep"):
            skipped.add(int(parts[1][2:]))

for ep in range(a, b + 1):
    qa = load(ep)
    d = ROOT / "out" / f"ep{ep:03d}"
    if not qa or not any(f["file"].endswith("-4k.mp4") for f in qa["files"]):
        v = "SKIPPED" if ep in skipped else "PENDING"
        counts["PENDING"] += 1
        rows.append((ep, v, "", "", "", "", "", ""))
        continue
    long = next(f for f in qa["files"] if f["file"].endswith("-4k.mp4"))
    shorts = [f for f in qa["files"] if "-S" in f["file"]]
    n_ok = sum(1 for s in shorts if s["verdict"] != "FAIL" and (d / s["file"]).exists())
    nb = sum(len(f.get("black") or []) for f in qa["files"])
    black += nb
    v = qa["verdict"]
    counts[v] = counts.get(v, 0) + 1
    if long.get("seconds"):
        secs_total += long["seconds"]
        done_n += 1
    notes = "; ".join(n for f in qa["files"] for n in (f.get("notes") or []))[:90]
    rows.append((ep, v, f"{long.get('lufs')}", f"{long.get('tp')}", f"{long.get('mb')}", f"{n_ok}/5", str(nb), notes))

finished = sum(counts[k] for k in ("PASS", "WARN", "FAIL"))
total = b - a + 1
eta = ""
if done_n and finished < total:
    avg = secs_total / done_n
    eta = f" ETA about {avg * (total - finished) / 3600:.1f} h of long-video render time (plus Shorts)."
summary = (f"EP{a}-{b}: {finished}/{total} done. PASS {counts['PASS']}, WARN {counts['WARN']}, FAIL {counts['FAIL']}, "
           f"pending/skipped {counts['PENDING']}. Black frames: {black}.{eta}")
if status_only:
    print(summary)
    sys.exit(0)

lines = [f"# Full render report EP{a}-EP{b}", "", f"Generated {datetime.now(timezone.utc).isoformat(timespec='seconds')}", "", summary, ""]
lines += ["Rule: PASS = loudness -16 +/- 1 and true peak below -1.5 dBTP; WARN = -1.5 to -1.0 (listen); FAIL = above -1.0 or black frames or missing file.", "",
          "| EP | Verdict | LUFS | True peak | Long MB | Shorts OK | Black | Notes |", "|---|---|---|---|---|---|---|---|"]
lines += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |" for r in rows]
attention = [r[0] for r in rows if r[1] not in ("PASS",)]
lines += ["", f"Needs attention: {', '.join(str(e) for e in attention) if attention else 'none'}", ""]
out = ROOT / "out" / "render-all-report.md"
out.write_text("\n".join(lines), encoding="utf-8")
print(summary)
print(f"Wrote {out}")
