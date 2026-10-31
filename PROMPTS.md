# Koding Konkani — prompts for Claude Code

Paste these one at a time, in order. Wait for each phase to finish and review its draft PR before the next one.

## Before you start (you, ~15 minutes)

1. Create the GitHub repo **koding-konkani** (private) and clone it.
2. Put `CLAUDE.md` (from this kit) in the repo root.
3. In Claude Docs, export the **C Course Plan** and every tab of the **Episode Bible** as Markdown. Save them as:
   - `docs/course-plan.md`
   - `docs/bible/m00.md` … `docs/bible/m13.md` (one file per module tab) and `docs/bible/overview.md` (the "Overview & format" tab)
4. Install: Node LTS, Python 3.11, Git. (Remotion downloads its own Chrome and ffmpeg.)
5. Open the repo folder in Claude Code.

---

## Phase 1 — Scaffold the project

```
Read CLAUDE.md and everything in docs/. Then scaffold the Remotion project exactly as CLAUDE.md describes:
TypeScript, src/theme (palette, fonts, module colour pairs), the folder layout, eslint + prettier,
.gitignore for out/ and audio/voice/. Register an empty LongVideo and Short composition.
Show me your plan first, then work on a branch called feat/scaffold and open a draft PR.
```

## Phase 2 — Build the scene templates

```
Build all 11 scene templates and the Xecxec mascot from CLAUDE.md as Remotion components, each driven
by props (no hard-coded episode content). Add a "SceneGallery" composition that shows every template
with sample props so I can preview them in Remotion Studio. Match the design system exactly:
neo-brutalism, pastel palette, 4–5px black borders, 8px hard shadows, Archivo Black / Space Grotesk /
JetBrains Mono, snappy spring motion. Plan first, branch feat/scene-templates, draft PR.
```

## Phase 3 — Voice test (you pick the narrator)

```
Set up scripts/voice.py with Kokoro TTS on CPU. Check the current Kokoro licence first and tell me.
Generate the same 30-second sample (EP 04 scene 5 narration from docs/bible/m00.md) in these male
voices: am_michael, am_adam, bm_george, bm_lewis. Also generate it with Piper en_US-ryan as a fallback.
Save them to audio/voice-test/ and list the files. Don't pick for me — I'll listen and choose.
```

Then tell Claude Code which voice you chose: `Use <voice> as the narrator. Save it in config/voice.json.`

## Phase 4 — Convert the Bible into episode files

```
Write scripts/bible_to_json.py to convert docs/bible/*.md into episodes/ep001.json … ep086.json using
the Episode type in CLAUDE.md. Validate every file against the type (add a zod schema in src/lib).
Compile every C code sample with gcc and check its output matches the "expected output" in the Bible;
give me a report of any mismatch instead of silently fixing it. Plan first, branch feat/episode-data, draft PR.
```

## Phase 5 — Pilot: EP 01 + its 5 Shorts (approval gate)

```
Phase 5: produce the EP 01 pilot, long video and its 5 Shorts. Read CLAUDE.md and docs/STYLE.md first.
Show me a short plan, then work on branch feat/pilot-ep001, draft PR, never push to main.
Do NOT start any other episode. When done, stop and wait for my approval.

PIPELINE (reusable for all 86 episodes: build it as one command, `npm run episode -- <n>`)
1. Narration: scripts/voice.py with config/voice.json (Piper en_US-ryan-high, pacing.lengthScale 1.12).
   One WAV per scene with the pauses from docs/STYLE.md section 1. Strip [HL]/[TRACK] cues before
   speaking but keep their word positions. Normalise to -16 LUFS, peaks below -1 dBTP.
2. Word timestamps for every scene (Piper phoneme timing if available, otherwise faster-whisper),
   saved next to the audio. [HL n] and [TRACK] cues fire on the word they sit in front of.
3. Timing: the narration audio length wins. Scene lengths = audio length + pauses; update the
   episode timeline, never the voice speed.
4. Composition: build LongVideo from episodes/ep001.json using the scene components in src/scenes.
   Implement the transitions and camera moves from docs/STYLE.md in src/transitions (TransitionSeries
   from @remotion/transitions where possible, custom flat ones for ink wipe, window pop, whip, split).
   Never the same transition twice in a row; max 12 frames; every one has its SFX on the cut.
5. Audio: music bed (src/audio MusicBed, ducked under speech, stopped for the Bug reveal), SFX
   mapped from each scene's sfx text to the 12 files in audio/sfx (list any that did not map), the
   3 s sting on the title card.
6. Overlays: burnt-in word-highlight captions; the SpeedTip chip ("TIP: SET SPEED TO 1.5x", 3 s,
   within the first 10 s) from docs/STYLE.md.
7. Shorts: the 5 Shorts from episodes/ep001.json (1080x1920), each opening on its hook in 1.5 s,
   with the end card (FOLLOW / SUBSCRIBE / Full video: EP 01) from docs/shorts-reels.md.
8. Render: long video at 1080p first, then 4K (--scale=2), Shorts at 1080x1920, all into out/ep001/.
   Log how long each took on this PC (and the real-time ratio).

SELF-REVIEW BEFORE YOU SHOW ME (fix problems yourself, then report)
- Look at stills at every transition and every scene; check contrast (npm run check:contrast), text
  overflow, and that no flash is faster than 3 per second.
- Measure the final mix loudness and the music ducking; confirm captions match the words.
- Write out/ep001/review.md: total length, per-scene length vs the Bible target, render times,
  unmapped SFX, deviations from docs/STYLE.md and why.
- Remember: every fix at this stage is a fix to the template for all 86 episodes.
```

Review the pilot carefully. Approve it (or list changes) before Phase 6.

## Phase 6 — Batch a module (only after the pilot is approved)

```
The EP 01 pilot is approved. Using the same pipeline, produce Module <N> (episodes <a> to <b>) and all
their Shorts. Read docs/STYLE.md again. Before rendering, run the gcc check for this module
(npm run episodes:check) and show me any problems. Render one episode at a time, long video at 1080p
and 4K, log progress to out/render-log.txt, skip episodes that are already rendered.
Branch feat/module-<N>, draft PR with the episode list, lengths and render times. Stop after the module.
```

Order: Module 0 (EP 2 to 4), then Module 1 (EP 5 to 14), then the rest. Approve each module before the next.

## Phase 7 — Upload packs (you upload)

```
For every rendered episode, create out/epNNN/upload/ with: youtube.txt (title, description with
chapters, tags), thumbnail.png (1280x720 from the Thumbnail composition), and for each Short a .txt
with its caption and hashtags. Don't upload anything.
```

---

## Handy one-liners

- Fix something across all episodes: `Change <thing> in the <Scene> template, re-render EP <nn> as a check, then tell me which episodes need a re-render.`
- Edit one episode: `In episodes/ep0NN.json change <thing>, re-run the gcc check for it, re-render only that episode.`
- Check the plan: `Compare episodes/ep0NN.json with docs/bible and list differences.`
