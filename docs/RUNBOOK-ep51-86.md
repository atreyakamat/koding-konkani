# Run-book: render C course EP51–86 (PC = EP51–65, laptop = EP66–86)

Branch: `feat/ep51-86-render-data` (based on `feat/module-0` @ b1bf10c). Never push to main. Never upload videos.

## What was blocking, and what this branch fixes

| Blocker (found 2026-11-08) | Fix in this branch |
| --- | --- |
| 40 memory-boxes scenes in EP52–83 had no data, so `check_scenes.mts` would skip those episodes | `docs/fix4/boxes-draft-ep52-83.json` (made by `gen_boxes_52_83.py`) applied by `scripts/apply_boxes_52_83.py` |
| EP77 s4 (Hanoi) and EP81 s4 (showdown) bars scenes had no `trace` | same script adds them |
| EP81 had `[MEASURED]` placeholders in narration, code output, bug text and challenge answer (the narrator would say "measured") | same script writes the real times of one run of `showdown.c` and of the buggy variant |
| `episode_pipeline.mts` skips any episode whose GCC check has a non-PASS row | 13 owner-reviewable entries added to `KNOWN_CHECKER_LIMITS` (programs that print addresses or need typed input or earlier files); each was hand-run and matched |

Episodes already clean (no data gaps): EP51, 63, 70, 72–76, 78–80, 82, 84–86.
All data changes are in `episodes/` and nothing else: narration wording is unchanged except EP81.

## Checks already passed (sandbox, GCC 13.3, Node 22)

- `node scripts/check_scenes.mts 51 86`: every memory-boxes and algorithm-bars scene has data.
- `node scripts/check_boxes.mts 51 86`: 40 memory scenes OK (schema, arrows, layout, narrowest cell 126 px).
- Stills of every new scene were rendered and viewed (contact sheets in the PR).
- C samples: EP51–86 all compile. Hand-run with real input/files and matched: EP51, 66, 70, 71, 84, 85. Address/timing programs (EP52, 53, 56, 57, 65, 81) are non-deterministic by nature. EP73 `wrong.c` hangs on purpose.
- EP61, 62, 63 `wrong.c` show BUG-MESSAGE-DIFFERS only on the sandbox locale (curly vs straight quotes); on Windows they should PASS. If one does not, show the diff to the owner before changing text.

## Checker limits (why the pipeline would otherwise skip them)

| EP | File | Why non-PASS | Verified by hand |
| --- | --- | --- | --- |
| 51 | file1.c | typed line | yes, output equals Bible |
| 52, 53, 56, 57, 65 | file1.c | `%p` addresses | n/a (non-deterministic) |
| 66 | file1.c | typed input | yes |
| 70 | file1.c, file2.c | need diary.txt, marks.txt | yes |
| 71 | file2.c, file3.c | need students.dat from file1.c | yes |
| 73 | wrong.c | intentional infinite loop | yes (traced by hand) |
| 81 | file1.c | milliseconds | n/a |
| 84 | students.c, wrong.c, fixed.c | menu needs stdin | yes (table matches) |
| 85 | atm.c | menu needs stdin | yes (deposit/decline/withdraw logic) |

## Part A — PC (EP51–65), Windows 11

1. `git status -sb`. If anything outside `out/` is modified, stop and tell the owner.
2. `git fetch origin` then `git switch feat/ep51-86-render-data`.
3. Checks (use `.venv\Scripts\python.exe` for Python):
   - `node scripts/check_scenes.mts 51 86` → must say every scene has data.
   - `node scripts/check_boxes.mts 51 86` → must say 40 memory scene(s) OK.
   - `node scripts/validate_episodes.mts` → no failures.
4. Stills (optional second look, about 15 minutes): `node scripts/stills_new_scenes.mts 52 65` → `out/stills-ep52-83/`. Look at them. Fix only memory data by editing `docs/fix4/gen_boxes_52_83.py`, regenerate the JSON, run `python scripts/apply_boxes_52_83.py` again (safe to repeat). If a problem needs a component change, stop and report.
5. GCC gate: `.venv\Scripts\python.exe scripts/check_c.py --episode N` for N = 51…65. Rows beyond the table above are real problems: report them, do not hide them.
6. Render: `powershell -File scripts\overnight.ps1 -StartEp 51 -EndEp 65` (add `-NoTimebox` if you are awake and want it to run through the 05:30 cut-off). It does GCC check, narration, 4K long video and Shorts S1–S5, then QA, one episode at a time, resumable.
7. When it finishes: write `out/ep51-65-report.md` (per episode PASS/WARN/FAIL, black frames, LUFS, true peak, time). Do not delete anything.
8. Commit the data on the branch, push the branch, open a draft PR. Never main.

Estimate: about 18–20 minutes per episode, so 5–6 hours.

## Part B — laptop (EP66–86), Linux

1. `git status -sb` clean, then `git fetch origin` and `git switch feat/ep51-86-render-data` (if the Linux audio-encoder fix lives on another branch, merge that branch locally as in Pass-5c; do not push it).
2. Same checks as Part A step 3, with `LC_ALL=C` set so GCC prints straight quotes.
3. Stills for your range: `node scripts/stills_new_scenes.mts 66 83`.
4. GCC gate with `LC_ALL=C python scripts/check_c.py --gcc "$(command -v gcc)" --episode N` for N = 66…86.
5. Render exactly like Pass-5c (tmux session under `systemd-inhibit --what=sleep:idle:handle-lid-switch`, one video at a time, concurrency 2), but full renders (long 4K + S1–S5) for EP66–86. These episodes have no earlier renders and may have no narration yet: generate it with `python scripts/render_episode_audio.py N` first if `audio/voice/epNNN/` is missing.
6. Same verdict rule as Pass-5c (FAIL = LUFS outside −16 ± 0.5, true peak above −1.0 dBTP, or any black frame). Write `out/ep66-86-report.md`.
7. Move nothing, delete nothing. Send the report and contact sheets to the owner (Taildrop → `out\from-laptop\`).

Estimate: about 17–20 minutes per episode, so 6–7 hours.

## If something fails

- Two failures in a row stop the pipeline on purpose (exit code 2). Read `out/episode-skips.log`, fix the cause, run the same command again; finished steps are skipped.
- EP81 reads its own measured times aloud. Do not regenerate them from your machine; they are fixed in the JSON.
