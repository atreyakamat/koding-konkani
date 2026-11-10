# 540p draft review pass — report

Last updated 2026-11-04T05:21:48.826Z. Drafts in out/draft540/epNNN/ (long: 960x540, Shorts: 540x960; crf 20, veryfast, 192k AAC, audio mastered to -16 LUFS / -1.7 dBTP target). Contact sheets next to each file (*.sheet.png).

| Episode | Long (time, size) | Black frames | Long loudness | Shorts (time each) | Shorts loudness | Anything odd |
| --- | --- | --- | --- | --- | --- | --- |
| ep041 | 4m16s, 26.8 MB | none | -16.0 LUFS / -1.69 dBTP ok | 19s / 25s / 20s / 10s / 20s | all ok | — |
| ep042 | 4m39s, 23.7 MB | none | -16.0 LUFS / -1.67 dBTP ok | 26s / 27s / 33s / 15s / 31s | all ok | — |
| ep043 | 4m35s, 26.1 MB | none | -16.0 LUFS / -1.68 dBTP ok | 19s / 20s / 19s / 12s / 19s | all ok | — |
| ep044 | 4m00s, 26.0 MB | none | -16.0 LUFS / -1.69 dBTP ok | 17s / 21s / 19s / 11s / 18s | all ok | — |
| ep045 | 3m17s, 21.0 MB | none | -16.0 LUFS / -1.71 dBTP ok | 18s / 19s / 19s / 10s / 18s | all ok | — |
| ep046 | 3m42s, 23.8 MB | none | -16.0 LUFS / -1.66 dBTP ok | 16s / 21s / 23s / 11s / 20s | all ok | — |
| ep047 | 3m36s, 23.2 MB | none | -16.0 LUFS / -1.67 dBTP ok | 17s / 19s / 21s / 22s / 20s | all ok | — |
| ep048 | 3m46s, 24.8 MB | none | -16.0 LUFS / -1.71 dBTP ok | 18s / 21s / 18s / 12s / 21s | all ok | — |
| ep049 | 4m01s, 26.6 MB | none | -16.0 LUFS / -1.68 dBTP ok | 20s / 20s / 23s / 12s / 16s | all ok | — |
| ep050 | 3m50s, 25.0 MB | none | -16.0 LUFS / -1.64 dBTP ok | 18s / 18s / 21s / 10s / 16s | all ok | — |

10 episode(s) in this report; 55m18s of render time in total.

## Narration and draft time per episode

| Episode | Narration | Draft job (long + 5 Shorts, incl. mastering and aids) | Contact sheet (long) |
| --- | --- | --- | --- |
| ep041 | 2m42s | 6m05s | out/draft540/ep041/ep041-540p.sheet.png |
| ep042 | 2m11s | 7m11s | out/draft540/ep042/ep042-540p.sheet.png |
| ep043 | 2m19s | 6m18s | out/draft540/ep043/ep043-540p.sheet.png |
| ep044 | 2m31s | 5m40s | out/draft540/ep044/ep044-540p.sheet.png |
| ep045 | 2m02s | 4m52s | out/draft540/ep045/ep045-540p.sheet.png |
| ep046 | 1m57s | 5m24s | out/draft540/ep046/ep046-540p.sheet.png |
| ep047 | 1m57s | 5m27s | out/draft540/ep047/ep047-540p.sheet.png |
| ep048 | 2m32s | 5m29s | out/draft540/ep048/ep048-540p.sheet.png |
| ep049 | 2m28s | 5m44s | out/draft540/ep049/ep049-540p.sheet.png |
| ep050 | 2m31s | 5m26s | out/draft540/ep050/ep050-540p.sheet.png |

## Notes

- **EP41:** check_c.py flags `copy.c` as a compile error. That file is a deliberate compile-error teaching example, so this is a checker limit; the episode was rendered anyway.
- **EP48:** check_c.py flags an output mismatch because the sample needs typed stdin (the checker supplies none). Checker limit; rendered anyway.
- **EP42, EP43, EP44:** the algorithm-bars scenes now carry `scene.trace` (commit 8e92482). EP43's search tables have no compare pair, so there is no current-box highlight (flagged, not fixed); binary search shows the unchanged array for its 2 steps.
- No failed files, no black frames, all loudness within spec. Drafts were checked by the automatic aids only (contact sheets not reviewed by hand).
- Narration was generated for all ten episodes; drafts ran one job at a time.
