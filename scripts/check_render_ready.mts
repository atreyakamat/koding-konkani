/**
 * Render-readiness check of an episode folder: everything a scene needs to draw something, so no
 * scene can come out empty or black. Static (no browser, no audio). Run before narration and render.
 *
 * Checks per episode: zod schema; 11 scenes in the template order; each scene has the data its
 * template draws (code, output, points, memory, trace, diagram); [HL n] cues point at real code
 * lines; text fits its card (the limits below were set from rendered stills); the outro names the
 * next episode (except the finale); 5 Shorts of 35-45 s that reference real scenes.
 *
 * Usage: node scripts/check_render_ready.mts [--lang cpp]       (C++ only; other courses use validate_episodes.mts and stills_all.mts)
 * Exit 1 on any problem.
 */
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { EpisodeSchema } from "../src/lib/episode.ts";
import { terminalLinesFor } from "../src/lib/terminalLines.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const langIdx = process.argv.indexOf("--lang");
const lang = langIdx >= 0 ? process.argv[langIdx + 1] : "cpp";
if (lang !== "cpp") {
  // The rules below describe the C++ episode shape (points, analogy and diagram fields on the scene). The Python course
  // keeps that data in scene.props and scene.memory, and the C course in its own tables, so these rules would
  // report false problems for them. Use the course's own checks instead.
  console.error(
    `check_render_ready.mts only checks the C++ course (--lang cpp). For "${lang}" run: KK_LANG=${lang} node scripts/validate_episodes.mts, then KK_LANG=${lang} node scripts/stills_all.mts <from> <to>`,
  );
  process.exit(2);
}
const dirName =
  lang === "cpp" ? "episodes-cpp" : lang === "python" ? "episodes-python" : "episodes";
const total = lang === "c" ? 86 : 90;
const dir = join(ROOT, dirName);

const TEMPLATE_ORDER = [
  "title-card",
  "concept-slide",
  "code-explain",
  null, // scene 4 is memory-boxes, algorithm-bars or a concept-slide with a diagram
  "code-explain",
  "terminal",
  "concept-slide",
  "bug-of-the-day",
  "pun-card",
  "challenge",
  "outro",
] as const;

/** Text-length limits for what is drawn on screen (characters). */
const LIMITS = {
  point: 70,
  analogyBody: 100,
  flowLabel: 22,
  flowDetail: 52,
  graphLabel: 20,
  graphSub: 30,
  tableCell: 52,
  stackFrame: 34,
  stackNote: 70,
  memoryValue: 24,
  memoryName: 26,
};

const problems: string[] = [];
const fail = (ep: number, msg: string): void => {
  problems.push(`EP ${ep}: ${msg}`);
};

const files = readdirSync(dir)
  .filter((f) => /^ep\d{3}\.json$/.test(f))
  .sort();
const seen = new Set<number>();

