/**
 * Cues let Phase 5 (word-timestamp driven timing) tell a scene exactly when to
 * highlight a line, update a tracked variable, or reveal the next item.
 * Until then, scenes fall back to evenly spaced defaults derived from `durationInFrames`.
 */
export type Cue =
  | { frame: number; type: "reveal"; index: number }
  | { frame: number; type: "hl"; line: number }
  | { frame: number; type: "track"; name: string; value: string };

/** Evenly spaced `reveal` cues for `count` items across `durationInFrames`. */
export const defaultRevealCues = (count: number, durationInFrames: number): Cue[] => {
  if (count <= 0) {
    return [];
  }
  return Array.from({ length: count }, (_, index) => ({
    type: "reveal" as const,
    index,
    frame: Math.round((durationInFrames * index) / count),
  }));
};

/** Frame at which the `reveal` cue for `index` fires, falling back to even spacing. */
export const revealFrame = (
  cues: Cue[] | undefined,
  index: number,
  count: number,
  durationInFrames: number,
): number => {
  const explicit = cues?.find((cue) => cue.type === "reveal" && cue.index === index);
  if (explicit) {
    return explicit.frame;
  }
  return defaultRevealCues(count, durationInFrames)[index]?.frame ?? 0;
};

/** Evenly spaced `hl` cues across `durationInFrames`, one per non-blank source line. */
export const defaultHlCues = (sourceLines: string[], durationInFrames: number): Cue[] => {
  const codeLines = sourceLines
    .map((text, index) => ({ text, line: index + 1 }))
    .filter(({ text }) => text.trim().length > 0);
  if (codeLines.length === 0) {
    return [];
  }
  return codeLines.map(({ line }, index) => ({
    type: "hl" as const,
    line,
    frame: Math.round((durationInFrames * index) / codeLines.length),
  }));
};

/** The highlighted line at `frame`: the latest `hl` cue at or before it. */
export const hlLineAt = (cues: Cue[], frame: number): number | undefined => {
  let current: number | undefined;
  for (const cue of cues) {
    if (cue.type === "hl" && cue.frame <= frame) {
      current = cue.line;
    }
  }
  return current;
};

/** All tracked variable values visible at `frame` (every `track` cue at or before it). */
export const trackValuesAt = (cues: Cue[], frame: number): Record<string, string> => {
  const values: Record<string, string> = {};
  for (const cue of cues) {
    if (cue.type === "track" && cue.frame <= frame) {
      values[cue.name] = cue.value;
    }
  }
  return values;
};
