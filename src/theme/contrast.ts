import { palette } from "./palette";

const channel = (v: number): number => {
  const s = v / 255;
  return s <= 0.03928 ? s / 12.92 : Math.pow((s + 0.055) / 1.055, 2.4);
};

/** WCAG relative luminance of a #RRGGBB colour. */
export const luminance = (hex: string): number => {
  const n = parseInt(hex.slice(1), 16);
  return (
    0.2126 * channel((n >> 16) & 255) + 0.7152 * channel((n >> 8) & 255) + 0.0722 * channel(n & 255)
  );
};

/** WCAG contrast ratio between two #RRGGBB colours (1 to 21). */
export const contrastRatio = (a: string, b: string): number => {
  const [hi, lo] = [luminance(a), luminance(b)].sort((x, y) => y - x);
  return (hi + 0.05) / (lo + 0.05);
};

/** Ink or white, whichever reads better on `bg`. Use for any text that sits on a coloured block. */
export const readableOn = (bg: string): string =>
  contrastRatio(palette.ink, bg) >= contrastRatio(palette.white, bg) ? palette.ink : palette.white;

/**
 * The accent colour when it is readable on `bg` (at least 3:1, the WCAG bar for large text, which
 * all our accent text is), otherwise ink or white. Use for headings, labels and strokes in accent.
 */
export const accentOn = (bg: string, accent: string): string =>
  contrastRatio(accent, bg) >= 3 ? accent : readableOn(bg);
