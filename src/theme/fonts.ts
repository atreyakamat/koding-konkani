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

for (const { family, file, weight } of FILES) {
  void loadFont({ family, url: staticFile(`fonts/${file}`), weight, format: "woff2" });
}

/** Titles (all caps), body text, and code. */
export const fonts = {
  title: "Archivo Black",
  body: "Space Grotesk",
  code: "JetBrains Mono",
} as const;
