import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

/** Self-hosted: the woff2 files live in audio/fonts/ (the Remotion public dir, licences in
 * audio/fonts/LICENSES.md). Nothing is fetched from the network at render time — a DNS blip
 * to fonts.gstatic.com failed a whole batch of renders on 1 Nov 2026. The two body faces are
 * variable fonts, so one file covers both weights. */
const FILES = [
  { family: "Archivo Black", file: "ArchivoBlack-Regular.woff2", weight: "400" },
  { family: "Space Grotesk", file: "SpaceGrotesk-Variable.woff2", weight: "300 700" },
  { family: "JetBrains Mono", file: "JetBrainsMono-Variable.woff2", weight: "100 800" },
] as const;

/** C has no ligature operators: JetBrains Mono would draw "<=" as one "less-or-equal" glyph and "!=" as "not equal",
 * and students copy what they see. Ligatures and contextual alternates are switched off for every face (the font-face
 * descriptor) and for every element and SVG text in the composition (the global rule below), so no code panel,
 * terminal, tracker chip or Short can show them. */
export const NO_LIGATURES = {
  fontVariantLigatures: "none",
  fontFeatureSettings: '"liga" 0, "calt" 0',
} as const;

for (const { family, file, weight } of FILES) {
  void loadFont({ family, url: staticFile(`fonts/${file}`), weight, format: "woff2", featureSettings: NO_LIGATURES.fontFeatureSettings });
}

if (typeof document !== "undefined") {
  const style = document.createElement("style");
  style.setAttribute("data-no-ligatures", "");
  style.textContent = `*, *::before, *::after { font-variant-ligatures: none; font-feature-settings: "liga" 0, "calt" 0; }`;
  document.head.appendChild(style);
}

/** Titles (all caps), body text, and code. */
export const fonts = {
  title: "Archivo Black",
  body: "Space Grotesk",
  code: "JetBrains Mono",
} as const;
