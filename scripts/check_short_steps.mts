/**
 * Lists every Short whose boxes visual steps through several memory frames, with the second each frame starts, and flags
 * a Short whose last frame appears too late (less than HOLD_SEC before the end card) or whose frames stack up.
 * Usage: node scripts/check_short_steps.mts [startEp endEp]   (needs audio/voice/epNNN/*.captions.json and manifest.json)
 */
import { existsSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { frameStarts } from "../src/lib/shortFrames.ts";
import { deriveShortVisuals } from "../src/lib/shortVisual.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const FPS = 30;
const END_CARD = 66;
const HOLD_SEC = 2;
const [a = "1", b = "86"] = process.argv.slice(2);
let bad = 0;
for (let ep = Number(a); ep <= Number(b); ep++) {
  const id = `ep${String(ep).padStart(3, "0")}`;
  const voice = join(ROOT, "audio", "voice", id);
  if (!existsSync(join(voice, "manifest.json"))) continue;
  const episode = JSON.parse(readFileSync(join(ROOT, "episodes", `${id}.json`), "utf-8"));
  const manifest = JSON.parse(readFileSync(join(voice, "manifest.json"), "utf-8"));
  for (const short of episode.shorts) {
    const visual = deriveShortVisuals(episode)[short.id];
    if (!visual || visual.kind !== "boxes" || !visual.frames) continue;
    const sec = manifest.timings.find((t: { short?: string }) => t.short === short.id)?.durationSec;
    const words = JSON.parse(readFileSync(join(voice, `${short.id}.captions.json`), "utf-8"));
    const dur = Math.round(sec * FPS);
    const starts = frameStarts(visual.frames.map((f) => f.label), words, FPS, dur);
    const last = starts[starts.length - 1];
    const left = (dur - END_CARD - last) / FPS;
    const flag = left < HOLD_SEC ? "  <-- LATE" : "";
    if (flag) bad++;
    console.log(`${id} ${short.id}: ${starts.map((s) => (s / FPS).toFixed(1)).join(" ")} | end card at ${((dur - END_CARD) / FPS).toFixed(1)}s, last frame held ${left.toFixed(1)}s${flag}`);
  }
}
console.log(bad ? `${bad} LATE` : "none late");
