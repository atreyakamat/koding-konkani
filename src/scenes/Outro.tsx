import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { Panel, Chip } from "../ui";
import { Xecxec } from "../mascot/Xecxec";
import { typewriterChars, enterProgress } from "../lib/motion";
import type { BaseSceneProps } from "./types";

export type OutroProps = BaseSceneProps & {
  nextEp: number;
  nextTitle: string;
};

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

  return (
    <AbsoluteFill style={{ background: colours.bg, padding: 96, display: "flex" }}>
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
          <Panel background={palette.cream}>
            <Chip text="Next episode" background={colours.accent} color={palette.white} />
            <div
              style={{
                fontFamily: fonts.title,
                fontSize: 52,
                color: palette.ink,
                marginTop: 20,
                textTransform: "uppercase",
                lineHeight: 1.2,
              }}
            >
              EP {String(nextEp).padStart(2, "0")} · {nextTitle}
            </div>
          </Panel>
        </div>

        <div style={{ display: "flex", alignItems: "center", gap: 28 }}>
          <Xecxec pose="wave" size={150} />
          <div
            style={{ fontFamily: fonts.body, fontWeight: 700, fontSize: 38, color: palette.ink }}
          >
            {SIGN_OFF.slice(0, visibleChars)}
          </div>
        </div>
      </div>

      {/* right 42% intentionally empty: YouTube end-screen (next video + subscribe) */}
      <div style={{ width: "42%" }} />
    </AbsoluteFill>
  );
};
