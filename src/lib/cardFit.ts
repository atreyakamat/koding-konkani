/** Fits the explanation-card text (CodeExplain) into the room the right column has left for it.
 *
 * The column has a fixed height. It holds the card, the tracker chips and, in scenes with program output, the output
 * panel (laid out from the first frame). Before fix pass 5 the card was a flex child with `minHeight: 160`, so when the
 * three did not fit, flexbox squeezed the card to 160px and its 44px text spilled over the tracker (EP42, EP45, EP49).
 * Now the card never shrinks: one size for the whole scene, the largest of 44 / 40 / 36 / 32 / 28px at which EVERY label
 * of the scene fits the budget; a label that still does not fit at 28px is cut to its first clause. */
export const CARD_SIZES = [44, 40, 36, 32, 28] as const;
const LINE_HEIGHT = 1.35;
/** Padding 32 + border 5 on both sides, top and bottom. */
export const CARD_CHROME = 74;
export const CARD_PADDING_X = 74;
export const CARD_MIN_HEIGHT = 160;
/** Space Grotesk, measured on EP42 at 44px: about 25px per character. */
const CHAR_EM = 0.57;
export const COLUMN_GAP = 24;

const rowsFor = (text: string, size: number, textWidth: number): number => {
  const perRow = Math.max(8, Math.floor(textWidth / (size * CHAR_EM)));
  let rows = 1;
  let cur = 0;
  for (const word of text.split(/\s+/).filter(Boolean)) {
    if (cur === 0) cur = word.length;
    else if (cur + 1 + word.length <= perRow) cur += 1 + word.length;
    else {
      rows++;
      cur = word.length;
    }
  }
  return rows;
};

/** Height of the card at `size` for this text, never below the minimum card. */
export const cardHeight = (text: string, size: number, columnWidth: number): number =>
  Math.max(CARD_MIN_HEIGHT, Math.ceil(rowsFor(text, size, columnWidth - CARD_PADDING_X) * size * LINE_HEIGHT) + CARD_CHROME);

/** The text up to its first clause break (comma, colon or semicolon after at least 20 characters), else the first 90
 * characters at a word boundary; "…" marks the cut. */
export const firstClause = (text: string): string => {
  // The first break at least 20 characters in ("Line 13: switch, ..." breaks at the comma, not the early colon).
  const at = [...text.matchAll(/[,:;]\s/g)].map((m) => m.index ?? 0).find((i) => i >= 20);
  if (at !== undefined) return `${text.slice(0, at)}…`;
  if (text.length <= 90) return text;
  const cut = text.lastIndexOf(" ", 90);
  return `${text.slice(0, cut > 20 ? cut : 90)}…`;
};

export type FittedLabels = { size: number; labels: Record<number, string>; cut: number[] };

/** `budget` is the most height the card may take. */
export const fitLabels = (labels: Record<number, string>, budget: number, columnWidth: number): FittedLabels => {
  const entries = Object.entries(labels);
  const room = Math.max(CARD_MIN_HEIGHT, budget);
  const fitsAll = (size: number): boolean => entries.every(([, t]) => cardHeight(t, size, columnWidth) <= room);
  const size = CARD_SIZES.find(fitsAll);
  if (size !== undefined) return { size, labels, cut: [] };
  const smallest = CARD_SIZES[CARD_SIZES.length - 1];
  const out: Record<number, string> = {};
  const cut: number[] = [];
  for (const [key, text] of entries) {
    let t = text;
    if (cardHeight(t, smallest, columnWidth) > room) {
      t = firstClause(t);
      // Still too tall: drop words from the end until it fits.
      const words = t.replace(/…$/, "").split(/\s+/);
      while (words.length > 4 && cardHeight(`${words.join(" ")}…`, smallest, columnWidth) > room) words.pop();
      if (cardHeight(t, smallest, columnWidth) > room) t = `${words.join(" ")}…`;
      cut.push(Number(key));
    }
    out[Number(key)] = t;
  }
  return { size: smallest, labels: out, cut };
};

/** Height of the tracker block (title + chips) for the widest tracked state; 0 when nothing is tracked. */
export const trackerHeight = (states: Record<string, string>[], columnWidth: number): number => {
  let rows = 0;
  for (const state of states) {
    const chips = Object.entries(state).map(([name, value]) => `${name} = ${value}`.length * 15.6 + 40);
    if (!chips.length) continue;
    let cur = 0;
    let r = 1;
    for (const w of chips) {
      if (cur === 0) cur = w;
      else if (cur + 12 + w <= columnWidth) cur += 12 + w;
      else {
        r++;
        cur = w;
      }
    }
    rows = Math.max(rows, r);
  }
  return rows === 0 ? 0 : 36 + rows * 57;
};
