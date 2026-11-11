/**
 * Fails (exit 1) if two Shorts in one episode would show the same visual, and prints each
 * Short's derived visual kind so the choices can be reviewed. Run by the render queues
 * before an episode is rendered.
 *
 * Usage: node scripts/check_short_visuals.mts [episode-number...]   (default: every episode)
 */
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { deriveShortVisuals, findDuplicateVisuals, signature } from "../src/lib/shortVisual.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const dir = join(ROOT, "episodes");
const wanted = process.argv.slice(2).map(Number);
const files = readdirSync(dir)
  .filter((f) => /^ep\d{3}\.json$/.test(f))
  .filter((f) => wanted.length === 0 || wanted.includes(Number(f.slice(2, 5))));

let failed = false;
for (const file of files) {
  const episode = JSON.parse(readFileSync(join(dir, file), "utf-8"));
  const visuals = deriveShortVisuals(episode);
  const summary = ["S1", "S2", "S3", "S4", "S5"]
    .map((id) => `${id}:${visuals[id]?.kind ?? "MISSING"}`)
    .join(" ");
  const dupes = findDuplicateVisuals(episode);
  const generic = Object.entries(visuals).filter(([, v]) => signature(v) === 'code:printf("Hi");');
  if (dupes.length || generic.length) {
    failed = true;
    for (const [ep, a, b] of dupes)
      console.error(`FAIL ep${ep}: ${a} and ${b} show the same visual`);
    for (const [id] of generic) console.error(`FAIL ${file} ${id}: generic printf("Hi"); visual`);
  }
  console.log(`${file.slice(0, 5)} ${summary}`);
}
process.exit(failed ? 1 : 0);
