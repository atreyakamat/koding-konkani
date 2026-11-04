/** Pure layout for monospace code panels: wraps source lines into whole rows so a line is
 * never clipped or cut in half, and picks the largest font that fits the free space.
 * JetBrains Mono advances 0.6em per character. */

export const CHAR_EM = 0.6;
export const GUTTER_CH = 2.5;
export const GUTTER_GAP = 20;
export const PADDING_X = 28;
export const PADDING_Y = 20;
export const BORDER = 5;
/** Extra space under the last row so a descender or the shadow edge never touches the border. */
export const BOTTOM_EXTRA = 12;
export const LINE_HEIGHT = 1.5;
export const MIN_FONT = 40;
export const MAX_FONT = 60;

export type CodeRow = {
  /** 1-based source line this row belongs to. */
  line: number;
  /** True for the first row of a wrapped line (the only one that shows the line number). */
  first: boolean;
  text: string;
  /** Leading spaces added to a wrapped continuation row (not source characters). */
  hang: number;
};

export const rowHeightPx = (fontSize: number): number => Math.round(fontSize * LINE_HEIGHT);

export const chromePx = (): number => 2 * PADDING_Y + 2 * BORDER + BOTTOM_EXTRA;

/** Characters that fit on one row at `fontSize` inside a panel `width` px wide. */
export const charsPerRow = (width: number, fontSize: number, lineNumbers = true): number => {
  const gutter = lineNumbers ? GUTTER_GAP + GUTTER_CH * CHAR_EM * fontSize : 0;
  const text = width - 2 * PADDING_X - 2 * BORDER - gutter;
  return Math.max(8, Math.floor(text / (CHAR_EM * fontSize)));
};

const wrapLine = (text: string, limit: number): { text: string; hang: number }[] => {
  if (text.length <= limit) return [{ text, hang: 0 }];
  const indent = (text.match(/^\s*/)?.[0] ?? "").length;
  const hang = " ".repeat(Math.min(indent + 2, Math.floor(limit / 2)));
  const out: { text: string; hang: number }[] = [];
  let rest = text;
  let isFirst = true;
  while (rest.length > limit) {
    const room = isFirst ? limit : limit;
    let cut = rest.lastIndexOf(" ", room);
    if (cut <= (isFirst ? indent : hang.length) + 4) cut = room;
    else cut += 1;
    out.push({ text: rest.slice(0, cut), hang: isFirst ? 0 : hang.length });
    rest = hang + rest.slice(cut);
    isFirst = false;
  }
  out.push({ text: rest, hang: hang.length });
  return out;
};

export const layoutRows = (
  source: string,
  width: number,
  fontSize: number,
  lineNumbers = true,
): CodeRow[] => {
  const limit = charsPerRow(width, fontSize, lineNumbers);
  const rows: CodeRow[] = [];
  source.split("\n").forEach((text, i) => {
    wrapLine(text, limit).forEach((chunk, k) => {
      rows.push({ line: i + 1, first: k === 0, text: chunk.text, hang: chunk.hang });
    });
  });
  return rows;
};

/** Largest font in [MIN_FONT, MAX_FONT] (4px steps) whose layout has no wrapped lines and
 * fits `maxHeight`; failing that the largest that fits with wrapping; failing that
 * MIN_FONT (the panel then scrolls by whole rows). */
export const chooseFontSize = (
  source: string,
  width: number,
  maxHeight: number,
  maxFont: number = MAX_FONT,
  lineNumbers = true,
): number => {
  const fonts: number[] = [];
  for (let f = maxFont; f >= MIN_FONT; f -= 4) fonts.push(f);
  const lineCount = source.split("\n").length;
  const fits = (f: number, allowWrap: boolean): boolean => {
    const rows = layoutRows(source, width, f, lineNumbers);
    if (!allowWrap && rows.length > lineCount) return false;
    return rows.length * rowHeightPx(f) + chromePx() <= maxHeight;
  };
  return fonts.find((f) => fits(f, false)) ?? fonts.find((f) => fits(f, true)) ?? MIN_FONT;
};
