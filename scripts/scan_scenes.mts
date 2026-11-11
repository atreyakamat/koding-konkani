/** Read-only scan of all 86 episodes: scenes per template, and scenes whose props are empty (blank MemoryBoxes, AlgorithmBars with no trace). Usage: node scripts/scan_scenes.mts */
import { readFileSync } from "node:fs";
import { scenePropsFor } from "../src/compositions/sceneProps.ts";
const tot: Record<string, number> = {};
const empty: Record<string, string[]> = {};
const mb = { with: 0, without: 0, withEps: new Set<number>(), withoutEps: new Set<number>() };
const mbRows: string[] = [];
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(`episodes/ep${String(n).padStart(3, "0")}.json`, "utf8"));
  for (const s of ep.scenes) {
    tot[s.template] = (tot[s.template] ?? 0) + 1;
    const p: any = scenePropsFor(ep, s);
    const emptyField =
      (s.template === "memory-boxes" && !(p.boxes?.length)) ? "boxes"
      : (s.template === "algorithm-bars" && !(p.trace?.length)) ? "trace"
      : (s.template === "terminal" && !(p.lines?.length)) ? "lines"
      : (s.template === "concept-slide" && !(p.lines?.length ?? p.points?.length ?? 1)) ? "lines" : "";
    if (s.template === "memory-boxes") {
      if (p.boxes?.length) { mb.with++; mb.withEps.add(n); } else { mb.without++; mb.withoutEps.add(n); }
      mbRows.push(`EP${n}s${s.id}:${p.boxes?.length ?? 0}`);
    }
    if (emptyField) (empty[`${s.template}.${emptyField}`] ??= []).push(`EP${n}s${s.id}`);
  }
}
console.log("scenes per template:", JSON.stringify(tot));
console.log(`memory-boxes scenes: ${mb.with + mb.without} total, ${mb.with} with boxes, ${mb.without} WITHOUT (blank)`);
console.log("episodes with a blank memory-boxes scene:", [...mb.withoutEps].sort((a, b) => a - b).join(","));
console.log("episodes where memory-boxes scenes have data:", [...mb.withEps].sort((a, b) => a - b).join(","));
for (const [k, v] of Object.entries(empty)) console.log(`empty ${k}: ${v.length}`);
console.log(mbRows.join(" "));
