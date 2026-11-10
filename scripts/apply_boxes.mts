/**
 * Fix pass 5b: writes the `memory` data of the 14 blank memory-boxes scenes of EP41-50 into episodes/ep041..ep050.json.
 * The values come from docs/fix4/boxes-draft-ep41-50.json, which scripts/derive_boxes.mts makes from C probes that are
 * compiled with gcc and run. Before anything is written, every number the data shows is checked against the scene's own
 * narration and on-screen text, the episode challenge, and (for EP41 s7) a fresh gcc run, and the result is validated
 * with the zod schema (src/lib/memory.ts). JSON only: no Remotion.
 * Usage: node scripts/derive_boxes.mts && node scripts/apply_boxes.mts [--dry]
 */
import { spawnSync } from "node:child_process";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { MemoryDataSchema, type MemoryCell, type MemoryData, type MemoryFrame, type MemoryGroup } from "../src/lib/memory.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const DRY = process.argv.includes("--dry");

type DraftCell = { index?: number; value: string; address?: string; filled?: string; row?: number; col?: number };
type Draft = Record<string, unknown> & { ep: number; scene: number };
const drafts = JSON.parse(readFileSync(join(ROOT, "docs", "fix4", "boxes-draft-ep41-50.json"), "utf-8")) as Draft[];
const draftOf = (ep: number, scene: number): Draft => {
  const d = drafts.find((x) => x.ep === ep && x.scene === scene);
  if (!d) throw new Error(`no draft for EP${ep} s${scene}`);
  return d;
};

type EpFile = { path: string; raw: string; data: { ep: number; challenge: string; scenes: { id: number; onScreen: string; narration: string; memory?: MemoryData; boxes?: unknown[] }[] } };
const files = new Map<number, EpFile>();
const epFile = (ep: number): EpFile => {
  let f = files.get(ep);
  if (!f) {
    const path = join(ROOT, "episodes", `ep${String(ep).padStart(3, "0")}.json`);
    const raw = readFileSync(path, "utf-8");
    f = { path, raw, data: JSON.parse(raw) };
    files.set(ep, f);
  }
  return f;
};
const sceneOf = (ep: number, id: number) => epFile(ep).data.scenes.find((s) => s.id === id)!;

const problems: string[] = [];
const must = (label: string, ok: boolean): void => {
  if (!ok) problems.push(label);
};
const words = (s: string): string => s.replace(/\s+/g, " ").toLowerCase();

// ---------- small builders ----------
const cell = (c: DraftCell, extra: Partial<MemoryCell> = {}): MemoryCell => ({
  value: c.value,
  ...(c.index !== undefined ? { index: c.index } : {}),
  ...(c.address ? { address: c.address } : {}),
  ...extra,
});
const stopIfNul = (c: DraftCell): Partial<MemoryCell> => (c.value === "\\0" ? { mark: "stop" } : {});
const chars = (cells: DraftCell[], extra: (c: DraftCell, i: number) => Partial<MemoryCell> = () => ({})): MemoryCell[] =>
  cells.map((c, i) => cell(c, { ...stopIfNul(c), ...extra(c, i) }));
const group = (name: string | undefined, cells: MemoryCell[], more: Partial<MemoryGroup> = {}): MemoryGroup => ({ ...(name ? { name } : {}), ...more, cells });
const frame = (groups: MemoryGroup[], more: Partial<MemoryFrame> = {}): MemoryFrame => ({ ...more, groups });

const out = new Map<string, MemoryData>();
const put = (ep: number, scene: number, frames: MemoryFrame[]): void => {
  const parsed = MemoryDataSchema.safeParse({ frames });
  if (!parsed.success) {
    problems.push(`EP${ep} s${scene}: schema: ${parsed.error.issues.map((i) => `${i.path.join(".")} ${i.message}`).join("; ")}`);
    return;
  }
  out.set(`${ep}.${scene}`, parsed.data);
};

