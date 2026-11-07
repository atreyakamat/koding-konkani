# Koding Konkani — Full Project Handoff (2026-11-08)

Claude Doc: https://claude.ai/artifact/KZLkjQRrpFFdezurHP5XEn (this file is the Markdown copy).

## Status at a glance

The C course has EP1–50 fully rendered (4K long video plus Shorts S1–S5, QA PASS); EP51–86 are not rendered. The C++ and Python Bibles have M0 and M1 (EP1–12) written in the strict parser format, but M2–M10 and the pipeline changes are not started.

| Track | Done | Open |
| --- | --- | --- |
| C course (86 eps) | EP1–50 rendered, QA PASS | EP51–86 render; Memory boxes data for ~43 scenes (EP51–83); bars traces; EP77/EP81 pegs |
| C++ course (90 eps) | M0 (EP1–4) and M1 (EP5–12) written and parse-checked | M1 not yet in the Claude Doc; M2–M10 (EP13–90); pipeline; GCC 16 re-check of error texts |
| Python course (90 eps) | M0 (EP1–4) and M1 (EP5–12) written and parse-checked | M1 not yet in the Claude Doc; M2–M10 (EP13–90); pipeline |
| Uploads | Owner uploads from EP1 in order | Claude never uploads |

## Channel and course decisions

- **Volume:** 86 long videos (5–8 min, 1920×1080, 30 fps, H.264 CRF 18; 4K masters via `--scale=2`) and 430 Shorts (1080×1920, 5 per episode).
- **Language and tone:** English only; friendly, fun, puns. Sign-off: "Keep coding, says Xecxec!"
- **Mascot:** Crab Xecxec ("Sheck Sheck") never speaks.
- **Narrator:** Kokoro TTS on CPU (`config/voice.json`), deliberately slow. About 1.8 words/second for scenes, 2.0 for Shorts. Never speed the voice up; audio length wins over Bible scene targets.
- **Audio:** −16 LUFS integrated, peaks below −1 dBTP; music bed about −24 dB under speech; royalty-free only, licences in `audio/*/LICENSES.md`.
- **Design system:** neo-brutalism pastel; Archivo Black, Space Grotesk, JetBrains Mono; 14 module colour pairs.
- **Machine:** Windows 11, Ryzen 7 5700G, 16 GB, CPU only; concurrency starts at 4, lower if RAM passes ~13 GB.

### Module maps (new courses)

| Module | C++ episodes | Python episodes |
| --- | --- | --- |
| M0 | 1–4 | 1–4 |
| M1 | 5–12 | 5–12 |
| M2 | 13–20 | 13–22 |
| M3 | 21–30 | 23–32 |
| M4 | 31–40 | 33–40 |
| M5 | 41–50 | 41–50 |
| M6 | 51–60 | 51–60 |
| M7 | 61–68 | 61–72 |
| M8 | 69–76 | 73–80 |
| M9 | 77–84 | 81–86 |
| M10 | 85–90 | 87–90 |

## C course progress

- **Rendered:** EP1–50, 4K long plus Shorts S1–S5. EP34 re-verified and rendered on the PC on 2026-11-07.
- **EP34 "bug":** not a Bible error. `check_c.py` failed on the laptop because GCC's quote style (curly vs straight) follows the locale.
- **Sheets not yet eyeballed:** EP1–19 long sheets and S1–S4; EP41–50 long sheets; EP20–33 Shorts S1–S4.
- **Data gaps for EP51–86:** ~43 Memory boxes scenes (EP51–83); some Algorithm bars traces; EP77 and EP81 pegs and mini rows.
- **Bible correction pending:** quick-sort count should read 4 visible swaps plus 5 self-swaps (owner has not said "fix Bible").
- **Cosmetic:** EP2 S5 wraps "TRANSLA / TOR?"; "?" glyph in EP39/40 output panel; EP25 S3 tiny bug text; EP36 `shapes.h` wrapping; EP37/EP34 transition frames look clipped (probably sampling).

## C++ and Python courses

Both Bibles were reworked into the strict format `bible_to_json.py` parses, then checked in about 10 passes. M0 is in both Claude Docs; M1 is in `bible-drafts/` only.

- **Format:** `## EP NN — Title`, bold module line, learning goals, `### YouTube`, scene table, narration with `[HL n]` / `[TRACK a=1]` cues, `### Code shown`, `### Bug of the Day`, `### Pun & challenge`, five Shorts.
- **Rules found:** Code explain scenes need a mapped code file (else Concept slide); `[HL]` only in code scenes and in range; pun scene length = `max(4, ceil(words/WPS))`; Python parser reads one-line stdin only ("Input: 3").
- **M0:** 11 scenes per episode, 4:53–5:34.

| Course | M1 lengths | Bug notes |
| --- | --- | --- |
| C++ | 5:37, 5:12, 5:04, 5:04, 5:19, 5:32, 5:24, 5:24 | Real compile errors in EP9 (narrowing), EP10 (read-only variable), EP11 (invalid operands). Compiles-but-wrong in EP5, 6, 7, 8, 12 |
| Python | 5:17, 5:17, 5:10, 5:03, 5:04, 5:17, 5:09, 5:13 | EP5 NameError, EP6 assert on 0.1+0.2, EP7 str + int, EP8 input() times float, EP9 2 ^ 0.5, EP10 `{total:.2d}` on float, EP11 `print(age = 17)`, EP12 `int("abc")` |

## Pipeline and tooling facts

- **C-hardcoded:** 86 episodes in `validate_episodes.mts`, `check_puns.mts`, `check_c.py`; fences c / cpp / text / bash only.
- **Needed for C++/Python:** language-aware parser, 90 episodes, python fences, `check_cpp` / `check_py`, Python highlighter, `derive_boxes` data. Not started (see `pipeline-patches/` for the scratch parser changes).
- **Gate:** `check_scenes.mts` fails Memory boxes scenes with no boxes and Algorithm bars with no trace.
- **Compiler:** PC uses MSYS2 GCC 16.2.0 (`C:\msys64\ucrt64\bin`). The MinGW.org GCC 6.3.0 from `cc --version` is a stray in PATH; install nothing. C Bible assumes GCC 14+.
- **C++ error texts** were checked on g++ 13.3; re-check on GCC 16 before rendering.
- **Laptop → PC:** Taildrop, then move from Downloads into `out\from-laptop\`.
- **Bridge folders:** `G:\Projects\koding-konkani`, `G:\Projects\new-channel`.

## Guardrails

- Show a short plan before each piece of work; owner reviews everything.
- Feature branches and draft PRs; **never push to main**.
- No spending, paid sign-ups or paid APIs without asking.
- No deleting files, repos or data without asking.
- Never touch credentials, API keys or `.env`; never commit secrets.
- Never touch client production systems, live sites, bank, payment or store accounts.
- Never publish or upload videos; owner uploads.
- Compile every C sample with GCC before rendering. Renders go to `out/`, never the repo.

## Open items and next steps

1. Put C++ and Python M1 into the two Claude Docs.
2. Write M2 (C++ EP13–20, Python EP13–22), then M3–M10.
3. Build the C++/Python pipeline changes; re-check C++ error texts on GCC 16.
4. Render C EP51–86 after adding Memory boxes data and bars traces.
5. Fix the Bible quick-sort count if the owner says so.
6. Eyeball the unchecked sheets.
7. Owner uploads videos from EP1 in order.
