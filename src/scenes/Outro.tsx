import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { Panel, Chip } from "../ui";
import { typewriterChars, enterProgress } from "../lib/motion";
import { textTransformFor } from "../lib/textCase";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type OutroProps = BaseSceneProps & {
  nextEp: number;
  /** Missing after the last episode: the card then says thank you instead. */
  nextTitle?: string;
};

const FINALE_LINE = "86 episodes. You did it.";
/** Long headlines drop a size so they stay within three lines of the card. */
const headlineSize = (text: string): number => (text.length > 26 ? 64 : 76);

const SIGN_OFF = "Keep coding, says Xecxec!";

/**
 * Next-episode teaser and sign-off. The right 40% stays empty for YouTube's
 * end-screen elements (next video + subscribe) over the last 20s.
 */
export const Outro: React.FC<OutroProps> = ({ nextEp, nextTitle, colours, durationInFrames }) => {
  const frame = useCurrentFrame();
  const cardProgress = enterProgress(frame, 0, 12);
  const signOffStart = Math.round(durationInFrames * 0.35);
  const visibleChars = typewriterChars(SIGN_OFF, frame, signOffStart, 1);
  const isFinale = nextTitle === undefined;
  const headline = isFinale
    ? FINALE_LINE
    : `EP ${String(nextEp).padStart(2, "0")} · ${nextTitle}`;

  return (
    <SceneFrame colours={colours} mascot={{ pose: "dance", side: "left", size: 380, bottom: 60 }}>
      <AbsoluteFill style={{ padding: 96, display: "flex" }}>
        <div
          style={{
            width: "58%",
            display: "flex",
            flexDirection: "column",
            gap: 32,
            justifyContent: "center",
          }}
        >
          <div
            style={{
              opacity: cardProgress,
              translate: `0px ${(1 - cardProgress) * 40}px`,
            }}
          >
            <Panel background={palette.cream} padding={44}>
              <Chip
                text={isFinale ? "Thank you" : "Next episode"}
                fontSize={44}
                background={colours.accent}
                color={readableOn(colours.accent)}
              />
              <div
                style={{
                  fontFamily: fonts.title,
                  fontSize: headlineSize(headline),
                  color: palette.ink,
                  marginTop: 20,
                  textTransform: textTransformFor(headline),
                  lineHeight: 1.2,
                }}
              >
                {headline}
              </div>
            </Panel>
          </div>

          <div style={{ display: "flex", alignItems: "center", gap: 28 }}>
            <div
              style={{
                fontFamily: fonts.body,
                fontWeight: 700,
                fontSize: 60,
                color: readableOn(colours.bg),
              }}
            >
              {SIGN_OFF.slice(0, visibleChars)}
            </div>
          </div>
        </div>

        {/* right 42% intentionally empty: YouTube end-screen (next video + subscribe) */}
        <div style={{ width: "42%" }} />
      </AbsoluteFill>
    </SceneFrame>
  );
};
