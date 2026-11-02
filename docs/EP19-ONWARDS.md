# EP 19 onwards: rules for any model (or person) making these episodes

Read `CLAUDE.md` and `docs/STYLE.md` first. This file adds what went wrong in EP 01–19 and what
to do about it. It is written so a small model can follow it step by step without guessing.
Rule of thumb: if a step says FIX, do not render until it is fixed.

## 0. Before you touch anything

1. Work on a branch. Open a draft PR. Never push to `main`.
2. Never touch `.env`, keys or accounts. Never delete files (move them to `out/old/`).
3. Run `python scripts/preflight_bible.py --from <first episode>`. Read `docs/ep19-preflight.md`.
   Every `FIX:` flag for your episodes must be repaired in the Bible or the episode JSON first.
4. Compile every C sample with GCC (`python scripts/check_c.py`). The expected output in the JSON
   must match what GCC prints, character for character.

## 1. Defect catalogue (what broke before, why, what to do)

| Symptom on screen | Cause | Rule |
| --- | --- | --- |
| `**word**` or backticks visible | Bible markdown copied into on-screen text | Strip `** ` `` ` `` `#` from every string that is drawn (bug why/fixed, challenge, onScreen, hooks). One shared sanitiser; never hand-edit per scene. |
| Empty explanation card before the first highlight | Card rendered before its text exists | Render the card only when its text is non-empty. |
| Butter highlight on a blank row | Panel scrolled to lines not typed yet | Highlight a row only after it has finished typing. Scroll by whole rows. |
| Last code row cut in half | Panel height not a multiple of row height | Panel height = rows x row height + padding. Never clip mid-row. |
| Code or terminal line cut off in a Short | Line wider than the panel | Wrap at the panel width. Never clip. Never shrink below the minimum font. |
| "OUTPUT ?" panel on a quiz Short | Short has no code | No code, no output panel. Show the question and options as a card. |
| Two Shorts of one episode look the same | Visual chosen by episode, not by Short | Each Short builds its visual from its own `onScreen` / `script` / `fromScenes`. `check_short_visuals.mts` must pass. |
| Short card repeats the hook word for word | Hook reused as card text | Card text must add something (code, output, answer), never the hook. |
| Terminal panel on top of Xecxec | No reserved zone for the mascot | Keep the mascot zone free. Move the panel, never the mascot. |
| Tiny GCC error in Bug of the Day | Font shrunk to fit | Minimum 22 px at 1080p. Wrap. Trim the error to the first two lines. |
| Pun card text off-centre or clipped | Checked mid-transition | Judge a still at the card's midpoint, not the first frames. |
| Render died with out-of-memory | Two jobs, or concurrency too high | One job at a time. 4K uses `--concurrency=2`. 720p drafts may use 6. |
| Fonts failed with a DNS error | Fonts loaded from the network at render time | Fonts are self-hosted in `audio/fonts/` and loaded with `staticFile()`. No network at render time. |
| Black frames | Missing `from` or bad scene length | Every scene has a start and a length that sum to the audio length. The narration audio length wins. |
| Audio too loud or clipping | Master skipped | Narration at -16 LUFS, true peak at or below -1.5 dBTP (target -1.7). Run `loudness.py`. |

## 2. Data each scene template needs (no data, no scene)

| Template | Needs | If missing |
| --- | --- | --- |
| Code explain | `code.source`, `[HL n]` cues with n <= number of lines, `[TRACK a=1]` cues | Fix the cue. Do not guess a line. |
| Terminal | Expected output block from a real GCC run | Run GCC, paste the real output. |
| Memory boxes | Real variable names, values and addresses from the episode code | Derive them from the code. Never reuse EP 07 sample data. |
| Algorithm bars | A `Step trace` table: step, array, compared pair, swapped pair, sorted indexes | Add the table, or change the scene to Memory boxes. EP 42, 43, 44, 72 and 77 need one of these now. |
| Bug of the Day | wrong code, GCC message (real), fixed code, one-sentence why | Run GCC with `-Wall`. Quote the real message. |
| Short | hook, script, onScreen, fromScenes, caption, 5 hashtags | 5 Shorts per episode: S1 to S5. |

