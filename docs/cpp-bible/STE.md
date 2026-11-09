# STE rules for the C++ Bible

This file tells you how to write and read every episode in `docs/cpp-bible/`. It uses Simplified Technical English (STE, from ASD-STE100). The goal: one meaning for each sentence, so a person, the narrator voice and Claude Code all read the same thing.

The official ASD-STE100 dictionary is licensed. `scripts/ste_lint.py` checks only the rules a machine can check. Passing the lint means "mechanically clean". It does not prove full STE.

## Rules for narration

1. Write one idea in each sentence. Use at most **20 words** in a sentence.
2. Write at most **6 sentences** in a paragraph.
3. Use the active voice. Say "The compiler prints an error", not "An error is printed". The lint gives a warning for passive voice. A warning does not stop a render.
4. Use one word for one thing. Say "function" every time. Do not switch to "method" or "routine" for the same thing.
5. Use short, common words. Do not use these words: utilize, perform, ensure, in order to, prior to, approximately, subsequently, whereas, additionally, furthermore, via, thus, hence, basically, obviously, just, very, really, etc.
6. Do not use apostrophes or contractions. Write "do not", "it is", "cannot".
7. Write no digits and no symbols in narration. The narrator voice reads them badly.
   - Numbers: write words. Write "twenty-one", not "21".
   - Code: say it in words. Say "C plus plus", "g plus plus", "v dot begin", "double colon", "less than or equal to".
   - File names: say "find dot cpp".
8. Write a command or a step as an instruction. Say "Compile the file. Then run the program."
9. Put one action in each step. Show the result after each step.

The pun in an episode is free text. It follows only the rule for voice-safe characters (no digits and no symbols).

## Cues in narration

- `[HL: text]` marks the code line that the next words explain. `text` must appear in exactly one place in the code file you mean. The generator turns it into a line number, `[HL n]`. Do not type `[HL n]` by hand in new episodes.
- `[TRACK name=value]` updates the live variable tracker. Use it in code scenes only.
- Cues are removed before the narrator reads the text.

## Rules for code

- Every code sample compiles with `g++ -std=c++20 -Wall -Wextra -pthread`, with **no warnings**, and prints the expected output. Exception: a Bug of the Day "wrong" sample may fail on purpose.
- The expected output in the Bible is the output of a real run. Do not type it by hand.
- Use `using namespace std;` only in short samples, as the course does. Say once that big programs should not use it (EP 84).
- Use 4 spaces for indentation. Put one statement on each line.
- Each episode has exactly two code files and one bug.

## Bug of the Day kinds

| Kind | What the checker needs |
| --- | --- |
| `compile` | The wrong code does not compile. The compiler message line matches the Bible. |
| `warn` | The wrong code compiles and gives a warning. The message line matches. |
| `output` | The wrong code runs with no warning, and the output is wrong. |
| `runtime` | The wrong code compiles, then fails when it runs. |

The fixed code must compile with no warning and exit with code 0.

## What Claude Code must do with an episode

1. Read the episode file top to bottom. Each section has one job.
2. Copy code only from the "Code shown" and "Bug of the Day" blocks. Do not retype it.
3. Use the scene table for times. The narration audio length wins over the table after voice generation.
4. Build the illustration only from the JSON in the "Illustrations" section (see `ILLUSTRATIONS.md`). Do not draw anything that the JSON does not say.
5. Run `python scripts/preflight_cpp.py` before a render. A render starts only with 0 errors.
