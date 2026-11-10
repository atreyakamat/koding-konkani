/**
 * Fix pass 5c: MemoryBoxes `memory` data for the three blank memory-boxes scenes of EP37-39 (EP37 s4 scope and
 * lifetime, EP38 s5 call by value, EP39 s6 the call stack). Every value comes out of a C program that is COMPILED AND
 * RUN with gcc: the episode's own sample must reproduce its `code.output`, and a probe (the same program with printf
 * added) gives the values of each step. Every number the scene narrates (5 and 9, 1 2 6 24, ...) must be in the data.
 * Then the data is checked against the zod schema and written (idempotent) in the repo's JSON format. JSON only.
 * Usage: node scripts/apply_boxes_37_39.mts [--dry]
 */
import { spawnSync } from "node:child_process";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { MemoryDataSchema, type MemoryData, type MemoryFrame } from "../src/lib/memory.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const DRY = process.argv.includes("--dry");
const NL = String.fromCharCode(10);
const BS = String.fromCharCode(92);

type Sc = { id: number; narration: string; onScreen: string; code?: { source: string; output?: string }; memory?: MemoryData; boxes?: unknown[] };
type EpData = { ep: number; scenes: Sc[] };
const files = new Map<number, { path: string; raw: string; data: EpData }>();
const load = (ep: number): EpData => {
  let f = files.get(ep);
  if (!f) {
    const path = join(ROOT, "episodes", `ep${String(ep).padStart(3, "0")}.json`);
    const raw = readFileSync(path, "utf-8");
    f = { path, raw, data: JSON.parse(raw) as EpData };
    files.set(ep, f);
  }
  return f.data;
};
const sceneOf = (ep: number, id: number): Sc => load(ep).scenes.find((s) => s.id === id)!;
const problems: string[] = [];
const must = (label: string, ok: boolean): void => {
  if (!ok) problems.push(label);
};
const squash = (s: string): string => s.replace(/\s+/g, " ").toLowerCase();
const lines = (s: string): string[] => s.trim().split(/\r?\n/);

const dir = join(tmpdir(), "koding-boxes-37-39");
mkdirSync(dir, { recursive: true });
let probeNo = 0;
/** Compiles with -Wall -Wextra and runs; returns stdout lines. A warning is a problem. */
const run = (source: string): string[] => {
  const base = join(dir, `p${probeNo++}`);
  writeFileSync(`${base}.c`, source);
  const cc = spawnSync("gcc", ["-Wall", "-Wextra", "-D__USE_MINGW_ANSI_STDIO=1", "-o", `${base}.exe`, `${base}.c`], { encoding: "utf-8" });
  if (cc.status !== 0 || cc.stderr.trim()) {
    problems.push(`gcc: ${cc.stderr.trim().split(NL)[0]}`);
    return [];
  }
  return lines(spawnSync(`${base}.exe`, { encoding: "utf-8" }).stdout);
};
const ints = (s: string): number[] => (s.match(/-?\d+/g) ?? []).map(Number);
/** A probe printf format line: printf("fmt\n", args). */
const pf = (fmt: string, args: string): string => `  printf("${fmt}${BS}n", ${args});`;

const BASE = 0x7ffd1a2c3f00;
const addr = (offset: number): string => `0x${(BASE + offset).toString(16)}`;
const out = new Map<string, MemoryData>();
const put = (ep: number, scene: number, frames: MemoryFrame[]): void => {
  const parsed = MemoryDataSchema.safeParse({ frames });
  if (!parsed.success) problems.push(`EP${ep} s${scene}: schema: ${parsed.error.issues.map((i) => `${i.path.join(".")} ${i.message}`).join("; ")}`);
  else out.set(`${ep}.${scene}`, parsed.data);
};

