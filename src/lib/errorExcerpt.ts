/** Picks the two lines of a Bug-of-the-Day "error" text worth showing big in the terminal panel.
 * The Bible text mixes prose ("GCC gives no error ..."), GCC diagnostics and program output.
 *  - GCC diagnostics: the first `error:`/`warning:` line plus the line after it (the echoed source).
 *  - Otherwise program output: the last two lines of the output block (where the wrong value is).
 * Never returns more than two lines. */
const DIAGNOSTIC = /\b(error|warning):/;
const SOURCE_ECHO = /^\s*\d+\s*\|/;

const blocks = (text: string): string[][] =>
  text
    .split(/\n\s*\n/)
    .map((block) => block.split("\n").map((l) => l.trimEnd()).filter((l) => l.trim() !== ""))
    .filter((block) => block.length > 0);

export const errorExcerpt = (error: string): string[] => {
  const lines = error.split("\n").map((l) => l.trimEnd()).filter((l) => l.trim() !== "");
  const at = lines.findIndex((l) => DIAGNOSTIC.test(l));
  if (at >= 0) {
    const next = lines[at + 1];
    return next !== undefined && SOURCE_ECHO.test(next) ? [lines[at], next] : [lines[at]];
  }
  const all = blocks(error);
  // Block 0 is the prose lead-in when there is more than one block; the output follows it.
  const output = all.length > 1 ? all[1] : all[0] ?? [];
  return output.slice(-2);
};
