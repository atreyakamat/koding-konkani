/**
 * Fix pass 5b, on paper: derives MemoryBoxes data for the 14 blank memory-boxes scenes of EP41-50 from the
 * episode's own code samples, the scene's on-screen text and narration, and the episode's challenge text.
 * Every value comes out of a C probe program that is COMPILED AND RUN with GCC (so the declarations, zero fill,
 * sizeof and string functions are what a real compiler does), then cross-checked against the numbers the scene
 * itself states (sizeof 20/4/5, strlen 6, 7 boxes for "Panjim", ...).
 * Writes JSON only (docs/fix4/boxes-draft-ep41-50.json); episodes/*.json are not touched, no Remotion.
 * Usage: node scripts/derive_boxes.mts
 */
import { execFileSync, spawnSync } from "node:child_process";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { tmpdir } from "node:os";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const WORK = join(tmpdir(), "koding-boxes-probe");
mkdirSync(WORK, { recursive: true });

type Ep = { ep: number; challenge: string; scenes: { id: number; onScreen: string; narration: string; code?: { source: string } }[] };
const load = (n: number): Ep => JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
const scene = (e: Ep, id: number) => e.scenes.find((s) => s.id === id)!;
const sample = (e: Ep, id: number): string => scene(e, id).code?.source ?? "";

/** Compiles and runs a probe with GCC; returns its stdout lines. */
let probeNo = 0;
const runC = (source: string): string[] => {
  const base = join(WORK, `p${probeNo++}`);
  writeFileSync(`${base}.c`, source);
  const cc = spawnSync("gcc", ["-Wall", "-Wextra", "-D__USE_MINGW_ANSI_STDIO=1", "-o", `${base}.exe`, `${base}.c`], { encoding: "utf-8" });
  if (cc.status !== 0) throw new Error(`gcc failed for probe ${probeNo - 1}: ${cc.stderr}`);
  if (cc.stderr.trim()) compilerWarnings.push(`probe ${probeNo - 1}: ${cc.stderr.trim().split(/\r?\n/)[0]}`);
  return execFileSync(`${base}.exe`, { encoding: "utf-8" }).trim().split(/\r?\n/);
};

const BASE = 0x7ffd1a2c3f00;
const addr = (offset: number): string => `0x${(BASE + offset).toString(16)}`;
const nums = (s: string): number[] => (s.match(/-?\d+/g) ?? []).map(Number);
const fail: string[] = [];
const compilerWarnings: string[] = [];
const check = (label: string, ok: boolean): void => {
  if (!ok) fail.push(label);
};

type Draft = { ep: number; scene: number; layout: string; [k: string]: unknown };
const drafts: Draft[] = [];

