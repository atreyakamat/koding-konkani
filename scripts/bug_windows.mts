/**
 * For all 86 episodes: does the Bug-of-the-Day code window (what CodeBlock shows with maxHeight 410,
 * fontSize 40, width 1100 and no highlight line) contain the line that differs between the wrong and the
 * fixed code, or the line the compiler complains about? Read-only report; it changes nothing.
 *
 * How the window is chosen (BugOfTheDay -> CodeBlock): the panel is capped to floor((410 - chrome) / rowHeight)
 * ROWS (a wrapped line takes several rows). BugOfTheDay passes no `highlightLine` and no `visibleChars`, so the
 * panel follows the typing to the end: the window is always the LAST rows of the file, snapped to whole lines.
 *
 * Usage: node scripts/bug_windows.mts
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { chromePx, layoutRows, rowHeightPx } from "../src/lib/codeLayout.ts";
import { stripMarkdown } from "../src/lib/sanitize.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const WIDTH = 1100;
const FONT = 40;
const MAX_HEIGHT = 410;
const isCode = (t: string): boolean => /[;{]|#include/.test(t);
const bugText = (t: string): string => (isCode(t) ? t : stripMarkdown(t));

/** Source line numbers (1-based) in the visible window, mirroring CodeBlock's scroll rules. */
const windowLines = (code: string): { from: number; to: number; total: number } => {
  const rows = layoutRows(code, WIDTH, FONT, true);
  const cap = Math.min(rows.length, Math.max(1, Math.floor((MAX_HEIGHT - chromePx()) / rowHeightPx(FONT))));
  let scroll = rows.length > cap ? rows.length - cap : 0;
  while (scroll > 0 && !rows[scroll].first) scroll--;
  let last = Math.min(rows.length - 1, scroll + cap - 1);
  const endsLine = (i: number): boolean => i === rows.length - 1 || rows[i + 1].first;
  while (last > scroll && !endsLine(last)) last--;
  return { from: rows[scroll].line, to: rows[last].line, total: code.split("\n").length };
};

/** Line-level diff by LCS on trimmed text. Returns the wrong-side and fixed-side lines that changed;
 * for a pure insertion (a line only the fix has) the wrong-side neighbours at the insertion point. */
const diffLines = (wrong: string[], fixed: string[]): { wrongSide: number[]; fixedSide: number[]; fragment: boolean } => {
  const a = wrong.map((l) => l.trim());
  const b = fixed.map((l) => l.trim());
  const n = a.length;
  const m = b.length;
  const lcs = Array.from({ length: n + 1 }, () => new Array<number>(m + 1).fill(0));
  for (let i = n - 1; i >= 0; i--)
    for (let j = m - 1; j >= 0; j--)
      lcs[i][j] = a[i] === b[j] ? lcs[i + 1][j + 1] + 1 : Math.max(lcs[i + 1][j], lcs[i][j + 1]);
  const wrongSide = new Set<number>();
  const fixedSide: number[] = [];
  let i = 0;
  let j = 0;
  while (i < n || j < m) {
    if (i < n && j < m && a[i] === b[j]) {
      i++;
      j++;
    } else if (j < m && (i === n || lcs[i][j + 1] >= lcs[i + 1][j])) {
      fixedSide.push(j + 1);
      // Pure insertion: the wrong lines around the gap stand in for "where the fix goes".
      if (i > 0) wrongSide.add(i);
      if (i < n) wrongSide.add(i + 1);
      j++;
    } else {
      wrongSide.add(i + 1);
      i++;
    }
  }
  const nonBlank = (xs: string[]): number => xs.filter((l) => l.trim() !== "").length;
  // A FRAGMENT fix (a few lines that replace part of the program) shares little with the wrong code, so the
  // line diff would call every line "different". Then the culprit is the wrong line that shares the most
  // identifiers with the fragment's first line (EP67: the realloc line), and the whole fragment is the fix.
  const fragment = nonBlank(fixed) < 0.6 * nonBlank(wrong) && lcs[0][0] < 0.5 * nonBlank(fixed);
  if (fragment) {
    const tokens = (l: string): Set<string> => new Set(l.match(/[A-Za-z_][A-Za-z0-9_]{2,}/g) ?? []);
    const anchor = tokens(fixed.find((l) => l.trim() !== "") ?? "");
    let best = 0;
    let bestScore = 0;
    wrong.forEach((l, k) => {
      const score = [...tokens(l)].filter((t) => anchor.has(t)).length;
      if (score > bestScore) {
        bestScore = score;
        best = k + 1;
      }
    });
    return {
      wrongSide: bestScore >= 2 ? [best] : [],
      fixedSide: fixed.map((_, k) => k + 1).filter((l) => fixed[l - 1].trim() !== ""),
      fragment: true,
    };
  }
  // Blank lines are not culprits.
  return {
    wrongSide: [...wrongSide].filter((l) => wrong[l - 1].trim() !== "").sort((x, y) => x - y),
    fixedSide: fixedSide.filter((l) => fixed[l - 1].trim() !== ""),
    fragment: false,
  };
};

