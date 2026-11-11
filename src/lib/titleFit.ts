import { wrapLineCount } from "./punFit.ts";

/** Layout for the TitleCard headline. Xecxec stands bottom-right (about 520px wide, top edge near
 * y = 610), so the title block (text + underline) has to end above that. The size steps down
 * until the wrapped, uppercase title fits the box. */
export const TITLE_BOX = { width: 1555, height: 360 } as const;
export const TITLE_MAX_PX = 128;
export const TITLE_MIN_PX = 72;
export const TITLE_LINE_HEIGHT = 1.05;
/** Archivo Black capitals plus the 10px outline average ~0.78em per character. */
const CAPS_EM = 0.78;

export type TitleFit = { size: number; lines: number };

export const fitTitle = (title: string): TitleFit => {
  const lines = (size: number): number => wrapLineCount(title, size, TITLE_BOX.width, CAPS_EM);
  for (let size = TITLE_MAX_PX; size >= TITLE_MIN_PX; size -= 8) {
    if (lines(size) * size * TITLE_LINE_HEIGHT <= TITLE_BOX.height) return { size, lines: lines(size) };
  }
  return { size: TITLE_MIN_PX, lines: lines(TITLE_MIN_PX) };
};
