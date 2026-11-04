/**
 * Adds ONLY the `trace` field to the algorithm-bars scenes of EP42, EP43 and EP44 in
 * episodes/epNNN.json, from the "### Step trace" tables in docs/bible/m06.md. Nothing else in
 * the JSON is touched (the file's CRLF line endings and 2-space layout are kept).
 *
 * Sections, in m06.md order (EP43 has two tables): EP42 scene 4 (max/min), EP43 scene 3 (linear search), EP43 scene 5
 * (binary search), EP44 scene 1 (one bubble pass). Search tables have no compare pair, so those
 * steps carry no `compare` (there is no current-box highlight; flagged, not fixed).
 *
 * Usage: node scripts/add_step_traces.mts [--write]   (dry run without --write)
 */
import { readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const WRITE = process.argv.includes("--write");

type Step = {
  step: string;
  array: number[];
  compare?: [number, number];
  swap?: [number, number];
};

const md = readFileSync(join(ROOT, "docs", "bible", "m06.md"), "utf-8").replace(/\r\n/g, "\n");
const sections = md.split("### Step trace").slice(1);
if (sections.length < 3)
  throw new Error(`expected 3 step-trace sections (EP42, EP43, EP44), found ${sections.length}`);

/** Table rows of the first table after `heading` (or the first table when no heading). */
const rowsAfter = (section: string, heading?: string): string[][] => {
  const start = heading ? section.indexOf(heading) : 0;
  if (start < 0) throw new Error(`heading ${heading} not found`);
  const rows: string[][] = [];
  let seen = false;
  for (const line of section.slice(start).split("\n")) {
    if (line.startsWith("|")) {
      seen = true;
      const cells = line
        .split("|")
        .slice(1, -1)
        .map((c) => c.trim());
      if (!cells[0].startsWith("---") && cells[0] !== "Step") rows.push(cells);
    } else if (seen) break;
  }
  return rows;
};

const numbers = (text: string): number[] => [...text.matchAll(/-?\d+/g)].map((m) => Number(m[0]));
const unescape = (text: string): string => text.split("\\").join("");
const headerArray = (section: string): number[] => {
  const m = /Array `\{([^}]*)\}`/.exec(section);
  if (!m) throw new Error("array header not found");
  return numbers(m[1]);
};

/** EP42 and EP44: one comparison per step, "a[i]=x OP a[j]=y ...". */
const pairTrace = (section: string): Step[] =>
  rowsAfter(section).map((cells) => {
    const [step, state, compared, swapped] = cells.map(unescape);
    const array = numbers(state);
    const idx = [...compared.matchAll(/a\[(\d+)\]/g)].map((m) => Number(m[1]));
    const out: Step = { step, array };
    if (idx.length === 2) out.compare = [idx[0], idx[1]];
    if (out.compare && /↔/.test(swapped)) out.swap = out.compare;
    return out;
  });

/** EP43: array never changes; no compare pair in the Bible tables. */
const searchTrace = (section: string, heading: string | undefined): Step[] => {
  const array = headerArray(section);
  return rowsAfter(section, heading).map((cells) => ({ step: cells[0], array }));
};

const plan: { ep: number; scene: number; trace: Step[] }[] = [
  { ep: 42, scene: 4, trace: pairTrace(sections[0]) },
  { ep: 43, scene: 3, trace: searchTrace(sections[1], "Linear search:") },
  { ep: 43, scene: 5, trace: searchTrace(sections[1], "Binary search:") },
  { ep: 44, scene: 1, trace: pairTrace(sections[2]) },
];

for (const ep of [42, 43, 44]) {
  const file = join(ROOT, "episodes", `ep0${ep}.json`);
  const raw = readFileSync(file, "utf-8");
  const data = JSON.parse(raw) as { scenes: { id: number; template: string; trace?: Step[] }[] };
  for (const item of plan.filter((p) => p.ep === ep)) {
    const scene = data.scenes.find((s) => s.id === item.scene);
    if (!scene || scene.template !== "algorithm-bars") {
      throw new Error(`ep${ep} scene ${item.scene} is not an algorithm-bars scene`);
    }
    scene.trace = item.trace;
    console.log(`ep${ep} scene ${item.scene}: ${item.trace.length} steps`);
  }
  if (WRITE) {
    writeFileSync(file, (JSON.stringify(data, null, 2) + "\n").replace(/\n/g, "\r\n"), "utf-8");
  }
}
console.log(WRITE ? "written" : "dry run (use --write)");
