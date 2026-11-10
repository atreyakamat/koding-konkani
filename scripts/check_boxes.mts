/**
 * Checks every `memory` scene (MemoryBoxes frames) without rendering: zod schema, every arrow names an existing group
 * and cell, and the pure layout (src/lib/memoryLayout.ts) fits every frame inside the free band at a readable cell width
 * with the groups inside the band. Prints the cell width and frame count per scene. Exits 1 on any problem.
 * Usage: node scripts/check_boxes.mts [from] [to]   (default 1 86)
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { MemoryDataSchema } from "../src/lib/memory.ts";
import { BAND, layoutFrame } from "../src/lib/memoryLayout.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const from = Number(process.argv[2] ?? 1);
const to = Number(process.argv[3] ?? 86);
/** Narrowest cell that still shows a value, an address-less index and a 26px index label. */
const MIN_READABLE = 96;

const problems: string[] = [];
let scenes = 0;
for (let n = from; n <= to; n++) {
  const ep = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  for (const s of ep.scenes as { id: number; memory?: unknown }[]) {
    if (!s.memory) continue;
    scenes++;
    const tag = `EP${n} s${s.id}`;
    const parsed = MemoryDataSchema.safeParse(s.memory);
    if (!parsed.success) {
      problems.push(`${tag}: schema: ${parsed.error.issues.map((i) => `${i.path.join(".")} ${i.message}`).join("; ")}`);
      continue;
    }
    let narrowest = Infinity;
    parsed.data.frames.forEach((frame, k) => {
      const layout = layoutFrame(frame);
      narrowest = Math.min(narrowest, layout.cellWidth);
      if (!layout.fits) problems.push(`${tag} frame ${k}: does not fit the free band even at the smallest cell`);
      if (layout.cellWidth < MIN_READABLE) problems.push(`${tag} frame ${k}: cell width ${layout.cellWidth}px is below ${MIN_READABLE}px`);
      for (const g of layout.groups) {
        if (g.x < BAND.x - 1 || g.x + g.width > BAND.x + BAND.width + 1 || g.y < BAND.top - 1 || g.y + g.height > BAND.bottom + 1)
          problems.push(`${tag} frame ${k}: a group leaves the free band`);
      }
      for (const a of frame.arrows ?? []) {
        for (const ref of [a.from, a.to]) {
          const [gi, ci] = ref.split(":").map(Number);
          if (!frame.groups[gi]?.cells[ci]) problems.push(`${tag} frame ${k}: arrow ${ref} names a cell that does not exist`);
        }
      }
      if (frame.joiners && frame.joiners.length !== frame.groups.length - 1)
        problems.push(`${tag} frame ${k}: ${frame.joiners.length} joiners for ${frame.groups.length} groups`);
    });
    console.log(`${tag}: ${parsed.data.frames.length} frame(s), narrowest cell ${narrowest}px`);
  }
}
console.log(problems.length ? `PROBLEMS (${problems.length}):\n- ${problems.join("\n- ")}` : `check_boxes: ${scenes} memory scene(s) OK`);
process.exit(problems.length ? 1 : 0);