// gcc for the two facts of EP41 s7 that are not in the draft: the compiler's error for `b = a;` and the copy loop.
const gcc = (source: string, run: boolean): { ok: boolean; text: string } => {
  const dir = join(tmpdir(), "koding-apply-boxes");
  mkdirSync(dir, { recursive: true });
  const c = join(dir, `x${Math.random().toString(36).slice(2)}.c`);
  writeFileSync(c, source);
  const cc = spawnSync("gcc", ["-Wall", "-Wextra", "-D__USE_MINGW_ANSI_STDIO=1", "-o", `${c}.exe`, c], { encoding: "utf-8" });
  if (cc.status !== 0 || !run) return { ok: cc.status === 0, text: cc.stderr };
  return { ok: true, text: spawnSync(`${c}.exe`, { encoding: "utf-8" }).stdout.trim() };
};

// ---------- EP41 ----------
{
  const d = draftOf(41, 4) as unknown as { name: string; badge: string; highlightIndex: number; cells: DraftCell[] };
  const s = sceneOf(41, 4);
  must("EP41 s4: five boxes (scene text)", d.cells.length === 5 && /five boxes/.test(s.onScreen) && /marks\[5\]/.test(s.onScreen));
  must("EP41 s4: size 5, last index 4 (narration)", /size five, last index four/i.test(s.narration));
  put(41, 4, [frame([group("marks[5]", d.cells.map((c, i) => cell(c, i === d.highlightIndex ? { mark: "hl" } : {})))], { badges: [d.badge] })]);
}
{
  const d = draftOf(41, 7) as unknown as { arrays: { name: string; cells: DraftCell[] }[] };
  const [a, b] = d.arrays;
  const s = sceneOf(41, 7);
  must("EP41 s7: a is 1 2 0 0 0 and b has size 3 (scene text)", a.cells.map((c) => c.value).join(" ") === "1 2 0 0 0" && b.cells.length === 3 && /fills 1 2 0 0 0/.test(s.onScreen) && /size 3/.test(s.onScreen));
  const err = gcc("int main(void) { int a[5] = {1, 2}; int b[] = {4, 5, 6}; b = a; return 0; }", false);
  must("EP41 s7: gcc rejects `b = a;` with an array-type error", !err.ok && /assignment to expression with array type/.test(err.text));
  const copy = gcc('#include <stdio.h>\nint main(void) { int a[5] = {1, 2}; int b[] = {4, 5, 6}; for (int i = 0; i < 3; i++) b[i] = a[i]; for (int i = 0; i < 3; i++) printf("%d ", b[i]); return 0; }', true);
  const copied = copy.text.trim().split(" ");
  must("EP41 s7: the copy loop gives 1 2 0 (gcc run)", copied.join() === "1,2,0");
  const aCells = a.cells.map((c) => cell(c, c.filled === "zero" ? { mark: "zero" } : {}));
  const bCells = b.cells.map((c) => cell(c));
  const gA = group("a[5]", aCells);
  put(41, 7, [
    frame([gA, group("b[] (size 3)", bCells)], { label: "int a[5] = {1, 2};   int b[] = {4, 5, 6};" }),
    frame([gA, group("b[] (size 3)", bCells)], { label: "b = a;   error: assignment to expression with array type" }),
    frame([gA, group("b[] (size 3)", copied.map((v, i) => ({ value: v, index: i, address: b.cells[i].address, mark: "hl" as const })))], { label: "copy one box at a time: b[i] = a[i]" }),
  ]);
}

