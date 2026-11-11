/**
 * Renders one still per scene (ScenePreview, no narration) for a range of episodes with ONE bundle and ONE browser,
 * so a whole course can be checked in minutes. Usage:
 *   KK_COURSE=python node scripts/stills_all.mts <fromEp> <toEp> [fraction=0.85] [scale=0.5]
 * Output: out/stills-<course>/epNNN-sM-<template>.png, plus out/stills-<course>/errors.txt for any scene that failed.
 * Set KK_BROWSER to a Chrome/Chromium executable if Remotion's own headless shell is not installed.
 */
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { bundle } from "@remotion/bundler";
import { openBrowser, renderStill, selectComposition } from "@remotion/renderer";
import { COURSE, episodeJsonPath } from "./lib/course.mts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const [fromArg = "1", toArg = fromArg, fracArg = "0.85", scaleArg = "0.5"] = process.argv.slice(2);
const from = Number(fromArg);
const to = Number(toArg);
const frac = Number(fracArg);
const scale = Number(scaleArg);
const outDir = join(ROOT, "out", `stills-${COURSE}`);
mkdirSync(outDir, { recursive: true });

const browserExecutable = process.env.KK_BROWSER ?? null;
const serveUrl = await bundle({
  entryPoint: join(ROOT, "src/index.ts"),
  publicDir: join(ROOT, "audio"),
});
const browser = await openBrowser("chrome", {
  browserExecutable,
  chromiumOptions: { gl: "swangle" },
});

const errors: string[] = [];
let done = 0;
for (let n = from; n <= to; n++) {
  const epId = `ep${String(n).padStart(3, "0")}`;
  const episode = JSON.parse(readFileSync(episodeJsonPath(ROOT, epId), "utf-8"));
  for (const scene of episode.scenes as { id: number; template: string; lengthSec: number }[]) {
    const inputProps = { episode, sceneId: scene.id };
    const png = join(outDir, `${epId}-s${scene.id}-${scene.template}.png`);
    try {
      const composition = await selectComposition({
        serveUrl,
        id: "ScenePreview",
        inputProps,
        puppeteerInstance: browser,
      });
      const length = Math.round(scene.lengthSec * 30);
      await renderStill({
        composition: { ...composition, durationInFrames: length },
        serveUrl,
        output: png,
        frame: Math.min(length - 1, Math.round(length * frac)),
        inputProps,
        scale,
        puppeteerInstance: browser,
        timeoutInMS: 120000,
      });
      done++;
    } catch (e) {
      errors.push(
        `${epId} scene ${scene.id} [${scene.template}]: ${(e as Error).message.split("\n")[0]}`,
      );
    }
  }
  console.log(`${epId} done`);
}
await browser.close({ silent: true });
writeFileSync(join(outDir, "errors.txt"), errors.join("\n") + (errors.length ? "\n" : ""));
console.log(
  `${done} stills rendered, ${errors.length} errors${errors.length ? " (see errors.txt)" : ""}`,
);
process.exit(errors.length ? 1 : 0);
