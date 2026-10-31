# Koding Konkani — project guide for Claude Code

Read this file at the start of every session. It is the source of truth for how this repo works.

## What this is

**Koding Konkani** is a YouTube + Instagram channel teaching the C language to school (Class 11–12) and first-year college students. Everything is made in code:

- **86 long videos** (5–8 min, 16:9) and **430 Shorts** (5 per episode, 9:16).
- **English only**: narration, on-screen text, code.
- **No on-camera host.** 100% Remotion animation. An AI male narrator explains code line by line.
- **Mascot:** Crab Xecxec (pronounced "Sheck Sheck"). Never speaks; reacts with animation, claw-click sound, speech bubbles.
- **Tone:** friendly, fun, puns. Sign-off: "Keep coding, says Xecxec!"

Planning lives in two Claude Docs the owner reviews (exported to `docs/` as Markdown):
- `docs/course-plan.md` — channel decisions, episode template, design system, full 86-episode outline.
- `docs/bible/` — the Episode Bible: one Markdown file per module with every episode's scenes, narration, code, bug, pun, challenge and 5 Shorts.

## Stack

- **Video:** Remotion (React + TypeScript). Node LTS.
- **Voice + audio tooling:** Python 3.11 scripts in `scripts/`.
- **Narrator:** Kokoro TTS on CPU (Apache-2.0). Voice chosen in the voice test; stored in `config/voice.json`.
- **Timestamps:** Kokoro word timestamps if available, otherwise faster-whisper / whisper.cpp on the generated audio.
- **Platform:** Windows 11, Ryzen 7 5700G, 16 GB RAM, integrated GPU. Everything must run on CPU.

## Repo layout

```text
koding-konkani/
  CLAUDE.md
  docs/                course plan + Episode Bible (Markdown exports, read-only input)
  episodes/            ep001.json … ep086.json — generated from docs/bible, then hand-tuned
  src/
    theme/             palette.ts, fonts.ts, modules.ts (colour pair per module)
    scenes/            one component per scene template (see below)
    mascot/            Xecxec.tsx (SVG, poses: idle, scuttle, claws-up, shell-shake, snap, wave)
    compositions/      LongVideo.tsx, Short.tsx, Thumbnail.tsx
    lib/               timing from word timestamps, code tokenizer/highlighter
    Root.tsx           registers one composition per episode and per Short
  audio/
    sfx/               sound-effect library (royalty-free, licences in audio/sfx/LICENSES.md)
    music/             background beds (royalty-free)
    voice/             generated narration (git-ignored)
  scripts/
    bible_to_json.py   docs/bible/*.md  ->  episodes/epNNN.json
    voice.py           episode JSON -> narration WAV per scene + timestamps JSON
    loudness.py        normalise to -16 LUFS integrated
    render.ts / .ps1   batch render a module or an episode range
  out/                 renders (git-ignored)
```

## Design system (neo-brutalism, pastel)

Flat pastel blocks, thick black borders, hard offset shadows, chunky type. No gradients, no blur, no emoji.

| Token | Hex | Use |
|---|---|---|
| tomato | #FF6F59 | Xecxec, title cards, errors |
| peach | #FFD8BE | backgrounds |
| apricot | #FFB88A | secondary blocks, badges |
| butter | #FFE58A | line highlights, Bug of the Day |
| cream | #FFF4EC | cards, code panels |
| pastelBlue | #BFD7FF | backgrounds, concept slides |
| mint | #B8F2D0 | success, sorted, correct |
| lilac | #D9C9FF | memory and pointer scenes |
| darkBlue | #1E2A4A | terminal, dark scenes |
| ink | #111111 | borders (4–5px), shadows (8px offset), text — accents only |
| white | #FFFFFF | text on dark — accents only |

Fonts (Google Fonts, load via `@remotion/google-fonts`): **Archivo Black** (titles, all caps), **Space Grotesk** 500/700 (body), **JetBrains Mono** 500/700 (code).

Module colour pairs (background + accent): M0 peach+tomato · M1 pastelBlue+tomato · M2 cream+apricot · M3 mint+darkBlue · M4 butter+darkBlue · M5 lilac+tomato · M6 peach+darkBlue · M7 pastelBlue+apricot · M8 lilac+darkBlue · M9 cream+tomato · M10 mint+tomato · M11 apricot+darkBlue · M12 darkBlue+butter (bars mint/tomato/pastelBlue) · M13 peach+lilac.