## 3. Module notes (what is new, what to watch)

- **M3 Decisions (EP 20 to 25, mint + dark blue):** first `if`/`else`; flowchart concept slides. EP 25 has a 56-row program: split it into two code scenes, never one scrolling wall. Bug = stray `;` after `if`, `=` vs `==`.
- **M4 Loops (EP 26 to 33, butter + dark blue):** loop trackers change every iteration. Use `[TRACK i=..]` on every pass. Keep tables to 6 rows.
- **M5 Functions (EP 34 to 40, lilac + tomato):** Memory boxes show scope (local appears and vanishes). Draw each call as a new box group.
- **M6 Arrays (EP 41 to 46, peach + dark blue):** first bars-like scenes in EP 42 to 44: add Step trace tables. Index labels 0..n-1 under every box.
- **M7 Strings (EP 47 to 51, pastel blue + apricot):** show the `\0` terminator as its own box. Never drop it from diagrams.
- **M8 Pointers (EP 52 to 60, lilac + dark blue):** arrows draw on from pointer box to target address. Addresses are labels, keep them short and consistent in one episode (e.g. 0x1000, 0x1004).
- **M9 Structures (EP 61 to 64, cream + tomato)** and **M10 Dynamic memory (EP 65 to 68, mint + tomato):** heap and stack side by side; malloc/free shown as boxes appearing and disappearing.
- **M11 Files (EP 69 to 71, apricot + dark blue):** file contents shown as a second terminal-style panel. Output paths must be relative, never absolute.
- **M12 Algorithms (EP 72 to 83, dark blue + butter, bars mint/tomato/pastel blue):** bars driven only by the Step trace table. compare = butter, swap = tomato, sorted = mint. Counters (passes, compares, swaps) must equal the table totals. EP 72 and 77 are concept-heavy: add traces or switch template.
- **M13 Projects (EP 84 to 86, peach + lilac):** long code. Show the project in stages (file by file), one stage per scene.

## 4. Per-episode procedure (follow in order)

1. Preflight line for the episode is `ok`, or every FIX is repaired.
2. `check_c.py` passes for this episode.
3. Build the episode JSON (`npm run episodes:build`). Open its `qa.md` if one exists.
4. Generate narration, master loudness.
5. Render a 720p draft. Look at the contact sheet, check the table in section 1 line by line.
6. Only then render the 4K master and the Shorts at 1080x1920.
7. Record the result in the render log. Do not publish or upload anything; the owner uploads.

## 5. Rendering 4K by hand (no AI credits needed)

Run from the repo root in PowerShell, one job at a time.

```powershell
# 0. check the tree and the code samples
git status
python scripts/check_c.py

# 1. keep the old renders (resume logic skips existing files, so move them first)
New-Item -ItemType Directory -Force out\old4k | Out-Null
Move-Item out\ep001 out\old4k\ep001     # repeat for each episode you want re-rendered

# 2. render a range, supervised restart on crash, ignore the 05:30 time-box
powershell -File scripts/overnight.ps1 -StartEp 1 -EndEp 19 -NoTimebox

# 3. watch progress in another window
Get-Content out\render-queue.log -Wait -Tail 20
```

Before starting: close Chrome and other heavy apps (16 GB machine), plug in power, turn off sleep.
If it is killed for low memory, run the same `overnight.ps1` line again: finished files are skipped.
Open `out\morning-report.md` and the per-episode `qa.md` when it ends.

## 6. Definition of done for an episode

- Preflight `ok`, GCC outputs match, loudness inside limits, no black frames.
- Section 1 table checked on the contact sheet, nothing on it still true.
- Long video 3840x2160 at 30 fps, Shorts 1080x1920 at 30 fps, one file per Short.
- Metadata files written next to the renders. Nothing uploaded.
