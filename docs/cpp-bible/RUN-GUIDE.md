# C++ course: run guide (Windows 11, PowerShell)

For an agent-run version, see `AGENT-RUNBOOK.md`. Run `npm run system:check` first.

Follow the steps in order. Each step says what you should see. If a check fails, the video does not start rendering. Nothing renders into the repo: all output goes to `out/`.

Run every command in the repo folder: `cd C:\path\to\koding-konkani`.

## Step 0. One-time setup

```powershell
git fetch origin
git checkout <the branch of this PR>
npm install
.venv\Scripts\python.exe -m pip install -r scripts\requirements.txt
```

You need: Node LTS, Python 3.13 (the `.venv`), FFmpeg on PATH, GCC 16 (MSYS2), and the Piper voice files from the C course.

## Step 1. Build the episode files

```powershell
.venv\Scripts\python.exe scripts\check_cpp.py
npm run cpp:build
```

- `check_cpp.py` compiles every code sample with GCC 16 and compares the output. Expect no ERROR lines. Send me the output if GCC 16 prints different error text.
- `npm run cpp:build` makes `episodes-cpp\ep001.json` to `ep090.json` and runs the render-ready check. Expect: `90 episodes, 0 problems`.

## Step 2. Dry run with silent audio (no voice, about 1 hour for all 90)

```powershell
.venv\Scripts\python.exe scripts\render_episode_audio.py 1 --lang cpp --fake-voice
npm run cpp:smoke -- 1
```

For all episodes:

```powershell
foreach ($n in 1..90) { .venv\Scripts\python.exe scripts\render_episode_audio.py $n --lang cpp --fake-voice }
npm run cpp:smoke -- all
```

 This renders still frames of every scene and every Short, and tests that none is blank or black. Read `out\smoke\cpp\report.md`. Expect `0 problems`. Look at a few JPG files in `out\smoke\cpp\`.

## Step 3. Real narration for the pilot episode

```powershell
.venv\Scripts\python.exe scripts\render_episode_audio.py 1 --lang cpp
```

This replaces the silent audio. Listen to `audio\voice\cpp-ep001\scene2.wav`. Check how the narrator says `std::cout`, `vector` and `nullptr`. Tell me any word that sounds wrong.

## Step 4. Pilot render (EP1, then EP13 and EP31)

```powershell
npm run cpp:render -- 1
```

The queue renders the long video (4K), then the 5 Shorts, one at a time. It then checks size, frame rate, loudness and black frames. The summary at the end must show `PASS` on every row. Open `out\cpp-ep001\` and watch the video. Do the same for EP13 (loops) and EP31 (arrays and bars) before you start a batch.

The queue stops with a message if the audio is silent dry-run audio or if there is no narration yet. This is on purpose.

## Step 5. Batches (overnight)

Make the narration for a module, then render it:

```powershell
foreach ($n in 5..12) { .venv\Scripts\python.exe scripts\render_episode_audio.py $n --lang cpp }
npm run cpp:render -- 5 6 7 8 9 10 11 12
```

One module for each night. If RAM goes above 13 GB, the queue lowers the concurrency by itself. The log is `out\render-queue.log`.

## If something fails

| What you see | What to do |
| --- | --- |
| `check_render_ready` lists a problem | Send me the line. Do not render. |
| `smoke` reports a blank frame | Open the JPG named in the report. Send it to me. |
| Queue says `BLACK at 12.3s` | The video has a black stretch. Send me the episode number and the time. |
| Queue says `silent dry-run audio` | Run step 3 for that episode. |
| `g++` error text differs from the Bible | Send me the `check_cpp.py` output. |

## What is not checked here

- The real Piper narration for C++ words (step 3 is your listening check).
- GCC 16 on your PC (step 1).
- A full 4K render on your PC (step 4). I rendered EP1 end to end here at low resolution with silent audio: 204 s, no black or frozen frames. Stills of 9 episodes, all scene types, also passed.

Upload data (titles, descriptions, tags, thumbnails, Shorts captions) is in `docs/cpp-bible/metadata/`. You upload the videos yourself.
