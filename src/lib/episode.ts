import { z } from "zod";
import { MemoryDataSchema } from "./memory.ts";

/**
 * The 10 scene templates from CLAUDE.md, as the schema's canonical slugs.
 * `sceneTemplateFromBibleName` maps the Episode Bible's human-written names
 * onto these; it throws on anything it doesn't recognise rather than
 * guessing, so a typo or a new template in the Bible surfaces immediately.
 */
export const SCENE_TEMPLATES = [
  "title-card",
  "concept-slide",
  "code-explain",
  "memory-boxes",
  "algorithm-bars",
  "terminal",
  "bug-of-the-day",
  "pun-card",
  "challenge",
  "outro",
] as const;

export const SceneTemplateSchema = z.enum(SCENE_TEMPLATES);
export type SceneTemplate = z.infer<typeof SceneTemplateSchema>;

const BIBLE_TEMPLATE_NAMES: Record<string, SceneTemplate> = {
  "Title card": "title-card",
  "Concept slide": "concept-slide",
  "Code explain": "code-explain",
  "Memory boxes": "memory-boxes",
  Terminal: "terminal",
  "Algorithm bars": "algorithm-bars",
  "Bug of the Day": "bug-of-the-day",
  "Pun card": "pun-card",
  Challenge: "challenge",
  Outro: "outro",
};

/** Maps an Episode Bible scene-list "Template" cell to a SceneTemplate. Fails loudly on anything unrecognised. */
export const sceneTemplateFromBibleName = (name: string): SceneTemplate => {
  const trimmed = name.trim();
  const mapped = BIBLE_TEMPLATE_NAMES[trimmed];
  if (!mapped) {
    throw new Error(
      `Unknown Episode Bible scene template name: ${JSON.stringify(trimmed)}. ` +
        `Expected one of: ${Object.keys(BIBLE_TEMPLATE_NAMES).join(", ")}.`,
    );
  }
  return mapped;
};

/** Course language. Absent means the original C course. */
export const LANGS = ["c", "cpp", "python"] as const;
export type Lang = (typeof LANGS)[number];

/** Folder name of an episode's narration under audio/voice/. The C course keeps its plain `ep001`
 * names; every other language gets a prefix, so two courses never share a folder. */
export const epFolder = (lang: Lang | string | undefined, ep: number): string =>
  `${lang && lang !== "c" ? `${lang}-` : ""}ep${String(ep).padStart(3, "0")}`;

/** True for the original C course, the only one that the ep-number keyed tables (bug overrides, titles) describe. */
export const isCCourse = (lang: Lang | string | undefined): boolean => !lang || lang === "c";

/** Structured diagram for a concept slide (scene 4 of the C++ Bible): see docs/cpp-bible/ILLUSTRATIONS.md. */
const DiagramBaseSchema = { caption: z.string().optional() };
export const DiagramSchema = z.discriminatedUnion("kind", [
  z.object({
    kind: z.literal("flow"),
    ...DiagramBaseSchema,
    steps: z.array(z.object({ id: z.string(), label: z.string().min(1), detail: z.string() })).min(2).max(6),
  }),
  z.object({
    kind: z.literal("graph"),
    ...DiagramBaseSchema,
    layout: z.enum(["row", "column", "tree"]),
    nodes: z.array(z.object({ id: z.string(), label: z.string().min(1), sub: z.string() })).min(2).max(8),
    edges: z.array(z.object({ from: z.string(), to: z.string(), label: z.string() })),
  }),
  z.object({
    kind: z.literal("table"),
    ...DiagramBaseSchema,
    headers: z.array(z.string().min(1)).min(2).max(5),
    rows: z.array(z.array(z.string())).min(1).max(7),
  }),
  z.object({
    kind: z.literal("callstack"),
    ...DiagramBaseSchema,
    steps: z
      .array(z.object({ step: z.number(), frames: z.array(z.string().min(1)).min(1).max(8), note: z.string() }))
      .min(1)
      .max(12),
  }),
]);
export type Diagram = z.infer<typeof DiagramSchema>;

const CodeSchema = z.object({
  file: z.string().min(1),
  source: z.string().min(1),
  output: z.string().optional(),
});

/** One step of an AlgorithmBars trace: `step` is "1.1"-style in the Bible, a plain index elsewhere. */
const TraceStepSchema = z.object({
  step: z.union([z.number(), z.string()]),
  array: z.array(z.number()),
  compare: z.tuple([z.number(), z.number()]).optional(),
  swap: z.tuple([z.number(), z.number()]).optional(),
  sorted: z.array(z.number()).optional(),
});

