# Run the Python course on your PC (guide for you and for Agy)

Goal: make the EP5 pilot render on Windows with the real narrator, then render the rest one video at a time. Nothing here uploads or publishes.

## Part A. Get the PC ready (once)

Run these in PowerShell from the repo folder. Each line says what "good" looks like.

1. `git fetch origin; git checkout claude/project-thread-d7o7tc; git pull` - branch is up to date.
2. `node -v` - Node LTS (20 or 22). Then `npm ci` finishes without errors.
3. `python --version` - 3.13 (the repo pins it). Then `python -m venv .venv; .venv\Scripts\Activate.ps1; pip install -r requirements.txt` (if there is no requirements file, install `piper-tts` and `faster-whisper`).
4. `ffmpeg -version` - works (loudness step needs it).
5. Narrator model exists: `.cache\piper-voices\en_US-ryan-high.onnx` (the voice in `config/voice.json`). If missing, download that Piper voice into that folder.
6. `$env:KK_COURSE = "python"` - set this in every new PowerShell window. It switches to `episodes-python/` and `audio/voice-py/`.
7. Checks, all must pass:
   - `python scripts/check_py.py docs/python-bible/m*.md` - 90 episodes, 0 problems
   - `python scripts/ste_lint_py.py docs/python-bible/m*.md` - 0 errors (warnings are fine)
   - `python scripts/check_illustrations.py` - 38 illustrations, 0 problems
   - `node scripts/validate_episodes.mts` - 90 files, 0 failures
   - `npx tsc --noEmit` and `npm run lint` - no output
8. Close other heavy apps. Keep 13 GB RAM free. Use `--concurrency=4`; drop to 3 if RAM goes over about 13 GB.

## Part B. Pilot (EP5), then the rest

1. Narration: `python scripts/render_episode_audio.py 5` - writes `audio/voice-py/ep005` (WAV per scene, captions, manifest).
2. Listen to 2 scenes. Check that "print", "input", "str" and "int" sound right. Note any wrong word.
3. Long video: `npx remotion render src/index.ts LongVideo out/py-ep005.mp4 --props='{"episodeNumber":5,"course":"python"}' --concurrency=4`
4. Short: `npx remotion render src/index.ts Short-S4 out/py-ep005-S4.mp4 --props='{"episodeNumber":5,"shortId":"S4","course":"python"}'`
5. Watch both files end to end. Pass if: voice matches captions, no text hits the caption bar, no black frames, sound is steady.
6. Pilot passed: tell Claude "open the PR" (draft). Then render the rest one video at a time, a module per night.

Use PowerShell quoting for `--props`: if it fails, put the JSON in a file `props.json` and pass `--props=props.json`.

## Part C. Prompt to paste to Agy

> You are working in the repo `koding-konkani` on branch `claude/project-thread-d7o7tc`. Do the steps in `docs/python-bible/AGY-RUN-GUIDE.md`, Part A then Part B, for episode 5 only.
> Rules: set `KK_COURSE=python` first. Run one command at a time and show me the output. Stop and ask me if any check fails; do not edit files to make a check pass. Never push to main, never delete files, never touch `.env`, credentials or API keys, never upload or publish anything. Render only one video at a time.
> At the end, give me: the result of each check, the two output file paths and sizes, and any word the narrator said wrongly.

## If something fails

| Symptom | Likely fix |
|---|---|
| Remotion cannot download the browser | Set `$env:KK_BROWSER` and add `--browser-executable=$env:KK_BROWSER` to the render command, pointing to Chrome. |
| `ModuleNotFoundError: piper` | Activate `.venv`, then `pip install piper-tts`. |
| Voice model not found | Check the path in `config/voice.json`. |
| Missing `audio/voice-py/ep005` | Run Part B step 1 again (the render needs the narration folder). |
| `--props` JSON error | Use `props.json` as above. |
| Out of memory | Lower `--concurrency` to 3 or 2. |

Placeholder (silent) audio from `scripts/placeholder_audio.py` is for developers only. Never render a real video with it.
