# EP 01 pilot — review (Claude, 31 Oct 2026)

Inputs: `ep001-1080p.mp4` (260.97 s) and Shorts S1–S5. Frames sampled every 10 s (long) and 2.5 s (Shorts).

## Verdict: NOT approved. Fix list below, then re-render EP 01 only.

The pipeline works (voice, captions, timing, audio, C content). The *visual layer* does not meet the brief: it reads as a captioned slideshow, not a mascot-led animation. Owner's feedback is correct.

## What works
- Audio: -15.8 LUFS integrated, true peak -0.6 dBTP (target -16 / below -1: peak slightly hot, fix with limiter at -1.5).
- Karaoke-style captions with highlighted word; code panel, line highlight, Bug of the Day, Pun card render correctly.
- Pacing is slow as designed; speed tip is spoken.

## Problems (ordered by impact)
1. **Xecxec is effectively absent.** Visible in only ~4 of 27 sampled frames (Pun, Challenge, Outro), ~60-100 px wide on a 1920 px frame, in a corner. Not in the cold open, concept slides, code scenes or Bug scene. No pose changes, no bubbles, no reactions. The mascot is the brand; right now there is no brand.
2. **No title card / no channel identity.** Video opens on a flat peach screen with "Hello?". No EP sticker, module chip, logo or sting visible.
3. **Large dead areas.** ~50–60 % of most frames is empty peach: concept slides are left-aligned text with nothing on the right (the analogy card is missing or blank), code scenes leave the bottom half empty, Challenge/Outro are tiny cards top-left. Text is small for 1080p mobile viewing.
4. **No interaction / life.** Scenes only fade-swap. No variable tracker, no output terminal after the code, no arrows, no sticker pops, no screen-shake, no background motion (shapes, grid, parallax). Style guide (docs/STYLE.md) camera moves and transitions are not visible.
5. **Empty analogy card** at 0:40-ish (empty box next to code) — a bug, not a design choice.
6. **Compression.** Video bitrate is ~245 kbps for 1080p. Flat colours hide it, but small code text will smear. Render with CRF 18 (CLAUDE.md) and check the output really used it.
7. **Smart quotes in the panel**: explanation card shows curly quotes around "Hi" — the exact bug the episode teaches. Use straight quotes.
8. **Black tail frames** after Outro in the sheet; trim.

## Shorts (all five share one template — "plain" is accurate)
- Layout is: headline top, a cream box with one line of text in the middle, red caption, tiny "Full video" badge. The middle "visual" is a placeholder box; no crab, no code, no motion.
- **End card shows the literal text `FOLLOW @YOUR_IG_HANDLE`** — placeholder shipped. It also dims the whole frame to grey and overlaps the box text, hard to read.
- Captions appear as a line-by-line block, not word-by-word; small for a phone.
- Hook has no motion in the first 0.5 s; nothing stops the scroll.
- Content lives mid-screen but the bottom third is mostly empty; the "Full video" badge is tiny.

## Required changes (acceptance criteria for re-render)
**Mascot**
- Xecxec at least 22 % of frame height on concept/code scenes (hero size on title/pun/outro, ~45 %). Fixed home position, never hidden behind panels.
- Pose per beat (idle blink, claws-up on success, shell-shake on error, snap on pun, wave on intro/outro), plus a speech bubble with 1–4 words at key moments (e.g. "Oops!", "Nice!").
- Visible in the first second of every Short.

**Scenes**
- Add TitleCard (EP sticker, module chip, big outlined title, Xecxec scuttles in, sting) and a real Outro.
- Fill the frame: concept slides get a large diagram or analogy illustration on the right; code scenes get an output terminal below that types the result and a live variable tracker; Bug scene shows the error in a dark terminal.
- Ambient motion on every scene: drifting pastel shapes / dot grid, parallax on entrance, sticker pops with 2-frame impact shake, springs on every element.
- Implement the STYLE.md transitions (wipes, slides, punch-in) instead of plain cuts.
- Minimum body text 44 px at 1080p.

**Shorts**
- Own layout, not the long-video clone: Xecxec big, a visual per Short (animated code, bug, memory box), hook animates in at frame 0, word-by-word captions in the lower third at ≥56 px, progress bar, bigger "Full video: EP 01" badge.
- End card (last ~2 s): clear "Follow Koding Konkani" + handle, no full-frame dimming.

**Fixes**
- Replace `@YOUR_IG_HANDLE` everywhere (docs/shorts-reels.md, scripts/shorts_to_md.py, Short end card) once the owner confirms the handle — **open question**.
- Straight quotes in explanation text; trim black tail; limiter to -1.5 dBTP; verify CRF 18.

## Pushback
- Don't start Module 0 until EP 01 passes this list; fixing templates now is cheap, after 86 episodes it is not.
- Ambient motion and mascot presence should be built once in shared components, not per scene, so all 86 episodes inherit it.

## Open questions for owner
1. Exact Instagram handle (e.g. `@kodingkonkani`)?
2. Xecxec size: OK with ~22 % of frame height as default, hero-size on title/pun/outro?
