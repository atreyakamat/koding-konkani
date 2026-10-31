import { Easing, interpolate } from "remotion";

/** Snappy spring presets shared by every scene. No floaty easing. */
export const springs = {
  /** Quick pop-in for cards, chips, badges. ~10 frames. */
  pop: Easing.spring({ damping: 12, mass: 0.6 }),
  /** A touch slower for big titles and panels. ~12 frames. */
  slam: Easing.spring({ damping: 14, mass: 0.8 }),
  /** Fast tick for small UI (ticks, counters). ~8 frames. */
  tick: Easing.spring({ damping: 10, mass: 0.4 }),
} as const;

/**
 * Standard "enter" progress: 0 before `start`, spring to 1 over `durationFrames`.
 * Use for scale/translate/opacity on an element appearing at `start`.
 */
export const enterProgress = (frame: number, start: number, durationFrames: number = 10): number =>
  interpolate(frame, [start, start + durationFrames], [0, 1], {
    easing: springs.pop,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

/**
 * 2-frame impact shake: returns a translateX offset in px, for a hit landing at `impactFrame`.
 */
export const impactShakeX = (frame: number, impactFrame: number, magnitude: number = 6): number =>
  interpolate(frame, [impactFrame, impactFrame + 1, impactFrame + 2], [magnitude, -magnitude, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

/**
 * Typewriter: how many characters of `text` should be visible at `frame`,
 * typing at `charsPerFrame` starting at `start`.
 */
export const typewriterChars = (
  text: string,
  frame: number,
  start: number,
  charsPerFrame: number = 0.9,
): number => {
  const typed = Math.floor((frame - start) * charsPerFrame);
  return Math.max(0, Math.min(text.length, typed));
};

/** Frame at which the typewriter above finishes typing `text`. */
export const typewriterEndFrame = (
  text: string,
  start: number,
  charsPerFrame: number = 0.9,
): number => start + Math.ceil(text.length / charsPerFrame);
