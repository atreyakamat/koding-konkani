/** Picks the lines of a Bug-of-the-Day "error" text worth showing big in the terminal panel (at most two).
 * The Bible text mixes prose ("GCC gives no error ..."), GCC diagnostics, shell commands and program output.
 *  - diagnostic: the first `file:line:col: error|warning: message` line plus the echoed source line after it.
 *  - myth: a quoted claim followed by a numbered list (EP02): the first item, with the claim above it
 *    unless the code card already shows the claim (`shown`, compared after normalising quotes).
 *  - output: the last two lines of the program-output block. Shell commands (`./a`, `gcc ...`) and
 *    prose lead-ins ("Wrong output (...):", "GCC gives no error ...") are skipped; the block that follows
 *    the lead-in is the wrong output. With no lead-in the first block is context (paths, a command)
 *    and the second is the output (EP03); a single block is the output.
 *  - crash: prose only, but it names the crash message ("Segmentation fault"): that message.
 *  - prose: prose only and nothing to show but a sentence (flagged by scripts/bug_excerpts.mts).
 * Never returns more than two lines. */
export type ExcerptKind = "diagnostic" | "myth" | "output" | "crash" | "prose" | "empty";
export type Excerpt = { kind: ExcerptKind; lines: string[] };

// A real compiler line has text after "error:" / "warning:" ("GCC error:" alone is a heading).
const DIAGNOSTIC = /^\S.*?\b(error|warning):\s*\S/;
const SOURCE_ECHO = /^\s*\d+\s*\|/;
const COMMAND = /^(\.\/\S+|gcc\b.*|\$ .*)$/;
/** "gcc -Wall bug.c gives no warning ..." starts like a command but is a sentence. */
const NO_ERROR_PROSE = /\b(no (compiler |compile )?(error|warning)s?|gives no|compiles with)\b/i;
const LEAD_IN = /\b(wrong output|press ctrl|forever)\b/i;
const CRASH = /\b(Segmentation fault|Aborted|core dumped)\b/;
const QUOTED = /^["“].*["”]$/;
const LIST_ITEM = /^\d+\.\s+/;

const blocksOf = (text: string): string[][] =>
  text
    .split(/\n\s*\n/)
    .map((block) => block.split("\n").map((l) => l.trimEnd()).filter((l) => l.trim() !== ""))
    .filter((block) => block.length > 0);

const isProseBlock = (block: string[]): boolean =>
  block.some((l) => l.endsWith(":") || NO_ERROR_PROSE.test(l) || LEAD_IN.test(l));

const isCommandBlock = (block: string[]): boolean =>
  block.every((l) => COMMAND.test(l.trim()) && !NO_ERROR_PROSE.test(l) && !l.endsWith(":"));

const sentences = (text: string): string[] =>
  text
    .replace(/\s+/g, " ")
    .split(/(?<=[.!?])\s+(?=[A-Z])/)
    .map((s) => s.trim())
    .filter(Boolean);

/** Lower-case, curly quotes straightened, quotes and spacing dropped: two spellings of one sentence compare equal. */
export const normaliseClaim = (text: string): string =>
  text
    .replace(/[‘’“”]/g, "'")
    .replace(/["']/g, "")
    .replace(/\s+/g, " ")
    .trim()
    .toLowerCase();

/** `shown` is the text of the code card above the panel, used to avoid repeating it. */
export const classifyError = (error: string, shown?: string): Excerpt => {
  const lines = error.split("\n").map((l) => l.trimEnd()).filter((l) => l.trim() !== "");
  const at = lines.findIndex((l) => DIAGNOSTIC.test(l));
  if (at >= 0) {
    const next = lines[at + 1];
    return {
      kind: "diagnostic",
      lines: next !== undefined && SOURCE_ECHO.test(next) ? [lines[at], next] : [lines[at]],
    };
  }

  const all = blocksOf(error);
  // Myth-buster: a quoted claim, then a numbered list of evidence.
  if (all.length > 1 && all[0].length === 1 && QUOTED.test(all[0][0].trim()) && LIST_ITEM.test(all[1][0])) {
    const proof = all[1][0].replace(LIST_ITEM, "");
    const claimShown = shown !== undefined && normaliseClaim(shown) === normaliseClaim(all[0][0]);
    return { kind: "myth", lines: claimShown ? [proof] : [all[0][0], proof] };
  }

  const blocks = all.filter((b) => !isCommandBlock(b));
  const lead = blocks.findIndex(isProseBlock);
  const outputBlock =
    lead >= 0
      ? blocks.slice(lead + 1).find((b) => !isProseBlock(b))
      : blocks.length > 1
        ? blocks[1]
        : blocks[0];
  if (outputBlock) return { kind: "output", lines: outputBlock.slice(-2) };

  const text = lines.join(" ");
  const crash = CRASH.exec(text)?.[1];
  if (crash) return { kind: "crash", lines: [crash] };
  // Prose only: the first sentence that is not the "no error" lead-in.
  const sentence = sentences(text).find((s) => !NO_ERROR_PROSE.test(s)) ?? sentences(text)[0];
  return sentence ? { kind: "prose", lines: [sentence] } : { kind: "empty", lines: [] };
};

export const errorExcerpt = (error: string, shown?: string): string[] => classifyError(error, shown).lines;