Motion: snappy springs, 8–12 frame moves, 2-frame shake on impacts, every move has a sound. Respect the scene timings in the episode JSON.

**Pacing, cuts, transitions and camera moves are defined in `docs/STYLE.md`. Read it before building any scene or composition.** The narrator is deliberately slow (Piper `length_scale` 1.12, see `config/voice.json`); viewers can speed up with the player. Never speed the voice up to save time.

## Scene templates (one component each in `src/scenes/`)

1. **TitleCard** — accent background, EP sticker (butter, rotated), huge outlined title, module chip, Xecxec scuttles in. SFX thud + whoosh + claw click.
2. **ConceptSlide** — 1–3 numbered lines spring in as narrated; analogy card on the right.
3. **CodeExplain** — code panel types itself, then active line gets butter highlight (`[HL n]` cues), explanation card + live variable tracker (`[TRACK name=value]` cues). SFX keys, marker swipe.
4. **MemoryBoxes** — variables as labelled boxes with addresses; pointers as thick arrows that draw on.
5. **Terminal** — dark-blue window; command types, output prints; mint success, tomato error. SFX ding / buzzer.
6. **AlgorithmBars** — bars driven by the episode's step-trace table: compare (butter), swap (tomato, bars slide past), sorted (mint); pass/compare/swap counters.
7. **BugOfTheDay** — butter background; wrong code shakes, GCC error appears, fix slides in.
8. **PunCard** — full tomato screen, one line, Xecxec snap. ~4s.
9. **Challenge** — task card with ticking checklist + "Comment your answer".
10. **Outro** — next-episode text; keep the right side empty for YouTube end-screen elements (next video + subscribe) for the last 20s.
11. **Short** layout — 1080×1920: hook top, visual middle, captions bottom third, nothing under YouTube's right-side buttons, "Full video: EP NN" badge.

## Episode JSON (episodes/epNNN.json)

```ts
type Episode = {
  ep: number; title: string; module: number; lengthSec: number;
  colours: { bg: string; accent: string };
  learningGoals: string[];
  youtube: { title: string; description: string; chapters: {t: string; label: string}[]; tags: string[];
             thumbnail: { text: string; visual: string; pose: string } };
  scenes: {
    id: number; template: SceneTemplate; startSec: number; lengthSec: number;
    onScreen: string; animation: string; sfx: string[];
    narration: string;              // with [HL n] / [TRACK a=1] cues
    code?: { file: string; source: string; output?: string };
    trace?: { step: number; array: number[]; compare?: [number, number]; swap?: [number, number]; sorted?: number[] }[];
  }[];
  bug: { wrong: string; error: string; fixed: string; why: string };
  pun: string; challenge: string; challengeAnswer: string;
  shorts: { id: 'S1'|'S2'|'S3'|'S4'|'S5'; title: string; hook: string; script: string; onScreen: string;
            fromScenes: number[]; lengthSec: number; caption: string; hashtags: string[] }[];
};
```

Timing rule: scene lengths in the Bible are targets. After voice generation, **the narration audio length wins**; scenes stretch or shrink to fit, and animations fire on word timestamps.

## Audio rules

- Narration normalised to −16 LUFS integrated, peaks below −1 dBTP.
- Music bed at about −24 dB under speech, ducked when the narrator talks; 3s channel sting on title cards.
- Royalty-free music and SFX only; record the source and licence of every file in `audio/*/LICENSES.md`.

## Render settings

- Long videos: composition 1920×1080, 30 fps, H.264 (CRF 18). **4K masters:** same composition rendered with `--scale=2` (3840×2160). Design everything as vectors/CSS so 4K stays sharp.
- Shorts: 1080×1920, 30 fps.
- Concurrency: start at 4 on this machine; lower it if RAM goes above ~13 GB.
- Batch renders run overnight, one module at a time. Never render into the repo; output goes to `out/` (git-ignored).

## Working rules (owner's guardrails — always follow)

- Show a short plan before each piece of work; the owner reviews everything.
- Work on feature branches; open **draft PRs** for review. **Never push to main.**
- Never spend money, sign up for paid tools, or add paid APIs without asking.
- Never delete files, repos or data without asking.
- Never touch credentials, API keys or `.env` files. Never commit secrets.
- Never publish or upload videos; the owner uploads. Prepare metadata files only.
- Keep code production-grade: typed, linted, small components, no copy-pasted scenes.
- Technical accuracy of the C content matters more than speed: compile every code sample with GCC and check outputs match the episode JSON before rendering.
