# Fix pass 5b: MemoryBoxes for the 14 blank EP41–50 scenes

## Short plan (as built, phase A)
1. One new optional scene field, `memory` = `{ frames: [{ label?, badges?, arrange?, joiners?, groups: [{ name?, tags?, cols?, ruler?, cells: [{ value, name?, index?, address?, mark?, lost? }] }], arrows? }] }` (`src/lib/memory.ts`, zod). The flat `boxes` of EP7–18 is untouched.
2. `src/lib/memoryLayout.ts` (pure) picks the largest cell width (up to 220px) at which a frame fits the free band; `MemoryBoxes` renders `memory` through `MemoryFrames` + `MemoryCell` and keeps the old flat path as `FlatBoxes`.
3. Reused: `SceneFrame`, the box look, `enterProgress` pops, the pointer-arrow draw-on style, `Chip`, `readableOn`, the free-band position. New: index row, grids, stacked groups, frames, joiners, arrows between cells, byte ruler, name tags, marks.
4. `scripts/derive_boxes.mts` (gcc-run probes) → `scripts/apply_boxes.mts` writes the 14 scenes into `episodes/ep041..ep050.json` after checking every number against the scene's narration, `onScreen`, the challenge text and fresh gcc runs.
5. `scripts/check_boxes.mts` (schema, arrows, layout fits at ≥96px) and `scripts/check_scenes.mts` (accepts `memory.frames`) must pass; `tsc`, `eslint src` and `validate_episodes` clean. Shorts: the boxes visual reads the first group of the first frame when it has at most 6 cells.
6. Stills and the 4K render wait for PHASE B (after the EP1–19 job); the original, longer plan follows.

---

Status: **plan, nothing coded.** Branch `fix/5b-data`. Data drafts already exist: `docs/fix4/boxes-draft-ep41-50.json`
(made by `scripts/derive_boxes.mts`, every value from a C probe compiled with `gcc -Wall -Wextra` and run, cross-checked against the numbers each scene states).
Scope: exactly the 14 scenes below. EP77, EP81 and the other 43 blank MemoryBoxes scenes (EP37–39, EP52–83) wait until after EP41–50.

## a) The 14 scenes

"flat" is today's component: one row of up to about 6 name / value / address boxes. None of the 14 can use it alone, because they need an index under each box,
more than 6 boxes, a grid, several states over time, or arrows.

| Episode | Scene | What the narration shows | Layout it needs |
|---|---|---|---|
| EP41 | 4 | `int marks[5]`: five boxes side by side, index under each, values 78 92 65 88 71; "the first box is number zero"; badge "size 5, last index 4" | **cells** (5, indexed, index 0 highlighted) |
| EP41 | 7 | `a[5] = {1, 2}` fills 1 2 0 0 0 (zeros grey); `b[] = {4, 5, 6}` gets size 3; then `b = a;` is an error and a copy loop | **cells**, two groups stacked, zero marks, then **steps** (error frame, copy frame) |
| EP44 | 4 | `a = 10, b = 20`; `a = b;` makes both 20; `b = a;` both 20; the 10 is gone | **steps** (3 frames of 2 scalar boxes, one "lost" mark) |
| EP44 | 5 | Three glasses a, b, temp: `temp = a; a = b; b = temp;` ends with a = 20, b = 10 | **steps** (4 frames of 3 scalar boxes) |
| EP45 | 4 | `seats[3][4]` as a grid with row and column indexes, then the same 12 boxes laid out in one line in memory (row 0, row 1, row 2) | **grid**, then **steps** (grid frame, unrolled-row frame) |
| EP45 | 7 | Matrix A + matrix B = Sum, cell by cell (a = 1 2 3 / 4 5 6, b = 6 5 4 / 3 2 1, sum all 7) | **matrix** (three grids side by side) |
| EP46 | 4 | `sizeof(marks)` = 20 bytes, `sizeof(marks[0])` = 4, 20 / 4 = 5 | **cells** with a byte bracket and three badges |
| EP46 | 7 | main's `marks` and the function's `arr` are two name tags on the same row; changing a locker through `arr` shows in `marks` | **alias** (one group with two name tags and an arrow), two frames (before, after `addBonus`) |
| EP47 | 3 | `char word[6]` filled with G O A N S and `\0`, one letter per box | **cells** (6, the last marked `\0`) |
| EP47 | 4 | "Panjim" in 7 boxes; the last box `\0` is the stop sign | **cells** (7, stop mark on `\0`) |
| EP48 | 3 | Keyboard buffer `A t r e y a ␠ K a m a t \n`; `scanf("%s")` takes "Atreya" and leaves " Kamat\n" | **cells** with taken / left marks, two frames (typed, after scanf) |
| EP49 | 4 | "Xecxec" in 7 boxes; `strlen` counts 6 and skips `\0`; `sizeof` is 7 | **cells** (7) with a counter badge that ticks 1…6 (frames) |
| EP49 | 5 | `strcpy` copies Xecxec into `copy[20]`; `strcat` moves the `\0` and appends | **steps** (copy, first "Crab " then "Crab Xecxec"; `\0` position per frame) |
| EP50 | 3 | "feni" over `rev`: arrows pair index i with len − 1 − i | **cells**, two groups, **arrows** between them |

