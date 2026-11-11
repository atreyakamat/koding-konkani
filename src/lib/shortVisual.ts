import type { Episode } from "./episode";
import type { MemoryGroup } from "./memory.ts";
import { stripMarkdown } from "./sanitize.ts";

/** Pure (no React, no imports beyond types) so scripts/check_short_visuals.mts can run it too.
 * Every Short's visual is derived from ITS OWN data (hook, onScreen, script, fromScenes and
 * their scenes), never from a generic fallback shared across episodes. */

type Short = Episode["shorts"][number];
type Scene = Episode["scenes"][number];

export type ShortBox = { name: string; value: string; address?: string; mark?: string; lost?: string };
export type Bits = { label: string; bits: string };
export type ShortVisual =
  | { kind: "pun"; text: string }
  | { kind: "quiz"; code: string[]; options: string[]; question: string; card: string }
  | { kind: "pron"; written: string; spoken: string }
  | { kind: "boxes"; boxes: ShortBox[]; frames?: { label?: string; boxes: ShortBox[] }[] }
  | { kind: "bits"; rows: Bits[]; result?: Bits; sum?: string }
  | { kind: "code"; source: string; mode: "advance" | "static" }
  | { kind: "bug" }
  | { kind: "analogy"; title: string; body: string }
  | { kind: "terminal"; lines: string[] }
  | { kind: "text"; text: string };

export const signature = (v: ShortVisual): string => {
  switch (v.kind) {
    case "pun":
      return `pun:${v.text}`;
    case "quiz":
      return `quiz:${v.code.join("|")}#${v.options.join("|")}#${v.question}`;
    case "pron":
      return `pron:${v.written}>${v.spoken}`;
    case "boxes":
      return `boxes:${v.boxes.map((b) => `${b.name}=${b.value}`).join(",")}`;
    case "bits":
      return `bits:${v.rows.map((r) => `${r.label}=${r.bits}`).join(",")}`;
    case "code":
      return `code:${v.source}`;
    case "bug":
      return "bug";
    case "analogy":
      return `analogy:${v.title}|${v.body}`;
    case "terminal":
      return `terminal:${v.lines.join("|")}`;
    case "text":
      return `text:${v.text}`;
  }
};

/** At most this many boxes fit the Short's boxes visual. */
const SHORT_MAX_BOXES = 6;

const groupBoxes = (g: MemoryGroup): ShortBox[] => {
  // "word[6]" -> "word", "marks" -> "marks"; an unnamed group borrows the first name tag ("marks (in main)").
  const base = (g.name ?? g.tags?.[0] ?? "").replace(/s*(.*)$/, "").replace(/[d*]$/, "");
  return g.cells.map((c, i) => ({
    name: c.name ?? `${base}${typeof c.index === "string" ? c.index : `[${c.index ?? i}]`}`,
    value: c.value,
    address: c.address,
    mark: c.mark,
    lost: c.lost,
  }));
};

/** The boxes a Short can draw from a memory-boxes scene: its flat `boxes`, or the first group of the first `memory`
 * frame when it has at most 6 cells (an array of 5 or a few scalars; longer rows and grids keep the Short's other visual).
 * Every frame of a memory scene gives its first group, when all frames have the same count of at most 6 cells. */
const boxesOf = (scene: Scene): { boxes: ShortBox[]; frames?: { label?: string; boxes: ShortBox[] }[] } | undefined => {
  if (scene.template !== "memory-boxes") return undefined;
  if (scene.boxes?.length) return { boxes: scene.boxes.map((b) => ({ name: b.name, value: b.value, address: b.address })) };
  const frames = scene.memory?.frames ?? [];
  const first = frames[0]?.groups[0];
  if (!first || first.cells.length > SHORT_MAX_BOXES) return undefined;
  const all = frames.map((f) => ({ label: f.label, boxes: f.groups[0] ? groupBoxes(f.groups[0]) : [] }));
  // Stepping needs frames of the same shape in which some value actually changes (else the label alone would change).
  const changes = all.some((f, k) => k > 0 && f.boxes.some((b, i) => b.value !== all[k - 1].boxes[i]?.value));
  const steppable = all.length > 1 && changes && all.every((f) => f.boxes.length === first.cells.length);
  return { boxes: all[0].boxes, ...(steppable ? { frames: all } : {}) };
};

