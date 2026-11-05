/** Read-only scan: explanation-card labels in code-explain scenes with program output that are taller than the card can be (card + tracker + output > column). An estimate (24 chars/row at 44px). Usage: node scripts/scan_label_overflow.mts */
import { readFileSync } from "node:fs";
import { scenePropsFor } from "../src/compositions/sceneProps.ts";
import { layoutOutput } from "../src/lib/outputFit.ts";
const LIMIT = 24, ROW = 44 * 1.35, CARD_CHROME = 74, TRACKER = 90, GAP = 24;
const rowsOf = (t: string): number => { let r = 1, c = 0; for (const w of t.split(/\s+/)) { if (!c) c = w.length; else if (c + 1 + w.length <= LIMIT) c += 1 + w.length; else { r++; c = w.length; } } return r; };
const OUTPUT_ROOM = 700 - 96 - 160 - 24 - 90 - 24;
const per: Record<number, { scenes: Set<number>; labels: number; worst: number }> = {};
const ex: string[] = [];
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(`episodes/ep${String(n).padStart(3, "0")}.json`, "utf8"));
  for (const s of ep.scenes) {
    if (s.template !== "code-explain" || !s.code?.source || !s.code?.output) continue;
    const p: any = scenePropsFor(ep, s);
    const lay = layoutOutput(s.code.output, OUTPUT_ROOM, 790 - 96);
    const H = lay.fullColumn ? 694 : 604;
    const lines = s.code.output.replace(/\n+$/, "").split("\n").length + 1;
    const outH = Math.ceil(lay.size * 1.35) * lines + 40; // natural height before it stretches
    const hasTrack = /\[TRACK\s/.test(s.narration);
    const bad: number[] = [];
    for (const l of Object.values(p.labels ?? {}) as string[]) {
      const card = Math.max(160, rowsOf(l) * ROW + CARD_CHROME);
      const total = card + GAP + (hasTrack ? TRACKER + GAP : 0) + outH + (lay.fullColumn ? 0 : 0);
      if (total > H) bad.push(rowsOf(l));
    }
    if (bad.length) {
      const e = (per[n] ??= { scenes: new Set(), labels: 0, worst: 0 });
      e.scenes.add(s.id); e.labels += bad.length; e.worst = Math.max(e.worst, ...bad);
      if ([42, 45, 49].includes(n)) ex.push(`EP${n}s${s.id}(${bad.length} labels, worst ${Math.max(...bad)} rows)`);
    }
  }
}
const eps = Object.keys(per).map(Number);
const sc = eps.reduce((a, k) => a + per[k].scenes.size, 0);
const lb = eps.reduce((a, k) => a + per[k].labels, 0);
console.log(`overflowing: ${sc} scenes, ${lb} labels, ${eps.length} episodes`);
console.log("episodes:", eps.join(","));
console.log("EP1-19:", eps.filter((k) => k <= 19).join(",") || "none", "| EP20-50:", eps.filter((k) => k >= 20 && k <= 50).join(","));
console.log(ex.join(" | "));
