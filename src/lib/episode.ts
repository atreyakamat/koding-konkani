import { z } from "zod";

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

const BugSchema = z.object({
  wrong: z.string().min(1),
  error: z.string().min(1),
  fixed: z.string().min(1),
  why: z.string().min(1),
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