const missing: string[] = [];
const unknown: string[] = [];
const noCode: string[] = [];
const fixedMissing: string[] = [];
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  const wrong = bugText(ep.bug?.wrong ?? "");
  const fixed = bugText(ep.bug?.fixed ?? "");
  const tag = `EP${String(n).padStart(2, "0")}`;
  if (!isCode(wrong)) {
    noCode.push(tag);
    console.log(`${tag} (the wrong slot is prose, not code: text card, no window)`);
    continue;
  }
  const w = windowLines(wrong);
  const wl = wrong.split("\n");
  const { wrongSide, fixedSide, fragment } = diffLines(wl, fixed.split("\n"));
  // The compiler's line, when the error text has one (file:LINE:col: error|warning), if it matches the code.
  const err = stripMarkdown(ep.bug?.error ?? "");
  const diag = /:(\d+):\d+:\s*(?:error|warning)/.exec(err);
  const diagLine = diag ? Number(diag[1]) : undefined;
  const echo = diagLine !== undefined ? new RegExp(`^\\s*${diagLine}\\s*\\|\\s?(.*)$`, "m").exec(err)?.[1]?.trim() : undefined;
  const diagOk = diagLine !== undefined && echo !== undefined && wl[diagLine - 1]?.trim() === echo;
  const inWin = (l: number): boolean => l >= w.from && l <= w.to;
  // The compiler's own line is the best evidence; otherwise the lines that differ from the fix.
  const evidence = diagOk ? [diagLine!] : wrongSide;
  const status = evidence.length === 0 ? "UNKNOWN" : evidence.some(inWin) ? "OK" : "MISS";
  const fw = fixed.trim() && isCode(fixed) ? windowLines(fixed) : undefined;
  const fixedIn = fw ? fixedSide.some((l) => l >= fw.from && l <= fw.to) : true;
  if (status === "MISS") missing.push(tag);
  if (status === "UNKNOWN") unknown.push(tag);
  if (!fixedIn) fixedMissing.push(tag);
  console.log(
    `${tag} ${status.padEnd(7)} window ${w.from}-${w.to} of ${w.total} | ${fragment ? "fragment fix; best-matching line" : "differing lines"} ${wrongSide.join(",") || "-"} | compiler line ${diagOk ? diagLine : diagLine !== undefined ? `${diagLine}(?)` : "-"}${fixedIn ? "" : " | FIXED-WINDOW MISS " + (fw ? `${fw.from}-${fw.to}` : "")}`,
  );
}
console.log(`\nwrong-code window does NOT contain the culprit (${missing.length}): ${missing.join(", ") || "none"}`);
console.log(`culprit not decidable, no compiler line and no matching line (${unknown.length}): ${unknown.join(", ") || "none"}`);
console.log(`fixed-code window does NOT contain a changed line (${fixedMissing.length}): ${fixedMissing.join(", ") || "none"}`);
console.log(`wrong slot is prose, no window (${noCode.length}): ${noCode.join(", ") || "none"}`);
