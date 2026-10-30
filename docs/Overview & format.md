# Koding Konkani — Episode Bible

Oct 30, 2026 · @Atreya

This tab is the format and production guide. Every episode lives in its module tab (M0–M13): 86 episodes and 430 Shorts, each fully specified for Remotion.

## How every episode is specified

Every episode page carries the same 9 fields, so Claude Code can turn each one straight into a Remotion composition.

| Field | What it holds |
| --- | --- |
| Header | Number, title, module, target length, colour pair, prerequisite |
| Learning goals | 2–4 things the student can do after watching |
| YouTube | Title, description with chapters, tags, thumbnail concept |
| Scene list | Each scene: template, start, length, what's on screen, animation and sound effects |
| Narration script | Word-for-word English narration per scene, with \[HL n\] highlight and \[TRACK\] variable-tracker cues |
| Code | Every file exactly as typed, plus the expected output |
| Bug of the Day | Wrong code, the exact GCC error, the fix, why |
| Pun & challenge | Pun line, challenge, and the challenge answer for the next episode |
| 5 Shorts | For each: title, hook, full script, on-screen text, source scenes, length, caption + hashtags |
| Algorithms only | Step-trace table for the bar animation, time and space complexity |

In the repo, each episode becomes one file (`episodes/ep001.json`) holding these same fields; the doc is where you review them.

## Shorts system

Each episode gets 5 Shorts of the same 5 types: 86 × 5 = 430 Shorts, each posted to both YouTube Shorts and Instagram Reels.

| # | Type | Length | Built from | Job |
| --- | --- | --- | --- | --- |
| S1 | Hook teaser | 20–30s | Cold open + title card | Drive views to the full episode |
| S2 | Concept in 30 seconds | 30–45s | Concept slide + one code-explain moment | Teach one idea on its own |
| S3 | Bug of the Day | 20–30s | Bug of the Day scene | Relatable mistake, high shares |
| S4 | Pun / meme | 10–20s | Pun card + Xecxec reaction | Fun, follows, comments |
| S5 | Quiz / challenge | 15–25s | Challenge card as "What does this print?" | Comments, answer pinned later |

**The maths:** 430 Shorts over the 29-week run is about 2 a day. Posting only 1 a day means 203 Shorts get used and the rest bank up. My suggestion: 2 a day (morning S2/S3, evening S1/S4/S5), so Shorts finish with the series.

**Rules for every Short:** 1080×1920, hook in the first 1.5 seconds, burned-in captions in the bottom third, nothing under YouTube's right-side buttons, "Full video: EP NN" badge, same file for both platforms with platform-specific captions and hashtags.

## Colour system

The palette now mixes pastel warms and cools with one dark blue; black and white are used only for borders, shadows, text and small accents.

| Name | Hex | Family | Main use |
| --- | --- | --- | --- |
| Tomato | #FF6F59 | Warm | Xecxec, title cards, errors |
| Peach | #FFD8BE | Warm | Backgrounds |
| Apricot | #FFB88A | Warm | Secondary blocks, badges |
| Butter | #FFE58A | Warm | Line highlights, Bug of the Day |
| Cream | #FFF4EC | Neutral | Cards, code panels |
| Pastel blue | #BFD7FF | Cool | Backgrounds, concept slides |
| Mint | #B8F2D0 | Cool | Success, sorted, correct |
| Lilac | #D9C9FF | Cool | Memory and pointer scenes |
| Dark blue | #1E2A4A | Deep | Terminal, dark scenes, contrast blocks |
| Black | #111111 | Accent | Borders, shadows, text |
| White | #FFFFFF | Accent | Text on dark, eye highlights |

**One colour pair per module,** so a viewer can tell the module from a thumbnail. Background first, accent second:

