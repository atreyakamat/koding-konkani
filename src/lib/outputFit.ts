/** Layout for the program-output terminal in CodeExplain. The strip sits in the right column
 * (about 604px of text width); JetBrains Mono averages 0.6em per character. Short outputs keep the
 * normal room (under the explanation card and tracker). A long one (EP20: 11 lines, EP25: 14) would
 * need a size under READABLE_PX there, so it takes the whole column instead. The size goes down to
 * MIN_PX (22) before anything is cut; if the output still does not fit, the FIRST lines are dropped
 * and the last lines are kept (the end of a run is where the result is), with "…" on top. */
export const OUTPUT_TEXT_WIDTH = 604;
export const OUTPUT_SIZES = [34, 32, 30, 28, 26, 24, 22] as const;
/** Smallest size accepted while the explanation card and tracker stay on screen. */
export const READABLE_PX = 28;
const LINE_HEIGHT = 1.35;
const CHROME = 40;

export type OutputLayout = {
  size: number;
  text: string;
  fullColumn: boolean;
  /** How many leading lines were cut (0 when everything is shown). */
  dropped: number;
};

const rowsFor = (lines: string[], size: number): number => {
  const perRow = Math.max(1, Math.floor(OUTPUT_TEXT_WIDTH / (size * 0.6)));
  return 1 + lines.reduce((n, l) => n + Math.max(1, Math.ceil(l.length / perRow)), 0); // +1 prompt line
};

export const layoutOutput = (output: string, normalRoom: number, fullRoom: number): OutputLayout => {
  const lines = output.replace(/\n+$/, "").split("\n");
  const fits = (all: string[], size: number, room: number): boolean =>
    rowsFor(all, size) * size * LINE_HEIGHT + CHROME <= room;
  const normal = OUTPUT_SIZES.find((s) => s >= READABLE_PX && fits(lines, s, normalRoom));
  if (normal) return { size: normal, text: output, fullColumn: false, dropped: 0 };
  const full = OUTPUT_SIZES.find((s) => fits(lines, s, fullRoom));
  if (full) return { size: full, text: output, fullColumn: true, dropped: 0 };
  const size = OUTPUT_SIZES[OUTPUT_SIZES.length - 1];
  const kept: string[] = [];
  for (let i = lines.length - 1; i >= 0; i--) {
    if (!fits(["…", lines[i], ...kept], size, fullRoom)) break;
    kept.unshift(lines[i]);
  }
  return {
    size,
    text: ["…", ...kept].join("\n"),
    fullColumn: true,
    dropped: lines.length - kept.length,
  };
};
