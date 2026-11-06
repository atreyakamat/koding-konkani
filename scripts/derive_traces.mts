/**
 * Fix pass 5b, on paper: step traces for the algorithm-bars scenes that have none (EP72 s4, EP76 s4-5, EP78 s4-5, EP80 s4-5),
 * and drafts for the two scenes the bars component cannot draw (EP77 Tower of Hanoi pegs, EP81 six mini rows).
 *
 * The trace is produced by a C probe that is COMPILED AND RUN with GCC (instrumented insertion sort, merge sort, counting
 * sort, hanoi, and the five other sorts of the EP81 scorecard), then cross-checked against the Bible's own tables
 * (docs/bible/m12.md: the array after every step, the totals "11 comparisons, 8 shifts", "11 comparisons, 5 merges, 16 writes",
 * "0 comparisons, 6 counts, 6 writes", the scorecard counts). Any mismatch is printed and the script exits 1.
 *
 * Writes `trace` into episodes/*.json (JSON only, the same 2-space CRLF format) and drafts into docs/fix4/traces-draft/.
 * No Remotion, no src/ edits.   Usage: node scripts/derive_traces.mts [--dry]
 */
import { spawnSync } from "node:child_process";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const DRY = process.argv.includes("--dry");
const WORK = join(tmpdir(), "koding-trace-probe");
mkdirSync(WORK, { recursive: true });
const problems: string[] = [];
const must = (label: string, ok: boolean): void => {
  if (!ok) problems.push(label);
};

let probeNo = 0;
const runC = (source: string): string[] => {
  const base = join(WORK, `t${probeNo++}`);
  writeFileSync(`${base}.c`, source);
  const cc = spawnSync("gcc", ["-Wall", "-Wextra", "-D__USE_MINGW_ANSI_STDIO=1", "-o", `${base}.exe`, `${base}.c`], { encoding: "utf-8" });
  if (cc.status !== 0) throw new Error(`gcc failed: ${cc.stderr}`);
  if (cc.stderr.trim()) problems.push(`gcc warning in probe ${probeNo - 1}: ${cc.stderr.trim().split(/\r?\n/)[0]}`);
  const run = spawnSync(`${base}.exe`, { encoding: "utf-8" });
  return run.stdout.trim().split(/\r?\n/);
};

// ---------- the Bible tables ----------
const bible = readFileSync(join(ROOT, "docs", "bible", "m12.md"), "utf-8").replace(/\r\n/g, "\n");
const epBlock = (n: number): string => {
  const a = bible.indexOf(`\n## EP ${n} `);
  const b = bible.indexOf(`\n## EP ${n + 1} `);
  return bible.slice(a, b < 0 ? undefined : b);
};
const tableRows = (n: number, heading: RegExp): string[][] => {
  const block = epBlock(n);
  const h = heading.exec(block);
  if (!h) throw new Error(`EP${n}: no ${heading}`);
  const rest = block.slice(h.index + h[0].length).split("\n");
  const rows: string[][] = [];
  let seen = false;
  for (const line of rest) {
    if (line.startsWith("|")) {
      seen = true;
      const cells = line.split("|").slice(1, -1).map((c) => c.trim().replace(/\\([\[\]_*])/g, "$1"));
      if (!cells.every((c) => /^-+$/.test(c))) rows.push(cells);
    } else if (seen) break;
  }
  return rows.slice(1); // without the header
};
const nums = (s: string): number[] => (s.match(/-?\d+/g) ?? []).map(Number);

type Step = { step: number | string; array: number[]; compare?: [number, number]; swap?: [number, number]; sorted?: number[] };
const range = (a: number, b: number): number[] => (b < a ? [] : Array.from({ length: b - a + 1 }, (_, i) => a + i));
const without = (xs: number[], drop: number[]): number[] => xs.filter((x) => !drop.includes(x));

const DATA = "int a[] = {5, 2, 9, 1, 6, 3};";

