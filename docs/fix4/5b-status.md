# Fix pass 5b, phase A: status

Branch `fix/5b-data` (worktree `../koding-konkani-wt-5b`), local commits only. Nothing was rendered; the main working tree was not touched.
Verified without Remotion: `tsc --noEmit` clean, `eslint src` clean, `scripts/validate_episodes.mts` (86 files, 0 failures), `scripts/check_scenes.mts 41 50` passes (it failed 14 scenes before),
`scripts/check_boxes.mts` (14 memory scenes OK, narrowest cell 120px), `scripts/check_short_visuals.mts 41…50` passes, `scripts/bug_windows.mts` still 0 misses.

## Files changed

| File | Change |
|---|---|
| `src/lib/memory.ts` (new) | zod schema and types for `memory` (frames, groups, cells, arrows); limits 13 cells per group, 3 groups per frame, 6 frames |
| `src/lib/memoryLayout.ts` (new) | pure layout: cell width (up to 220px) at which a frame fits the free band, group and cell positions, joiner positions, which frame is current |
| `src/scenes/MemoryCell.tsx` (new) | one cell: the existing box look, optional name on top, value, address, index below, marks (zero / stop / taken / hl), struck-through `lost` value |
| `src/scenes/MemoryFrames.tsx` (new) | frames of groups: label and badges (HTML strip at the top), name tags, byte ruler, joiners, cell-to-cell arrows that draw on; first frame staggers in, later frames only pop the cells that changed |
| `src/scenes/MemoryBoxes.tsx` | now a dispatcher: `memory` → `MemoryFrames`, else the old flat component (renamed `FlatBoxes`, unchanged) |
| `src/lib/episode.ts`, `src/compositions/sceneProps.ts` | `memory` on the scene schema; passed to the scene next to `boxes` |
| `src/lib/shortVisual.ts` | the Short "boxes" visual also reads `memory` (first group of the first frame, at most 6 cells) |
| `src/lib/bugCulprit.ts` | lint fix: a regex had a literal tab (`no-control-regex`); now `/^\s*#/` |
| `episodes/ep041,044,045,046,047,048,049,050.json` | `memory` data on the 14 scenes (format unchanged: 2-space, CRLF) |
| `scripts/apply_boxes.mts`, `scripts/check_boxes.mts` (new) | writes the 14 scenes after checking numbers against the scene text and gcc; preflight for `memory` |
| `scripts/check_scenes.mts` | a memory-boxes scene passes with `boxes` or `memory.frames` |
| `docs/fix4/boxes-draft-ep41-50.json`, `docs/fix4/5b-plan.md` | draft regenerated (same values); short plan added on top |

## What each of the 14 scenes shows (all numbers checked against the scene's narration or onScreen, and compiled with gcc)

EP41 s4 marks[5] = 78 92 65 88 71, index 0 highlighted, badge "size 5, last index 4". EP41 s7 a[5] = 1 2 0 0 0 (zeros grey), b[] size 3; `b = a;` with gcc's real error text; copy loop (gcc run: 1 2 0).
EP44 s4 a = 10, b = 20, `a = b;` (10 struck through, both 20), `b = a;`. EP44 s5 a, b, temp: three steps, ends a = 20, b = 10. EP45 s4 seats[3][4] grid, then the same 12 boxes in one line. EP45 s7 a + b = sum, all 7 (challenge text).
EP46 s4 marks with a byte ruler (4 bytes each, 20 bytes) and badges 20 / 4 / 5. EP46 s7 two name tags on one row, before and after `addBonus` (the bonus comes from running the sample). EP47 s3 `word[6]` G O A N S `\0`. EP47 s4 "Panjim" in 7 boxes, stop sign on `\0`.
EP48 s3 the 13-key buffer, then "Atreya" taken by `scanf` and " Kamat\n" left. EP49 s4 "Xecxec" 7 boxes, then strlen 6 / sizeof 7. EP49 s5 `strcpy` / `strcat` on first[20] and copy[20] (first 12 boxes shown). EP50 s3 word over rev with four arrows (i to len − 1 − i).

## Shorts that reference these scenes (checked)

Six Shorts switch from another visual to the boxes visual and show the right values: EP41 S2 (marks[0..4]), EP44 S1 (a = 10, b = 20), EP44 S2 (a, b, temp = ?), EP46 S2 (marks), EP47 S2 (word, `\0` last), EP50 S2 (word f e n i `\0`).
The others keep their visual because their source scene has more than 6 cells (EP45 grid, EP47 s4, EP48, EP49) or because a quiz takes precedence (EP41 S5, EP45 S5, EP46 S5, EP49 S5); none of their scripts states a number that differs from the data.

## Decisions

- Up to 13 cells per group (the plan said 12; EP48's buffer is 13 keys). The narrowest cell is 120px (EP48), so the value and index stay readable.
- Frames are spread evenly over the scene length; a frame change pops only the cells whose value or mark changed.
- The EP44 values (10, 20) come from the narration; EP44 s5 reuses them. EP41 s7's copy loop copies the first 3 boxes because b has 3.
- Cells need no name in arrays (index under the cell); scalars carry their variable name on top of the cell.
- EP49 s5 shows 12 of the 20 boxes of `first` and `copy` (the longest string "Crab Xecxec" plus `\0` is 12), and says so in the label of the first frame.

## Open issues

1. **No picture has been looked at yet.** The layout is checked by arithmetic only (fits the band, readable cell width). Things most likely to need a fix after the stills: the label strip against Xecxec at the top right, the byte ruler's position, the name-tag chips, arrow paths in EP50, the joiner height in EP45 s7.
2. Frame timing is even, not tied to the narration (the plan's "reveal cues from word timestamps" is not done); the Bible's extras (bus on EP47 s4, pouring glasses on EP44 s5, zero fade, smoke on the lost 10) are not animated.
3. EP45 s4: row and column indexes are written in each cell (`[1][2]`) instead of a row index on the left and a column index on top.
4. The 7 Shorts whose source scenes have 7–13 cells or a grid have no boxes visual (they keep a code, text or quiz visual).
5. The earlier merge (`438f7af`) carried a lint error in `bugCulprit.ts` (literal tab in a regex); it is fixed on this branch, so `feat/module-0` has it until this branch is merged.
6. Not part of phase A: EP77, EP81, the other 43 blank MemoryBoxes scenes (EP37–39, EP52–83), the EP73/EP79 traces without markers, the Bible's quick-sort count.
