/** Layout for the program-output terminal in CodeExplain. The strip sits in the right column
 * (about 604px of text width); JetBrains Mono averages 0.6em per character. Short outputs keep the
 * normal room (under the explanation card and tracker). A long one (EP20: 11 lines, EP25: 14) would
 * need a size under READABLE_PX there, so it takes the whole column instead, and as a last resort
 * the lines that do not fit are cut with an ellipsis. */
export const OUTPUT_TEXT_WIDTH = 604;
export const OUTPUT_SIZES = [34, 32, 30, 28, 26] as const;
/** Smallest size accepted while the explanation card and tracker stay on screen. */
export const READABLE_PX = 28;
const LINE_HEIGHT = 1.35;
const CHROME = 40;

export type OutputLayout = { size: number; text: string; fullColumn: boolean };

const rowsFor = (lines: string[], size: number): number => {
  const perRow = Math.max(1, Math.floor(OUTPUT_TEXT_WIDTH / (size * 0.6)));
  return 1 + lines.reduce((n, l) => n + Math.max(1, Math.ceil(l.length / perRow)), 0); // +1 prompt line
};

export const layoutOutput = (output: string, normalRoom: number, fullRoom: number): OutputLayout => {
  const lines = output.replace(/\n+$/, "").split("\n");
  const fits = (size: number, room: number): boolean => rowsFor(lines, size) * size * LINE_HEIGHT + CHROME <= room;
  const normal = OUTPUT_SIZES.find((s) => s >= READABLE_PX && fits(s, normalRoom));
  if (normal) return { size: normal, text: output, fullColumn: false };
  const full = OUTPUT_SIZES.find((s) => fits(s, fullRoom));
  if (full) return { size: full, text: output, fullColumn: true };
  const size = OUTPUT_SIZES[OUTPUT_SIZES.length - 1];
  const kept: string[] = [];
  for (const line of lines) {
    if (!fits(size, fullRoom) && kept.length === 0) break;
    if (rowsFor([...kept, line, "…"], size) * size * LINE_HEIGHT + CHROME > fullRoom) break;
    kept.push(line);
  }
  return { size, text: [...kept, "…"].join("\n"), fullColumn: true };
};
