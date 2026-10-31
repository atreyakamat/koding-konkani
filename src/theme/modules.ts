import { palette, type ColourName } from "./palette";

export type ModuleColours = { bg: ColourName; accent: ColourName };

/** Colour pair (background + accent) for each of the 14 modules, M0 to M13. */
export const moduleColours: readonly ModuleColours[] = [
  { bg: "peach", accent: "tomato" }, // M0 Welcome & setup
  { bg: "pastelBlue", accent: "tomato" }, // M1 Basics
  { bg: "cream", accent: "apricot" }, // M2 Operators
  { bg: "mint", accent: "darkBlue" }, // M3 Decisions
  { bg: "butter", accent: "darkBlue" }, // M4 Loops
  { bg: "lilac", accent: "tomato" }, // M5 Functions
  { bg: "peach", accent: "darkBlue" }, // M6 Arrays
  { bg: "pastelBlue", accent: "apricot" }, // M7 Strings
  { bg: "lilac", accent: "darkBlue" }, // M8 Pointers
  { bg: "cream", accent: "tomato" }, // M9 Structures
  { bg: "mint", accent: "tomato" }, // M10 Dynamic memory
  { bg: "apricot", accent: "darkBlue" }, // M11 Files
  { bg: "darkBlue", accent: "butter" }, // M12 Algorithms (bars: mint / tomato / pastelBlue)
  { bg: "peach", accent: "lilac" }, // M13 Projects & finale
];

/** Bar colours used by the AlgorithmBars scene in Module 12. */
export const algorithmBarColours = {
  sorted: palette.mint,
  swap: palette.tomato,
  idle: palette.pastelBlue,
  compare: palette.butter,
} as const;

export const coloursForModule = (module: number): { bg: string; accent: string } => {
  const pair = moduleColours[module];
  if (!pair) {
    throw new Error(`Unknown module ${module}; expected 0 to ${moduleColours.length - 1}`);
  }
  return { bg: palette[pair.bg], accent: palette[pair.accent] };
};
