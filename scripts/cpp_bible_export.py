#!/usr/bin/env python3
"""Export upload metadata for every C++ episode from docs/cpp-bible/m*.md.

Read-only on the Bible. Writes docs/cpp-bible/metadata/:
  epNNN.json            one file per episode: YouTube title, description, chapters, tags,
                        thumbnail spec, and the five Shorts
  index.json            all 90 episodes in one list
  upload-sheet.md       one readable page per episode, ready to copy into YouTube Studio
It also checks the YouTube limits and exits 1 on any problem:
  title <= 100 characters, description <= 5000, tags total <= 500 characters,
  chapters start at 0:00, at least three chapters, each at least 10 seconds.

The owner uploads. This script never uploads anything.

Usage: python scripts/cpp_bible_export.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BIBLE = ROOT / "docs" / "cpp-bible"
OUT = BIBLE / "metadata"


def mmss(s: str) -> int:
    a, b = s.split(":")
    return int(a) * 60 + int(b)


def bullet(body: str, label: str) -> str:
    m = re.search(rf"^- \*\*{re.escape(label)}:\*\* (.+)$", body, re.M)
    return m.group(1).strip() if m else ""


def parse_episode(n: int, title: str, body: str) -> tuple[dict, list[str]]:
    errs: list[str] = []
    head = re.search(r"^\*\*Module (\d+) · (.+?) · (\d+:\d+) · (.+?) · Prerequisite: (.+?)\*\*", body, re.M)
    if not head:
        return {}, [f"EP {n}: header line not found"]
    yt_title = bullet(body, "Title")
    desc_raw = bullet(body, "Description")
    tags = [t.strip() for t in bullet(body, "Tags").split(",") if t.strip()]
    thumb_raw = bullet(body, "Thumbnail")
    m = re.match(r'big text "(.+?)" in (.+?); Xecxec (.+?); (.+)', thumb_raw)
    thumb = {"raw": thumb_raw, "text": m.group(1) if m else "", "colours": m.group(2) if m else "",
             "visual": m.group(3) if m else "", "style": m.group(4) if m else ""}
    # The description holds the chapters after the intro sentence, separated by " · ".
    first = re.search(r"\s0:00 ", desc_raw)
    intro = desc_raw[:first.start()].strip() if first else desc_raw
    chapters = []
    if first:
        for part in desc_raw[first.start():].split(" · "):
            mm = re.match(r"\s*(\d+:\d{2}) (.+)", part)
            if mm:
                chapters.append({"t": mm.group(1), "label": mm.group(2).strip()})
    description = intro + "\n\n" + "\n".join(f"{c['t']} {c['label']}" for c in chapters) + \
        "\n\nKeep coding, says Xecxec!\n\n#cpp #kodingkonkani"
    length = mmss(head.group(3))
    # limits
    if len(yt_title) > 100:
        errs.append(f"EP {n}: title is {len(yt_title)} characters (max 100)")
    if len(description) > 5000:
        errs.append(f"EP {n}: description is {len(description)} characters (max 5000)")
    if sum(len(t) for t in tags) + len(tags) > 500:
        errs.append(f"EP {n}: tags are too long (max 500 characters)")
    if len(chapters) < 3:
        errs.append(f"EP {n}: {len(chapters)} chapters (need 3 or more)")
    elif chapters[0]["t"] != "0:00":
        errs.append(f"EP {n}: first chapter must start at 0:00")
    for a, b in zip(chapters, chapters[1:]):
        if mmss(b["t"]) - mmss(a["t"]) < 10:
            errs.append(f"EP {n}: chapter {a['t']} is shorter than 10 seconds")
    if chapters and mmss(chapters[-1]["t"]) >= length:
        errs.append(f"EP {n}: last chapter starts after the end")
    if not thumb["text"]:
        errs.append(f"EP {n}: thumbnail text not found")
    elif len(thumb["text"]) > 20:
        errs.append(f"EP {n}: thumbnail text is longer than 20 characters")
    # shorts
    shorts = []
    for sm in re.finditer(r"^\*\*(S[1-5]) · (.+?)\*\* — (\d+:\d+) · built from scenes? ([\d, ]+)\n(.*?)(?=^\*\*S[1-5] ·|\Z)",
                          body.split(f"### Shorts for EP {n}")[-1], re.M | re.S):
        blk = sm.group(5)
        cap = bullet(blk, "Caption + hashtags")
        tagsx = re.findall(r"#\w+", cap)
        shorts.append({
            "id": sm.group(1), "title": sm.group(2), "lengthSec": mmss(sm.group(3)),
            "fromScenes": [int(x) for x in re.findall(r"\d+", sm.group(4))],
            "hook": bullet(blk, "Hook (first 1.5s)").strip('"'), "script": bullet(blk, "Script"),
            "onScreen": bullet(blk, "On-screen text"),
            "caption": re.sub(r"\s*#\w+", "", cap).strip(), "hashtags": tagsx,
            "link": f"Full video: EP {n:02d}",
        })
    if [s["id"] for s in shorts] != ["S1", "S2", "S3", "S4", "S5"]:
        errs.append(f"EP {n}: found Shorts {[s['id'] for s in shorts]} (need S1 to S5)")
    for s in shorts:
        if not 35 <= s["lengthSec"] <= 45:
            errs.append(f"EP {n} {s['id']}: {s['lengthSec']} seconds (need 35 to 45)")
    ep = {"ep": n, "title": title, "module": int(head.group(1)), "moduleName": head.group(2), "lengthSec": length,
          "colours": head.group(4), "prerequisite": head.group(5),
          "youtube": {"title": yt_title, "description": description, "chapters": chapters, "tags": tags, "thumbnail": thumb},
          "shorts": shorts}
    return ep, errs


def sheet(ep: dict) -> str:
    y = ep["youtube"]
    t = y["thumbnail"]
    L = [f"## EP {ep['ep']:02d} — {ep['title']}", "",
         f"Module {ep['module']} · {ep['moduleName']} · {ep['lengthSec'] // 60}:{ep['lengthSec'] % 60:02d}", "",
         "**YouTube title**", "", y["title"], "", "**Description**", "", "```text", y["description"], "```", "",
         "**Tags**", "", ", ".join(y["tags"]), "",
         "**Thumbnail**", "", f"- Text: {t['text']}", f"- Colours: {t['colours']}", f"- Picture: Xecxec {t['visual']}", f"- Style: {t['style']}", "",
         "**Shorts**", ""]
    for s in ep["shorts"]:
        L += [f"- **{s['id']} · {s['title']}** ({s['lengthSec']} s)", f"  - Caption: {s['caption']} {' '.join(s['hashtags'])}",
              f"  - Hook: {s['hook']}", f"  - On screen: {s['onScreen']}"]
    return "\n".join(L) + "\n"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    eps: list[dict] = []
    errs: list[str] = []
    for f in sorted(BIBLE.glob("m[0-9][0-9].md")):
        text = f.read_text(encoding="utf-8")
        parts = re.split(r"^## EP (\d+) — (.+)$", text, flags=re.M)
        for i in range(1, len(parts) - 2, 3):
            ep, e = parse_episode(int(parts[i]), parts[i + 1].strip(), parts[i + 2])
            errs += e
            if ep:
                eps.append(ep)
    eps.sort(key=lambda e: e["ep"])
    if [e["ep"] for e in eps] != list(range(1, 91)):
        errs.append(f"found {len(eps)} episodes, need EP 1 to 90 with no gap")
    titles = [e["youtube"]["title"] for e in eps]
    if len(set(titles)) != len(titles):
        errs.append("two episodes share one YouTube title")
    for e in eps:
        (OUT / f"ep{e['ep']:03d}.json").write_text(json.dumps(e, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "index.json").write_text(json.dumps(eps, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (OUT / "upload-sheet.md").write_text(
        "# C++ upload sheet (EP 1 to 90)\n\nGenerated by scripts/cpp_bible_export.py. Do not edit by hand; edit the Bible and run the script again.\n\n"
        + "\n".join(sheet(e) for e in eps), encoding="utf-8")
    for e in errs:
        print("PROBLEM", e)
    print(f"{len(eps)} episodes, {sum(len(e['shorts']) for e in eps)} Shorts, {len(errs)} problems -> {OUT.relative_to(ROOT)}")
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
