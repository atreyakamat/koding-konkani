# Python Bible: builder notes

Source of truth: this repo (`docs/python-bible/mNN.md`, generated from `scripts/python_bible/mNN.py`). Claude Docs copies are regenerated from it for review.

## Fixed decisions
- Python 3.13 everywhere. Checker flags: `-s -P`, `PYTHONHASHSEED=0`, `PYTHONUNBUFFERED=1`, typed stdin, fixture files, timeouts.
- Missing-file errors are written in Windows wording (`[WinError 2] The system cannot find the file specified`). The checker converts the Linux text to it, so both machines agree. Confirm on the Windows PC in the pilot.
- Shorts are 35-45 s for all five (template table of 25-35 s / 20-30 s is superseded). Length = ceil(words / 2) + 4 s lead-in and badge.
- 11 scenes per episode (Title, Concept, Code A, Memory or Concept, Code B, Terminal, Recap, Bug, Pun, Challenge, Outro).
- S5 badge reads "EP NN" (zero padded) at render time.
- Random is always seeded (EP22, EP82). No `now()` is printed (EP81). Sets use ints or `sorted()`.
- EP84 uses a recorded response, labelled "recorded response" on screen.

## Open before rendering
1. Windows commands for `python` vs `python3` (EP2) and venv activation (EP58): confirm the on-screen text on the PC.
2. Pilot render on the PC: EP1, EP4 (first Memory scene), one aliasing episode (EP28 or EP31). View stills of the Memory component with shared objects.
3. Pipeline: language-aware parser, 90 episodes, python fences, own folders and marker tags. Branch from the tip of `feat/ep51-86-render-data` (check_c Linux fix, `RENDER_CONCURRENCY`).
4. Recompute YouTube chapters from the final audio.
5. Narrator pronunciation test (~40 words) before generating audio: `__init__`, `**kwargs`, `elif`, `strptime`, `argparse`, `venv`, `pip`, `sys.argv`, `lambda`, `f-string`, `def`, `self`.
6. Render budget: about 19 min per episode on the PC, so about 29 h for 90; plan the PC and laptop split.

## Writing rules and illustrations

- Writing style: Simplified Technical English subset. Rules and commands: [STE.md](STE.md). Linter: `scripts/ste_lint.py`.
- Drawn explanations are structured data: [ILLUSTRATIONS.md](ILLUSTRATIONS.md). Files: `illustrations/epNNN.json`. Validator: `scripts/check_illustrations.py`.
- Run all three checks before every render: `check_py.py`, `ste_lint.py`, `check_illustrations.py`.