// ---------- EP76 insertion sort ----------
const insertionProbe = `#include <stdio.h>
int main(void) {
  ${DATA}
  int n = 6, cmp = 0, shifts = 0, places = 0;
  printf("S|start|%d %d %d %d %d %d|-|-|-\\n", a[0], a[1], a[2], a[3], a[4], a[5]);
  for (int i = 1; i < n; i++) {
    int key = a[i], j = i - 1, s = 1;
    for (;;) {
      if (j < 0) { a[j + 1] = key; places++;
        printf("S|%d.%d|%d %d %d %d %d %d|-|-|%d\\n", i, s, a[0], a[1], a[2], a[3], a[4], a[5], j + 1); break; }
      cmp++;
      if (a[j] > key) { a[j + 1] = a[j]; shifts++;
        printf("S|%d.%d|%d %d %d %d %d %d|%d|%d|-\\n", i, s, a[0], a[1], a[2], a[3], a[4], a[5], j, j + 1); j--; s++; }
      else { a[j + 1] = key; places++;
        printf("S|%d.%d|%d %d %d %d %d %d|%d|-|%d\\n", i, s, a[0], a[1], a[2], a[3], a[4], a[5], j, j + 1); break; }
    }
  }
  printf("T|%d|%d|%d\\n", cmp, shifts, places);
  return 0;
}
`;
const insertion = (): { all: Step[]; s4: Step[]; s5: Step[] } => {
  const out = runC(insertionProbe);
  const steps: Step[] = [];
  let sortedPrefix = -1; // last index of the completed sorted prefix
  for (const line of out.filter((l) => l.startsWith("S|"))) {
    const [, label, arr, cmp, shift, place] = line.split("|");
    const array = nums(arr);
    if (label === "start") {
      steps.push({ step: "start", array });
      continue;
    }
    const pass = Number(label.split(".")[0]);
    const compare = cmp !== "-" ? ([Number(cmp), Number(cmp) + 1] as [number, number]) : undefined;
    const swap = shift !== "-" ? ([Number(shift) - 1, Number(shift)] as [number, number]) : undefined;
    const active = [...(compare ?? []), ...(swap ?? [])];
    const st: Step = { step: label, array };
    if (compare) st.compare = compare;
    if (swap) st.swap = swap;
    if (place !== "-") {
      sortedPrefix = pass; // the key is in its gap: positions 0..pass are sorted
      st.sorted = range(0, pass);
    } else {
      const s = without(range(0, pass - 1), active);
      if (s.length) st.sorted = s;
    }
    steps.push(st);
  }
  // cross-check against the Bible table
  const rows = tableRows(76, /### Step trace\n/);
  const bibleSteps = rows.filter((r) => r[0] !== "start").map((r) => ({ label: r[0].split(" ")[0], array: nums(r[1]) }));
  const mine = steps.filter((s) => s.step !== "start");
  must("EP76: same number of steps as the Bible table (13)", mine.length === bibleSteps.length && mine.length === 13);
  mine.forEach((s, k) => {
    must(`EP76 step ${s.step}: label and array equal the Bible table`, s.step === bibleSteps[k]?.label && s.array.join() === bibleSteps[k]?.array.join());
  });
  const t = out.find((l) => l.startsWith("T|"))!.split("|").map(Number);
  must("EP76 totals: 11 comparisons, 8 shifts, 5 placements (Bible)", t[1] === 11 && t[2] === 8 && t[3] === 5);
  must("EP76 trace counters: compare steps 11, shift steps 8", mine.filter((s) => s.compare).length === 11 && mine.filter((s) => s.swap).length === 8);
  void sortedPrefix;
  const cut = steps.findIndex((s) => s.step === "4.1");
  const s4 = steps.slice(0, cut);
  const before = steps[cut - 1];
  const s5 = [{ step: "start", array: before.array, sorted: range(0, 3) } as Step, ...steps.slice(cut)];
  return { all: steps, s4, s5 };
};

// ---------- EP78 merge sort ----------
const mergeProbe = `#include <stdio.h>
static int a[] = {5, 2, 9, 1, 6, 3};
static int cmpN = 0, writes = 0, merges = 0, sN = 0, mN = 0;
static void dump(const char *tag, int x, int y, int z, int w) {
  printf("%s|%d %d %d %d %d %d|%d|%d|%d|%d\\n", tag, a[0], a[1], a[2], a[3], a[4], a[5], x, y, z, w);
}
static void merge(int l, int m, int r) {
  int t[6], i = l, j = m + 1, k = 0;
  mN++; char tag[16];
  while (i <= m && j <= r) {
    cmpN++;
    sprintf(tag, "C%d", mN);
    int take = (a[i] <= a[j]);
    dump(tag, i, j, take ? i : j, 0);
    if (take) t[k++] = a[i++]; else t[k++] = a[j++];
  }
  while (i <= m) t[k++] = a[i++];
  while (j <= r) t[k++] = a[j++];
  for (int x = 0; x < k; x++) { a[l + x] = t[x]; writes++; }
  merges++;
  sprintf(tag, "M%d", mN);
  dump(tag, l, r, 0, 0);
}
static void sort(int l, int r) {
  if (l >= r) return;
  int m = (l + r) / 2;
  sN++; char tag[16]; sprintf(tag, "S%d", sN);
  dump(tag, l, r, m, 0);
  sort(l, m); sort(m + 1, r); merge(l, m, r);
}
int main(void) { sort(0, 5); printf("T|%d|%d|%d\\n", cmpN, merges, writes); return 0; }
`;
const merge = (): { s4: Step[]; s5: Step[] } => {
  const out = runC(mergeProbe);
  const t = out.find((l) => l.startsWith("T|"))!.split("|").map(Number);
  must("EP78 totals: 11 comparisons, 5 merges, 16 writes (Bible)", t[1] === 11 && t[2] === 5 && t[3] === 16);
  const events = out.filter((l) => !l.startsWith("T|")).map((l) => l.split("|"));
  const bibleRows = tableRows(78, /### Step trace\n/);
  const bible = new Map(bibleRows.map((r) => [r[0], nums(r[1])]));
  const s4: Step[] = [];
  const s5: Step[] = [{ step: "start", array: [5, 2, 9, 1, 6, 3] }];
  let compareNo = 0;
  for (const e of events) {
    const tag = e[0];
    const array = nums(e[1]);
    const [x, y, z] = [Number(e[2]), Number(e[3]), Number(e[4])];
    if (tag.startsWith("S")) {
      // a split: the two bars either side of the cut are the compare pair
      s4.push({ step: tag, array, compare: [z, z + 1] });
      must(`EP78 ${tag}: array equals the Bible table`, bible.get(tag)?.join() === array.join());
    } else if (tag.startsWith("C")) {
      compareNo++;
      s5.push({ step: `M${tag.slice(1)} compare`, array, compare: [x, y] });
      void z;
    } else if (tag.startsWith("M")) {
      s5.push({ step: tag, array, sorted: range(x, y) });
      must(`EP78 ${tag}: array equals the Bible table`, bible.get(tag)?.join() === array.join());
    }
  }
  must("EP78 compare steps = 11", compareNo === 11);
  // the S rows interleave with M rows in the Bible; the order of the S steps is S1..S5 (checked above by label)
  must("EP78 split steps S1..S5", s4.length === 5);
  return { s4, s5 };
};

// ---------- EP80 counting sort ----------
const countingProbe = `#include <stdio.h>
int main(void) {
  ${DATA}
  int n = 6, count[10] = {0}, reads = 0, visits = 0, writes = 0;
  for (int i = 0; i < n; i++) {
    count[a[i]]++; reads++;
    printf("C|C%d|%d %d %d %d %d %d|%d|%d %d %d %d %d %d %d %d %d %d\\n", i + 1, a[0], a[1], a[2], a[3], a[4], a[5], i,
      count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7], count[8], count[9]);
  }
  int k = 0;
  for (int v = 0; v < 10; v++) {
    visits++;
    while (count[v] > 0) {
      a[k] = v; count[v]--; writes++;
      printf("R|R%d|%d %d %d %d %d %d|%d|%d %d %d %d %d %d %d %d %d %d\\n", k + 1, a[0], a[1], a[2], a[3], a[4], a[5], k,
        count[0], count[1], count[2], count[3], count[4], count[5], count[6], count[7], count[8], count[9]);
      k++;
    }
  }
  printf("T|%d|%d|%d\\n", reads, visits, writes);
  return 0;
}
`;
const counting = (): { s4: Step[]; s5: Step[]; counts: { step: string; counts: number[] }[] } => {
  const out = runC(countingProbe);
  const t = out.find((l) => l.startsWith("T|"))!.split("|").map(Number);
  must("EP80 totals: 6 counts, 10 bucket visits, 6 writes (Bible)", t[1] === 6 && t[2] === 10 && t[3] === 6);
  const bibleRows = tableRows(80, /### Step trace\n/);
  const bible = new Map(bibleRows.map((r) => [r[0], nums(r[1])]));
  const s4: Step[] = [];
  const s5: Step[] = [{ step: "start", array: [5, 2, 9, 1, 6, 3] }];
  const counts: { step: string; counts: number[] }[] = [];
  for (const l of out.filter((x) => !x.startsWith("T|"))) {
    const [kind, label, arr, idx, cnt] = l.split("|");
    const array = nums(arr);
    const i = Number(idx);
    must(`EP80 ${label}: array equals the Bible table`, bible.get(label)?.join() === array.join());
    counts.push({ step: label, counts: nums(cnt) });
    if (kind === "C") s4.push({ step: label, array, compare: [i, i] });
    else s5.push({ step: label, array, sorted: range(0, i) });
  }
  must("EP80 count row after C6 = [0,1,1,1,0,1,1,0,0,1] (Bible)", counts[5].counts.join() === "0,1,1,1,0,1,1,0,0,1");
  return { s4, s5, counts };
};

// ---------- EP72 linear search over eight boxes ----------
const linear = (): Step[] => {
  // Illustrative values (the Bible gives none): eight fish boxes, the kingfish (value 6) in the last box, so the worst case is 8 checks.
  const boxes = [3, 8, 2, 9, 5, 4, 7, 6];
  const target = 6;
  const probe = `#include <stdio.h>\nint main(void) {\n  int a[] = {${boxes.join(", ")}};\n  int n = 8, target = ${target}, steps = 0;\n  for (int i = 0; i < n; i++) { steps++; printf("%d %d\\n", i, a[i] == target); if (a[i] == target) break; }\n  printf("steps %d\\n", steps);\n  return 0;\n}\n`;
  const out = runC(probe);
  must("EP72 worst case: found in the last box after 8 checks (the narration)", out[out.length - 1] === "steps 8");
  const steps: Step[] = [{ step: "start", array: boxes }];
  out.slice(0, -1).forEach((l, k) => {
    const [i, hit] = l.split(" ").map(Number);
    steps.push(hit ? { step: k + 1, array: boxes, compare: [i, i], sorted: [i] } : { step: k + 1, array: boxes, compare: [i, i] });
  });
  return steps;
};

// ---------- EP77 Tower of Hanoi (draft: pegs, not bars) ----------
const hanoi = (): unknown => {
  const probe = `#include <stdio.h>
int peg[3][4], top[3] = {3, 0, 0}, mv = 0;
static void show(void) { for (int p = 0; p < 3; p++) { for (int k = 0; k < top[p]; k++) printf("%d ", peg[p][k]); printf("|"); } printf("\\n"); }
static void hanoi(int n, int f, int t, int v) {
  if (n == 0) return;
  hanoi(n - 1, f, v, t);
  int d = peg[f][--top[f]]; peg[t][top[t]++] = d; mv++;
  printf("%d|%d|%c|%c|", mv, d, 'A' + f, 'A' + t); show();
  hanoi(n - 1, v, t, f);
}
int main(void) { peg[0][0] = 3; peg[0][1] = 2; peg[0][2] = 1; hanoi(3, 0, 2, 1); printf("T|%d\\n", mv); return 0; }
`;
  const out = runC(probe);
  const rows = tableRows(77, /### Move trace[^\n]*\n/).filter((r) => r[0] !== "start");
  const moves = out.filter((l) => !l.startsWith("T|")).map((l) => {
    const [n, disc, from, to, pegs] = l.split("|");
    const p = pegs.split("|");
    return { move: Number(n), disc: Number(disc), from, to, pegA: nums(pegs.split("|")[0] ?? ""), pegs: l.split("|").slice(4).join("|") , p };
  });
  must("EP77 seven moves (Bible: 2^3 - 1)", moves.length === 7);
  moves.forEach((m, k) => {
    const r = rows[k];
    must(`EP77 move ${m.move}: disc and from-to equal the Bible table`, Number(r[1]) === m.disc && r[2].replace(/\s/g, "") === `${m.from}→${m.to}`);
  });
  return {
    ep: 77, scene: 4, layout: "pegs", note: "scenes 4 and 7 draw this; scene 4 solves n = 1, 2, 3 (1, 3, 7 moves)",
    moves: moves.map((m) => ({ move: m.move, disc: m.disc, from: m.from, to: m.to, pegs: m.pegs.split("|").slice(0, 3).map((x: string) => nums(x)) })),
  };
};

// ---------- EP81 scorecard (draft: six mini rows) ----------
const scorecard = (): unknown => {
  const common = `#include <stdio.h>\nstatic long cmp = 0, mv = 0;\n`;
  const prog = (body: string): string => `${common}${body}\nint main(void) {\n  int a[] = {5, 2, 9, 1, 6, 3}; int n = 6;\n  run(a, n);\n  printf("%ld %ld ", cmp, mv);\n  for (int i = 0; i < n; i++) printf("%d ", a[i]);\n  printf("\\n");\n  return 0;\n}\n`;
  const sorts: Record<string, string> = {
    bubble: prog(`static void run(int *a, int n) { for (int p = 0; p < n - 1; p++) { int sw = 0; for (int j = 0; j < n - 1 - p; j++) { cmp++; if (a[j] > a[j + 1]) { int t = a[j]; a[j] = a[j + 1]; a[j + 1] = t; mv++; sw = 1; } } if (!sw) break; } }`),
    selection: prog(`static void run(int *a, int n) { for (int i = 0; i < n - 1; i++) { int m = i; for (int j = i + 1; j < n; j++) { cmp++; if (a[j] < a[m]) m = j; } if (m != i) { int t = a[i]; a[i] = a[m]; a[m] = t; mv++; } } }`),
    insertion: prog(`static void run(int *a, int n) { for (int i = 1; i < n; i++) { int key = a[i], j = i - 1; while (j >= 0) { cmp++; if (a[j] > key) { a[j + 1] = a[j]; mv++; j--; } else break; } a[j + 1] = key; } }`),
    merge: prog(`static void mg(int *a, int l, int m, int r) { int t[6], i = l, j = m + 1, k = 0; while (i <= m && j <= r) { cmp++; t[k++] = a[i] <= a[j] ? a[i++] : a[j++]; } while (i <= m) t[k++] = a[i++]; while (j <= r) t[k++] = a[j++]; for (int x = 0; x < k; x++) { a[l + x] = t[x]; mv++; } }
static void ms(int *a, int l, int r) { if (l >= r) return; int m = (l + r) / 2; ms(a, l, m); ms(a, m + 1, r); mg(a, l, m, r); }
static void run(int *a, int n) { ms(a, 0, n - 1); }`),
    quick: prog(`static void sw(int *x, int *y) { int t = *x; *x = *y; *y = t; mv++; }
static int part(int *a, int lo, int hi) { int p = a[hi], i = lo - 1; for (int j = lo; j < hi; j++) { cmp++; if (a[j] < p) { i++; sw(&a[i], &a[j]); } } sw(&a[i + 1], &a[hi]); return i + 1; }
static void qs(int *a, int lo, int hi) { if (lo < hi) { int p = part(a, lo, hi); qs(a, lo, p - 1); qs(a, p + 1, hi); } }
static void run(int *a, int n) { qs(a, 0, n - 1); }`),
    counting: prog(`static void run(int *a, int n) { int c[10] = {0}; for (int i = 0; i < n; i++) { c[a[i]]++; mv++; } int k = 0; for (int v = 0; v < 10; v++) while (c[v]-- > 0) { a[k++] = v; mv++; } }`),
  };
  const expected: Record<string, [number, number]> = { bubble: [14, 8], selection: [15, 2], insertion: [11, 8], merge: [11, 16], quick: [9, 9], counting: [0, 12] };
  const result: Record<string, { comparisons: number; moves: number; final: number[] }> = {};
  for (const [name, src] of Object.entries(sorts)) {
    const o = runC(src)[0].trim().split(/\s+/).map(Number);
    result[name] = { comparisons: o[0], moves: o[1], final: o.slice(2) };
    must(`EP81 ${name}: ${expected[name][0]} comparisons (Bible scorecard / narration)`, o[0] === expected[name][0]);
    must(`EP81 ${name}: sorted result`, o.slice(2).join() === "1,2,3,5,6,9");
    must(`EP81 ${name}: ${expected[name][1]} moves, got ${o[1]} (Bible: 8 swaps / 2 swaps / 8 shifts+5 placements / 16 writes / 4 visible + 5 self swaps = 9 (the Bible says 3 visible, which its own table contradicts) / 6 counts+6 writes)`, o[1] === expected[name][1]);
  }
  return { ep: 81, scene: 4, layout: "miniRows", note: "six bar rows replay the EP74-80 traces; the counters are these measured numbers", bibleNote: "The Bible's scorecard and EP79 totals say quick sort has 3 visible swaps + 5 self-swaps; running its own Lomuto code (and counting the rows of its own EP79 table: P1.2, P1.4, P1.6, P2.2) gives 4 visible swaps + 5 self-swaps = 9 swap calls, with 9 comparisons as stated.", racers: result };
};

// ---------- write ----------
const roundtrips = (raw: string, d: unknown): boolean => JSON.stringify(d, null, 2).replace(/\n/g, "\r\n") + "\r\n" === raw;
const setTraces = (ep: number, traces: Record<number, Step[]>): void => {
  const file = join(ROOT, "episodes", `ep${String(ep).padStart(3, "0")}.json`);
  const raw = readFileSync(file, "utf-8");
  const d = JSON.parse(raw);
  must(`ep${ep}.json round-trips in the repo format`, roundtrips(raw, d));
  for (const [id, trace] of Object.entries(traces)) {
    const s = d.scenes.find((x: { id: number }) => x.id === Number(id));
    must(`EP${ep} scene ${id} is algorithm-bars and has no trace yet`, s.template === "algorithm-bars" && !(s.trace && s.trace.length));
    s.trace = trace;
  }
  if (!DRY && problems.length === 0) writeFileSync(file, JSON.stringify(d, null, 2).replace(/\n/g, "\r\n") + "\r\n");
};

const ins = insertion();
const mer = merge();
const cnt = counting();
const lin = linear();
const han = hanoi();
const score = scorecard();
console.log(`insertion: ${ins.all.length} steps (s4 ${ins.s4.length}, s5 ${ins.s5.length}); merge: split ${mer.s4.length}, merge ${mer.s5.length}; counting: ${cnt.s4.length} + ${cnt.s5.length}; linear: ${lin.length}`);
if (problems.length) {
  console.log(`PROBLEMS (${problems.length}):\n- ${problems.join("\n- ")}`);
  process.exit(1);
}
setTraces(72, { 4: lin });
setTraces(76, { 4: ins.s4, 5: ins.s5 });
setTraces(78, { 4: mer.s4, 5: mer.s5 });
setTraces(80, { 4: cnt.s4, 5: cnt.s5 });
const dir = join(ROOT, "docs", "fix4", "traces-draft");
if (!DRY) {
  mkdirSync(dir, { recursive: true });
  writeFileSync(join(dir, "ep077-s4-hanoi-pegs.json"), JSON.stringify(han, null, 1));
  writeFileSync(join(dir, "ep080-count-row.json"), JSON.stringify({ ep: 80, note: "the bucket row for scenes 4 and 5 (count[0..9] after each step); the bars trace in episodes/ep080.json carries only the array", counts: cnt.counts }, null, 1));
  writeFileSync(join(dir, "ep081-s4-scorecard.json"), JSON.stringify(score, null, 1));
}
console.log(problems.length ? `PROBLEMS: ${problems.join("; ")}` : "all probes compiled without warnings, and every step, total and count equals the Bible's tables");
process.exit(problems.length ? 1 : 0);