// ---------- EP41 ----------
const e41 = load(41);
{
  const m = /int\s+marks\[(\d+)\]\s*=\s*\{([^}]*)\}/.exec(sample(e41, 5))!;
  const probe = `#include <stdio.h>\nint main(void) {\n  int marks[${m[1]}] = {${m[2]}};\n  for (int i = 0; i < ${m[1]}; i++) printf("%d\\n", marks[i]);\n  printf("%zu %zu\\n", sizeof(marks), sizeof(marks[0]));\n  return 0;\n}\n`;
  const out = runC(probe);
  const values = out.slice(0, Number(m[1]));
  check("EP41 s4 size 5 / last index 4", values.length === 5);
  drafts.push({
    ep: 41, scene: 4, layout: "cells", name: "marks", badge: `size ${values.length}, last index ${values.length - 1}`, highlightIndex: 0,
    cells: values.map((v, i) => ({ index: i, value: v, address: addr(4 * i) })),
    derivedFrom: "ep41 scene 5 code, line 4 (int marks[5] = {...})", probe,
  });
}
{
  const t = scene(e41, 7).onScreen;
  const a = /\{([^}]*)\}\s*into\s*(\w)\[(\d+)\]/.exec(t)!;
  const b = /(\w)\[\]\s*=\s*\{([^}]*)\}/.exec(t)!;
  const probe = `#include <stdio.h>\nint main(void) {\n  int ${a[2]}[${a[3]}] = {${a[1]}};\n  int ${b[1]}[] = {${b[2]}};\n  for (int i = 0; i < ${a[3]}; i++) printf("%d\\n", ${a[2]}[i]);\n  printf("size %zu\\n", sizeof(${b[1]}) / sizeof(${b[1]}[0]));\n  for (int i = 0; i < (int)(sizeof(${b[1]}) / sizeof(${b[1]}[0])); i++) printf("%d\\n", ${b[1]}[i]);\n  return 0;\n}\n`;
  const out = runC(probe);
  const av = out.slice(0, Number(a[3]));
  const size = Number(out[Number(a[3])].replace("size ", ""));
  const bv = out.slice(Number(a[3]) + 1);
  check("EP41 s7 a is 1 2 0 0 0", av.join(" ") === "1 2 0 0 0");
  check("EP41 s7 b has size 3", size === 3 && bv.length === 3);
  const given = nums(a[1]).length;
  drafts.push({
    ep: 41, scene: 7, layout: "cells",
    arrays: [
      { name: a[2], cells: av.map((v, i) => ({ index: i, value: v, address: addr(4 * i), filled: i >= given ? "zero" : "given" })) },
      { name: b[1], cells: bv.map((v, i) => ({ index: i, value: v, address: addr(64 + 4 * i) })), note: `the compiler counts: size ${size}` },
    ],
    then: "b = a;  (GCC error: arrays cannot be assigned) -> copy loop, values hop box to box",
    derivedFrom: "scene on-screen text: {1, 2} into a[5]; b[] = {4, 5, 6}", probe,
  });
}

// ---------- EP44 ----------
const e44 = load(44);
{
  const m = /(\w) equals (\d+) and (\w) equals (\d+)/.exec(scene(e44, 4).narration)!;
  const [va, vb] = [Number(m[2]), Number(m[4])];
  const probe = `#include <stdio.h>\nint main(void) {\n  int ${m[1]} = ${va}, ${m[3]} = ${vb};\n  printf("%d %d\\n", ${m[1]}, ${m[3]});\n  ${m[1]} = ${m[3]};\n  printf("%d %d\\n", ${m[1]}, ${m[3]});\n  ${m[3]} = ${m[1]};\n  printf("%d %d\\n", ${m[1]}, ${m[3]});\n  return 0;\n}\n`;
  const out = runC(probe).map((l) => l.split(" "));
  check("EP44 s4 both end as 20", out[2][0] === "20" && out[2][1] === "20");
  drafts.push({
    ep: 44, scene: 4, layout: "scalars",
    steps: [
      { label: `${m[1]} = ${va}, ${m[3]} = ${vb}`, boxes: [{ name: m[1], value: out[0][0], address: addr(0) }, { name: m[3], value: out[0][1], address: addr(4) }] },
      { label: `${m[1]} = ${m[3]};`, boxes: [{ name: m[1], value: out[1][0], address: addr(0) }, { name: m[3], value: out[1][1], address: addr(4) }], lost: { box: m[1], value: String(va) } },
      { label: `${m[3]} = ${m[1]};`, boxes: [{ name: m[1], value: out[2][0], address: addr(0) }, { name: m[3], value: out[2][1], address: addr(4) }] },
    ],
    derivedFrom: "scene narration: a equals 10 and b equals 20", probe,
  });
  const probe2 = `#include <stdio.h>\nint main(void) {\n  int ${m[1]} = ${va}, ${m[3]} = ${vb}, temp;\n  printf("%d %d\\n", ${m[1]}, ${m[3]});\n  temp = ${m[1]};\n  printf("%d %d %d\\n", ${m[1]}, ${m[3]}, temp);\n  ${m[1]} = ${m[3]};\n  printf("%d %d %d\\n", ${m[1]}, ${m[3]}, temp);\n  ${m[3]} = temp;\n  printf("%d %d %d\\n", ${m[1]}, ${m[3]}, temp);\n  return 0;\n}\n`;
  const o2 = runC(probe2).map((l) => l.split(" "));
  check("EP44 s5 swapped", o2[3][0] === String(vb) && o2[3][1] === String(va));
  const box = (r: string[]) => [{ name: m[1], value: r[0], address: addr(0) }, { name: m[3], value: r[1], address: addr(4) }, { name: "temp", value: r[2] ?? "?", address: addr(8) }];
  drafts.push({
    ep: 44, scene: 5, layout: "scalars",
    steps: [
      { label: "start", boxes: box([...o2[0], "?"]) },
      { label: `1: temp = ${m[1]};`, boxes: box(o2[1]) },
      { label: `2: ${m[1]} = ${m[3]};`, boxes: box(o2[2]) },
      { label: `3: ${m[3]} = temp;`, boxes: box(o2[3]) },
    ],
    note: "the narration pours kokum and feni; the glasses are a, b and temp",
    derivedFrom: "scene 4's values (10, 20) and the three-step swap named in the narration", probe: probe2,
  });
}

