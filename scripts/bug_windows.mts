/**
 * For all 86 episodes: does the Bug-of-the-Day code window (what CodeBlock shows with maxHeight 410,
 * fontSize 40, width 1100 and no highlight line) contain the line that causes the bug? Read-only report;
 * it changes nothing.
 *
 * How the window is chosen (BugOfTheDay -> CodeBlock): the panel is capped to floor((410 - chrome) / rowHeight)
 * ROWS (a wrapped line takes several rows). BugOfTheDay passes no `highlightLine` and no `visibleChars`, so the
 * panel follows the typing to the end: the window is always the LAST rows of the file, snapped to whole lines.
 *
 * The culprit is, in order of trust:
 *  1. the compiler's own line (`file:LINE:col: error|warning`), when its echoed source matches the code;
 *  2. the wrong lines that the fix changes. Fixed lines are aligned to wrong lines (monotonic, by token
 *     similarity >= 0.5, exact matches first); an aligned pair that is not identical is a changed line, wrong lines
 *     between aligned pairs are removed lines, and a fixed line with no partner is an insertion, which makes the
 *     wrong lines on both sides of the gap culprits. A short fragment fix is aligned the same way, so lines of the
 *     wrong program outside the fragment's span are not counted.
 *
 * A window passes only if the PRIMARY culprit (the compiler line, else the first changed line) is in it.
 *
 * Usage: node scripts/bug_windows.mts [--json]
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { chromePx, layoutRows, rowHeightPx } from "../src/lib/codeLayout.ts";
import { stripMarkdown } from "../src/lib/sanitize.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const WIDTH = 1100;
const FONT = 40;
const MAX_HEIGHT = 410;
const MIN_SIM = 0.5;
const isCode = (t: string): boolean => /[;{]|#include/.test(t);
const bugText = (t: string): string => (isCode(t) ? t : stripMarkdown(t));

/** Source line numbers (1-based) in the visible window, mirroring CodeBlock's scroll rules. */
export const windowLines = (code: string): { from: number; to: number; total: number } => {
  const rows = layoutRows(code, WIDTH, FONT, true);
  const cap = Math.min(rows.length, Math.max(1, Math.floor((MAX_HEIGHT - chromePx()) / rowHeightPx(FONT))));
  let scroll = rows.length > cap ? rows.length - cap : 0;
  while (scroll > 0 && !rows[scroll].first) scroll--;
  let last = Math.min(rows.length - 1, scroll + cap - 1);
  const endsLine = (i: number): boolean => i === rows.length - 1 || rows[i + 1].first;
  while (last > scroll && !endsLine(last)) last--;
  return { from: rows[scroll].line, to: rows[last].line, total: code.split("\n").length };
};

const tokensOf = (l: string): Map<string, number> => {
  const m = new Map<string, number>();
  for (const t of l.match(/\w+|[^\s\w]/g) ?? []) m.set(t, (m.get(t) ?? 0) + 1);
  return m;
};
const similarity = (a: string, b: string): number => {
  if (a.trim() === "" || b.trim() === "") return 0;
  if (a.trim() === b.trim()) return 1;
  const ta = tokensOf(a);
  const tb = tokensOf(b);
  let inter = 0;
  let union = 0;
  for (const k of new Set([...ta.keys(), ...tb.keys()])) {
    const x = ta.get(k) ?? 0;
    const y = tb.get(k) ?? 0;
    inter += Math.min(x, y);
    union += Math.max(x, y);
  }
  // Identical token multisets in a different order (a re-sorted array) still count as a changed line.
  return union ? Math.min(0.99, inter / union) : 0;
};

export type Culprits = { wrongSide: number[]; fixedSide: number[] };