/** One MemoryBoxes box: a variable's name, current value, and an illustrative
 * (not real, not run-to-run stable) stack address. `pointsTo` names another
 * box in the same scene for a pointer arrow. */
const MemoryBoxSchema = z.object({
  name: z.string().min(1),
  value: z.string().min(1),
  address: z.string().min(1),
  isPointer: z.boolean().optional(),
  pointsTo: z.string().optional(),
});

/** One Bug of the Day: the episode has one record; a second bug scene (EP10's bonus bug) carries its own on the scene. */
const BugSchema = z.object({
  wrong: z.string().min(1),
  error: z.string().min(1),
  fixed: z.string().min(1),
  why: z.string().min(1),
});

const SceneSchema = z.object({
  id: z.number().int().positive(),
  template: SceneTemplateSchema,
  startSec: z.number().nonnegative(),
  lengthSec: z.number().positive(),
  onScreen: z.string(),
  animation: z.string(),
  sfx: z.array(z.string()),
  /** Narration for this scene, with [HL n] / [TRACK a=1] cues left inline. */
  narration: z.string(),
  code: CodeSchema.optional(),
  trace: z.array(TraceStepSchema).optional(),
  boxes: z.array(MemoryBoxSchema).optional(),
  /** Arrays, strings, grids and steps for a memory-boxes scene (see lib/memory.ts); instead of `boxes`. */
  memory: MemoryDataSchema.optional(),
  /** Only for a bug-of-the-day scene that is not the episode's main bug. */
  bug: BugSchema.optional(),
  /** Concept slide only: the numbered points, written out (otherwise they are cut from the narration). */
  points: z.array(z.string().min(1)).min(1).max(4).optional(),
  /** Concept slide only: the analogy card, written out (otherwise cut from `onScreen`). */
  analogy: z.object({ title: z.string().min(1), body: z.string().min(1) }).optional(),
  /** Concept slide only: a structured diagram drawn instead of the numbered points. */
  diagram: DiagramSchema.optional(),
});

const ChapterSchema = z.object({
  /** Timestamp as written in the Bible, e.g. "1:05". */
  t: z.string(),
  label: z.string(),
});

const ThumbnailSchema = z.object({
  /** The big on-thumbnail text, best-effort extracted from the Bible's Thumbnail bullet. */
  text: z.string(),
  /** The full Thumbnail bullet, verbatim — nothing is lost even when text/pose extraction is imperfect. */
  visual: z.string(),
  /** Best-effort extract of what Xecxec is doing in the thumbnail. */
  pose: z.string(),
});

const YouTubeSchema = z.object({
  title: z.string().min(1),
  description: z.string().min(1),
  chapters: z.array(ChapterSchema),
  tags: z.array(z.string()),
  thumbnail: ThumbnailSchema,
});

const ShortSchema = z.object({
  id: z.enum(["S1", "S2", "S3", "S4", "S5"]),
  title: z.string().min(1),
  hook: z.string().min(1),
  script: z.string().min(1),
  onScreen: z.string(),
  fromScenes: z.array(z.number().int().positive()),
  lengthSec: z.number().positive(),
  caption: z.string(),
  hashtags: z.array(z.string()),
});

export const EpisodeSchema = z.object({
  /** Course language; absent = C. Decides the narration folder, the compile command and which ep-keyed tables apply. */
  lang: z.enum(LANGS).optional(),
  /** Title of the next episode for the outro. The C course reads it from a table; other courses carry it here. */
  nextTitle: z.string().optional(),
  ep: z.number().int().positive(),
  title: z.string().min(1),
  module: z.number().int().min(0).max(13),
  lengthSec: z.number().positive(),
  colours: z.object({ bg: z.string().min(1), accent: z.string().min(1) }),
  learningGoals: z.array(z.string().min(1)).min(1),
  youtube: YouTubeSchema,
  scenes: z.array(SceneSchema).min(1),
  bug: BugSchema,
  pun: z.string().min(1),
  challenge: z.string().min(1),
  challengeAnswer: z.string().min(1),
  shorts: z.array(ShortSchema),
});

export type Episode = z.infer<typeof EpisodeSchema>;
export type Scene = z.infer<typeof SceneSchema>;
export type Short = z.infer<typeof ShortSchema>;
