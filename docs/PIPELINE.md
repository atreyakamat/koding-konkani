# Episode data pipeline

Two commands turn the Episode Bible (`docs/bible/m00.md`..`m13.md`) into
validated, compiler-checked episode data.

## `npm run episodes:build`

Runs `scripts/bible_to_json.py`, which parses all 86 episodes out of the
Bible and writes `episodes/ep001.json`..`episodes/ep086.json`, then runs
`scripts/validate_episodes.mts`, which validates every file against the zod
`Episode` schema in `src/lib/episode.ts` and fails the build if any file
doesn't match it, has a duplicate `ep` number, or an episode number is
missing.

The parser never edits `docs/` to make things pass. Where the Bible's
formatting is inconsistent or a section doesn't fit the strict schema (a
handful of these exist — see below), it makes a documented, principled
choice and reports it as a warning rather than silently guessing. Every run
writes `out/bible-to-json-report.md` (git-ignored): a per-episode summary
table (scene/file/Shorts counts, and any scene-time-sum or Shorts-count
mismatch) followed by every warning, grouped by episode.

The parser is **idempotent** — running it twice produces byte-identical
`episodes/*.json` files, since nothing in it depends on wall-clock time,
randomness, or filesystem iteration order beyond a stable sort.

Known Bible-format inconsistencies the parser works around (reported, not
hidden):

- Backslash-escaped markdown punctuature outside code blocks (`\[` `\]` `\*`
  `\_` `\\` `\|` etc.) is un-escaped; text inside fenced code blocks is never
  touched.
- Multi-file "Code shown" sections use three different announcement formats
  across episodes ("File 1: `x.c`", "File 1, x.c:", and a bare `x.c` line on
  its own) — all three are accepted.
- Which files must be compiled together is decided by tracing local
  `#include "x.h"` relationships between the shown files (a union-find over
  the file set), not by parsing the spoken-prose gcc command in the
  narration — that's both more robust and language-independent of exactly
  how the command is phrased.
- "Bug of the Day" sections vary enormously in shape: some show a full GCC
  error block, some describe the bug in prose only (no error text), some
  have no code at all (a "wrong idea", or an environment/PATH mistake), and
  most "fixed" examples are a one-line diff snippet rather than a full
  program. The parser captures whichever shape is actually present and
  flags when it had to fall back (e.g. "used the section's last prose
  paragraph" for an unlabelled explanation).
- Two scenes (EP28, EP29) use `"Challenge + Outro"` as a combined Template
  cell instead of one of the 10 canonical names; these are mapped to
  `outro` with a reported warning rather than inventing an 11th template.
- Module 12's "Step trace" sections only fit the schema's strict
  `{step, array, compare, swap}` shape for the simple pairwise
  compare-and-swap sorts (bubble, selection). Search, merge/quick/counting
  sort, insertion sort (which shifts, not swaps), recursion (Hanoi's "Move
  trace"), and EP81/82's renamed variants use their own table shapes and are
  intentionally left unparsed into `scene.trace`, reported as informational.

Each `episodes/epNNN.json` is a superset of the strict `Episode` type: it
also carries `codeFiles` (every file from "Code shown", independent of which
scene it's attached to) and `bugExtra` (language/reconstruction metadata),
which `episodes:check` reads directly. zod validation ignores these extra
keys, so the file still passes as a strict `Episode`.

## `npm run episodes:check`

Runs `scripts/check_c.py`: compiles and runs every C file in every episode
(both "Code shown" and the Bug of the Day's wrong/fixed code) with the
installed MSYS2 UCRT64 gcc (`-Wall -Wextra -std=c17`), in a temp folder
outside the repo, with a 5-second run timeout.

Each result is classified as `PASS`, `OUTPUT-MISMATCH`, `COMPILE-ERROR`,
`BUG-MESSAGE-DIFFERS` (the Bible's described GCC message doesn't appear in
the real one), `NEEDS-INPUT` (the program reads `scanf` and no stdin could
be determined), `NONDETERMINISTIC` (uses `rand`/`time`/`clock`/`%p`, or the
Bible marks it `[MEASURED]`/"may differ"), `TIMEOUT`, or `SKIPPED` (not C,
or a bare excerpt rather than a full program). When a "fixed" block is a
diff snippet rather than a full program, it's reconstructed by patching it
into the wrong code (via a best-match line replacement); every episode
where that reconstruction happened is listed in the report.

Writes `out/c-check-report.md` (git-ignored, full detail) and
`docs/c-check-summary.md` (committed): counts per class, then every
non-`PASS` result with episode, file, and the first 10 lines of expected vs.
actual.

This machine's gcc (16.2.0) already enforces GCC 14's stricter defaults
(implicit function declarations and implicit `int` are hard errors, not
warnings); `COMPILE-ERROR` results matching that pattern are labelled
`COMPILE-ERROR (GCC14+: implicit decl/int now an error)` specifically, since
that's a toolchain-version finding, not a content bug.

Run a single episode while iterating: `python scripts/check_c.py --episode 74`.

No video is rendered in this phase.
