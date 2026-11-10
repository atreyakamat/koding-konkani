/**
 * Read-only scan: episodes with more Bug-of-the-Day scenes than bug records (episodes/epNNN.json has one `bug` record
 * unless a scene carries its own `bug`). Also counts the "Bug of the Day" rows in the Bible's scene tables and the
 * "Bonus bug" blocks, so a second bug that never reached the JSON is found.
 * Usage: node scripts/scan_bug_records.mts
 */
import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
// Bible rows per episode: scene-table rows whose template is "Bug of the Day", and "Bonus bug" blocks.
const bible: Record<number, { rows: number; bonus: number }> = {};
for (const f of readdirSync(join(ROOT, "docs", "bible")).filter((x) => /^m\d+\.md$/.test(x))) {
  const text = readFileSync(join(ROOT, "docs", "bible", f), "utf-8").split("\n");
  let ep = 0;
  for (const line of text) {
    const h = /^## EP (\d+)\b/.exec(line);
    if (h) {
      ep = Number(h[1]);
      bible[ep] = { rows: 0, bonus: 0 };
      continue;
    }
    if (!ep) continue;
    if (/^\|\s*\d+\s*\|[^|]*\|[^|]*\|\s*Bug of the Day\s*\|/.test(line)) bible[ep].rows++;
    if (/Bonus bug/i.test(line) && /^\*\*Bonus bug/.test(line)) bible[ep].bonus++;
  }
}
const problems: string[] = [];
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  const scenes = (ep.scenes as { id: number; template: string; bug?: unknown }[]).filter((s) => s.template === "bug-of-the-day");
  const own = scenes.filter((s) => s.bug).length;
  const records = 1 + own; // the episode record serves the scenes that carry none
  const b = bible[n] ?? { rows: 0, bonus: 0 };
  const uncovered = scenes.length - (scenes.length > 0 ? 1 : 0) - own;
  if (uncovered > 0 || scenes.length !== b.rows || b.bonus > own)
    problems.push(`EP${n}: ${scenes.length} bug scene(s) [${scenes.map((s) => s.id).join(",")}], ${records} record(s) (episode + ${own} own), Bible rows ${b.rows}, bonus blocks ${b.bonus}${uncovered > 0 ? "  <-- scene without its own bug data" : ""}`);
}
console.log(problems.length ? problems.join("\n") : "every bug scene has its own record, and the counts match the Bible");
process.exit(problems.length ? 1 : 0);
