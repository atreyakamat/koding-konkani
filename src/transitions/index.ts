import { wipe } from "@remotion/transitions/wipe";
import { slide } from "@remotion/transitions/slide";
import { flip } from "@remotion/transitions/flip";
import { clockWipe } from "@remotion/transitions/clock-wipe";
import { fade } from "@remotion/transitions/fade";
import type { TransitionPresentation } from "@remotion/transitions";
import type { SceneTemplate } from "../lib/episode";
import { palette } from "../theme/palette";
import { hardCutImpact, pushIn, windowPop, whip, split } from "./custom";
import type { SfxName } from "../audio/sfx-levels";

export { TRANSITION_FRAMES } from "./custom";

export type TransitionName =
  | "hard-cut"
  | "ink-wipe"
  | "slide-left"
  | "slide-right"
  | "push-in"
  | "window-pop"
  | "whip"
  | "split"
  | "flip"
  | "clock-wipe"
  | "fade";

const SFX_FOR: Record<TransitionName, SfxName> = {
  "hard-cut": "thud",
  "ink-wipe": "whoosh",
  "slide-left": "whoosh",
  "slide-right": "whoosh",
  "push-in": "marker-swipe",
  "window-pop": "key-tick",
  whip: "buzzer",
  split: "ding",
  flip: "pop",
  "clock-wipe": "stamp",
  fade: "chime",
};

/** docs/STYLE.md section 2: From-template -> To-template -> named transition.
 * "Cold open" is scene id 1 specifically; everything else keys off template. */
type Pair = { from: SceneTemplate | "cold-open" | "any"; to: SceneTemplate | "any"; name: TransitionName };

const RULES: Pair[] = [
  { from: "cold-open", to: "title-card", name: "hard-cut" },
  { from: "title-card", to: "any", name: "ink-wipe" },
  { from: "concept-slide", to: "concept-slide", name: "slide-left" }, // direction alternates, see pickSlideDirection
  { from: "concept-slide", to: "code-explain", name: "push-in" },
  { from: "code-explain", to: "terminal", name: "window-pop" },
  { from: "any", to: "bug-of-the-day", name: "whip" },
  { from: "any", to: "pun-card", name: "flip" },
  { from: "pun-card", to: "challenge", name: "clock-wipe" },
  { from: "challenge", to: "outro", name: "fade" },
];

/**
 * Resolves the STYLE.md transition for a from -> to scene pair. `isColdOpen`
 * marks the very first scene of the episode (template-based rules can't
 * distinguish "the cold open" from any other concept-slide). `previousName`
 * and a running `slideDirectionToggle` are used to honour "never the same
 * transition twice in a row" and "alternate left and right" for repeated
 * Concept-slide-to-Concept-slide cuts.
 */
export const resolveTransition = (
  fromTemplate: SceneTemplate,
  toTemplate: SceneTemplate,
  opts: { isColdOpen: boolean; previousName: TransitionName | null; slideGoesLeft: boolean },
): { name: TransitionName; nextSlideGoesLeft: boolean } => {
  const from = opts.isColdOpen ? "cold-open" : fromTemplate;
  const match =
    RULES.find((r) => r.from === from && r.to === toTemplate) ??
    RULES.find((r) => r.from === from && r.to === "any") ??
    RULES.find((r) => r.from === "any" && r.to === toTemplate);

  let name: TransitionName = match?.name ?? "fade";
  let nextSlideGoesLeft = opts.slideGoesLeft;

  if (name === "slide-left") {
    name = opts.slideGoesLeft ? "slide-left" : "slide-right";
    nextSlideGoesLeft = !opts.slideGoesLeft;
  }

  if (name === opts.previousName) {
    // Never the same transition twice in a row: fall back to fade, or to
    // ink-wipe if fade was itself the repeat.
    name = name === "fade" ? "ink-wipe" : "fade";
  }

  return { name, nextSlideGoesLeft };
};

export const sfxForTransition = (name: TransitionName): SfxName => SFX_FOR[name];

export const presentationForTransition = (name: TransitionName): TransitionPresentation<Record<string, unknown>> => {
  switch (name) {
    case "hard-cut":
      return hardCutImpact() as TransitionPresentation<Record<string, unknown>>;
    case "ink-wipe":
      return wipe({
        direction: "from-left",
        innerEnterStyle: { backgroundColor: palette.tomato },
        innerExitStyle: { backgroundColor: palette.tomato },
      }) as TransitionPresentation<Record<string, unknown>>;
    case "slide-left":
      return slide({ direction: "from-right" }) as TransitionPresentation<Record<string, unknown>>;
    case "slide-right":
      return slide({ direction: "from-left" }) as TransitionPresentation<Record<string, unknown>>;
    case "push-in":
      return pushIn() as TransitionPresentation<Record<string, unknown>>;
    case "window-pop":
      return windowPop() as TransitionPresentation<Record<string, unknown>>;
    case "whip":
      return whip() as TransitionPresentation<Record<string, unknown>>;
    case "split":
      return split() as TransitionPresentation<Record<string, unknown>>;
    case "flip":
      return flip({ direction: "from-right" }) as TransitionPresentation<Record<string, unknown>>;
    case "clock-wipe":
      return clockWipe({ width: 1920, height: 1080 }) as unknown as TransitionPresentation<Record<string, unknown>>;
    case "fade":
      return fade() as TransitionPresentation<Record<string, unknown>>;
    default:
      return fade() as TransitionPresentation<Record<string, unknown>>;
  }
};
