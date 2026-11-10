# Session summary (2026-11-06 → 2026-11-08)

## What was asked
- Rework the C++ and Python Bibles (90 episodes each) so they parse into the Remotion pipeline via the strict `bible_to_json.py` format, resolve all bugs, and check about 10 times.
- Review the PC and laptop renders and finish EP1–50.
- Write M1 (EP5–12) for both courses in parallel.
- Summarise progress, explain how to move the chat to a Project, then archive everything to GitHub and write this handoff.

## What happened
1. **M0 (EP1–4), both courses:** written in strict format, parsed with the real parser, inserted into both Claude Docs.
2. **Renders:** EP1–50 all rendered (4K long + Shorts S1–S5), QA PASS, across PC and laptop. Laptop output reached the PC via Taildrop into `out\from-laptop\`.
3. **EP34 investigation:** failure was a GCC quote-style (locale) mismatch in `check_c.py` on the laptop; Bible text was fine. Verified and rendered on the PC.
4. **M1 (EP5–12), both courses:** written by parallel subagents, checked with `check_m1.py`; delivered as `cpp_m01.md` and `py_m01.md`; not yet in the Claude Docs.
5. **Project migration:** a chat cannot be moved from this session; fallback is a new Project with the docs as knowledge plus this handoff.

## Errors and fixes
| Problem | Fix |
| --- | --- |
| Python tracebacks leaked temp paths | Regex in `run_py` rewrites to the bare file name |
| Code explain scenes with no code | Converted to Concept slide; stray `[HL]` removed |
| Python EP2 bug was a one-liner in `hello.py` | Two-line `fish.py` |
| Pun scenes fixed at 4 s | `max(4, ceil(words/WPS))` |
| I said the default was GCC 13 and suggested installing MSYS2 | Wrong: PC already has MSYS2 GCC 16.2.0; C Bible assumes GCC 14+. Corrected, nothing to install |
| EP35–36 wrongly listed as unreviewed | Corrected: approved earlier |
| EP34 prompt ran on laptop, file not on PC | Moved through Taildrop |

## Not done
- M1 into the Claude Docs; M2–M10 for both courses.
- C++/Python pipeline work; GCC 16 re-check of C++ error texts.
- C EP51–86 rendering and their data gaps.