Primary layout of the 14 scenes: cells 8 (EP41 s4, EP41 s7, EP46 s4, EP47 s3, EP47 s4, EP48 s3, EP49 s4, EP50 s3), steps 3 (EP44 s4, EP44 s5, EP49 s5), grid 1 (EP45 s4), matrix 1 (EP45 s7), alias 1 (EP46 s7).
Several of the cells scenes also change over time (EP41 s7, EP48 s3), and the grid scene unrolls. All of them are one idea: a list of **frames**, each frame a few **groups** of **cells**, with optional arrows.

## b) Smallest change

### Schema (`episodes/*.json`, and `SceneSchema` in `src/lib/episode.ts`)

One new optional field on a scene, `memory`. The existing `boxes` stays valid and unchanged (EP7, 8, 9, 12, 15, 17, 18 keep working); a scene has `boxes` or `memory`, not both.

```jsonc
"memory": {
  "frames": [
    {
      "label": "a = b;",                       // optional caption under the row
      "badge": "size 5, last index 4",         // optional stamp
      "groups": [
        {
          "name": "marks",                      // optional, drawn left of / above the group
          "tags": ["marks", "arr"],             // optional, extra name tags (EP46 s7)
          "cols": 4,                            // optional: wrap into a grid (EP45); default: one row
          "ruler": true,                        // optional: byte bracket under the cells (EP46 s4)
          "cells": [
            { "value": "78", "index": 0, "address": "0x7ffd1a2c3f00", "mark": "hl" }
            // mark: "zero" | "stop" | "taken" | "lost" | "hl"
          ]
        }
      ],
      "arrows": [ { "from": "0:3", "to": "1:0" } ]   // "group:cell", drawn on (EP50)
    }
  ]
}
```