// ---------- EP45 ----------
const e45 = load(45);
{
  const m = /int\s+seats\[(\d+)\]\[(\d+)\]\s*=\s*(\{[\s\S]*?\});/.exec(sample(e45, 5))!;
  const [R, C] = [Number(m[1]), Number(m[2])];
  const probe = `#include <stdio.h>\nint main(void) {\n  int seats[${R}][${C}] = ${m[3]};\n  for (int r = 0; r < ${R}; r++) for (int c = 0; c < ${C}; c++) printf("%d\\n", seats[r][c]);\n  int *flat = &seats[0][0];\n  for (int k = 0; k < ${R * C}; k++) printf("flat %d\\n", flat[k]);\n  printf("%zu\\n", sizeof(seats));\n  return 0;\n}\n`;
  const out = runC(probe);
  const grid = out.slice(0, R * C);
  const flat = out.slice(R * C, 2 * R * C).map((l) => l.replace("flat ", ""));
  check("EP45 s4 grid order equals memory order", grid.join() === flat.join());
  check("EP45 s4 sizeof = 12 ints", Number(out[2 * R * C]) === 12 * 4);
  drafts.push({
    ep: 45, scene: 4, layout: "grid", name: "seats", rows: R, cols: C,
    cells: grid.map((v, k) => ({ row: Math.floor(k / C), col: k % C, flatIndex: k, value: v, address: addr(4 * k) })),
    then: "unroll into one row of 12 boxes: row 0, then row 1, then row 2",
    derivedFrom: "ep45 scene 5 code (int seats[3][4] = {...})", probe,
  });
}
{
  const c = e45.challenge;
  const ma = /a is ([\d\s,]+?)\s*(?:\.|,)?\s*b is/i.exec(c) ?? /a = \{([^}]*)\} and b = \{([^}]*)\}/.exec(c);
  const grabs = /a = \{([^}]*)\} and b = \{([^}]*)\}/.exec(c)!;
  const parse = (s: string): number[][] => s.split(",").map((row) => nums(row));
  const A = parse(grabs[1]);
  const B = parse(grabs[2]);
  const probe = `#include <stdio.h>\nint main(void) {\n  int a[2][3] = {{${A[0].join(",")}},{${A[1].join(",")}}};\n  int b[2][3] = {{${B[0].join(",")}},{${B[1].join(",")}}};\n  int sum[2][3];\n  for (int r = 0; r < 2; r++) for (int c = 0; c < 3; c++) { sum[r][c] = a[r][c] + b[r][c]; printf("%d\\n", sum[r][c]); }\n  return 0;\n}\n`;
  const out = runC(probe);
  check("EP45 s7 all sevens (the challenge says so)", out.every((v) => v === "7"));
  void ma;
  drafts.push({
    ep: 45, scene: 7, layout: "matrices",
    a: A, b: B, sum: [out.slice(0, 3).map(Number), out.slice(3, 6).map(Number)],
    derivedFrom: "ep45 challenge text: a = {1 2 3, 4 5 6}, b = {6 5 4, 3 2 1}", probe,
  });
}