for (const file of files) {
  const raw = JSON.parse(readFileSync(join(dir, file), "utf-8"));
  const parsed = EpisodeSchema.safeParse(raw);
  const n = Number(file.slice(2, 5));
  if (!parsed.success) {
    for (const issue of parsed.error.issues)
      fail(n, `schema: ${issue.path.join(".")}: ${issue.message}`);
    continue;
  }
  const ep = parsed.data;
  seen.add(ep.ep);
  if (ep.ep !== n) fail(n, `file name says ${n} but ep is ${ep.ep}`);
  if (lang !== "c" && ep.lang !== lang) fail(n, `lang must be "${lang}"`);

  if (ep.scenes.length !== 11) fail(n, `${ep.scenes.length} scenes (need 11)`);
  ep.scenes.forEach((s, i) => {
    const want = TEMPLATE_ORDER[i];
    if (want && s.template !== want) fail(n, `scene ${s.id} is ${s.template}, expected ${want}`);
    if (s.id !== i + 1) fail(n, `scene ${i + 1} has id ${s.id}`);
    if (!s.narration.trim()) fail(n, `scene ${s.id} has no narration`);
    if (/\[HL:/.test(s.narration)) fail(n, `scene ${s.id}: unresolved [HL: text] anchor`);
  });
  const scene = (id: number) => ep.scenes.find((s) => s.id === id)!;

  // scene 2 and 7: authored points
  for (const id of [2, 7]) {
    const s = scene(id);
    if (!s?.points?.length) fail(n, `scene ${id}: no points`);
    for (const p of s?.points ?? []) {
      if (p.length > LIMITS.point) fail(n, `scene ${id}: point is ${p.length} characters: "${p}"`);
      if (/^\d+\./.test(p)) fail(n, `scene ${id}: point still starts with a number: "${p}"`);
    }
  }
  const analogy = scene(2)?.analogy;
  if (!analogy) fail(n, "scene 2: no analogy card");
  else if (analogy.body.length > LIMITS.analogyBody)
    fail(n, `scene 2: analogy is ${analogy.body.length} characters`);

  // code scenes
  for (const id of [3, 5]) {
    const s = scene(id);
    if (!s?.code?.source) {
      fail(n, `scene ${id}: no code`);
      continue;
    }
    if (!s.code.output?.trim()) fail(n, `scene ${id}: no expected output`);
    const lines = s.code.source.split("\n");
    const hl = [...s.narration.matchAll(/\[HL (\d+)\]/g)].map((m) => Number(m[1]));
    if (hl.length === 0) fail(n, `scene ${id}: no [HL n] cues`);
    for (const line of hl)
      if (line < 1 || line > lines.length)
        fail(n, `scene ${id}: [HL ${line}] is outside the ${lines.length} code lines`);
  }
  if (scene(3)?.code && scene(5)?.code && scene(3).code!.file === scene(5).code!.file)
    fail(n, "scenes 3 and 5 show the same file");

  // scene 4
  const s4 = scene(4);
  if (s4) {
    if (s4.template === "memory-boxes") {
      if (!s4.memory?.frames.length) fail(n, "scene 4: memory-boxes without memory frames");
      for (const f of s4.memory?.frames ?? [])
        for (const g of f.groups)
          for (const c of g.cells) {
            if (c.value.length > LIMITS.memoryValue)
              fail(n, `scene 4: memory value "${c.value}" is ${c.value.length} characters`);
            if ((c.name ?? "").length > LIMITS.memoryName)
              fail(n, `scene 4: memory name "${c.name}" is too long`);
          }
    } else if (s4.template === "algorithm-bars") {
      if (!s4.trace?.length) fail(n, "scene 4: algorithm-bars without a trace");
    } else if (s4.template === "concept-slide") {
      const d = s4.diagram;
      if (!d) fail(n, "scene 4: concept-slide without a diagram");
      else if (d.kind === "flow")
        d.steps.forEach((x) => {
          if (x.label.length > LIMITS.flowLabel)
            fail(n, `scene 4: flow label "${x.label}" is ${x.label.length} characters`);
          if (x.detail.length > LIMITS.flowDetail)
            fail(n, `scene 4: flow detail is ${x.detail.length} characters: "${x.detail}"`);
        });
      else if (d.kind === "graph") {
        const ids = new Set(d.nodes.map((x) => x.id));
        d.edges.forEach(
          (e) =>
            (!ids.has(e.from) || !ids.has(e.to)) &&
            fail(n, `scene 4: edge ${e.from}->${e.to} names a missing node`),
        );
        d.nodes.forEach((x) => {
          if (x.label.length > LIMITS.graphLabel)
            fail(n, `scene 4: graph label "${x.label}" is too long`);
          if (x.sub.length > LIMITS.graphSub) fail(n, `scene 4: graph sub "${x.sub}" is too long`);
        });
      } else if (d.kind === "table")
        d.rows.forEach((r) => {
          if (r.length !== d.headers.length)
            fail(n, "scene 4: table row has the wrong number of cells");
          r.forEach(
            (c) =>
              c.length > LIMITS.tableCell &&
              fail(n, `scene 4: table cell is ${c.length} characters: "${c}"`),
          );
        });
      else if (d.kind === "callstack")
        d.steps.forEach((x) => {
          x.frames.forEach(
            (f) =>
              f.length > LIMITS.stackFrame && fail(n, `scene 4: stack frame "${f}" is too long`),
          );
          if (x.note.length > LIMITS.stackNote)
            fail(n, `scene 4: stack note is ${x.note.length} characters`);
        });
    }
  }

  // terminal: must show a compile command and the program output
  const t = scene(6);
  if (t) {
    const lines = terminalLinesFor(ep, t);
    if (!lines.some((l) => l.kind === "input" && /^(g\+\+|gcc)(\s|$)/.test(l.text)))
      fail(n, "scene 6: terminal shows no compile command");
    if (!lines.some((l) => l.kind === "output"))
      fail(n, "scene 6: terminal shows no program output");
  }

  // bug
  for (const k of ["wrong", "error", "fixed", "why"] as const)
    if (!ep.bug[k].trim()) fail(n, `bug.${k} is empty`);
  if (ep.bug.error.split("\n").filter((l) => l.trim()).length < 2)
    fail(n, "bug.error has no compiler message or program output");

  // outro
  if (ep.ep < total && !ep.nextTitle) fail(n, "no nextTitle for the outro");
  if (ep.ep === total && ep.nextTitle) fail(n, "the last episode must have no nextTitle");

  // shorts
  if (ep.shorts.length !== 5) fail(n, `${ep.shorts.length} Shorts (need 5)`);
  for (const s of ep.shorts) {
    if (s.lengthSec < 35 || s.lengthSec > 45) fail(n, `${s.id}: ${s.lengthSec} s (need 35-45)`);
    if (!s.fromScenes.every((id) => ep.scenes.some((x) => x.id === id)))
      fail(n, `${s.id}: fromScenes names a missing scene`);
    if (!s.script.endsWith("Keep coding, says Xecxec!")) fail(n, `${s.id}: no sign-off`);
  }
  const total_sec = ep.scenes.reduce((a, s) => a + s.lengthSec, 0);
  if (total_sec > 540) fail(n, `scenes add to ${total_sec}s (max 540)`);
}

for (let i = 1; i <= total; i++) if (!seen.has(i)) problems.push(`EP ${i}: missing`);

for (const p of problems) console.log("PROBLEM", p);
console.log(`${files.length} episodes in ${dirName}, ${problems.length} problems`);
process.exit(problems.length ? 1 : 0);