- A frame is shown from its reveal cue (the existing `revealFrame` / `defaultRevealCues` spreading over the scene) until the next one.
- Cell values are strings, addresses illustrative as today (`0x7ffd1a2c3f00 + offset`).
- A zod schema for the above; the size limits (at most 13 cells per group (EP48's 13-key buffer), at most 3 groups per frame) are enforced by the preflight check below.
- `scripts/derive_boxes.mts` already produces the data; a small converter (`scripts/apply_boxes.mts`) maps the draft layouts onto `memory.frames` and writes the 14 scenes, in the repo's 2-space CRLF JSON format.
- Preflight and Shorts: `check_scenes.mts` accepts a scene with `memory.frames.length > 0`; `shortVisual.ts` builds its `boxes` visual from the first frame's first group when it has at most 6 cells (else it keeps its current fallback).

### Component (`src/scenes/MemoryBoxes.tsx` + one pure helper `src/lib/memoryLayout.ts`)

Reused unchanged: `SceneFrame`, the box look (cream fill, 5px ink border, 8px hard shadow, `palette`), name / value / address text styles and the readable-text contrast helper,
`enterProgress`, `defaultRevealCues` / `revealFrame`, the vertical band centre (`BAND_CENTER_Y`) that keeps clear of the top-right Xecxec and the caption band, and the pointer-arrow draw-on used for `pointsTo` (generalised from box-to-box to cell-to-cell).

New:
1. `memoryLayout.ts` (pure, no React, runs under Node): cell size from the cell count and column count (5 → 260px, 7 → about 200, 12 in a 4-column grid, three 2×3 grids side by side), row positions for stacked groups, the index row under the cells, the arrow endpoints, and which frame is current at a frame number.
2. In the component: when `memory` is present, render the current frame's groups with that layout; the cell is today's box with the name line replaced by the index and the address smaller;
   `mark` styles: `zero` grey fill, `stop` tomato border plus a "stop" tag, `taken` mint, `lost` ghosted with a strike, `hl` butter; a byte bracket for `ruler`; name tags as small chips; the frame badge reuses `Chip`/`Sticker`.
3. Frame change: values pop with the existing `springs.pop`; no other motion (the bus, the pour animation and the zero-fade from the Bible are out of scope).

Not changed: `boxes` rendering, the other scenes, `CodeExplain`, `BugOfTheDay`.

## c) Test plan (nothing renders until the EP1–19 job has finished)

**Preflight / checks (Node only, can run any time):**
- `scripts/check_scenes.mts`: a memory-boxes scene passes with `boxes` **or** `memory.frames`; after the data lands `check_scenes 41 50` must pass (it fails 14 scenes today).
- `scripts/check_boxes.mts` (new): zod-validates `memory`; at most 13 cells per group (EP48's 13-key buffer), at most 3 groups per frame; every cell value is a short string; every arrow references an existing group and cell; the layout helper says every frame of every scene fits inside the 1728px-wide free band without overlap.
- `scripts/derive_boxes.mts` is re-run and its output is diffed against what is stored in the episode JSON (recompiles every C probe with gcc, so a changed value cannot slip in).

**540p stills after the EP1–19 job ends** (`remotion still` with the real props through `scenePropsFor`, one still per frame at about 60% of the frame's time, about 26 stills, plus one contact sheet of all of them for your review):

| Scene | Stills |
|---|---|
| EP41 s4 | 1 (five boxes, index 0 highlighted, badge) |
| EP41 s7 | 3 (two arrays; `b = a;` error; copy loop) |
| EP44 s4 | 3 |
| EP44 s5 | 4 |
| EP45 s4 | 2 (grid, unrolled row) |
| EP45 s7 | 1 |
| EP46 s4 | 1 |
| EP46 s7 | 2 |
| EP47 s3, EP47 s4 | 1 each |
| EP48 s3 | 2 |
| EP49 s4 | 1 (counter at 6) |
| EP49 s5 | 3 |
| EP50 s3 | 1 |

Also one regression still of EP7 s3 (the existing flat boxes) and one of EP18 s6 (5 boxes) to show `boxes` is unchanged, and a Short still for EP41 S2 to show the boxes visual still works.
After you OK the stills: `check_scenes 41 50` must pass, then EP41–50 are re-rendered (the 10 episodes, about 3 hours at concurrency 2).

## d) Time estimate (my working time, not render time)

| Step | Estimate |
|---|---|
| Schema + zod + `check_scenes` / `check_boxes` | 1.5 h |
| `memoryLayout.ts` (pure) + its Node check | 2 h |
| `MemoryBoxes.tsx` (cells, grid, marks, frames, arrows, tags, ruler) | 4 h |
| `apply_boxes.mts` converter + writing the 14 scenes | 1.5 h |
| Shorts boxes visual tweak | 0.5 h |
| Stills (about 26 + regressions), looking, fixing | 2.5 h |
| **Total** | **about 12 hours**, in two sittings; the stills can only start after the EP1–19 job ends |
