/** When each memory frame of a Short's boxes visual starts, in sync with the narration (pure, so Node scripts can run it).
 * A frame's cue is the spoken form of its label's code ("temp = a;" -> "temp equals a"); the frame starts at the first
 * narrated word run that matches, searching forward so frames stay in order. A frame whose cue is not found starts at its
 * even share of the Short. Each frame is held at least MIN_HOLD frames, and every later frame keeps room to appear. */
export type WordTime = { text: string; startMs: number };

export const MIN_HOLD = 24;
const LEAD = 3;

const norm = (s: string): string => s.toLowerCase().replace(/[^a-z0-9]/g, "");

/** Spoken tokens of a label: a leading "step 2:" is dropped and "=" is read as "equals". */
export const cueTokens = (label: string | undefined): string[] =>
  (label ?? "")
    .replace(/^\s*step\s*\d+\s*:/i, " ")
    .replace(/=+/g, " equals ")
    .split(/[^A-Za-z0-9]+/)
    .map(norm)
    .filter((t) => t !== "");

const findRun = (words: string[], tokens: string[], from: number): number => {
  for (let i = from; i + tokens.length <= words.length; i++)
    if (tokens.every((t, k) => words[i + k] === t)) return i;
  return -1;
};

export const frameStarts = (
  labels: (string | undefined)[],
  words: WordTime[],
  fps: number,
  durationInFrames: number,
): number[] => {
  const spoken = words.map((w) => norm(w.text));
  const count = labels.length;
  const starts: number[] = [0];
  let from = 0;
  for (let k = 1; k < count; k++) {
    const all = cueTokens(labels[k]);
    let idx = -1;
    for (const n of [Math.min(3, all.length), Math.min(2, all.length)]) {
      if (n < 2 && !(n === 1 && all[0].length >= 4)) continue;
      idx = findRun(spoken, all.slice(0, n), from);
      if (idx >= 0) break;
    }
    let start = Math.round((k * durationInFrames) / count);
    if (idx >= 0) {
      start = Math.max(0, Math.round((words[idx].startMs / 1000) * fps) - LEAD);
      from = idx + 1;
    }
    start = Math.max(start, starts[k - 1] + MIN_HOLD);
    starts.push(Math.min(start, Math.max(starts[k - 1] + 1, durationInFrames - MIN_HOLD * (count - k))));
  }
  return starts;
};

/** Index of the frame shown at `frame`. */
export const frameAt = (starts: number[], frame: number): number => {
  let k = 0;
  for (let i = 0; i < starts.length; i++) if (frame >= starts[i]) k = i;
  return k;
};
