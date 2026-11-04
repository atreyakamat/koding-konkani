/**
 * Fix pass 4, item 4. Gives the EP43 search traces a current box on every step. The Bible's
 * "Compared" column names it ("a[3]=17 vs 26 ..."), so each step gets `compare: [i, i]` (a
 * one-index compare: the AlgorithmBars scene paints it butter) and the step that finds the value
 * ("yes" / "equal") also gets `sorted: [i]`, which paints that box mint. Only `trace` entries of
 * EP43 scenes 3 and 5 change; array values and step labels are checked against the Bible table.
 *
 * Usage: node scripts/add_search_highlights.mts [--write]   (dry run without --write)
 */
import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const WRITE = process.argv.includes("--write");

type Step = { step: string; array: number[]; compare?: [number, number]; sorted?: number[] };

const md = readFileSync(join(ROOT, "docs", "bible", "m06.md"), "utf-8").replace(/\r\n/g, "\n");
const section = md.split("### Step trace")[2]; // m06.md order: EP42, EP43, EP44 -> [1] is EP43 (split drops the head)
if (!section || !section.includes("Linear search:")) throw new Error("EP43 step-trace section not found");

const rowsAfter = (heading: string): string[][] => {
  const rows: string[][] = [];
  let seen = false;
  for (const line of section.slice(section.indexOf(heading)).split("\n")) {
    if (line.startsWith("|")) {
      seen = true;
      const cells = line.split("|").slice(1, -1).map((c) => c.trim().split("\\").join(""));
      if (!cells[0].startsWith("---") && cells[0] !== "Step") rows.push(cells);
    } else if (seen) break;
  }
  return rows;
};

/** step label -> { index, found } from the "Compared" column (third cell). */
const parse = (heading: string): Map<string, { index: number; found: boolean }> =>
  new Map(
    rowsAfter(heading).map((cells) => {
      const m = /a\[(\d+)\]/.exec(cells[2]);
      if (!m) throw new Error(`no a[i] in ${cells[2]}`);
      return [cells[0], { index: Number(m[1]), found: /\byes\b|\bequal\b/.test(cells[2]) }];
    }),
  );

const file = join(ROOT, "episodes", "ep043.json");
const data = JSON.parse(readFileSync(file, "utf-8")) as { scenes: { id: number; trace?: Step[] }[] };
for (const [sceneId, heading] of [[3, "Linear search:"], [5, "Binary search:"]] as const) {
  const scene = data.scenes.find((s) => s.id === sceneId);
  if (!scene?.trace) throw new Error(`ep43 scene ${sceneId} has no trace`);
  const info = parse(heading);
  if (info.size !== scene.trace.length) throw new Error(`scene ${sceneId}: step count differs`);
  scene.trace = scene.trace.map((step) => {
    const hit = info.get(step.step);
    if (!hit) throw new Error(`scene ${sceneId}: step ${step.step} missing in Bible`);
    const { index, found } = hit;
    return { step: step.step, array: step.array, compare: [index, index], ...(found ? { sorted: [index] } : {}) };
  });
  console.log(`scene ${sceneId}:`, scene.trace.map((s) => `${s.step}->${s.compare?.[0]}${s.sorted ? "*" : ""}`).join(" "));
}
if (WRITE) writeFileSync(file, (JSON.stringify(data, null, 2) + "\n").replace(/\n/g, "\r\n"), "utf-8");
console.log(WRITE ? "written" : "dry run (use --write)");