// ---------- EP37 s4: local / global / static ----------
{
  const code = sceneOf(37, 5).code!;
  const own = run(code.source);
  must("EP37: the sample reproduces its output", own.join(NL) === lines(code.output!).join(NL));
  const rows = own.map(ints); // Basket, Total | Basket, Total | visits, fresh x3
  const [b1, t1] = rows[0];
  const [b2, t2] = rows[1];
  const visits = [rows[2][0], rows[3][0], rows[4][0]];
  const fresh = [rows[2][1], rows[3][1], rows[4][1]];
  const s = sceneOf(37, 4);
  const text = squash(`${s.narration} ${s.onScreen}`);
  must("EP37 s4: local, global and static scopes named", /local variable/.test(text) && /global variable/.test(text) && /static/.test(text));
  must("EP37 s4: a brand-new local on the second call", /brand-new/.test(text));
  must("EP37 s4: values 5,5 / 3,8 / visits 1 2 3 / fresh always 1", b1 === 5 && t1 === 5 && b2 === 3 && t2 === 8 && visits.join() === "1,2,3" && fresh.join() === "1,1,1");
  const visit = (call: number, label: string) => ({
    label,
    groups: [
      {
        name: `visit(), call ${call + 1}`,
        cells: [
          { name: "visits", value: String(visits[call]), address: addr(96), mark: "hl" as const },
          { name: "fresh", value: String(fresh[call]), address: addr(0) },
        ],
      },
    ],
  });
  put(37, 4, [
    { label: "local: made when the function is called", groups: [{ name: "addFish(5)", cells: [{ name: "basket", value: String(b1), address: addr(0) }] }] },
    { label: "it is destroyed on return; call again and you get a brand-new basket", groups: [{ name: "addFish(3)", cells: [{ name: "basket", value: String(b2), address: addr(0) }] }] },
    { label: "global: made outside every function, it lives for the whole program", groups: [{ name: "global", cells: [{ name: "total", value: String(t2), address: addr(64) }] }] },
    visit(0, "static: set up once, keeps its value between calls"),
    visit(1, "call 2: visits remembers, fresh starts over"),
    visit(2, "call 3: visits = 3, fresh is a new 1 again"),
  ]);
}

// ---------- EP38 s5: call by value ----------
{
  const code = sceneOf(38, 4).code!;
  const own = run(code.source);
  must("EP38: the sample reproduces its output", own.join(NL) === lines(code.output!).join(NL));
  const probe = [
    "#include <stdio.h>",
    "void swap(int a, int b) {",
    pf("in %d %d", "a, b"),
    "  int temp = a;",
    "  a = b;",
    "  b = temp;",
    pf("out %d %d %d", "a, b, temp"),
    "}",
    "int main(void) {",
    "  int x = 5, y = 9;",
    "  swap(x, y);",
    pf("main %d %d", "x, y"),
    "  return 0;",
    "}",
    "",
  ].join(NL);
  const p = run(probe).map(ints);
  const [ia, ib] = p[0];
  const [oa, ob, ot] = p[1];
  const [mx, my] = p[2];
  const s = sceneOf(38, 5);
  const text = squash(`${s.narration} ${s.onScreen}`);
  must("EP38 s5: x = 5, y = 9; the values 5 and 9 are copied", /x=5, y=9/.test(text) && /values 5 and 9 are copied/.test(text));
  must("EP38 s5: copied 5 and 9, swapped to 9 and 5, main unchanged", ia === 5 && ib === 9 && oa === 9 && ob === 5 && ot === 5 && mx === 5 && my === 9);
  must("EP38 s5: swap's boxes are thrown away", /thrown away/.test(text));
  const main = { name: "main", cells: [{ name: "x", value: String(mx), address: addr(0) }, { name: "y", value: String(my), address: addr(4) }] };
  const swapCells = (a: string, b: string, t: string) => [
    { name: "a", value: a, address: addr(-64) },
    { name: "b", value: b, address: addr(-60) },
    { name: "temp", value: t, address: addr(-56) },
  ];
  put(38, 5, [
    { label: "main has two boxes, x and y", groups: [main] },
    { label: "swap is called: the values 5 and 9 are copied into a and b", groups: [main, { name: "swap", cells: swapCells(String(ia), String(ib), "?") }], arrows: [{ from: "0:0", to: "1:0" }, { from: "0:1", to: "1:1" }] },
    { label: "inside swap: temp = a; a = b; b = temp;", groups: [main, { name: "swap", cells: swapCells(String(oa), String(ob), String(ot)) }] },
    { label: "swap ends: its boxes are thrown away; x and y never changed", groups: [main] },
  ]);
}

