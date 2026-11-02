/**
 * Renders one 720p still per requested scene, one at a time, into out/stills720/.
 * Frame = scene start (from the narration manifest, minus the 12-frame transition overlaps,
 * as LongVideo lays them out) + fraction * scene length.
 *
 * Usage: node scripts/scene_stills.mts <episode> <template-or-id>[@fraction] ...
 *   e.g. node scripts/scene_stills.mts 15 pun-card@0.5 8@0.9
 */
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { execSync } from "node:child_process";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const FPS = 30;
const OVERLAP = 12;
const [epArg, ...specs] = process.argv.slice(2);
const ep = Number(epArg);
const epId = `ep${String(ep).padStart(3, "0")}`;
const voice = join(ROOT, "audio", "voice", epId);
const episode = JSON.parse(readFileSync(join(ROOT, "episodes", `${epId}.json`), "utf-8"));
const manifest = JSON.parse(readFileSync(join(voice, "manifest.json"), "utf-8"));

const starts = new Map<number, { start: number; length: number; template: string }>();
let frame = 0;
episode.scenes.forEach((scene: { id: number; template: string; lengthSec: number }, i: number) => {
  const sec = manifest.timings.find((t: { scene?: number }) => t.scene === scene.id)?.durationSec;
  const length = Math.round((sec ?? scene.lengthSec) * FPS);
  if (i > 0) frame -= OVERLAP;
  starts.set(scene.id, { start: Math.max(0, frame), length, template: scene.template });
  frame += length;
});

const outDir = join(ROOT, "out", "stills720");
mkdirSync(outDir, { recursive: true });
const propsFile = join(outDir, `${epId}.props.json`);
writeFileSync(propsFile, JSON.stringify({ episodeNumber: ep }));

for (const spec of specs) {
  const [what, frac = "0.5"] = spec.split("@");
  const targets = /^\d+$/.test(what)
    ? [[Number(what), starts.get(Number(what))] as const]
    : [...starts.entries()].filter(([, v]) => v.template === what);
  for (const [id, info] of targets) {
    if (!info) continue;
    const at = info.start + Math.min(info.length - 1, Math.round(info.length * Number(frac)));
    const png = join(outDir, `${epId}-scene${id}-${info.template}-${frac}.png`);
    execSync(
      `npx remotion still src/index.ts LongVideo "${png}" --frame=${at} --props="${propsFile}" --scale=0.6666666666666666 --timeout=120000`,
      { cwd: ROOT, stdio: "inherit" },
    );
    console.log(png);
  }
}
