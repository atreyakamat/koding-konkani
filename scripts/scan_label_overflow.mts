/**
 * Read-only scan of all 86 episodes: how the explanation-card fit (src/lib/cardFit.ts) lays out each
 * code-explain scene: font size per scene (44 -> 28px) and the labels that had to be cut to their first clause.
 * `--old` counts the scenes that overflowed under the old rule (card squeezed to 160px, text at 44px).
 * The room arithmetic mirrors CodeExplain (column height/width, tracker and output panel heights); it is an estimate.
 * Usage: node scripts/scan_label_overflow.mts [--old] [--cuts]
 */
import { readFileSync } from "node:fs";
import { scenePropsFor } from "../src/compositions/sceneProps.ts";
import { layoutOutput, outputPanelHeight, TAKEOVER_PANEL_WIDTH } from "../src/lib/outputFit.ts";
import { cardHeight, COLUMN_GAP, fitLabels, trackerHeight } from "../src/lib/cardFit.ts";

const RIGHT_COLUMN_BOTTOM = 700; // only for OUTPUT_ROOM (which scenes take over)
const TAKEOVER_BOTTOM = 790;
const OUTPUT_ROOM = RIGHT_COLUMN_BOTTOM - 96 - 160 - 24 - 90 - 24;
const oldMode = process.argv.includes("--old");
const showCuts = process.argv.includes("--cuts");

const sizes: Record<number, number> = {};
let scenes = 0;
let overflowScenes = 0;
let overflowLabels = 0;
const overflowEps = new Set<number>();
const cutRows: string[] = [];
let cutLabels = 0;
const cutEps = new Set<number>();
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(`episodes/ep${String(n).padStart(3, "0")}.json`, "utf8"));
  for (const s of ep.scenes) {
    if (s.template !== "code-explain" || !s.code?.source) continue;
    const labels: Record<number, string> = (scenePropsFor(ep, s) as { labels?: Record<number, string> }).labels ?? {};
    if (!Object.keys(labels).length) continue;
    const lay = s.code.output ? layoutOutput(s.code.output, OUTPUT_ROOM, TAKEOVER_BOTTOM - 96) : undefined;
    const columnWidth = lay?.fullColumn ? TAKEOVER_PANEL_WIDTH : 1920 - 192 - 48 - 1002;
    const columnHeight = lay ? TAKEOVER_BOTTOM - 96 : 1080 - 192;
    // Tracker block: every tracked name at once with a 5-character value (a close estimate for a scan).
    const tracked = new Set(
      (s.narration.match(/\[TRACK\s+([^\]]*)\]/g) ?? []).flatMap((m: string) =>
        m.slice(7, -1).trim().split(/\s+/).map((kv: string) => kv.split("=")[0]),
      ),
    );
    const state: Record<string, string> = {};
    for (const k of tracked) state[k] = "00000";
    const trackerH = trackerHeight(tracked.size ? [state] : [], columnWidth);
    const outputH = lay ? outputPanelHeight(lay) : 0;
    const gaps = ((trackerH ? 1 : 0) + (lay ? 1 : 0)) * COLUMN_GAP;
    const budget = columnHeight - trackerH - outputH - gaps;
    scenes++;
    if (oldMode) {
      const bad = Object.values(labels).filter((t) => cardHeight(t, 44, columnWidth) > Math.max(160, budget));
      if (bad.length) {
        overflowScenes++;
        overflowLabels += bad.length;
        overflowEps.add(n);
      }
      continue;
    }
    const fit = fitLabels(labels, budget, columnWidth);
    sizes[fit.size] = (sizes[fit.size] ?? 0) + 1;
    if (fit.cut.length) {
      cutLabels += fit.cut.length;
      cutEps.add(n);
      for (const k of fit.cut) cutRows.push(`EP${n}s${s.id} HL${k}: "${labels[k].slice(0, 70)}" -> "${fit.labels[k]}"`);
    }
  }
}
if (oldMode) {
  console.log(`OLD rule (44px, card squeezed to 160px): ${overflowScenes} of ${scenes} scenes, ${overflowLabels} labels, ${overflowEps.size} episodes overflow`);
  console.log("episodes:", [...overflowEps].join(","));
} else {
  console.log(`NEW fit: ${scenes} code-explain scenes with labels; font size per scene:`, JSON.stringify(sizes));
  console.log(`labels cut to their first clause (did not fit at 28px): ${cutLabels} in ${cutEps.size} episodes: ${[...cutEps].join(",") || "none"}`);
  if (showCuts) console.log(cutRows.join("\n"));
}
