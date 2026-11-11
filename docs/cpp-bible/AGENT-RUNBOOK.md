# C++ course: agent runbook

For Agy (or any coding agent) running on the owner's Windows 11 PC. The human guide is `RUN-GUIDE.md`. This file is the same job, written so an agent can follow it without questions.

## How to use this

**Option A: you tell Agy to do it.** Open the repo folder in Agy and paste this prompt:

> Read `docs/cpp-bible/AGENT-RUNBOOK.md` and follow it from Phase 0. Stop at every STOP line and tell me what you found. Do not skip a phase. Do not change any file outside `out/`, `audio/voice/`, and `episodes-cpp/` unless the runbook says so.

**Option B: you run it yourself.** Run `npm run system:check`. When it says `SYSTEM READY`, follow `RUN-GUIDE.md`.

## Rules (never break these)

1. Work in the repo folder. Output goes to `out/` only. Never render into the repo.
2. Never push to `main`. Never upload videos. Never touch `.env` files or credentials. Never delete files or folders. Never install paid tools.
3. Render one video at a time. Never start a second render while one runs.
4. Never speed up the narrator.
5. If a command fails, do not retry it more than once. Report the full error text and STOP.
6. Do not edit episode JSON or the Bible by hand. If a check says an episode is wrong, report the episode number and the message, then STOP.

## Phase 0. Get the code

```powershell
git fetch origin
git checkout claude/project-thread-5r64sb
git pull origin claude/project-thread-5r64sb
npm install
```

If PR #21 is already merged, use `main` instead.

## Phase 1. System ready

```powershell
npm run system:check
```

- Expect `SYSTEM READY`. Each `FAIL` line has a fix line. Do the fix, run the check again.
- The venv fix needs Python 3.13: `py -3.13 -m venv .venv`, then `.venv\Scripts\python.exe -m pip install -r scripts\requirements.txt`.
- STOP if a fix needs a download you cannot do (for example the Piper voice files). Tell the owner which file is missing.

## Phase 2. Build and check the episodes

```powershell
.venv\Scripts\python.exe scripts\check_cpp.py
npm run cpp:build
```

- `check_cpp.py` compiles every code sample with the local GCC. Expect no ERROR.
- `cpp:build` must end with `90 episodes, 0 problems`.
- If GCC error text differs from the Bible, report the difference. STOP. Do not edit the Bible.

## Phase 3. Dry run (silent audio, finds blank scenes)

```powershell
foreach ($n in 1..90) { .venv\Scripts\python.exe scripts\render_episode_audio.py $n --lang cpp --fake-voice }
npm run cpp:smoke -- all
```

- Takes about 1 to 6 hours. It can run overnight.
- Pass = last line says `0 problems`. The report is `out\smoke\cpp\report.md`.
- On any blank frame: report the JPG name from the report. STOP.

## Phase 4. Pilot (real voice, EP1 only)

```powershell
.venv\Scripts\python.exe scripts\render_episode_audio.py 1 --lang cpp
npm run cpp:render -- 1
```

- The queue prints a summary. Every row must say `PASS`.
- Report the result and the files in `out\cpp-ep001\`.
- **STOP. Tell the owner to watch EP1 and listen to the narrator.** Do not go on until the owner says the pilot is good.

## Phase 5. Pilot 2 (EP13 and EP31)

Same two commands for each episode. STOP and report after both pass.

## Phase 6. Batches (only after the owner approves the pilots)

One module for each run. Example for M1 (EP5 to 12):

```powershell
foreach ($n in 5..12) { .venv\Scripts\python.exe scripts\render_episode_audio.py $n --lang cpp }
npm run cpp:render -- 5 6 7 8 9 10 11 12
```

Module map: M0 1-4, M1 5-12, M2 13-20, M3 21-30, M4 31-40, M5 41-50, M6 51-60, M7 61-68, M8 69-76, M9 77-84, M10 85-90.

After each module, report the summary table from the queue and `out\render-queue.log`. STOP before the next module unless the owner said to run all modules.

## Failure table

| Message | Meaning | Action |
| --- | --- | --- |
| `silent dry-run audio` | The episode only has fake audio | Run `render_episode_audio.py N --lang cpp` (no `--fake-voice`) |
| `no narration yet` | Audio step not done | Same command |
| `BLACK at 12.3s` | Black stretch in the video | Report episode and time. STOP |
| Any `FAIL` row in the queue summary | QA failed | Report the row and the log lines. STOP |
| `check_render_ready` problem | Episode data wrong | Report the line. STOP |
| Out of memory | RAM too high | The queue lowers concurrency by itself. If it still fails, report. STOP |

## Report format

At every STOP, write: which phase, which command, pass or fail, the last 20 lines of output, and the files created.