// ---------- EP44 ----------
for (const sc of [4, 5]) {
  const d = draftOf(44, sc) as unknown as { steps: { label: string; boxes: { name: string; value: string; address: string }[]; lost?: { box: string; value: string } }[] };
  const s = sceneOf(44, sc);
  if (sc === 4) {
    must("EP44 s4: a is 10 and b is 20, both end as 20 (narration)", /a equals 10 and b equals 20/.test(s.narration) && d.steps[2].boxes.every((b) => b.value === "20") && /both are 20/i.test(s.narration));
  } else {
    const last = d.steps[3].boxes;
    must("EP44 s5: a and b swapped through temp (narration: three steps)", last[0].value === "20" && last[1].value === "10" && /step one/i.test(s.narration) && /step three/i.test(s.narration));
  }
  put(
    44,
    sc,
    d.steps.map((st, k) =>
      frame(
        [group(undefined, st.boxes.map((b) => ({ value: b.value, name: b.name, address: b.address, ...(st.lost && st.lost.box === b.name ? { lost: st.lost.value } : {}) })))],
        { label: sc === 5 && k > 0 ? `step ${k}: ${st.label.replace(/^\d: /, "")}` : st.label },
      ),
    ),
  );
}

// ---------- EP45 ----------
{
  const d = draftOf(45, 4) as unknown as { rows: number; cols: number; cells: (DraftCell & { flatIndex: number })[] };
  const s = sceneOf(45, 4);
  must("EP45 s4: 3 rows x 4 columns = 12 boxes (scene text and narration)", d.rows === 3 && d.cols === 4 && d.cells.length === 12 && /12 boxes/.test(s.onScreen) && /twelve boxes/i.test(s.narration));
  put(45, 4, [
    frame([group("seats[3][4]", d.cells.map((c) => cell(c, { index: `[${c.row}][${c.col}]` })), { cols: 4 })], { label: "drawn as a grid: 3 rows, 4 columns" }),
    frame([group("in memory: one long line", d.cells.map((c) => cell(c, { index: c.flatIndex })))], { label: "stored row 0, then row 1, then row 2" }),
  ]);
}
{
  const d = draftOf(45, 7) as unknown as { a: number[][]; b: number[][]; sum: number[][] };
  const e = epFile(45).data;
  must("EP45 s7: a = 1 2 3 / 4 5 6 and b = 6 5 4 / 3 2 1 equal the challenge text", /a is 1 2 3, 4 5 6/i.test(e.challenge.replace(/\s+/g, " ")) || /a = \{1 2 3, 4 5 6\}/.test(e.challenge));
  must("EP45 s7: every sum is 7 (the challenge says all sevens)", d.sum.flat().every((v) => v === 7));
  const grid = (name: string, m: number[][], fill?: MemoryCell["mark"], shown = true): MemoryGroup =>
    group(name, m.flatMap((r, ri) => r.map((v, ci) => ({ value: shown ? String(v) : "?", index: `[${ri}][${ci}]`, ...(fill ? { mark: fill } : {}) }))), { cols: 3 });
  put(45, 7, [
    frame([grid("a", d.a), grid("b", d.b), grid("sum", d.sum, undefined, false)], { arrange: "row", joiners: ["+", "="], label: "sum[r][c] = a[r][c] + b[r][c], cell by cell" }),
    frame([grid("a", d.a), grid("b", d.b), grid("sum", d.sum, "hl")], { arrange: "row", joiners: ["+", "="], label: "every cell: 7" }),
  ]);
}

// ---------- EP46 ----------
{
  const d = draftOf(46, 4) as unknown as { name: string; badges: string[]; cells: DraftCell[] };
  const s = sceneOf(46, 4);
  must("EP46 s4: 20 bytes, 4 bytes, 20 / 4 = 5 (scene text) and five boxes", d.badges[0].includes("= 20") && d.badges[1].includes("= 4") && d.badges[2] === "20 / 4 = 5" && d.cells.length === 5 && /= 20 bytes/.test(s.onScreen) && /= 5$/.test(s.onScreen.trim()));
  put(46, 4, [frame([group("marks", d.cells.map((c) => cell(c)), { ruler: { each: "4 bytes", total: "20 bytes" } })], { badges: d.badges })]);
}
{
  const d = draftOf(46, 7) as unknown as { tags: string[]; before: DraftCell[]; after: DraftCell[] };
  const s = sceneOf(46, 7);
  const bonuses = new Set(d.after.map((c, i) => Number(c.value) - Number(d.before[i].value)));
  must("EP46 s7: every locker changed by the same bonus (the addBonus call)", bonuses.size === 1 && [...bonuses][0] > 0);
  must("EP46 s7: two name tags on the same lockers (narration)", /two name tags on the same row of lockers/i.test(s.narration));
  const bonus = [...bonuses][0];
  put(46, 7, [
    frame([group(undefined, d.before.map((c) => cell(c)), { tags: d.tags })], { label: "main's marks and the function's arr: the same lockers" }),
    frame([group(undefined, d.after.map((c) => cell(c, { mark: "hl" })), { tags: d.tags })], { label: `addBonus(marks, n, ${bonus}) changes them through arr; marks sees it` }),
  ]);
}

