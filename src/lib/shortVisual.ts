import type { Episode } from "./episode";

/** Pure (no React, no imports beyond types) so scripts/check_short_visuals.mts can run it too.
 * Every Short's visual is derived from ITS OWN data (hook, onScreen, script, fromScenes and
 * their scenes), never from a generic fallback shared across episodes. */

type Short = Episode["shorts"][number];
type Scene = Episode["scenes"][number];

export type Bits = { label: string; bits: string };
export type ShortVisual =
  | { kind: "pun"; text: string }
  | { kind: "quiz"; code: string[]; options: string[]; question: string }
  | { kind: "pron"; written: string; spoken: string }
  | { kind: "boxes"; boxes: { name: string; value: string; address?: string }[] }
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

const unquote = (s: string): string => s.trim().replace(/^["“]+|["”]+$/g, "");

/** A fragment that is clearly C (or a terminal command), not a label. */
const isCodey = (part: string): boolean => {
  const p = part.trim();
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
  if (code.length === 0 && options.length === 0 && !question) question = unquote(short.hook);
  return { kind: "quiz", code, options, question };
};

const BIN_WORDS = /\bbinary\b|\bbits?\b|<<|>>|\b[01]{4,}\b/i;
const toBits = (n: number, width: number): string => n.toString(2).padStart(width, "0");

const bitsOf = (short: Short): ShortVisual | undefined => {
  const text = `${unquote(short.hook)} ${short.onScreen}`;
  const pair = text.match(/(\d{1,3})\s*(AND|OR|XOR|&|\||\^)\s*(\d{1,3})/i);
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

  const boxScene = sources.find((s) => s.template === "memory-boxes" && s.boxes?.length);
  if (boxScene?.boxes) {
    out.push({
      kind: "boxes",
      boxes: boxScene.boxes.map((b) => ({ name: b.name, value: b.value, address: b.address })),
    });
  }
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
      if (lines.length) out.push({ kind: "terminal", lines });
    } else if (scene.template === "concept-slide") {
      const a = analogyOf(scene.onScreen);
      if (a) out.push({ kind: "analogy", ...a });
    }
  }
  out.push({ kind: "text", text: short.onScreen.trim() || hook });
  out.push({ kind: "text", text: hook });
  return out;
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
    result[id] = pick;
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
