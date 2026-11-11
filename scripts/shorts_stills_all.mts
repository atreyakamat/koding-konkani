/**
 * One still per Short (S1-S5) of each episode in a range, with ONE bundle and ONE browser. Needs the episode's narration
 * folder (real or scripts/placeholder_audio.py) because Short's calculateMetadata reads its manifest and captions.
 *   KK_COURSE=python node scripts/shorts_stills_all.mts <fromEp> <toEp> [fraction=0.6] [scale=0.4]
 * Output: out/shorts-stills-<course>/epNNN-S1.png ..., errors in errors.txt.
 */
import { mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { bundle } from "@remotion/bundler";
import { openBrowser, renderStill, selectComposition } from "@remotion/renderer";
import { COURSE } from "./lib/course.mts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const [fromArg = "1", toArg = fromArg, fracArg = "0.6", scaleArg = "0.4"] = process.argv.slice(2);
const outDir = join(ROOT, "out", `shorts-stills-${COURSE}`);
mkdirSync(outDir, { recursive: true });

const serveUrl = await bundle({
  entryPoint: join(ROOT, "src/index.ts"),
  publicDir: join(ROOT, "audio"),
});
const browser = await openBrowser("chrome", {
  browserExecutable: process.env.KK_BROWSER ?? null,
  chromiumOptions: { gl: "swangle" },
});

const errors: string[] = [];
let done = 0;
for (let n = Number(fromArg); n <= Number(toArg); n++) {
  for (const shortId of ["S1", "S2", "S3", "S4", "S5"]) {
    const inputProps = { episodeNumber: n, shortId, lang: COURSE };
    try {
      const composition = await selectComposition({
        serveUrl,
        id: `Short-${shortId}`,
        inputProps,
        puppeteerInstance: browser,
      });
      await renderStill({
        composition,
        serveUrl,
        output: join(outDir, `ep${String(n).padStart(3, "0")}-${shortId}.png`),
        frame: Math.round((composition.durationInFrames - 1) * Number(fracArg)),
        inputProps,
        scale: Number(scaleArg),
        puppeteerInstance: browser,
        timeoutInMS: 120000,
      });
      done++;
    } catch (e) {
      errors.push(`ep${n} ${shortId}: ${(e as Error).message.split("\n")[0]}`);
    }
  }
  console.log(`ep${n} done`);
}
await browser.close({ silent: true });
writeFileSync(join(outDir, "errors.txt"), errors.join("\n") + (errors.length ? "\n" : ""));
console.log(
  `${done} Short stills rendered, ${errors.length} errors${errors.length ? " (see errors.txt)" : ""}`,
);
process.exit(errors.length ? 1 : 0);
