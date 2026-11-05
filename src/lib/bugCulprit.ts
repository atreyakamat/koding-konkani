/** Which line of the Bug-of-the-Day code is the culprit, so the code window can centre on it.
 *
 * In order of trust:
 *  1. an explicit entry in BUG_CULPRIT_OVERRIDES (for fixes that are a different program, where alignment is noise);
 *  2. the compiler's own line (`file:LINE:col: error|warning`) when its echoed source matches the code;
 *  3. the first wrong line that the fix changes. Fixed lines are aligned to wrong lines (monotonic, by token
 *     similarity >= 0.5, exact matches first). An aligned pair that differs is a changed line; wrong lines between
 *     aligned pairs without a partner were removed; a fixed line with no partner is an insertion, and the wrong
 *     lines on both sides of the gap count. A short fragment fix is aligned the same way, so lines of the wrong
 *     program outside the fragment's span are not counted.
 * The fixed panel highlights the first fixed line that differs from the wrong code. */
const MIN_SIM = 0.5;

/** Hand-picked 1-based lines where alignment cannot work. */
export const BUG_CULPRIT_OVERRIDES: Record<number, { wrong?: number; fixed?: number }> = {
  // EP05: the code is fine; the stale .exe is the bug. Point at the edited printf; the "fix" is a sentence.
  5: { wrong: 5 },
  // EP64: the fix is a different program (tagged union). Wrong: the printf that reads the other member; fixed: the tag check.
  64: { wrong: 11, fixed: 14 },
  // EP83: push four values into SIZE 3 and pop five; the fix is a sentence.
  83: { wrong: 17 },
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

/** Aligns the fixed lines to the wrong lines; returns the changed wrong lines and the changed fixed lines (1-based, ascending). */
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
  // Lines next to a pure insertion only count when no wrong line was changed or removed.
  const neighbours = new Set<number>();
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
  if (first && last)
    for (let a = first[0]; a <= last[0]; a++) if (!matchedW.has(a) && wrong[a].trim() !== "") wrongSide.add(a + 1);
  const prevNonBlank = (x: number | undefined): number | undefined => {
    for (let k = x ?? -1; k >= 0; k--) if (wrong[k].trim() !== "") return k + 1;
    return undefined;
  };
  const nextNonBlank = (x: number | undefined): number | undefined => {
    for (let k = x ?? n; k < n; k++) if (wrong[k].trim() !== "") return k + 1;
    return undefined;
  };
  for (let b = 0; b < m; b++) {
    // An added #include / #define is not the bug: it neither counts nor points at its neighbours.
    if (matchedF.has(b) || fixed[b].trim() === "" || /^[ 	]*#/.test(fixed[b])) continue;
    fixedSide.add(b + 1);
    const before = [...pairs].reverse().find((p) => p[1] < b);
    const after = pairs.find((p) => p[1] > b);
    const p = prevNonBlank(before ? before[0] : undefined);
    const q = nextNonBlank(after ? after[0] : undefined);
    if (p !== undefined && before) neighbours.add(p);
    if (q !== undefined && after) neighbours.add(q);
    if (!pairs.length) {
      // A fragment with no partner at all: the wrong line sharing the most tokens with it.
      let best = -1;
      let bestScore = 0;
      wrong.forEach((l, k) => {
        const s = similarity(l, fixed[b]);
        if (s > bestScore) {
          bestScore = s;
          best = k + 1;
        }
      });
      if (best > 0 && bestScore >= 0.25) neighbours.add(best);
    }
  }
  const core = wrongSide.size ? wrongSide : neighbours;
  const sortedCore = [...core].sort((x, y) => x - y);
  // A pure deletion (the fix only removes wrong lines): point at the fixed line that follows the gap
  // (else the one before it), so the fixed panel still shows where the fix happened.
  if (fixedSide.size === 0 && sortedCore.length > 0 && pairs.length > 0) {
    const a = sortedCore[0] - 1;
    const after = pairs.find((p) => p[0] > a);
    const before = [...pairs].reverse().find((p) => p[0] < a);
    const near = after ?? before;
    if (near) fixedSide.add(near[1] + 1);
  }
  return { wrongSide: sortedCore, fixedSide: [...fixedSide].sort((x, y) => x - y) };
};

/** The compiler's line from an error text like `bug.c:6:11: warning: ...` plus `    6 |     total = ...`, if it matches the code. */
export const compilerLine = (error: string, code: string[]): number | undefined => {
  const diag = /:(\d+):\d+:\s*(?:error|warning)/.exec(error);
  if (!diag) return undefined;
  const line = Number(diag[1]);
  const echo = new RegExp(`^\\s*${line}\\s*\\|\\s?(.*)$`, "m").exec(error)?.[1]?.trim();
  return echo !== undefined && code[line - 1]?.trim() === echo ? line : undefined;
};

export type BugCulprit = { wrong?: number; fixed?: number };

/** The first line that is not a preprocessor line (a fix often just adds an #include or a #define). */
const firstReal = (lines: number[], code: string[]): number | undefined =>
  lines.find((l) => !/^[ \t]*#/.test(code[l - 1] ?? "")) ?? lines[0];

/** 1-based lines to highlight in the wrong and in the fixed panel (undefined: nothing to point at, the window follows the end). */
export const bugCulprit = (ep: number, wrong: string, fixed: string, error: string): BugCulprit => {
  const override = BUG_CULPRIT_OVERRIDES[ep];
  const wl = wrong.split(String.fromCharCode(10));
  const fl = fixed.split(String.fromCharCode(10));
  const aligned = culpritLines(wl, fl);
  const fromCompiler = compilerLine(error, wl);
  return {
    wrong: override?.wrong ?? fromCompiler ?? firstReal(aligned.wrongSide, wl),
    fixed: override?.fixed ?? firstReal(aligned.fixedSide, fl),
  };
};
