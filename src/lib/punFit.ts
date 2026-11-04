/** Pure layout for the PunCard: picks the largest title size at which the pun, word-wrapped,
 * fits the text box without clipping. Archivo Black in mixed case averages ~0.52em per
 * character; 0.6 is used so a caps- or digit-heavy pun still fits. */

export const PUN_BOX = { width: 1428, height: 560 } as const;
export const PUN_MIN_PX = 56;
export const PUN_MAX_PX = 96;
export const PUN_LINE_HEIGHT = 1.3;
const CHAR_EM = 0.6;
/** A pun that needs more lines than this at the minimum size is reported by the check script. */
export const PUN_MAX_LINES = 3;

export const wrapLineCount = (
  text: string,
  size: number,
  width: number = PUN_BOX.width,
): number => {
  const perRow = Math.max(1, Math.floor(width / (size * CHAR_EM)));
  let rows = 1;
  let used = 0;
  for (const word of text.split(/\s+/).filter(Boolean)) {
    const need = word.length + (used ? 1 : 0);
    if (used && used + need > perRow) {
      rows++;
      used = word.length;
    } else used += need;
    if (word.length > perRow) rows += Math.floor(word.length / perRow);
  }
  return rows;
};

export type PunFit = { size: number; lines: number };

/** Largest size in [PUN_MIN_PX, PUN_MAX_PX] (4px steps) whose wrapped text is <= PUN_MAX_LINES
 * lines and fits the box height; else the largest that fits the height; else PUN_MIN_PX. */
export const fitPun = (text: string): PunFit => {
  const fitsHeight = (size: number): boolean =>
    wrapLineCount(text, size) * size * PUN_LINE_HEIGHT <= PUN_BOX.height;
  for (let size = PUN_MAX_PX; size >= PUN_MIN_PX; size -= 4) {
    if (wrapLineCount(text, size) <= PUN_MAX_LINES && fitsHeight(size)) {
      return { size, lines: wrapLineCount(text, size) };
    }
  }
  for (let size = PUN_MAX_PX; size >= PUN_MIN_PX; size -= 4) {
    if (fitsHeight(size)) return { size, lines: wrapLineCount(text, size) };
  }
  return { size: PUN_MIN_PX, lines: wrapLineCount(text, PUN_MIN_PX) };
};
