/**
 * Preflight gate: an episode whose scenes would render blank or crash must not be rendered.
 *  - memory-boxes with no `boxes`  -> the scene draws nothing (EP37-83 before fix pass 5);
 *  - algorithm-bars with no `trace` -> the component throws and the whole render fails.
 * Prints every offending scene and exits 1 if any episode in the range has one.
 * Called by scripts/overnight.ps1 (prints the list up front) and by scripts/episode_pipeline.mts (skips the episode).
 * Usage: node scripts/check_scenes.mts [from] [to]   (default 1 86)
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");

export type SceneProblem = { ep: number; scene: number; template: string; problem: string };

export const sceneProblems = (ep: number): SceneProblem[] => {
  const episode = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(ep).padStart(3, "0")}.json`), "utf-8"));
  const out: SceneProblem[] = [];
  for (const s of episode.scenes as { id: number; template: string; boxes?: unknown[]; trace?: unknown[] }[]) {
    if (s.template === "memory-boxes" && !(s.boxes && s.boxes.length))
      out.push({ ep, scene: s.id, template: s.template, problem: "no boxes: the scene would render blank" });
    if (s.template === "algorithm-bars" && !(s.trace && s.trace.length))
      out.push({ ep, scene: s.id, template: s.template, problem: "no trace: the scene would crash the render" });
  }
  return out;
};

if (process.argv[1]?.endsWith("check_scenes.mts")) {
  const from = Number(process.argv[2] ?? 1);
  const to = Number(process.argv[3] ?? 86);
  const bad: SceneProblem[] = [];
  for (let ep = from; ep <= to; ep++) bad.push(...sceneProblems(ep));
  const eps = [...new Set(bad.map((b) => b.ep))];
  if (bad.length === 0) {
    console.log(`check_scenes: EP${from}-EP${to}: every memory-boxes and algorithm-bars scene has data.`);
  } else {
    console.log(`check_scenes: ${bad.length} scene(s) in ${eps.length} episode(s) of EP${from}-EP${to} have no data; those episodes will not be rendered:`);
    for (const b of bad) console.log(`  EP${String(b.ep).padStart(2, "0")} scene ${b.scene} [${b.template}]: ${b.problem}`);
  }
  process.exit(bad.length ? 1 : 0);
}
