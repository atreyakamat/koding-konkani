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

## Phase 5 — Pilot: EP 01 + its 5 Shorts

```
Produce EP 01 end to end: generate narration with the chosen voice, normalise loudness, get word
timestamps, build the LongVideo composition from episodes/ep001.json (scenes stretch to the narration),
add music bed and SFX, and the 5 Shorts. Render the long video at 1080p and at 4K (--scale=2), and the
Shorts at 1080x1920, into out/ep001/. Tell me how long each render took on my PC.
Plan first, branch feat/pilot-ep001, draft PR.
```

Review the pilot carefully. Every fix you ask for here is a fix to the template for all 86 episodes.

## Phase 6 — Batch a module

```
Using the pipeline from the pilot, produce Module <N> (episodes <a>–<b>) and all their Shorts.
Before rendering, run the gcc check for this module and show me any problems. Render overnight-friendly:
one episode at a time, log progress to out/render-log.txt, and skip episodes that are already rendered.
Branch feat/module-<N>, draft PR with the episode list and render times.
```

Repeat for each module.

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