/** Card text comes from ONE source string: GCC-style `name' quotes become 'name', then
 * Markdown and stray backticks are stripped. Never a concatenation of two strings. */
export const cardText = (text: string): string =>
  stripMarkdown(text.replace(/`([^`'\n]*)'/g, "'$1'")).replace(/`/g, "");

const unquote = (s: string): string => s.trim().replace(/^["“]+|["”]+$/g, "");

/** A fragment that is clearly C (or a terminal command), not a label. */
const isCodey = (part: string): boolean => {
  const p = part.trim();
  if (/_{3,}/.test(p)) return false; // a fill-in-the-blank question, not code
  if (!p || (/^[A-Z0-9 ,.'’:?!-]+$/.test(p) && !/[;(){}<>=%*/+&|^]/.test(p))) return false;
  if (/[;{}]/.test(p) || /^#/.test(p) || /\b[A-Za-z_]\w*\s*\(/.test(p)) return true;
  if (/^gcc\b|^\.\//.test(p)) return true;
  const allCapsWords = p.match(/\b[A-Z]{3,}\b/g) ?? [];
  if (allCapsWords.length > 0) return false;
  return /[+\-*/%<>=&|^]/.test(p) && /[\w)]/.test(p) && /\d|\b[a-z_]\w*\b/.test(p);
};

const splitParts = (onScreen: string): string[] =>
  onScreen
    .split(/\s·\s|\n/)
    .map((s) => s.trim())
    .filter(Boolean);

const stripAnswerMark = (s: string): string => s.replace(/\s*(=|→)?\s*\?\s*$/, "").trim();

/** One statement per line, so a one-line `a; b; c;` reads as code. */
const splitStatements = (s: string): string[] =>
  /;\s+\S/.test(s) && !/^for\s*\(/.test(s) ? s.split(/(?<=;)\s+/) : [s];

const sceneOf = (episode: Episode, id: number): Scene | undefined =>
  episode.scenes.find((s) => s.id === id);

const sourcesOf = (episode: Episode, short: Short): Scene[] =>
  short.fromScenes.map((id) => sceneOf(episode, id)).filter((s): s is Scene => !!s);

const analogyOf = (onScreen: string): { title: string; body: string } | undefined => {
  const m = onScreen.match(/^"?([^":]{2,40})"?:\s*(.+)$/);
  return m ? { title: m[1].trim(), body: m[2].trim() } : undefined;
};

/** Quiz: exact code from onScreen (or the hook), a "?" output, options as text. */
const quizOf = (episode: Episode, short: Short): ShortVisual => {
  const parts = splitParts(short.onScreen);
  const code: string[] = [];
  const options: string[] = [];
  let question = "";
  for (const part of parts) {
    const bare = stripAnswerMark(part);
    if (/^vs\.?$/i.test(part)) {
      options.push("vs");
    } else if (
      /^(A\)|A:)/.test(part) ||
      (/\bor\b/i.test(part) && /\?$/.test(part) && !/[;(){}]/.test(part))
    ) {
      options.push(part.replace(/\?$/, ""));
    } else if (isCodey(bare) || (/`/.test(part) && !/\bor\b/i.test(part))) {
      code.push(...splitStatements(bare));
    } else if (/^[A-Z ,]+\??$/.test(part) || /\?$/.test(part)) {
      question = part;
    } else {
      options.push(part);
    }
  }
  if (code.length === 0) {
    const hookFn = unquote(short.hook).match(/[A-Za-z_]\w*\([^]*\)/)?.[0];
    if (hookFn) code.push(/;$/.test(hookFn) ? hookFn : `${hookFn};`);
  }
  if (code.length === 0) {
    const bugScene = sourcesOf(episode, short).find((s) => s.template === "bug-of-the-day");
    if (bugScene)
      code.push(
        ...episode.bug.wrong
          .split("\n")
          .filter((l) => l.trim())
          .slice(0, 6),
      );
  }
  // A compiler/linker message is something to name, not code to run: show it on the card.
  if (code.length > 0 && code.every((l) => /undefined reference|error:|warning:/i.test(l))) {
    options.unshift(...code);
    code.length = 0;
  }
  if (code.length === 0 && options.length === 0 && !question) question = unquote(short.hook);
  return {
    kind: "quiz",
    code,
    options,
    question,
    card: cardText(short.onScreen.trim() || unquote(short.hook)),
  };
};