// ---------- EP46 ----------
const e46 = load(46);
{
  const m = /int\s+marks\[\]\s*=\s*\{([^}]*)\}/.exec(sample(e46, 5))!;
  const probe = `#include <stdio.h>\nint main(void) {\n  int marks[] = {${m[1]}};\n  printf("%zu\\n%zu\\n%zu\\n", sizeof(marks), sizeof(marks[0]), sizeof(marks) / sizeof(marks[0]));\n  for (int i = 0; i < (int)(sizeof(marks) / sizeof(marks[0])); i++) printf("%d\\n", marks[i]);\n  return 0;\n}\n`;
  const out = runC(probe);
  const text = scene(e46, 4).onScreen;
  const whole = /sizeof\(marks\)\s*=\s*(\d+)/.exec(text)?.[1];
  const one = /sizeof\(marks\[0\]\)\s*=\s*(\d+)/.exec(text)?.[1];
  const count = /=\s*(\d+)\s*$/.exec(text.trim())?.[1];
  check("EP46 s4 scene text says 20, 4, 5", out[0] === whole && out[1] === one && out[2] === count);
  drafts.push({
    ep: 46, scene: 4, layout: "cells", name: "marks",
    badges: [`sizeof(marks) = ${out[0]} bytes`, `sizeof(marks[0]) = ${out[1]} bytes`, `${out[0]} / ${out[1]} = ${out[2]}`],
    byteRuler: true, cells: out.slice(3).map((v, i) => ({ index: i, value: v, address: addr(4 * i), bytes: [4 * i, 4 * i + 3] })),
    derivedFrom: "ep46 scene 5 code (int marks[] = {...}); numbers match the scene text", probe,
  });
  // scene 7: two name tags on one row; the function changes a locker
  const src = sample(e46, 5);
  const fn = /void addBonus\([^)]*\)\s*\{[\s\S]*?\n\}/.exec(src)![0];
  const call = /addBonus\(\s*marks\s*,\s*n\s*,\s*(\d+)\s*\)/.exec(src)!;
  const probe7 = `#include <stdio.h>\n${fn}\nint main(void) {\n  int marks[] = {${m[1]}};\n  int n = sizeof(marks) / sizeof(marks[0]);\n  for (int i = 0; i < n; i++) printf("%d ", marks[i]);\n  printf("\\n");\n  addBonus(marks, n, ${call[1]});\n  for (int i = 0; i < n; i++) printf("%d ", marks[i]);\n  printf("\\n");\n  return 0;\n}\n`;
  const o7 = runC(probe7).map((l) => l.trim().split(" "));
  check("EP46 s7 marks changed through arr", o7[0].join() !== o7[1].join());
  drafts.push({
    ep: 46, scene: 7, layout: "alias", tags: ["marks (in main)", "arr (in the function)"], arrow: { from: "arr", to: "marks" },
    before: o7[0].map((v, i) => ({ index: i, value: v, address: addr(4 * i) })),
    after: o7[1].map((v, i) => ({ index: i, value: v, address: addr(4 * i) })),
    derivedFrom: `ep46 scene 5: addBonus(marks, n, ${call[1]}) run for real`, probe: probe7,
  });
}

// ---------- EP47 / 48 / 49 / 50: strings ----------
const stringCells = (s: string): { index: number; value: string; code: number; address: string }[] =>
  [...s, "\0"].map((ch, i) => ({ index: i, value: ch === "\0" ? "\\0" : ch, code: ch.charCodeAt(0), address: addr(i) }));
const stringProbe = (decl: string, extra = ""): string =>
  `#include <stdio.h>\n#include <string.h>\nint main(void) {\n  ${decl}\n  for (size_t i = 0; i < sizeof(s); i++) printf("%d\\n", (int)s[i]);\n  printf("sizeof %zu strlen %zu\\n", sizeof(s), strlen(s));${extra}\n  return 0;\n}\n`;

