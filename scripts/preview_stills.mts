/**
 * One still per frame of a scene, WITHOUT narration (episodes whose narration is not generated yet): the ScenePreview
 * composition shows the scene at its planned length (lengthSec). Nothing is written to audio/.
 * Usage: STILL_OUT=docs/fix4/x STILL_SCALE=0.5 node scripts/preview_stills.mts <episode> <sceneId>@<fraction>,<fraction> ...
 */
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { execSync } from "node:child_process";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const [epArg, ...specs] = process.argv.slice(2);
const epId = `ep${String(Number(epArg)).padStart(3, "0")}`;
const episode = JSON.parse(readFileSync(join(ROOT, "episodes", `${epId}.json`), "utf-8"));
const outDir = join(ROOT, process.env.STILL_OUT ?? "out/stills-preview");
const scale = process.env.STILL_SCALE ?? "0.5";
mkdirSync(outDir, { recursive: true });

for (const spec of specs) {
  const [idText, fracs = "0.5"] = spec.split("@");
  const id = Number(idText);
  const scene = episode.scenes.find((s: { id: number }) => s.id === id);
  if (!scene) throw new Error(`${epId} has no scene ${id}`);
  const propsFile = join(outDir, `${epId}-s${id}.preview.props.json`);
  writeFileSync(propsFile, JSON.stringify({ episode, sceneId: id }));
  const length = Math.round(scene.lengthSec * 30);
  for (const frac of fracs.split(",")) {
    const at = Math.min(length - 1, Math.round(length * Number(frac)));
    const png = join(outDir, `${epId}-scene${id}-${scene.template}-${frac}.png`);
    execSync(`npx remotion still src/index.ts ScenePreview "${png}" --frame=${at} --props="${propsFile}" --scale=${scale} --timeout=120000`, { cwd: ROOT, stdio: "inherit" });
    console.log(png);
  }
}