// ---------- EP47 ----------
{
  const d = draftOf(47, 3) as unknown as { cells: DraftCell[] };
  const s = sceneOf(47, 3);
  const letters = [...s.onScreen.matchAll(/'(\\0|[^'])'/g)].map((m) => m[1]);
  must("EP47 s3: the six boxes are the letters on screen", d.cells.map((c) => c.value).join() === letters.map((l) => (l === "\\0" ? "\\0" : l)).join() && d.cells.length === 6);
  put(47, 3, [frame([group("word[6]", chars(d.cells))], { label: "one letter per box; the last box holds \\0" })]);
}
{
  const d = draftOf(47, 4) as unknown as { cells: DraftCell[] };
  const s = sceneOf(47, 4);
  must('EP47 s4: "Panjim" in 7 boxes, last is \\0 (scene text)', d.cells.length === 7 && /7 boxes/.test(s.onScreen) && d.cells[6].value === "\\0" && d.cells.slice(0, 6).map((c) => c.value).join("") === "Panjim");
  put(47, 4, [frame([group('"Panjim"', chars(d.cells))], { label: "\\0 is the stop sign: printf keeps printing until it hits it" })]);
}

// ---------- EP48 ----------
{
  const d = draftOf(48, 3) as unknown as { cells: DraftCell[]; taken: string; left: string };
  const s = sceneOf(48, 3);
  const typed = d.cells.map((c) => c.value).join("");
  must("EP48 s3: the buffer is the keys on screen (A t r e y a _ K a m a t \\n)", /A t r e y a _ K a m a t \\n/.test(s.onScreen) && typed === "Atreya␠Kamat\\n");
  must('EP48 s3: scanf takes "Atreya" and leaves " Kamat\\n" (narration)', d.taken === "Atreya" && d.left === " Kamat\\n" && /takes Atreya, and leaves space Kamat newline/i.test(s.narration));
  const taken = d.taken.length;
  put(48, 3, [
    frame([group("input buffer", d.cells.map((c, i) => cell(c, { index: i })))], { label: "you type Atreya Kamat and press Enter" }),
    frame([group("input buffer", d.cells.map((c, i) => cell(c, { index: i, ...(i < taken ? { mark: "taken" as const } : {}) })))], { label: 'scanf("%s") takes "Atreya"; " Kamat\\n" is left waiting' }),
  ]);
}

