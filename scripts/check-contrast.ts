/**
 * Contrast audit for every module colourway (WCAG ratios). Run: npm run check:contrast
 * Exits non-zero if any text pairing used by the scene templates falls below its bar.
 */
import { palette, moduleColours, coloursForModule, contrastRatio, readableOn, accentOn } from "../src/theme";

type Check = { label: string; fg: string; bg: string; min: number };
const failures: string[] = [];
const row = (module: number, c: Check) => {
  const ratio = contrastRatio(c.fg, c.bg);
  const ok = ratio >= c.min;
  if (!ok) failures.push(`M${module} ${c.label}: ${ratio.toFixed(2)} < ${c.min}`);
  return ok;
};

moduleColours.forEach((_, m) => {
  const { bg, accent } = coloursForModule(m);
  const checks: Check[] = [
    { label: "body text on background", fg: readableOn(bg), bg, min: 4.5 },
    { label: "accent heading/stroke on background", fg: accentOn(bg, accent), bg, min: 3 },
    { label: "chip text on accent", fg: readableOn(accent), bg: accent, min: 4.5 },
    { label: "accent label on cream card", fg: accentOn(palette.cream, accent), bg: palette.cream, min: 3 },
    { label: "accent prompt on terminal", fg: accentOn(palette.darkBlue, accent), bg: palette.darkBlue, min: 3 },
  ];
  const ok = checks.map((c) => row(m, c)).every(Boolean);
  console.log(`M${String(m).padStart(2, "0")} ${ok ? "OK  " : "FAIL"}  bg ${bg}  accent ${accent}  text ${readableOn(bg)}`);
});

const fixed: Check[] = [
  { label: "ink on cream", fg: palette.ink, bg: palette.cream, min: 4.5 },
  { label: "ink on white", fg: palette.ink, bg: palette.white, min: 4.5 },
  { label: "ink on butter (stickers)", fg: palette.ink, bg: palette.butter, min: 4.5 },
  { label: "pun text on tomato", fg: readableOn(palette.tomato), bg: palette.tomato, min: 4.5 },
  { label: "terminal white on dark blue", fg: palette.white, bg: palette.darkBlue, min: 4.5 },
  { label: "terminal mint on dark blue", fg: palette.mint, bg: palette.darkBlue, min: 4.5 },
  { label: "terminal tomato on dark blue", fg: palette.tomato, bg: palette.darkBlue, min: 3 },
];
fixed.forEach((c) => row(-1, c));

if (failures.length) {
  console.error(`\n${failures.length} contrast failure(s):\n` + failures.join("\n"));
  process.exit(1);
}
console.log("\nAll contrast checks passed.");