/** A bare run of 0/1 digits ("1000 names") is a count, not bits: only "= 1100" counts. */
const BIN_WORDS = /\bbinary\b|\bbits?\b|<<|>>|=\s*[01]{4,8}\b/i;
const toBits = (n: number, width: number): string => n.toString(2).padStart(width, "0");

const bitsOf = (short: Short): ShortVisual | undefined => {
  const text = `${unquote(short.hook)} ${short.onScreen}`;
  // Word operators must be written in capitals ("12 AND 10"): "2 or 3" is plain English.
  const pair = text.match(/(\d{1,3})\s*(AND|OR|XOR|&|\||\^)\s*(\d{1,3})/);
  if (pair) {
    const a = Number(pair[1]);
    const b = Number(pair[3]);
    const op = pair[2].toUpperCase();
    const width = Math.max(a, b) < 16 ? 4 : 8;
    const r = op === "AND" || op === "&" ? a & b : op === "OR" || op === "|" ? a | b : a ^ b;
    return {
      kind: "bits",
      rows: [
        { label: String(a), bits: toBits(a, width) },
        {
          label: `${op === "&" ? "AND" : op === "|" ? "OR" : op === "^" ? "XOR" : op} ${b}`,
          bits: toBits(b, width),
        },
      ],
      result: { label: String(r), bits: toBits(r, width) },
    };
  }
  if (!BIN_WORDS.test(text)) return undefined;
  const n = text.match(/(?<![\d.])(\d{1,3})(?![\d.])/);
  if (!n) return undefined;
  const value = Number(n[1]);
  if (value > 255) return undefined;
  const width = value < 16 ? 4 : 8;
  const bits = toBits(value, width);
  const on = [...bits].map((b, i) => (b === "1" ? 2 ** (width - 1 - i) : 0)).filter(Boolean);
  return {
    kind: "bits",
    rows: [{ label: String(value), bits }],
    sum: `${on.join(" + ")} = ${value}`,
  };
};

const words = (s: string): string[] =>
  (s.toLowerCase().match(/[a-z0-9]{3,}/g) ?? []).filter((w) => w.length > 2);

/** True when `text` just restates the hook (most of its words already appear in it), so a
 * card showing it would repeat what is printed above (EP01 S1). */
const repeatsHook = (text: string, hook: string): boolean => {
  const t = words(text);
  if (t.length === 0) return false;
  const h = new Set(words(hook));
  return t.filter((w) => h.has(w)).length / t.length >= 0.6;
};

/** The first one or two script sentences that say something the hook does not: no call to
 * action, no restated hook, no pronunciation line (that has its own Short). */
const takeawayOf = (short: Short, hook: string): string | undefined => {
  const sentences = stripMarkdown(short.script)
    .replace(/\s+/g, " ")
    .split(/(?<=[.?!])\s+/)
    .map((x) => x.trim())
    .filter((x) => x.length >= 12);
  const usable = sentences.filter(
    (x) => !repeatsHook(x, hook) && !/full (series|episode|video)|comment|say it|pronounc/i.test(x),
  );
  const out: string[] = [];
  for (const x of usable) {
    if ([...out, x].join(" ").length > 140) break;
    out.push(x);
    if (out.length === 2) break;
  }
  return out.length ? out.join(" ") : undefined;
};

