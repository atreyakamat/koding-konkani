/** Backtick-quoted code (the Bible's own convention for inline commands/identifiers,
 * e.g. `` `gcc --version` ``), a backslash escape sequence (`\n`, `\t`, ...), or a
 * function-call shape (`printf(`) — any of these means the text should keep its
 * original case. Uppercasing turns `printf` into `PRINTF` (not a real C function)
 * and `\n` into a visually different `\N` — confusing in a language that's
 * case-sensitive and where that one extra character is the whole point. */
const CODE_PATTERN = /`[^`]+`|\\[ntrvfb0"']|\b[a-zA-Z_]\w*\s*\(/;

export const hasCode = (text: string): boolean => CODE_PATTERN.test(text);

/** `"uppercase"` for plain text, `"none"` when the text contains code — drop
 * straight into a `textTransform` style value. */
export const textTransformFor = (text: string): "uppercase" | "none" =>
  hasCode(text) ? "none" : "uppercase";