// ---------- EP49 ----------
{
  const d = draftOf(49, 4) as unknown as { cells: DraftCell[] };
  const s = sceneOf(49, 4);
  must('EP49 s4: "Xecxec" in 7 boxes, strlen 6, sizeof 7 (scene text and narration)', d.cells.length === 7 && /7 boxes/.test(s.onScreen) && /strlen counts 6/.test(s.onScreen) && /strlen of Xecxec is six, while sizeof the array is seven/i.test(words(s.narration)));
  put(49, 4, [
    frame([group("second[]", chars(d.cells, (_c, i) => ({ index: i })))], { label: 'char second[] = "Xecxec";' }),
    frame([group("second[]", chars(d.cells, (_c, i) => (i < 6 ? { index: i, mark: "taken" as const } : { index: i })))], { badges: ["strlen = 6", "sizeof = 7"], label: "strlen counts letters up to \\0; the \\0 itself is not counted" }),
  ]);
}
{
  const d = draftOf(49, 5) as unknown as { steps: { label: string; copy: string; first: string; nulAt?: { copy: number; first: number } }[] };
  const s = sceneOf(49, 5);
  must("EP49 s5: strcpy then strcat, first ends as 'Crab Xecxec' (narration and the sample's own output)", /strcpy/.test(s.narration) && /strcat/.test(s.narration) && d.steps[d.steps.length - 1].first === "Crab Xecxec");
  const SHOWN = 12;
  const boxes = (text: string, nul: number | undefined, fillBeyond: string): MemoryCell[] =>
    Array.from({ length: SHOWN }, (_, i) =>
      nul === undefined
        ? { value: "?", index: i, mark: "zero" as const }
        : i < nul
          ? { value: text[i] === " " ? "␠" : text[i], index: i }
          : i === nul
            ? { value: "\\0", index: i, mark: "stop" as const }
            : { value: fillBeyond, index: i, mark: "zero" as const },
    );
  put(
    49,
    5,
    d.steps.map((st, k) => {
      const copyNul = k === 0 ? undefined : st.nulAt?.copy;
      const firstNul = k === 0 ? st.first.length : st.nulAt?.first;
      return frame([group("first[20]", boxes(st.first, firstNul, "\\0")), group("copy[20]", boxes(st.copy, copyNul, "?"))], {
        label: k === 0 ? 'first = "Crab", copy not set yet (first 12 of 20 boxes shown)' : st.label,
      });
    }),
  );
}

// ---------- EP50 ----------
{
  const d = draftOf(50, 3) as unknown as { word: DraftCell[]; rev: DraftCell[]; arrows: { from: number; to: number }[] };
  const s = sceneOf(50, 3);
  must('EP50 s3: "feni" (narration), 4 letters, arrows pair i with len - 1 - i', /Take feni\. Length four/.test(s.narration) && d.word.length === 5 && d.arrows.length === 4 && d.arrows.every((a) => a.from + a.to === 3));
  must("EP50 s3: rev reads i n e f", d.rev.slice(0, 4).map((c) => c.value).join("") === "inef");
  put(50, 3, [
    {
      label: "rev[i] = word[len - 1 - i]",
      groups: [group("word", chars(d.word, (_c, i) => ({ index: i }))), group("rev", chars(d.rev, (_c, i) => ({ index: i })))],
      arrows: d.arrows.map((a) => ({ from: `0:${a.from}`, to: `1:${a.to}` })),
    },
  ]);
}

// ---------- write ----------
must("all 14 scenes built", out.size === 14);
const REPO_FORMAT = (d: unknown): string => JSON.stringify(d, null, 2).replace(/\n/g, "\r\n") + "\r\n";
for (const f of files.values()) must(`${f.path.split(/[\\/]/).pop()} round-trips in the repo format`, REPO_FORMAT(f.data) === f.raw);
if (problems.length) {
  console.log(`PROBLEMS (${problems.length}):\n- ${problems.join("\n- ")}`);
  process.exit(1);
}
for (const [key, memory] of out) {
  const [ep, scene] = key.split(".").map(Number);
  const s = sceneOf(ep, scene);
  must(`EP${ep} s${scene} has no flat boxes (memory is written over, so the script can be re-run)`, !s.boxes?.length);
  s.memory = memory;
}
if (problems.length) {
  console.log(`PROBLEMS: ${problems.join("; ")}`);
  process.exit(1);
}
if (!DRY) for (const f of files.values()) writeFileSync(f.path, REPO_FORMAT(f.data));
console.log(`${DRY ? "dry run: " : ""}memory data for ${out.size} scenes in ${files.size} episodes (EP${[...files.keys()].join(", EP")}); every number matches its scene text, the gcc runs and the schema`);