/** Aligns the fixed lines to the wrong lines and returns the changed wrong lines and the changed fixed lines. */
export const culpritLines = (wrong: string[], fixed: string[]): Culprits => {
  const n = wrong.length;
  const m = fixed.length;
  const sim = (i: number, j: number): number => {
    const s = similarity(wrong[i], fixed[j]);
    return s >= MIN_SIM ? s : 0;
  };
  const dp = Array.from({ length: n + 1 }, () => new Array<number>(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--) {
      const s = sim(i, j);
      dp[i][j] = Math.max(dp[i + 1][j], dp[i][j + 1], s > 0 ? dp[i + 1][j + 1] + s : 0);
    }
  const pairs: [number, number][] = [];
  let i = 0;
  let j = 0;
  while (i < n && j < m) {
    const s = sim(i, j);
    if (s > 0 && Math.abs(dp[i][j] - (dp[i + 1][j + 1] + s)) < 1e-9) {
      pairs.push([i, j]);
      i++;
      j++;
    } else if (dp[i + 1][j] >= dp[i][j + 1]) i++;
    else j++;
  }
  const wrongSide = new Set<number>();
  const fixedSide = new Set<number>();
  const matchedW = new Set(pairs.map((p) => p[0]));
  const matchedF = new Set(pairs.map((p) => p[1]));
  for (const [a, b] of pairs) {
    if (wrong[a].trim() !== fixed[b].trim()) {
      wrongSide.add(a + 1);
      fixedSide.add(b + 1);
    }
  }
  const first = pairs.length ? pairs[0] : undefined;
  const last = pairs.length ? pairs[pairs.length - 1] : undefined;
  // Wrong lines between two aligned pairs that have no partner were removed or rewritten by the fix.
  if (first && last)
    for (let a = first[0]; a <= last[0]; a++) if (!matchedW.has(a) && wrong[a].trim() !== "") wrongSide.add(a + 1);
  // Fixed lines with no partner are insertions (or the fragment's extra lines): the wrong lines around the gap.
  for (let b = 0; b < m; b++) {
    if (matchedF.has(b) || fixed[b].trim() === "") continue;
    fixedSide.add(b + 1);
    const before = [...pairs].reverse().find((p) => p[1] < b);
    const after = pairs.find((p) => p[1] > b);
    const lo = before ? before[0] : undefined;
    const hi = after ? after[0] : undefined;
    const prev = (x: number | undefined): number | undefined => {
      for (let k = x ?? -1; k >= 0; k--) if (wrong[k].trim() !== "") return k + 1;
      return undefined;
    };
    const next = (x: number | undefined): number | undefined => {
      for (let k = x ?? n; k < n; k++) if (wrong[k].trim() !== "") return k + 1;
      return undefined;
    };
    const p = prev(lo);
    const q = next(hi);
    if (p !== undefined && before) wrongSide.add(p);
    if (q !== undefined && after) wrongSide.add(q);
    // A fragment with no partner at all: fall back to the wrong line sharing the most tokens with it.
    if (!pairs.length) {
      let best = -1;
      let bestScore = 0;
      wrong.forEach((l, k) => {
        const s = similarity(l, fixed[b]);
        if (s > bestScore) {
          bestScore = s;
          best = k + 1;
        }
      });
      if (best > 0 && bestScore >= 0.25) wrongSide.add(best);
    }
  }
  return { wrongSide: [...wrongSide].sort((x, y) => x - y), fixedSide: [...fixedSide].sort((x, y) => x - y) };
};

export type WindowVerdict = {
  ep: number;
  status: "OK" | "MISS" | "UNKNOWN" | "PROSE";
  window?: { from: number; to: number; total: number };
  culprit: number[];
  source: "compiler" | "diff" | "-";
  fixedWindow?: { from: number; to: number; total: number };
  fixedCulprit: number[];
  fixedOk: boolean;
};

export const checkEpisode = (n: number): WindowVerdict => {
  const ep = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  const wrong = bugText(ep.bug?.wrong ?? "");
  const fixed = bugText(ep.bug?.fixed ?? "");
  if (!isCode(wrong)) return { ep: n, status: "PROSE", culprit: [], source: "-", fixedCulprit: [], fixedOk: true };
  const w = windowLines(wrong);
  const wl = wrong.split("\n");
  const { wrongSide, fixedSide } = isCode(fixed) ? culpritLines(wl, fixed.split("\n")) : { wrongSide: [], fixedSide: [] };
  const err = stripMarkdown(ep.bug?.error ?? "");
  const diag = /:(\d+):\d+:\s*(?:error|warning)/.exec(err);
  const diagLine = diag ? Number(diag[1]) : undefined;
  const echo =
    diagLine !== undefined ? new RegExp(`^\\s*${diagLine}\\s*\\|\\s?(.*)$`, "m").exec(err)?.[1]?.trim() : undefined;
  const diagOk = diagLine !== undefined && echo !== undefined && wl[diagLine - 1]?.trim() === echo;
  const culprit = diagOk ? [diagLine!] : wrongSide;
  const status = culprit.length === 0 ? "UNKNOWN" : culprit[0] >= w.from && culprit[0] <= w.to ? "OK" : "MISS";
  const fw = isCode(fixed) ? windowLines(fixed) : undefined;
  const fixedOk = fw ? fixedSide.length === 0 || fixedSide.some((l) => l >= fw.from && l <= fw.to) : true;
  return { ep: n, status, window: w, culprit, source: diagOk ? "compiler" : "diff", fixedWindow: fw, fixedCulprit: fixedSide, fixedOk };
};

if (process.argv[1] && process.argv[1].endsWith("bug_windows.mts")) {
  const all = Array.from({ length: 86 }, (_, k) => checkEpisode(k + 1));
  if (process.argv.includes("--json")) console.log(JSON.stringify(all));
  else {
    for (const v of all) {
      const tag = `EP${String(v.ep).padStart(2, "0")}`;
      if (v.status === "PROSE") {
        console.log(`${tag} PROSE   (the wrong slot is prose: text card, no window)`);
        continue;
      }
      const w = v.window!;
      console.log(
        `${tag} ${v.status.padEnd(7)} window ${w.from}-${w.to} of ${w.total} | culprit ${v.culprit.join(",") || "-"} (${v.source})${v.fixedOk ? "" : ` | FIXED-WINDOW MISS ${v.fixedWindow!.from}-${v.fixedWindow!.to}, changed ${v.fixedCulprit.join(",")}`}`,
      );
    }
    const list = (f: (v: WindowVerdict) => boolean): string => all.filter(f).map((v) => `EP${v.ep}`).join(", ") || "none";
    console.log(`\nwrong-code window does NOT contain the culprit (${all.filter((v) => v.status === "MISS").length}): ${list((v) => v.status === "MISS")}`);
    console.log(`culprit not decidable (${all.filter((v) => v.status === "UNKNOWN").length}): ${list((v) => v.status === "UNKNOWN")}`);
    console.log(`fixed-code window does NOT contain a changed line (${all.filter((v) => !v.fixedOk).length}): ${list((v) => !v.fixedOk)}`);
    console.log(`wrong slot is prose, no window (${all.filter((v) => v.status === "PROSE").length}): ${list((v) => v.status === "PROSE")}`);
  }
}
