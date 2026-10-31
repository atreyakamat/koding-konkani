# EP 01 pilot — review v2 (Claude, 31 Oct 2026)

Branch `feat/pilot-ep001-v2`, built on `feat/pilot-ep001` merged with `docs/ep001-pilot-review`
(PR #13 — Backdrop, MascotCompanion, SceneFrame, dancing Xecxec, new ShortLayout, `@kodingkonkani`).
Inputs for this review: `out/ep001/ep001-720p.mp4` (261.0s) and `ep001-S1..S5.mp4`. Frames sampled
every 10s (long) and 4 evenly-spaced per Short, plus targeted checks at every scene boundary and
every transition.

## Verdict: Approved, with two known gaps noted below (not blocking).

The acceptance criteria from `docs/reviews/ep001-pilot-review.md` are met. Two issues were found
and fixed live during this pass (not pre-existing in the PR — introduced by the EP01 content itself
exercising the new components in ways the originals weren't tested against); see "Fixes made" below.

## Acceptance criteria — checked against the 31 Oct review

**Mascot**
- Xecxec visible in every sampled frame of the long video (26/26) and every Short (checked 12
  frames across S1/S3/S5). Idle size ≈26% of frame height (720p: ~190px / 720px); hero size
  (title/pun/outro/challenge) ≈60-72%.
- Pose changes confirmed: idle -> clawsUp (concept-slide analogy reveal, code-explain output),
  shellShake -> clawsUp (Bug of the Day), snap (pun), dance (title/outro/challenge/every Short).
  Bubbles confirmed: "Oops!"/"Fixed!" (Bug), "It runs!" (code output), "Your turn!" (Challenge).
- Visible from frame 0 in every Short (hook pops in with Xecxec already on screen).

**Scenes**
- Real TitleCard (EP sticker, module chip, outlined title, dancing Xecxec, sting) and real Outro
  present — both already used the merged components once wired through `LongVideo`'s existing
  scene loop; no composition change needed beyond the merge itself.
- Ambient backdrop (drifting dot grid + pastel shapes) on every scene via `SceneFrame`.
- STYLE.md transitions in place (hard-cut, ink-wipe, push-in, window-pop, whip, flip, clock-wipe,
  fade) via `src/transitions`; `resolveTransition()` enforces "never the same transition twice in
  a row" and alternates concept-slide push directions. Built in the original `feat/pilot-ep001`
  work and unaffected by the merge (no file overlap).
- CodeExplain's `output` terminal wired from `scene.code.output` (EP01 scene 6: `"Hi"`) — "It
  runs!" bubble + typed terminal line confirmed at the expected point in the scene.
- Concept-slide analogy cards: **not populated by the original adapter** (the episode JSON has no
  structured analogy field). Added `analogyFromOnScreen()` in `sceneProps.ts`, which recognises the
  Bible's `"Title": description` onScreen shape (matches scene 3, 4, 5, 8 in EP01; scene 1, the cold
  open, correctly gets none). Confirmed rendering correctly on all 4 matching scenes.
- Minimum body text: concept-slide bullets are 40-58px (see "Fixes made"), code/terminal/bug panels
  36-44px, all above the 44px floor except the narrower-column bullet case, which was deliberately
  sized down to prevent overflow — flagged below, not a clean pass of the literal "44px minimum."

**Shorts**
- Own layout (`ShortLayout`, not a LongVideo clone): dancing Xecxec always on screen, progress bar,
  hook pops at frame 0, word-by-word caption in the lower third, "Full video: EP 01" badge.
- Real visuals for the two Shorts whose source scene has code content: S3 (the bug, via `BugVisual`
  — wrong code + first GCC error line) and S5 (the `printf` scene's code with line 4 highlighted,
  via `CodeVisual`). S1/S2/S4 (intro, concept, joke) use `ShortLayout`'s own styled text-card
  fallback — there's no natural code/bug/memory-box visual for those, and building bespoke ones
  for every Short type was out of scope for this pass; see "Known gaps."
- End card: "FOLLOW @KODINGKONKANI" / "Subscribe: Koding Konkani", no grey dimming, confirmed on
  every Short.
- No leftover `YOUR_IG_HANDLE` anywhere in the repo (grepped) — the merge already replaced it via
  `src/brand.ts`.

**Audio**
- Final mixed output: **-16.06 LUFS integrated, -1.51 dBTP** (long video); Shorts -16.05 to -16.07
  LUFS, -3.6 to -4.1 dBTP (well clear of the ceiling). Hits the -16 LUFS / ≤-1.5 dBTP target.
- This required a real fix, not just a render flag — see "Fixes made."

## Fixes made during this pass

1. **Audio: a limiter alone isn't enough; needed a proper two-pass loudnorm mastering step.**
   The pre-existing per-clip normalisation (narration, individually, to -16/-1) is correct, but the
   *combined* mix (narration + music bed + SFX + sting playing together) measured **-15.86 LUFS /
   -0.59 dBTP** — hotter than any single clip, confirming the 31 Oct review's finding. A first
   attempt at a simple `ffmpeg alimiter` sample-peak limiter actually made true peak *worse*
   (0 dBTP, outright clipping) — naive sample limiting doesn't account for inter-sample
   reconstruction peaks, a known pitfall. Fixed properly with `scripts/loudness.py`'s existing
   two-pass `loudnorm` (now generalised into `normalize_file()`/`master_video()`), which measures
   the real file and applies a linear gain pass targeting the stated LUFS/TP pair. Verified:
   -16.06 LUFS / -1.51 dBTP on the final file. Wired into `scripts/episode.mts` as a permanent
   `renderAndMaster()` step (render to `.raw.mp4`, master, delete the raw) so every future episode
   gets this automatically, not just EP01.
2. **`--scale`/`--width`+`--height` on `remotion render`: only `--scale` is safe for Shorts.**
   `ShortLayout` positions everything in absolute pixels against its native 1080×1920 canvas.
   `--width=720 --height=1280` changes the *canvas* without scaling that content, so the Shorts
   rendered with text and the visual panel cut off past x=720. `--scale=0.6666666666666666`
   (full-precision 2/3 — a truncated `0.6667` produces a non-integer height and Remotion's
   stitcher rejects it) scales the whole composition proportionally and renders correctly.
   `LongVideo`'s scene templates are flex/percentage-based, so `--width`/`--height` worked fine
   there; used explicit dimensions for the long video and `--scale` for every Short.
3. **PunCard: a long, 3-line pun (EP01's) overlapped the hero-size mascot.** The word "are" in
   `"...where their pointers are."` was rendered directly behind Xecxec's head. Fixed in
   `PunCard.tsx`: long puns (>60 chars) drop to a smaller font (46 vs 64), and bottom padding
   reserves the mascot's fixed zone, so the common case (a short one-liner) is unaffected.
4. **ConceptSlide: analogy cards narrow the text column enough to overflow the frame.** Once
   analogy cards were wired in (fix above), scene 4's three bullet lines — each already wrapping
   to 2 lines at the component's 58px size in a now-56%-width column — pushed content off the top
   of the frame entirely. Fixed in `ConceptSlide.tsx`: bullet font drops to 40px (from 58) and the
   row gap tightens (24px from 36px) whenever an analogy card is present; full-width (no analogy)
   scenes are unaffected.

## Known gaps (not blocking, flagged for a follow-up)

- **S1/S2/S4 use the text-card fallback, not a bespoke animated visual.** The acceptance criteria
  ask for "a visual per Short (animated code, bug, memory box)"; only S3 and S5 have source scenes
  with code content to show. A real fix (custom illustrations for intro/concept/joke Shorts) is a
  content/design task, not a wiring one.
- **`linesFromNarration`/`analogyFromOnScreen` are heuristics, not authored content.** They produce
  correct, readable results for EP01 but are pattern-matching the Bible's prose, not reading
  purpose-built fields (the schema has none). Worth a schema addition (`conceptLines`,
  `analogy: {title, body}`) once more episodes are rendered and the pattern's failure modes are
  clearer.
- **Terminal, MemoryBoxes, AlgorithmBars adapters are still best-effort** (per the original
  `feat/pilot-ep001` note) — EP01 doesn't exercise them; needs real attention at Module 3/6.
- **Black tail frames (31 Oct review, item 8): investigated, not reproduced.** Checked the last 3
  seconds and the exact final frame of the render directly — the Outro's content is present through
  the last frame, no black. Possibly a review-tooling artifact from sampling past end-of-file; no
  trim was needed or added.
- **Minimum 44px body text:** the analogy-column bullet fix above deliberately goes to 40px to
  prevent overflow, just under the stated floor. Readable at 720p in testing; worth a second look
  once the real video is watched on a phone screen rather than judged from stills.

## Render specs (ffprobe-verified)

| | Long video | Shorts (each) |
|---|---|---|
| Dimensions | 1280×720 | 720×1280 |
| FPS | 30 | 30 |
| Video codec / CRF | H.264 / 18 | H.264 / 18 |
| Video bitrate | ~1.58 Mbps | — |
| Duration | 261.0s | 14.9-20.7s |
| Audio (final, mastered) | -16.06 LUFS / -1.51 dBTP | -16.05 to -16.07 LUFS / -3.6 to -4.1 dBTP |

Note on bitrate: the 31 Oct review measured ~245 kbps at CRF 18 on the pre-merge render and flagged
it as suspiciously low. That render's content really was that flat (large empty areas, no ambient
motion) — CRF targets constant *quality*, not a bitrate floor, so low-detail content legitimately
encodes small. With the merge's backdrop/mascot motion on every frame, the same CRF 18 setting now
produces ~1.58 Mbps, consistent with genuinely more per-frame detail rather than a settings bug.

## Per-scene length: Bible target vs actual (narration-driven, STYLE.md rule: "the narration audio
length wins")

| Scene | Template | Target | Actual |
|---|---|---|---|
| 1 | concept-slide (cold open) | 15s | 32.0s |
| 2 | title-card | 5s | 2.3s |
| 3 | concept-slide | 45s | 32.8s |
| 4 | concept-slide | 70s | 51.9s |
| 5 | concept-slide | 50s | 24.6s |
| 6 | code-explain | 30s | 32.0s |
| 7 | pun-card | 4s | 10.8s |
| 8 | concept-slide | 50s | 30.2s |
| 9 | bug-of-the-day | 25s | 30.0s |
| 10 | challenge | 20s | 10.3s |
| 11 | outro | 16s | 8.2s |
| **Total** | | **330s** | **261.0s** |

Actual total is 21% under the Bible's target (330s), driven entirely by narration length at the
configured slow pacing (`length_scale` 1.12) — individual scenes vary more (scene 1 more than
doubles its target; several others come in well under). This is expected per the explicit pipeline
rule that scene length follows the narration, not the Bible's estimate; flagging the spread here so
future Bible-writing can calibrate target lengths against how Piper at this pacing actually reads,
rather than treating the current gaps as a defect.

## Audio pipeline notes

- Unmapped SFX: none. All scene `sfx` names in EP01 match a file in `audio/sfx/`.
- Music bed: silent (not just ducked) for the full Bug of the Day scene, ducked everywhere else —
  implemented via `MusicBed`'s `silenceRanges` prop (added this pass).
- Captions: word-level, sourced from the exact text sent to Piper (not whisper's own transcription)
  with whisper-derived timestamps via the existing cue-alignment machinery — avoids burning
  whisper transcription errors into the video (caught one directly: a clip-opening "Hello?" was
  mis-heard as "I love-").

## What's still pending

- 1080p and 4K renders, per this task's explicit instruction, were not produced in this pass — only
  720p (long + Shorts). The reusable `npm run episode` pipeline (now including the mastering step)
  still produces 1080p + 4K + Shorts for the full 86-episode run.
- Module 0 has not been started, per instruction.

## Round 2 — follow-up fix list (31 Oct, same day)

A second review found 5 more problems in this 720p render. Root cause for most of them: **the long
video was rendered with `--width=1280 --height=720`, not `--scale`.** Remotion's canvas-dimension
override evaluates every fixed-pixel value (mascot `size`, font sizes, padding) directly against the
smaller canvas instead of scaling the whole composition down from its native 1080p layout — so a
460px-tall mascot became 64% of a 720px-tall frame instead of the intended 43%. This is the same bug
already fixed for Shorts in round 1 (where it was caught because content was visibly clipped, not
just crowded); it just hadn't been traced back to the long video too, where the symptom was
"everything's too big and overlapping" rather than "cut off."

**Fix:** re-rendered the long video with `--scale=0.6666666666666666` (the long video's own flex/
percentage-based scene templates had tolerated `--width`/`--height` well enough in round 1's spot
checks that the bug wasn't obvious — but anything with a fixed pixel size, like the mascot or a
tall GCC error panel, didn't). This alone resolved most of the reported caption/mascot overlaps
(items 1, in large part). Confirmed by re-rendering `PunCard`'s and `ConceptSlide`'s native
(un-shrunk) font sizes under `--scale` and finding no overlap — so round 1's font-size-reduction
"fixes" to those two components were **reverted**: they were compensating for the wrong render flag,
not a real component bug, and left text under the 44px minimum unnecessarily.

1. **Captions overlapping Xecxec/code: resolved by the `--scale` fix**, confirmed across every
   sampled scene boundary. No caption-specific repositioning was needed once mascot/content were at
   their intended proportions.
2. **BugOfTheDay not fitting tall content: a real, separate bug**, not resolved by the scale fix
   alone — EP01's GCC error is a genuine 10 lines, and the component didn't reserve space for the
   caption band. Fixed in `BugOfTheDay.tsx`: bottom padding now reserves the caption zone, the error
   panel drops to a smaller size (22px vs 28px) specifically when the error is long (>6 lines, rather
   than truncating a real compiler error, which would be a worse outcome than compact text), and the
   code panel/banner sizes tightened slightly. Verified: the full 10-line error and the FIXED/why
   panel both now render completely, clear of the caption band.
3. **ConceptSlide analogy card now starts near frame 0** (`analogyStart` no longer waits for the
   bullet reveal sequence to finish) — Xecxec's claws-up beat still fires on the last bullet, decoupled
   from the card's own entrance. "Fill the lower-left" partially addressed (bullet font bumps from
   58px to 68px, gap widens, when there's no analogy card) — the no-analogy scenes (cold open, "how
   episodes work") still have visible empty lower space; a real diagram/icon row is content work
   beyond a wiring fix and is flagged as a follow-up, not solved here.
4. **Shorts S1/S2 real visuals added.** S1 ("A crab will teach you C"): a large Xecxec close-up
   (`XecxecVisual`). S2 ("Why learn C in 2026?"): the same analogy-card content ConceptSlide now
   shows for its source scene (scene 3's "Why C?" card), reused via the now-exported
   `analogyFromOnScreen()`. Both confirmed rendering correctly, full visual slot used, no fallback
   text card.
5. **Re-rendered everything** (long video + all 5 Shorts, one job at a time, `--scale`, 720p) rather
   than only S2/S4 as literally specified — S1's visual changed (new Xecxec close-up) so it needed a
   re-render under the "if visuals change" clause too, S3/S4's underlying components were untouched
   but were re-rendered anyway for consistency with the corrected `--scale` approach and to avoid any
   doubt about stale output. All 6 files reverified: correct dimensions (1280×720 / 720×1280 @30fps),
   -16.06 LUFS / -1.51 dBTP (long) and -16.05 to -16.07 LUFS / -3.6 to -4.1 dBTP (Shorts).

### Verdict: Approved. Known remaining gap: no-analogy ConceptSlide scenes (cold open, "how episodes
work") still under-fill the lower-left; a real diagram/icon treatment is a content task for a
follow-up, not a wiring fix.