const e47 = load(47);
{
  const t = scene(e47, 3).onScreen;
  const chars = [...t.matchAll(/'(\\0|[^'])'/g)].map((m) => m[1]);
  const decl = `char s[6] = {${chars.map((c) => `'${c}'`).join(", ")}};`;
  const out = runC(stringProbe(decl));
  const codes = out.slice(0, 6).map(Number);
  check("EP47 s3 six boxes, last is 0", codes.length === 6 && codes[5] === 0);
  drafts.push({
    ep: 47, scene: 3, layout: "cells", name: "word",
    cells: codes.map((c, i) => ({ index: i, value: c === 0 ? "\\0" : String.fromCharCode(c), code: c, address: addr(i) })),
    derivedFrom: "scene text: char word[6] filled with 'G' 'O' 'A' 'N' 'S' '\\0'", probe: stringProbe(decl),
  });
}
{
  const word = /"([^"]+)"/.exec(scene(e47, 4).onScreen)![1];
  const out = runC(stringProbe(`char s[] = "${word}";`));
  const n = Number(/sizeof (\d+)/.exec(out[out.length - 1])![1]);
  check(`EP47 s4 "${word}" is 7 boxes`, n === Number(/in (\d+) boxes/.exec(scene(e47, 4).onScreen)![1]));
  drafts.push({
    ep: 47, scene: 4, layout: "cells", name: "word", stopSign: n - 1, bus: "drives along the boxes and brakes at the \\0",
    cells: out.slice(0, n).map((c, i) => ({ index: i, value: Number(c) === 0 ? "\\0" : String.fromCharCode(Number(c)), code: Number(c), address: addr(i) })),
    derivedFrom: `scene text: "${word}" laid out in 7 boxes`, probe: stringProbe(`char s[] = "${word}";`),
  });
}
const e48 = load(48);
{
  const t = scene(e48, 3).onScreen;
  const tokens = /Keyboard buffer:\s*([^;]+);/.exec(t)![1].trim().split(/\s+/);
  const typed = tokens.map((k) => (k === "_" ? " " : k === "\\n" ? "\n" : k)).join("");
  const probe = `#include <stdio.h>\nint main(void) {\n  const char *typed = "${typed.replace("\n", "\\n")}";\n  char name[30];\n  int used = 0;\n  sscanf(typed, "%29s%n", name, &used);\n  printf("%s\\n%d\\n", name, used);\n  for (const char *p = typed; *p; p++) printf("%d\\n", (int)*p);\n  return 0;\n}\n`;
  const out = runC(probe);
  const used = Number(out[1]);
  const codes = out.slice(2).map(Number);
  check("EP48 s3 scanf takes Atreya and leaves ' Kamat\\n'", out[0] === "Atreya" && used === 6);
  const show = (c: number): string => (c === 32 ? "␠" : c === 10 ? "\\n" : String.fromCharCode(c));
  drafts.push({
    ep: 48, scene: 3, layout: "buffer", typed: typed.replace("\n", "\\n"),
    cells: codes.map((c, i) => ({ index: i, value: show(c), code: c, taken: i < used })),
    taken: out[0], left: typed.slice(used).replace("\n", "\\n"),
    derivedFrom: "scene text: A t r e y a _ K a m a t \\n; sscanf(\"%s\") run for real", probe,
  });
}
const e49 = load(49);
{
  const word = /"([^"]+)"/.exec(scene(e49, 4).onScreen)![1];
  const out = runC(stringProbe(`char s[] = "${word}";`));
  const last = out[out.length - 1];
  const [size, len] = [Number(/sizeof (\d+)/.exec(last)![1]), Number(/strlen (\d+)/.exec(last)![1])];
  check(`EP49 s4 strlen ${len} / sizeof ${size} as the narration says (6 and 7)`, len === 6 && size === 7);
  drafts.push({
    ep: 49, scene: 4, layout: "cells", name: "second", counter: { upTo: len, skip: "\\0" },
    cells: out.slice(0, size).map((c, i) => ({ index: i, value: Number(c) === 0 ? "\\0" : String.fromCharCode(Number(c)), code: Number(c), address: addr(i), counted: i < len })),
    derivedFrom: `scene text: "${word}" in 7 boxes; strlen run for real`, probe: stringProbe(`char s[] = "${word}";`),
  });
}
{
  const src = sample(e49, 7);
  const firstDecl = /char\s+first\[(\d+)\]\s*=\s*"([^"]*)";/.exec(src)!;
  const secondDecl = /char\s+second\[\]\s*=\s*"([^"]*)";/.exec(src)!;
  const stmts = [...src.matchAll(/^\s*((?:strcpy|strcat)\([^;]*\);)/gm)].map((m) => m[1]);
  const body = stmts.map((s, i) => `  ${s}\n  printf("S${i}|%s|%s|%zu|%zu\\n", copy, first, strlen(copy), strlen(first));`).join("\n");
  const probe = `#include <stdio.h>\n#include <string.h>\nint main(void) {\n  char first[${firstDecl[1]}] = "${firstDecl[2]}";\n  char second[] = "${secondDecl[1]}";\n  char copy[20];\n  copy[0] = 0;\n${body}\n  return 0;\n}\n`;
  const out = runC(probe).map((l) => l.split("|"));
  check("EP49 s5 copy is Xecxec and first is 'Crab Xecxec' (the program's own output says Joined: Crab Xecxec)", out[0][1] === "Xecxec" && out[out.length - 1][2] === "Crab Xecxec");
  drafts.push({
    ep: 49, scene: 5, layout: "strings", capacity: { copy: 20, first: Number(firstDecl[1]) },
    steps: [
      { label: "start", copy: "", first: firstDecl[2], second: secondDecl[1] },
      ...stmts.map((s, i) => ({ label: s, copy: out[i][1], first: out[i][2], nulAt: { copy: Number(out[i][3]), first: Number(out[i][4]) } })),
    ],
    derivedFrom: "ep49 scene 7 code: strcpy / strcat statements executed for real", probe,
  });
}
const e50 = load(50);
{
  const word = /Take (\w+)\./.exec(scene(e50, 3).narration)![1];
  const probe = `#include <stdio.h>\n#include <string.h>\nint main(void) {\n  char word[] = "${word}";\n  int len = (int)strlen(word);\n  char rev[20];\n  for (int i = 0; i < len; i++) { rev[i] = word[len - 1 - i]; printf("%d %d %c\\n", i, len - 1 - i, rev[i]); }\n  rev[len] = '\\0';\n  printf("%s\\n", rev);\n  return 0;\n}\n`;
  const out = runC(probe);
  const pairs = out.slice(0, word.length).map((l) => l.split(" "));
  check("EP50 s3 rev[i] = word[len-1-i]", out[word.length] === [...word].reverse().join(""));
  drafts.push({
    ep: 50, scene: 3, layout: "mirror", word: stringCells(word), rev: stringCells(out[word.length]),
    arrows: pairs.map((p) => ({ from: Number(p[1]), to: Number(p[0]) })),
    derivedFrom: `scene narration: "Take ${word}"; the reverse loop run for real`, probe,
  });
}

writeFileSync(join(ROOT, "docs", "fix4", "boxes-draft-ep41-50.json"), JSON.stringify(drafts, null, 1));
console.log(`derived ${drafts.length} scenes (every probe compiled with gcc -Wall -Wextra and run): ${drafts.map((d) => `EP${d.ep}s${d.scene}:${d.layout}`).join(" ")}`);
console.log(compilerWarnings.length ? `GCC WARNINGS: ${compilerWarnings.join(" | ")}` : "gcc -Wall -Wextra: no warnings in any probe");
console.log(fail.length ? `CROSS-CHECKS FAILED: ${fail.join("; ")}` : "all cross-checks against the scene's own numbers passed");
process.exit(fail.length ? 1 : 0);
