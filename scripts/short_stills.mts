/**
 * One still per requested Short and time, one at a time (STILL_OUT dir under the repo, STILL_SCALE; 0.5 = 540x960).
 * Usage: node scripts/short_stills.mts <episode> <S1..S5>[@fraction,fraction,...] ...
 *   e.g. node scripts/short_stills.mts 44 S1@0.1,0.5,0.9 S2
 * Refreshes audio/voice/<ep>/episode.json from episodes/ like render_queue does.
 */
import { copyFileSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { execSync } from "node:child_process";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const FPS = 30;
const [epArg, ...specs] = process.argv.slice(2);
const ep = Number(epArg);
const epId = `ep${String(ep).padStart(3, "0")}`;
const voice = join(ROOT, "audio", "voice", epId);
copyFileSync(join(ROOT, "episodes", `${epId}.json`), join(voice, "episode.json"));
const manifest = JSON.parse(readFileSync(join(voice, "manifest.json"), "utf-8"));
const outDir = join(ROOT, process.env.STILL_OUT ?? "out/stills-shorts");
const scale = process.env.STILL_SCALE ?? "0.5";
mkdirSync(outDir, { recursive: true });
const propsFile = join(outDir, `${epId}.short.props.json`);

for (const spec of specs) {
  const [id, fracs = "0.5"] = spec.split("@");
  const sec = manifest.timings.find((t: { short?: string }) => t.short === id)?.durationSec;
  if (!sec) throw new Error(`no timing for ${id} in ${epId} manifest`);
  writeFileSync(propsFile, JSON.stringify({ episodeNumber: ep, shortId: id }));
  for (const frac of fracs.split(",")) {
    const at = Math.min(Math.round(sec * FPS) - 1, Math.round(sec * FPS * Number(frac)));
    const png = join(outDir, `${epId}-${id}-${frac}.png`);
    execSync(
      `npx remotion still src/index.ts Short-${id} "${png}" --frame=${at} --props="${propsFile}" --scale=${scale} --timeout=120000`,
      { cwd: ROOT, stdio: "inherit" },
    );
    console.log(png);
  }
}
