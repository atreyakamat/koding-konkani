# Archive 2026-11-08

Snapshot of everything produced in the Claude session of 2026-11-06 to 2026-11-08.
Each folder was committed separately (every commit is far under 50 MB; the whole archive is under 1 MB).

| Path | What it is |
| --- | --- |
| `HANDOFF.md` | Full project handoff: status, decisions, pipeline facts, guardrails, next steps |
| `SESSION-SUMMARY.md` | Chronological summary of the session, errors and fixes |
| `bible-drafts/cpp/` | C++ course Bible, M0 (EP1-4) and M1 (EP5-12), strict parser format |
| `bible-drafts/python/` | Python course Bible, M0 (EP1-4) and M1 (EP5-12), strict parser format |
| `generators/` | Python scripts and data that generate the Bible markdown |
| `pipeline-patches/` | Diffs of the scratch `bible_to_json.py` against `scripts/bible_to_json.py` (python fences, 90 episodes) |

The C++ and Python Claude Docs hold M0 only; M1 lives here until it is inserted.
Nothing here touches `main`'s code paths; `archive/` is not read by any script.
