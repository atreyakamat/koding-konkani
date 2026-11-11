"""Build copy-ready upload sheets from episode JSON (owner uploads by hand; nothing is published here).

Usage: python3 scripts/publish_pack.py [--lang python]
Reads  episodes-python/epNNN.json  (or episodes/ for C)
Writes docs/python-bible/publish/mNN.md  (or docs/publish/ for C)
One block per long video and per Short: title, description with chapters on their own lines, tags,
thumbnail text, caption and hashtags. Chapters come from planned timings: recompute them from the
final audio before upload (the pipeline does this after voice generation).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIGN = "Keep coding, says Xecxec!"


def long_description(yt: dict) -> str:
    intro = yt["description"].split(" 0:00 ")[0].strip()
    chapters = "\n".join(f"{c['t']} {c['label']}" for c in yt["chapters"])
    return f"{intro}\n\n{chapters}\n\n{SIGN}"


def block(ep: dict, prefix: str) -> str:
    yt = ep["youtube"]
    out = [f"## EP {ep['ep']:02d} — {ep['title']}", ""]
    out += ["### Long video", "", f"**Title:** {yt['title']}", "", "**Description:**", "", "```text", long_description(yt), "```", "",
            f"**Tags:** {', '.join(yt['tags'])}", "", f"**Thumbnail text:** {yt['thumbnail']['text']}", "",
            f"**Thumbnail art:** {yt['thumbnail']['visual']}", ""]
    out += ["### Shorts", ""]
    for s in ep["shorts"]:
        tags = " ".join(f"#{h.lstrip('#')}" for h in s["hashtags"])
        out += [f"**{s['id']} · {s['title']}** ({s['lengthSec']} s)", "",
                f"- Caption: {s['caption']} {tags}", f"- On screen: {s['onScreen']}",
                f"- Description: {s['caption']} Full video: EP {ep['ep']:02d} — {yt['title']}. {SIGN}", ""]
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang", choices=["c", "python"], default="python")
    a = ap.parse_args()
    src = ROOT / ("episodes-python" if a.lang == "python" else "episodes")
    dst = ROOT / "docs" / ("python-bible/publish" if a.lang == "python" else "publish")
    dst.mkdir(parents=True, exist_ok=True)
    mods: dict[int, list[dict]] = {}
    for f in sorted(src.glob("ep*.json")):
        ep = json.loads(f.read_text(encoding="utf-8"))
        mods.setdefault(ep["module"], []).append(ep)
    problems = 0
    for m, eps in sorted(mods.items()):
        text = [f"# Upload sheet — Module {m}", "",
                "Copy-ready titles, descriptions, tags, thumbnail text and Shorts captions. Chapters use planned timings; recompute from the final audio before upload.", ""]
        for ep in eps:
            yt = ep["youtube"]
            if len(yt["title"]) > 100:
                print(f"EP{ep['ep']:02d}: title over 100 characters"); problems += 1
            if len(ep["shorts"]) != 5:
                print(f"EP{ep['ep']:02d}: expected 5 Shorts"); problems += 1
            if not yt["chapters"] or yt["chapters"][0]["t"] != "0:00" or len(yt["chapters"]) < 3:
                print(f"EP{ep['ep']:02d}: chapters must start at 0:00 and have 3 or more entries"); problems += 1
            if len(", ".join(yt["tags"])) > 500:
                print(f"EP{ep['ep']:02d}: tags over 500 characters"); problems += 1
            text.append(block(ep, ""))
        (dst / f"m{m:02d}.md").write_text("\n".join(text) + "\n", encoding="utf-8")
    print(f"{sum(len(v) for v in mods.values())} episodes, {problems} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main())
