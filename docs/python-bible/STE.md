# Writing rules: Simplified Technical English (practical subset)

Every narration, on-screen text and challenge in the Python Bible follows these rules. Claude Code must follow them when it edits an episode.

**Honest limit:** the official ASD-STE100 specification and dictionary are not in this repository. `scripts/ste_lint.py` checks a practical subset. It does not prove full ASD-STE100 compliance. If the owner has the official dictionary, give it to the linter as an extra word list.

## Rules

| Code | Level | Rule |
|---|---|---|
| S1 | error | A sentence has at most 20 words. |
| S2 | error | No contractions (use "do not", not "don't"). |
| S3 | error | No future or conditional tense: will, would, shall, going to. Use the present tense. |
| S4 | error | No semicolon, bracket or dash in narration. One idea per sentence. |
| S5 | error | No vague phrase or idiom (for example "a bit", "kind of", "basically"). |
| W1 | warning | Avoid passive voice. Say who does the action. |
| W2 | warning | A paragraph has at most 6 sentences. |

Exempt: scene 9 (Pun) and the sign-off "Keep coding, says Xecxec!".

Also: one word, one meaning. Use the same name for the same thing in every episode. Use short, common words. Spoken code (`__x__`, `f(x)`, `a.b`) is turned into words by `spoken()` in `gen.py` ("dunder x", "f of x", "a dot b").

## Commands

```
python3 scripts/ste_lint.py docs/python-bible/m*.md          # errors only
python3 scripts/ste_lint.py docs/python-bible/m*.md --warn   # errors and warnings
python3 scripts/check_py.py docs/python-bible/m*.md                               # code, output, timing, Shorts length
python3 scripts/check_illustrations.py --write               # illustration specs
```

Status at last run: 0 STE errors, 0 checker problems, 0 illustration problems. Passive-voice and long-paragraph warnings remain and need no action for render.

Edit the data files in `scripts/python_bible/` and regenerate. Do not edit `m01.md`-`m10.md` by hand (`m00.md` is hand-written).