const candidatesFor = (episode: Episode, short: Short): ShortVisual[] => {
  const out: ShortVisual[] = [];
  const sources = sourcesOf(episode, short);
  const hook = unquote(short.hook);

  if (/pronounced/i.test(hook)) {
    const spoken = hook.match(/pronounced\s+([^.!?]+)/i)?.[1]?.trim();
    if (spoken) out.push({ kind: "pron", written: "Xecxec", spoken });
  }
  if (short.id === "S4" || sources.some((s) => s.template === "pun-card")) {
    const pun = sources.find((s) => s.template === "pun-card");
    out.push({ kind: "pun", text: unquote(pun ? pun.narration : episode.pun) });
  }
  if (short.id === "S5") out.push(quizOf(episode, short));

  const shortBoxes = sources.map(boxesOf).find((b) => b !== undefined);
  if (shortBoxes) out.push({ kind: "boxes", ...shortBoxes });
  if (sources.some((s) => s.template === "bug-of-the-day")) out.push({ kind: "bug" });
  const bits = bitsOf(short);
  if (bits) out.push(bits);

  const hookFn = hook.match(/[A-Za-z_]\w*\([^]*\)/)?.[0];
  if (hookFn)
    out.push({ kind: "code", source: /;$/.test(hookFn) ? hookFn : `${hookFn};`, mode: "static" });
  const codeParts = splitParts(short.onScreen).filter(isCodey).map(stripAnswerMark);
  if (codeParts.length) {
    out.push({
      kind: "code",
      source: codeParts.flatMap(splitStatements).join("\n"),
      mode: "static",
    });
  }

  for (const scene of sources) {
    if (scene.template === "code-explain" && scene.code) {
      out.push({ kind: "code", source: scene.code.source, mode: "advance" });
    } else if (scene.template === "terminal") {
      const lines = [...scene.onScreen.matchAll(/`([^`]+)`/g)].map((m) => m[1]);
      // A single command is too sparse to be a visual (EP05 S1): let a richer candidate win.
      if (lines.length >= 2) out.push({ kind: "terminal", lines });
    } else if (scene.template === "concept-slide") {
      const a = analogyOf(scene.onScreen);
      if (a) out.push({ kind: "analogy", ...a });
    }
  }
  const own = short.onScreen.trim();
  if (own && !repeatsHook(own, hook)) out.push({ kind: "text", text: own });
  const takeaway = takeawayOf(short, hook);
  if (takeaway) out.push({ kind: "text", text: takeaway });
  if (own) out.push({ kind: "text", text: own });
  out.push({ kind: "text", text: hook });
  return out;
};

/** Strips Markdown from every prose field (never from code lines). */
const cleanVisual = (v: ShortVisual): ShortVisual => {
  switch (v.kind) {
    case "pun":
      return { ...v, text: stripMarkdown(v.text) };
    case "text":
      return { ...v, text: cardText(v.text) };
    case "quiz":
      return {
        ...v,
        code: v.code.map((l) => stripMarkdown(l)),
        options: v.options.map(stripMarkdown),
        question: stripMarkdown(v.question),
        card: cardText(v.card),
      };
    case "analogy":
      return { ...v, title: stripMarkdown(v.title), body: stripMarkdown(v.body) };
    default:
      return v;
  }
};

/** The visual for each of an episode's Shorts. Shorts are resolved S5, S4, S3, S2, S1 so the
 * quiz, joke and bug Shorts claim their own visuals first; a later Short whose preferred
 * visual is already taken moves to its next derivable candidate. Never two the same. */
export const deriveShortVisuals = (episode: Episode): Record<string, ShortVisual> => {
  const used = new Set<string>();
  const result: Record<string, ShortVisual> = {};
  const order = ["S5", "S4", "S3", "S2", "S1"];
  for (const id of order) {
    const short = episode.shorts.find((s) => s.id === id);
    if (!short) continue;
    const candidates = candidatesFor(episode, short);
    const pick =
      candidates.find((c) => !used.has(signature(c))) ?? candidates[candidates.length - 1];
    used.add(signature(pick));
    result[id] = cleanVisual(pick);
  }
  return result;
};

/** Duplicate visuals within one episode, as `[episode, shortA, shortB]` — empty when fine. */
export const findDuplicateVisuals = (episode: Episode): string[][] => {
  const visuals = deriveShortVisuals(episode);
  const seen = new Map<string, string>();
  const dupes: string[][] = [];
  for (const [id, v] of Object.entries(visuals)) {
    const sig = signature(v);
    const prior = seen.get(sig);
    if (prior) dupes.push([String(episode.ep), prior, id]);
    else seen.set(sig, id);
  }
  return dupes;
};
