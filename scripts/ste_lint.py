#!/usr/bin/env python3
"""Mechanical lint for the Simplified Technical English (STE) rules in docs/cpp-bible/STE.md.

This is a subset of ASD-STE100. The official dictionary is licensed, so this lint cannot prove
full conformance. It enforces the rules a machine can check, so narration stays plain,
short and easy for the narrator voice to read.

Library use:  lint_paragraph(text) -> list[(level, code, message)]   (level is "ERROR" or "WARN")
CLI use:      python scripts/ste_lint.py "Some narration text."
"""
from __future__ import annotations

import re
import sys

MAX_WORDS = 20          # words in one sentence
MAX_SENTENCES = 6       # sentences in one paragraph
CUE = re.compile(r"\[(?:HL \d+|TRACK [^\]]*)\]\s*")
SENTENCE_END = re.compile(r"(?<=[.?!])\s+")
WORD = re.compile(r"[A-Za-z]+(?:-[A-Za-z]+)*")
# Characters the narrator voice reads badly or not at all.
BAD_CHARS = re.compile(r"[0-9_+=<>{}()\[\]/\\*&|#%^~;@$`\"]")
APOSTROPHE = re.compile(r"['’]")
BANNED = [
    "utilize", "utilise", "perform", "performs", "performed", "commence", "ensure", "ensures",
    "in order to", "prior to", "approximately", "subsequently", "whereas", "additionally",
    "furthermore", "e.g", "i.e", "etc", "via", "thus", "hence", "basically", "simply put",
    "obviously", "just ", "very ", "really ",
]
IRREGULAR = {"written", "given", "taken", "shown", "seen", "done", "made", "kept", "held", "known",
             "chosen", "broken", "begun", "run", "built", "sent", "found", "lost", "read"}
PASSIVE = re.compile(r"\b(is|are|was|were|be|been|being)\s+(?:not\s+)?(\w+ed|" + "|".join(IRREGULAR) + r")\b", re.I)
# Past participles that act as plain adjectives in our topic, so they are fine after "is" or "are".
PASSIVE_OK = {"required", "supposed", "allowed", "based", "related", "used", "unused", "closed", "called", "named",
              "assigned", "initialised", "initialized", "indented", "typed", "tied", "mixed", "needed", "empty"}


def clean(text: str) -> str:
    return CUE.sub("", text).strip()


def sentences(par: str) -> list[str]:
    return [s for s in SENTENCE_END.split(clean(par)) if s.strip()]


def count_words(s: str) -> int:
    return len(WORD.findall(s))


def lint_paragraph(text: str) -> list[tuple[str, str, str]]:
    probs: list[tuple[str, str, str]] = []
    t = clean(text)
    if not t:
        return probs
    sents = sentences(t)
    if len(sents) > MAX_SENTENCES:
        probs.append(("ERROR", "STE-PARA", f"{len(sents)} sentences in one paragraph (max {MAX_SENTENCES})"))
    for s in sents:
        n = count_words(s)
        if n > MAX_WORDS:
            probs.append(("ERROR", "STE-LEN", f"{n} words (max {MAX_WORDS}): {s[:80]}"))
    if APOSTROPHE.search(t):
        probs.append(("ERROR", "STE-APOS", "apostrophe or contraction: " + t[max(0, APOSTROPHE.search(t).start() - 12):][:30]))
    m = BAD_CHARS.search(t)
    if m:
        probs.append(("ERROR", "TTS-CHAR", f"digit or symbol {m.group(0)!r} in narration (write it as words): "
                      + t[max(0, m.start() - 15):m.start() + 15]))
    low = " " + t.lower() + " "
    for b in BANNED:
        if re.search(r"(?<![a-z])" + re.escape(b.strip()) + r"(?![a-z])", low):
            probs.append(("ERROR", "STE-WORD", f"banned word or phrase: {b.strip()!r}"))
    if "!" in t and t.count("!") > 2:
        probs.append(("ERROR", "STE-EXCL", "more than two exclamation marks in one paragraph"))
    for m in PASSIVE.finditer(t):
        if m.group(2).lower() not in PASSIVE_OK:
            probs.append(("WARN", "STE-PASSIVE", f"possible passive voice: {m.group(0)!r}"))
    return probs


def lint_text(text: str) -> list[tuple[str, str, str]]:
    out: list[tuple[str, str, str]] = []
    for par in re.split(r"\n\s*\n", text):
        out.extend(lint_paragraph(par))
    return out


if __name__ == "__main__":
    txt = " ".join(sys.argv[1:]) or sys.stdin.read()
    ps = lint_text(txt)
    for lv, code, msg in ps:
        print(f"{lv} {code}: {msg}")
    sys.exit(1 if any(p[0] == "ERROR" for p in ps) else 0)
