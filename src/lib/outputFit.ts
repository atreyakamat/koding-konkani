/** Layout for the program-output terminal in CodeExplain. In the normal slot (right column, under the
 * explanation card and tracker) the text is about 604px wide; JetBrains Mono averages 0.6em per
 * character. A long output (EP20: 11 lines, EP25: 14) would need a size under READABLE_PX there, so it
 * takes over the whole right column instead: the code panel narrows so the terminal gets
 * TAKEOVER_PANEL_WIDTH (42% of the frame), and it uses the full column height. In takeover the size
 * runs 30 -> 24px; if the output still does not fit at 24px the FIRST lines are dropped and the last
 * lines are kept (the end of a run is where the result is), with "…" on top. */
export const OUTPUT_TEXT_WIDTH = 604;
export const TAKEOVER_PANEL_WIDTH = 810;
/** Panel width minus the 5px borders and 32px side padding. */
export const TAKEOVER_TEXT_WIDTH = TAKEOVER_PANEL_WIDTH - 10 - 64;
export const OUTPUT_SIZES = [34, 32, 30, 28, 26, 24, 22] as const;
export const TAKEOVER_SIZES = [30, 28, 26, 24] as const;
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

const rowsFor = (lines: string[], size: number, width: number = OUTPUT_TEXT_WIDTH): number => {
  const perRow = Math.max(1, Math.floor(width / (size * 0.6)));
  return 1 + lines.reduce((n, l) => n + Math.max(1, Math.ceil(l.length / perRow)), 0); // +1 prompt line
};

/** Natural height of the output panel for a layout (what it takes in the column before it stretches). */
export const outputPanelHeight = (layout: OutputLayout): number => {
  const lines = layout.text.replace(/\n+$/, "").split("\n");
  const width = layout.fullColumn ? TAKEOVER_TEXT_WIDTH : OUTPUT_TEXT_WIDTH;
  return Math.ceil(rowsFor(lines, layout.size, width) * layout.size * LINE_HEIGHT) + CHROME;
};

export const layoutOutput = (output: string, normalRoom: number, fullRoom: number): OutputLayout => {
  const lines = output.replace(/\n+$/, "").split("\n");
  const fits = (all: string[], size: number, room: number, width: number = OUTPUT_TEXT_WIDTH): boolean =>
    rowsFor(all, size, width) * size * LINE_HEIGHT + CHROME <= room;
  const normal = OUTPUT_SIZES.find((s) => s >= READABLE_PX && fits(lines, s, normalRoom));
  if (normal) return { size: normal, text: output, fullColumn: false, dropped: 0 };
  const W = TAKEOVER_TEXT_WIDTH;
  const full = TAKEOVER_SIZES.find((s) => fits(lines, s, fullRoom, W));
  if (full) return { size: full, text: output, fullColumn: true, dropped: 0 };
  const size = TAKEOVER_SIZES[TAKEOVER_SIZES.length - 1];
  const kept: string[] = [];
  for (let i = lines.length - 1; i >= 0; i--) {
    if (!fits(["…", lines[i], ...kept], size, fullRoom, W)) break;
    kept.unshift(lines[i]);
  }
  return {
    size,
    text: ["…", ...kept].join("\n"),
    fullColumn: true,
    dropped: lines.length - kept.length,
  };
};
