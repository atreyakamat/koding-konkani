#!/usr/bin/env python3
"""Simplified Technical English (ASD-STE100 style) lint for the Python Bible narration.

Checks the spoken text of every scene and every Short in docs/python-bible/mNN.md.
ERROR rules must be zero. WARN rules are reviewed by a person.

Usage: python3 scripts/ste_lint_py.py docs/python-bible/m*.md [--warn]
Rules follow docs/python-bible/STE.md. Exempt: scene 9 (Pun card, a joke by design) and the
fixed sign-off "Keep coding, says Xecxec!".
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

MAX_WORDS = 20
CONTRACTION = re.compile(r"\b\w+n't\b|\b(?:it|we|let|that|there|here|he|she|who|what)'s\b|\b(?:I|you|we|they)'(?:ll|ve|re|d)\b", re.I)
FUTURE = re.compile(r"\b(?:will|would|shall|going to)\b", re.I)
IDIOMS = re.compile(r"\b(?:a bit|kind of|sort of|pretty much|piece of cake|under the hood|a lot of|stuff|things like that|and so on|etc|and the like)\b", re.I)
PART = ("called used given made shown stored tied written run passed returned created set built taken seen found known printed "
        "raised caught saved read opened closed changed kept held left put sent done chosen joined split sorted placed defined applied "
        "replaced removed added marked stopped skipped needed wrapped moved checked loaded converted ignored hidden lost broken filled "
        "mixed counted compared handled swallowed rejected finished started expected allowed assigned connected").split()
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being) (?:not )?(?:" + "|".join(PART) + r")\b", re.I)
SIGNOFF = "Keep coding, says Xecxec!"


def clean(text: str) -> str:
    text = re.sub(r"\\?\[(?:HL|TRACK)[^\]]*\\?\]", " ", text)
    return text.replace(SIGNOFF, " ").replace("\\", "")


def sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", clean(text)) if s.strip()]


def lint_text(text: str) -> tuple[list[str], list[str]]:
    errs: list[str] = []
    warns: list[str] = []
    sents = sentences(text)
    for s in sents:
        n = len(s.split())
        if n > MAX_WORDS:
            errs.append(f"S1 sentence has {n} words (max {MAX_WORDS}): {s[:70]}")
        if CONTRACTION.search(s):
            errs.append(f"S2 contraction: {s[:70]}")
        if FUTURE.search(s):
            errs.append(f"S3 future or conditional tense: {s[:70]}")
        if ";" in s or "(" in s or "—" in s:
            errs.append(f"S4 semicolon, bracket or dash: {s[:70]}")
        if IDIOMS.search(s):
            errs.append(f"S5 vague phrase or idiom: {s[:70]}")
        if PASSIVE.search(s):
            warns.append(f"W1 passive voice: {s[:70]}")
    if len(sents) > 6:
        warns.append(f"W2 paragraph has {len(sents)} sentences (aim for 6 or fewer)")
    return errs, warns


def main(argv: list[str]) -> int:
    show_warn = "--warn" in argv
    total_e = total_w = 0
    for f in [a for a in argv if not a.startswith("--")]:
        body = Path(f).read_text(encoding="utf-8")
        for ep in re.split(r"(?m)^## EP ", body)[1:]:
            tag = "EP " + ep.split(" ", 1)[0]
            items = [(f"scene {n}", t) for n, t in re.findall(r"^\*\*\\\[(\d+) · [^\]]*?\\\]\*\* (.*)$", ep, re.M) if n != "9"]
            items += [(sid, t) for sid, t in re.findall(r"^\*\*(S\d) · .*?\n- \*\*Hook.*?\n- \*\*Script:\*\* (.*?)$", ep, re.M | re.S)]
            for where, text in items:
                e, w = lint_text(text)
                total_e += len(e)
                total_w += len(w)
                for m in e:
                    print(f"ERROR {Path(f).name} {tag} {where}: {m}")
                if show_warn:
                    for m in w:
                        print(f"warn  {Path(f).name} {tag} {where}: {m}")
    print(f"{total_e} errors, {total_w} warnings")
    return 1 if total_e else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
