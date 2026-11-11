/**
 * For all 86 episodes: does the Bug-of-the-Day code window (what CodeBlock shows with maxHeight 410,
 * fontSize 40, width 1100) contain the line that causes the bug? Read-only report.
 *
 * Before fix pass 5 BugOfTheDay passed no highlight line, so the window was always the LAST rows of the file.
 * Now it passes the culprit (src/lib/bugCulprit.ts) and CodeBlock centres the window on it. `--old` reports the
 * old behaviour (window = last rows); the default reports the new one (window centred on the culprit), which
 * must contain the culprit for every episode (it is a check that centring works, and that the culprit exists).
 *
 * Usage: node scripts/bug_windows.mts [--old] [--show]   (--show prints the culprit line text)
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { chromePx, layoutRows, rowHeightPx } from "../src/lib/codeLayout.ts";
import { stripMarkdown } from "../src/lib/sanitize.ts";
import { bugCulprit } from "../src/lib/bugCulprit.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const WIDTH = 1100;
const FONT = 40;
const MAX_HEIGHT = 410;
const isCode = (t: string): boolean => /[;{]|#include/.test(t);
const bugText = (t: string): string => (isCode(t) ? t : stripMarkdown(t));

/** Source lines (1-based) in the visible window; mirrors CodeBlock's scroll rules (all rows typed). */
export const windowLines = (code: string, highlight?: number): { from: number; to: number; total: number } => {
  const rows = layoutRows(code, WIDTH, FONT, true);
  const cap = Math.min(rows.length, Math.max(1, Math.floor((MAX_HEIGHT - chromePx()) / rowHeightPx(FONT))));
  const firstHl = highlight !== undefined ? rows.findIndex((r) => r.line === highlight) : -1;
  const hlCount = firstHl >= 0 ? rows.filter((r) => r.line === highlight).length : 0;
  const anchor = firstHl >= 0 ? firstHl : rows.length - 1;
  let scroll =
    rows.length > cap
      ? Math.min(
          rows.length - cap,
          Math.max(0, anchor - Math.floor((cap - Math.max(1, hlCount)) / 2)),
          Math.max(0, rows.length - 1 - cap + 1 + (firstHl >= 0 ? hlCount : 0)),
        )
      : 0;
  while (scroll > 0 && !rows[scroll].first) scroll--;
  let last = Math.min(rows.length - 1, scroll + cap - 1);
  const endsLine = (i: number): boolean => i === rows.length - 1 || rows[i + 1].first;
  while (last > scroll && !endsLine(last)) last--;
  return { from: rows[scroll].line, to: rows[last].line, total: code.split("\n").length };
};

const old = process.argv.includes("--old");
const show = process.argv.includes("--show");
const missing: string[] = [];
const noCulprit: string[] = [];
const fixedMissing: string[] = [];
const noCode: string[] = [];
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  const records = [{ tag: "", bug: ep.bug }, ...(ep.scenes as { id: number; bug?: typeof ep.bug }[]).filter((s) => s.bug).map((s) => ({ tag: ` s${s.id}`, bug: s.bug }))];
  for (const r of records) {
  const wrong = bugText(r.bug?.wrong ?? "");
  const fixed = bugText(r.bug?.fixed ?? "");
  const tag = `EP${String(n).padStart(2, "0")}${r.tag}`;
  if (!isCode(wrong)) {
    noCode.push(tag);
    if (show) console.log(`${tag} (prose: text card)`);
    continue;
  }
  const c = bugCulprit(n, wrong, isCode(fixed) ? fixed : "", stripMarkdown(r.bug?.error ?? ""));
  const w = windowLines(wrong, old ? undefined : c.wrong);
  const inW = c.wrong !== undefined && c.wrong >= w.from && c.wrong <= w.to;
  const fw = isCode(fixed) ? windowLines(fixed, old ? undefined : c.fixed) : undefined;
  const inF = !fw || c.fixed === undefined || (c.fixed >= fw.from && c.fixed <= fw.to);
  if (c.wrong === undefined) noCulprit.push(tag);
  else if (!inW) missing.push(tag);
  if (!inF) fixedMissing.push(tag);
  if (show)
    console.log(
      `${tag} wrong ${c.wrong ?? "-"} (window ${w.from}-${w.to}/${w.total}) ${wrong.split("\n")[(c.wrong ?? 1) - 1]?.trim().slice(0, 60) ?? ""} | fixed ${c.fixed ?? "-"}${fw ? ` (window ${fw.from}-${fw.to}/${fw.total})` : ""}`,
    );
  }
}
const l = (xs: string[]): string => xs.join(", ") || "none";
console.log(`${old ? "OLD window (last rows)" : "NEW window (centred on the culprit)"}:`);
console.log(`wrong-code window does NOT contain the culprit (${missing.length}): ${l(missing)}`);
console.log(`no culprit found (${noCulprit.length}): ${l(noCulprit)}`);
console.log(`fixed-code window does NOT contain the changed line (${fixedMissing.length}): ${l(fixedMissing)}`);
console.log(`wrong slot is prose, no window (${noCode.length}): ${l(noCode)}`);
