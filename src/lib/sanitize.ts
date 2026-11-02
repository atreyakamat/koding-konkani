/** One shared cleaner for every on-screen string. The Episode Bible is written in Markdown, so
 * fields like bug.why, bug.error, challenge and onScreen can carry `**bold**`, `` `code` ``
 * ticks and `# headings` that must never reach the frame as literal characters.
 *
 * Deliberately conservative so it is safe on prose AND on C:
 *  - `**x**` / `__x__` pairs only (a lone `**p` pointer-to-pointer is untouched);
 *  - backticks only when paired on one line (GCC's own `print' quoting is untouched);
 *  - `#` only as a Markdown heading (`# Title`), never `#include` / `#define`. */
export const stripMarkdown = (text: string): string =>
  text
    .replace(/^\s*```[a-z]*\s*$/gim, "")
    .replace(/\*\*([^*\n]+?)\*\*/g, "$1")
    .replace(/(?<![\w])__([^_\n]+?)__(?![\w])/g, "$1")
    .replace(/`([^`\n]+)`/g, "$1")
    .replace(/^\s{0,3}#{1,6}\s+/gm, "")
    .replace(/\n{3,}/g, "\n\n")
    .trim();

/** True when the string still contains Markdown markers (used by the render checks). */
export const hasMarkdown = (text: string): boolean => stripMarkdown(text) !== text.trim();
