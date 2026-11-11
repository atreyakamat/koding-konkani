#!/usr/bin/env python3
"""Pixel checks on the scene stills made by stills_all.mts: finds text or panels that run into the caption band
(bottom 14 %) or off the left/right/top edge. A heuristic, not a proof: a hit means "look at this still".

Usage: python3 scripts/check_stills.py out/stills-python
"""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

INK = 70            # luminance below this counts as ink
SKIP = ("title-card", "pun-card", "outro")


def dark_count(im: Image.Image, box: tuple[int, int, int, int]) -> int:
    g = im.crop(box).convert("L")
    return sum(1 for p in g.getdata() if p < INK)


def main() -> int:
    root = Path(sys.argv[1])
    hits = 0
    files = sorted(root.glob("ep*-s*-*.png"))
    for f in files:
        tpl = f.stem.split("-", 2)[2]
        if tpl in SKIP:
            continue
        im = Image.open(f).convert("RGB")
        w, h = im.size
        # Caption band: the bottom 14 %, left 70 % (the mascot lives bottom right).
        band = dark_count(im, (0, int(h * 0.86), int(w * 0.70), h))
        edge = dark_count(im, (0, 0, 3, h)) + dark_count(im, (w - 3, 0, w, h)) + dark_count(im, (0, 0, w, 3))
        if band > 40 or edge > 20:
            print(f"{f.name}: caption-band ink {band}, edge ink {edge}")
            hits += 1
    print(f"{len(files)} stills checked, {hits} to look at")
    return 0


if __name__ == "__main__":
    sys.exit(main())
