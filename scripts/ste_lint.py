#!/usr/bin/env python3
"""Mechanical lint for the Simplified Technical English (STE) rules in docs/cpp-bible/STE.md.

This is a subset of ASD-STE100. The official dictionary is licensed, so this lint cannot prove
full conformance. It enforces the rules a machine can check, so narration stays plain,
short and easy for the narrator voice to read.

Library use:  lint_paragraph(text) -> list[(level, code, message)]   (level is "ERROR" or "WARN")
CLI use:      python scripts/ste_lint.py "Some narration text."
"""Simplified Technical English (ASD-STE100 style) lint for the Python Bible narration.

Checks the spoken text of every scene and every Short in docs/python-bible/mNN.md.
ERROR rules must be zero. WARN rules are reviewed by a person.

Usage: python3 scripts/ste_lint.py docs/python-bible/m*.md [--warn]
Rules follow docs/python-bible/STE.md. Exempt: scene 9 (Pun card, a joke by design) and the
fixed sign-off "Keep coding, says Xecxec!".
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
