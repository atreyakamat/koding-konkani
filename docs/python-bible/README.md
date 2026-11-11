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

- Writing style: Simplified Technical English subset. Rules and commands: [STE.md](STE.md). Linter: `scripts/ste_lint_py.py`.
- Drawn explanations are structured data: [ILLUSTRATIONS.md](ILLUSTRATIONS.md). Files: `illustrations/epNNN.json`. Validator: `scripts/check_illustrations.py`.
- Run all three checks before every render: `check_py.py docs/python-bible/m*.md`, `ste_lint_py.py docs/python-bible/m*.md`, `check_illustrations.py`.

## Build chain for the Remotion run

1. `python3 scripts/bible_to_json.py --lang python` writes `episodes-python/epNNN.json` (90 files, 0 warnings). Each file has scenes, narration cues, code files, bug, pun, challenge, 5 Shorts, and the `youtube` block (title, description, chapters, tags, thumbnail text and art).
1b. `python3 scripts/py_enrich.py` (run right after step 1, safe to repeat) adds the Python scene props: `course`, bug/terminal/memory data, recap and concept lines, illustration links. Without it Python episodes render with C defaults.
2. Illustration specs for drawn scenes are in `illustrations/epNNN.json` (see ILLUSTRATIONS.md).
3. `python3 scripts/publish_pack.py` writes copy-ready upload sheets to `publish/mNN.md`: title, description, tags, thumbnail text, and caption and hashtags for every Short.
4. After voice generation, recompute chapters from the final audio, then upload by hand. Nothing in this repo uploads or publishes.

## Rendering the Python course (Windows PowerShell)

Set `KK_COURSE=python` first (`$env:KK_COURSE = "python"`). It switches the episode folder to `episodes-python/`. Narration goes to `audio/voice/python-epNNN/`.

- Narration: `python scripts/render_episode_audio.py <ep>` writes `audio/voice/python-epNNN`.
- One long video: `npx remotion render src/index.ts LongVideo out/py-ep005.mp4 --props='{"episodeNumber":5,"lang":"python"}' --concurrency=4`
- One Short: `npx remotion render src/index.ts Short-S4 out/py-ep005-S4.mp4 --props='{"episodeNumber":5,"shortId":"S4","lang":"python"}'`
- Render one video at a time.
- Quick look without audio: `node scripts/stills_all.mts <from> <to>` (every scene) and `node scripts/shorts_stills_all.mts <from> <to>` (every Short). The Short stills need a narration folder. `python scripts/placeholder_audio.py <from> <to>` makes silent stand-ins (dev only; never use them for a real render).
- `python scripts/check_stills.py out/stills-python` flags text that runs into the caption band.
- Set `KK_BROWSER` to a Chrome path only if Remotion cannot download its own browser.

Checked in the build container: 990 scene stills and 450 Short stills with 0 errors, plus full renders of EP5 (3.5 min, 1920x1080 H.264+AAC) and its Short S4 (30 s, 1080x1920) using silent placeholder audio.
