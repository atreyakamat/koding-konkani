import { useCurrentFrame } from "remotion";
import { SpeechBubble } from "../ui/SpeechBubble";
import { enterProgress } from "../lib/motion";
import { Xecxec, type XecxecPose } from "./Xecxec";

export type MascotConfig = {
  /** Pose timeline: the last entry whose `frame` has passed is active. */
  poses?: { frame: number; pose: XecxecPose }[];
  pose?: XecxecPose;
  /** Short reactions (1-4 words), each shown from `at` for `frames` (default 75). */
  bubbles?: { at: number; text: string; frames?: number }[];
  side?: "left" | "right";
  /** Width in px. 300 is ~23% of a 1080p frame's height. */
  size?: number;
  /** Distance from the bottom edge in px. */
  bottom?: number;
  /** Anchor to the top edge instead (no bubble); for scenes that fill the lower canvas. */
  top?: number;
};

const poseAt = (config: MascotConfig, frame: number): { pose: XecxecPose; since: number } => {
  let active: { pose: XecxecPose; since: number } = { pose: config.pose ?? "idle", since: 0 };
  for (const entry of config.poses ?? []) {
    if (entry.frame <= frame) active = { pose: entry.pose, since: entry.frame };
  }
  return active;
};

/**
 * Xecxec's fixed home in a scene: scuttles in, switches pose on cue, and pops a short
 * speech bubble. Never covers the centre, where captions sit.
 */
export const MascotCompanion: React.FC<MascotConfig> = (config) => {
  const frame = useCurrentFrame();
  const { side = "right", size = 300, bottom = 96 } = config;
  const { pose, since } = poseAt(config, frame);
  const enter = enterProgress(frame, 4, 14);
  const offscreen = side === "right" ? 1 : -1;

  const activeBubble =
    config.top === undefined
      ? (config.bubbles ?? []).find((b) => frame >= b.at && frame < b.at + (b.frames ?? 75))
      : undefined;
  const bubbleProgress = activeBubble ? enterProgress(frame, activeBubble.at, 8) : 0;

  return (
    <div
      style={{
        position: "absolute",
        ...(config.top === undefined ? { bottom } : { top: config.top }),
        [side]: 72,
        translate: `${(1 - enter) * 260 * offscreen}px 0`,
      }}
    >
      {bubbleProgress > 0 ? (
        <div
          style={{
            position: "absolute",
            bottom: size * 0.83 + 8,
            [side === "right" ? "right" : "left"]: size * 0.2,
            whiteSpace: "nowrap",
            scale: `${bubbleProgress} ${bubbleProgress}`,
            transformOrigin: side === "right" ? "bottom right" : "bottom left",
          }}
        >
          <SpeechBubble tailSide={side} fontSize={40}>
            {activeBubble?.text}
          </SpeechBubble>
        </div>
      ) : null}
      <Xecxec pose={pose} size={size} frame={frame - since} flip={side === "left"} />
    </div>
  );
};
