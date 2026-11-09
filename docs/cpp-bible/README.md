# C++ Episode Bible (90 episodes)

Course: **C++ for school and first-year college students** · EP 1 to 90 · 11 modules · English only · Remotion animation, AI narrator, mascot Xecxec. Same 11-scene format as the Python Bible.

Every episode is written in Simplified Technical English (see `STE.md`), so Claude Code can follow it exactly. Every code sample was compiled and run, and the pasted outputs and compiler messages come from those runs.

## Files

| File | What it holds |
| --- | --- |
| `m00.md` to `m10.md` | The episodes, one file for each module |
| `STE.md` | Writing and reading rules for the episodes |
| `ILLUSTRATIONS.md` | Schema of the scene 4 data (memory, flow, graph, table, callstack, trace) |
| `metadata/` | Upload data for each episode: YouTube title, description with chapters, tags, thumbnail spec, 5 Shorts (`epNNN.json`, `index.json`, `upload-sheet.md`) |
| `check-report.md` | Result of the last compile-and-run check |
| `preflight.md` | Result of the last preflight check |

## Modules

| Module | Episodes | Topic |
| --- | --- | --- |
| M0 | 1 to 4 | Meet C++ |
| M1 | 5 to 12 | Variables and types |
| M2 | 13 to 20 | Decisions and loops |
| M3 | 21 to 30 | Functions |
| M4 | 31 to 40 | Arrays, vectors and sorting |
| M5 | 41 to 50 | Memory and pointers |
| M6 | 51 to 60 | Classes and objects |
| M7 | 61 to 68 | Inheritance and polymorphism |
| M8 | 69 to 76 | Templates and containers |
| M9 | 77 to 84 | Library and modern C++ |
| M10 | 85 to 90 | Data structures and projects |

## How an episode is built

1. Each episode has 11 scenes: title, concept, code, illustration, second code, terminal, recap, Bug of the Day, pun, challenge, outro.
2. The Bible gives scene times as targets. After voice generation, the audio length wins.
3. Each episode has 5 Shorts, built from its own narration (35 to 45 seconds each).
4. `docs/cpp-bible/metadata/` has the title, description, tags and thumbnail text for each long video and caption data for each Short.

## Commands

Run all commands from the repo root. Python 3.11 or newer. A C++20 compiler (g++) is needed only for the check.

```bash
# 1. Rebuild the Markdown from the episode data (after any edit in scripts/cpp_bible/mNN.py)
python scripts/cpp_bible/gen.py m00 m01 m02 m03 m04 m05 m06 m07 m08 m09 m10

# 2. Compile and run every sample, compare with the Bible
python scripts/check_cpp.py                 # or: --module m03, --episode 40

# 3. Check scene tables, STE rules, cues, illustration data, Shorts
python scripts/preflight_cpp.py             # or: --module m03, --episode 40

# 4. Export the upload metadata
python scripts/cpp_bible_export.py

# Review which code line each [HL] cue lights up
python scripts/cpp_bible/hl_view.py m03 21

# Lint one piece of narration
python scripts/ste_lint.py "Some narration text."
```

Edit the data in `scripts/cpp_bible/mNN.py`, not the Markdown. The generator compiles and runs the code, and it refuses to write an episode that has a problem.

## Before you render

1. Run the check on the Windows PC with MSYS2 **GCC 16**. These files were checked with g++ 13. The check compares the `error:` and `warning:` message lines. If GCC 16 words a message in another way, the check shows `BUG-MESSAGE-DIFFERS`. Run `gen.py` again with GCC 16, so the Bible gets the GCC 16 text.
2. Run `preflight_cpp.py`. It must show 0 errors. Passive-voice warnings do not stop a render.
3. Run `cpp_bible_export.py`. It must show 0 problems.
4. Render a pilot episode first, and look at it. Then render by module.

## Notes

- The old M0 and M1 drafts in the handoff branch (PR 16) are replaced by these files.
- Memory addresses in illustrations are for teaching. They are not real addresses.
- Nothing here uploads a video. The owner uploads.
