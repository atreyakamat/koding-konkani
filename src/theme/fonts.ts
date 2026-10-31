import { loadFont as loadArchivoBlack } from "@remotion/google-fonts/ArchivoBlack";
import { loadFont as loadSpaceGrotesk } from "@remotion/google-fonts/SpaceGrotesk";
import { loadFont as loadJetBrainsMono } from "@remotion/google-fonts/JetBrainsMono";

const archivo = loadArchivoBlack("normal", { weights: ["400"], subsets: ["latin"] });
const grotesk = loadSpaceGrotesk("normal", { weights: ["500", "700"], subsets: ["latin"] });
const mono = loadJetBrainsMono("normal", { weights: ["500", "700"], subsets: ["latin"] });

/** Titles (all caps), body text, and code. */
export const fonts = {
  title: archivo.fontFamily,
  body: grotesk.fontFamily,
  code: mono.fontFamily,
} as const;
