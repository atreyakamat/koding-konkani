/**
 * Renders review stills (no narration needed) of every scene that apply_boxes_52_83.py filled:
 * the 40 memory-boxes scenes of EP52-83 (one still per frame of the scene, taken in the middle of each frame)
 * plus the three bars scenes EP77 s4 and EP81 s4 (5 stills each).
 * Output: out/stills-ep52-83/  (git-ignored). Calls scripts/preview_stills.mts once per episode.
 * Usage: node scripts/stills_new_scenes.mts [fromEp] [toEp]      (default 52 83)
 */
import { spawnSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const from = Number(process.argv[2] ?? 52);
const to = Number(process.argv[3] ?? 83);
const draft = JSON.parse(readFileSync(join(ROOT, "docs", "fix4", "boxes-draft-ep52-83.json"), "utf-8")) as Record<string, { frames: unknown[] }>;

const specs = new Map<number, string[]>();
const add = (ep: number, scene: number, fractions: number[]): void => {
  const list = specs.get(ep) ?? [];
  list.push(`${scene}@${fractions.map((f) => f.toFixed(2)).join(",")}`);
  specs.set(ep, list);
};
for (const [key, mem] of Object.entries(draft)) {
  const [ep, scene] = key.split(".").map(Number);
  const k = mem.frames.length;
  add(ep, scene, Array.from({ length: k }, (_, i) => (i + 0.5) / k));
}
add(77, 4, [0.1, 0.3, 0.5, 0.7, 0.95]);
add(81, 4, [0.1, 0.3, 0.5, 0.7, 0.95]);

for (const ep of [...specs.keys()].sort((a, b) => a - b)) {
  if (ep < from || ep > to) continue;
  const args = ["scripts/preview_stills.mts", String(ep), ...(specs.get(ep) ?? [])];
  console.log(`EP${ep}: node ${args.join(" ")}`);
  const r = spawnSync(process.execPath, args, {
    cwd: ROOT,
    stdio: "inherit",
    env: { ...process.env, STILL_OUT: "out/stills-ep52-83", STILL_SCALE: "0.5" },
  });
  if (r.status !== 0) {
    console.error(`EP${ep}: preview_stills failed (exit ${r.status})`);
    process.exit(r.status ?? 1);
  }
}
console.log("stills written to out/stills-ep52-83/");