// ---------- EP39 s6: the call stack ----------
{
  const code = sceneOf(39, 4).code!;
  const own = run(code.source);
  must("EP39: the sample reproduces its output", own.join(NL) === lines(code.output!).join(NL));
  const probe = [
    "#include <stdio.h>",
    "int factorial(int n) {",
    "  int r = n <= 1 ? 1 : n * factorial(n - 1);",
    pf("%d %d", "n, r"),
    "  return r;",
    "}",
    "int main(void) {",
    "  factorial(4);",
    "  return 0;",
    "}",
    "",
  ].join(NL);
  const ret = new Map(run(probe).map(ints).map(([k, r]) => [k, r] as const)); // n -> its return value
  const s = sceneOf(39, 6);
  const text = squash(`${s.narration} ${s.onScreen}`);
  must("EP39 s6: returns 1, 2, 6, 24 (gcc run, scene on-screen text)", [1, 2, 6, 24].every((v, i) => ret.get(i + 1) === v) && /1, 2, 6, 24/.test(text));
  must("EP39 s6: plates, base case, and 24 goes back to main", /plate/.test(text) && /base case/.test(text) && /24 goes back to main/.test(text));
  const plate = (k: number, hl: boolean) => ({ name: `factorial(${k})`, value: `n = ${k}`, ...(hl ? { mark: "hl" as const } : {}) });
  /** The stack from the bottom (factorial(4)) up to `top`; the top plate is highlighted. */
  const stack = (top: number) => ({ name: "call stack (bottom to top)", cells: Array.from({ length: 5 - top }, (_v, i) => plate(4 - i, 4 - i === top)) });
  put(39, 6, [
    { label: "factorial(4) is called: a plate goes on the stack with its own n", groups: [stack(4)] },
    { label: "it calls factorial(3): another plate on top", groups: [stack(3)] },
    { label: "then factorial(2)", groups: [stack(2)] },
    { label: "then factorial(1): the base case", groups: [stack(1)] },
    { label: `factorial(1) returns ${ret.get(1)}; factorial(2) returns 2 × 1 = ${ret.get(2)}; those plates come off`, badges: [`return ${ret.get(1)}`, `return ${ret.get(2)}`], groups: [stack(3)] },
    { label: `3 × 2 = ${ret.get(3)}, then 4 × ${ret.get(3)} = ${ret.get(4)}: the last plate comes off and ${ret.get(4)} goes back to main`, badges: [`return ${ret.get(3)}`, `return ${ret.get(4)} to main`], groups: [stack(4)] },
  ]);
}

const REPO_FORMAT = (d: unknown): string => JSON.stringify(d, null, 2).replace(/\n/g, "\r\n") + "\r\n";
must("all 3 scenes built", out.size === 3);
for (const f of files.values()) must(`${f.path.split(/[\\/]/).pop()} round-trips in the repo format`, REPO_FORMAT(f.data) === f.raw);
if (problems.length) {
  console.log(`PROBLEMS (${problems.length}):${NL}- ${problems.join(`${NL}- `)}`);
  process.exit(1);
}
for (const [key, memory] of out) {
  const [ep, scene] = key.split(".").map(Number);
  const s = sceneOf(ep, scene);
  must(`EP${ep} s${scene} has no flat boxes`, !s.boxes?.length);
  s.memory = memory;
}
if (problems.length) {
  console.log(`PROBLEMS: ${problems.join("; ")}`);
  process.exit(1);
}
if (!DRY) for (const f of files.values()) writeFileSync(f.path, REPO_FORMAT(f.data));
console.log(`${DRY ? "dry run: " : ""}memory data for ${out.size} scenes (EP37 s4, EP38 s5, EP39 s6); numbers match the scene text, the gcc runs and the schema`);
