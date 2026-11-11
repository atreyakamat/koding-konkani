#!/usr/bin/env python3
"""Print each [HL n] cue with the code line it points at, for a human review of the highlight cues.

Usage: python scripts/cpp_bible/hl_view.py m03 [EP]
"""
import re
import sys
from pathlib import Path

BIBLE = Path(__file__).resolve().parent.parent.parent / "docs" / "cpp-bible"


def main() -> None:
    md = (BIBLE / f"{sys.argv[1]}.md").read_text(encoding="utf-8")
    only = int(sys.argv[2]) if len(sys.argv) > 2 else None
    parts = re.split(r"^## EP (\d+) — (.+)$", md, flags=re.M)
    for i in range(1, len(parts) - 2, 3):
        ep, body = int(parts[i]), parts[i + 2]
        if only and ep != only:
            continue
        files = re.findall(r"```cpp\n(.*?)\n```", body.split("### Illustrations")[0].split("### Code shown")[1], re.S)
        for scene, src in ((3, files[0]), (5, files[1])):
            m = re.search(r"^\*\*\\\[%d · .*?\\\]\*\* (.*?)(?=^\*\*\\\[\d+ · )" % scene, body, re.S | re.M)
            if not m:
                continue
            lines = src.split("\n")
            print(f"EP{ep:02d} scene {scene}")
            pieces = re.split(r"\\\[HL (\d+)\\\]", m.group(1))
            for k in range(1, len(pieces), 2):
                n = int(pieces[k])
                said = re.sub(r"\\\[TRACK [^\]]*\\\]", "", pieces[k + 1]).strip()
                print(f"   HL{n:>2} | {lines[n - 1].strip()[:44]:<44} | {said[:48]}")


main()