| Module | Background | Accent |
| --- | --- | --- |
| 0. Welcome & setup | Peach | Tomato |
| 1. Basics | Pastel blue | Tomato |
| 2. Operators | Cream | Apricot |
| 3. Decisions | Mint | Dark blue |
| 4. Loops | Butter | Dark blue |
| 5. Functions | Lilac | Tomato |
| 6. Arrays | Peach | Dark blue |
| 7. Strings | Pastel blue | Apricot |
| 8. Pointers | Lilac | Dark blue |
| 9. Structures | Cream | Tomato |
| 10. Dynamic memory | Mint | Tomato |
| 11. Files | Apricot | Dark blue |
| 12. Algorithms | Dark blue | Butter (bars in mint, tomato, pastel blue) |
| 13. Projects & finale | Peach | Lilac |

The scene template sheet will be updated to show these pairs.

## Narrator voice options

My pick is Kokoro: free, allows commercial use, runs well on your CPU, and has several good male voices to choose from.

| Option | Voices to try | Cost | Runs on your PC? | Quality | Notes |
| --- | --- | --- | --- | --- | --- |
| **Kokoro (recommended)** | am\_michael, am\_adam (American), bm\_george, bm\_lewis (British) | Free, Apache-2.0 | Yes, CPU, near real-time | Very natural for its size | Best balance for 86 videos |
| Piper | en\_US-ryan, en\_GB-alan | Free | Yes, very fast | Clear but a bit flat | Good fallback |
| Chatterbox | One voice + emotion control | Free, MIT | Yes, but slow on CPU | Most expressive free option | Hours per episode on CPU |
| ElevenLabs | Large library | Paid monthly plan | Cloud | Best | Needs your OK before signing up |

Skip XTTS: its licence doesn't allow commercial use, and the channel will be monetised.

**Next step:** in Claude Code, I generate the same 30-second EP 04 line-by-line explain in all four Kokoro voices plus Piper Ryan. You listen and pick one. Licences get checked again at install time.

## Running it locally with Claude Code

Yes, your PC can do this: a Ryzen 7 5700G with 16 GB RAM can render these videos; the 2 GB of video memory doesn't matter, because Remotion and Kokoro use the CPU.

| Task | Tool | Rough time per episode on your PC |
| --- | --- | --- |
| Narration | Kokoro on CPU | 2–5 min |
| Word timestamps | Kokoro's output, or whisper.cpp as backup | 1–3 min |
| Long video render (1080p, 6 min) | Remotion, 4 parallel tabs | 15–30 min |
| 5 Shorts render | Remotion | 10–15 min |

These are estimates; we'll measure on EP 01 and adjust.

**4K:** yes. Scenes are designed at 1920×1080 in vectors, and Remotion renders them at 3840×2160 with `--scale=2`, so text stays sharp. Expect about 3–4× the 1080p render time (roughly 1–2 hours per episode on your PC), so render 4K overnight. Worth it for long videos: YouTube gives 4K uploads a higher bitrate, so code text looks crisper even for viewers watching at 1080p. Keep Shorts at 1080×1920.

**Setup tips**

- Close Chrome and games while rendering; Remotion uses about 0.5 GB of RAM per parallel tab.
- Render overnight in batches: one module (4–12 episodes) per night.
- Repo: `koding-konkani` on GitHub, work on branches with draft PRs like your other projects.
- Keep raw voice files and renders out of git (they're large); store them in a separate folder or Google Drive.

**Repo layout (proposal)**

```text
koding-konkani/
  episodes/         ep001.json … ep086.json (scenes, script, code, shorts)
  src/scenes/       one Remotion component per scene template
  src/compositions/ LongVideo.tsx, Short.tsx
  src/theme/        palette, fonts, module colour pairs
  audio/sfx/        sound effects library
  scripts/          voice.py (Kokoro), timestamps, batch render
  out/              renders (git-ignored)
```

## What happens next

1. You review the module tabs (comment anywhere; start with M0 and M8).
2. Export this doc's tabs and the Course Plan as Markdown into the repo's `docs/` folder.
3. Run the Claude Code phases in PROMPTS.md: scaffold, scene templates, voice test, episode files, EP 01 pilot, then one module at a time.
4. In phase 4, Claude Code re-compiles every sample on your Windows GCC. The episodes were checked on Linux GCC 13, so a few outputs (crash messages, addresses, some GCC 14+ errors) may read differently on MSYS2; fix those then.
