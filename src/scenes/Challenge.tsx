import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn } from "../theme/contrast";
import { Panel, Chip } from "../ui";
import { enterProgress } from "../lib/motion";
import { defaultRevealCues, revealFrame } from "../lib/cues";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type ChallengeProps = BaseSceneProps & {
  task: string;
  examples?: string[];
};

/** Challenge card: the task, example chips bouncing in, and the "comment your answer" call to action. */
export const Challenge: React.FC<ChallengeProps> = ({
  task,
  examples = [],
  colours,
  durationInFrames,
  cues,
}) => {
  const frame = useCurrentFrame();
  const revealCues = cues?.length
    ? cues
    : defaultRevealCues(examples.length, durationInFrames * 0.5);

  return (
    <SceneFrame
      colours={colours}
      mascot={{ pose: "dance", size: 380, bubbles: [{ at: 20, text: "Your turn!", frames: 90 }] }}
    >
      <AbsoluteFill
        style={{
          padding: 96,
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          gap: 56,
        }}
      >
        <div
          style={{ flex: 1, maxWidth: "62%", display: "flex", flexDirection: "column", gap: 28 }}
        >
          <Panel background={palette.cream}>
            <div
              style={{
                fontFamily: fonts.title,
                fontSize: 36,
                color: accentOn(palette.cream, colours.accent),
                marginBottom: 16,
              }}
            >
              CHALLENGE
            </div>
            <div
              style={{
                fontFamily: fonts.body,
                fontWeight: 700,
                fontSize: 44,
                color: palette.ink,
                lineHeight: 1.35,
              }}
            >
              {task}
            </div>
          </Panel>

          {examples.length > 0 ? (
            <div style={{ display: "flex", gap: 16, flexWrap: "wrap" }}>
              {examples.map((example, index) => {
                const start = revealFrame(
                  revealCues,
                  index,
                  examples.length,
                  durationInFrames * 0.5,
                );
                const progress = enterProgress(frame, start, 10);
                return (
                  <div
                    key={example}
                    style={{ scale: `${progress} ${progress}`, opacity: progress }}
                  >
                    <Chip text={example} background={palette.white} />
                  </div>
                );
              })}
            </div>
          ) : null}

          <div
            style={{
              fontFamily: fonts.body,
              fontWeight: 700,
              fontSize: 32,
              color: accentOn(colours.bg, colours.accent),
            }}
          >
            Comment your answer
          </div>
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
