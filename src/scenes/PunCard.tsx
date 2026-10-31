import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { springs } from "../lib/motion";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type PunCardProps = BaseSceneProps & {
  pun: string;
};

/** Full tomato screen, one pun, Xecxec snaps. The card flips in, rimshot on landing. */
export const PunCard: React.FC<PunCardProps> = ({ pun }) => {
  const frame = useCurrentFrame();
  const flipScaleX = interpolate(frame, [0, 12], [0, 1], {
    easing: springs.slam,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const opacity = interpolate(frame, [0, 6], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Most puns are a short one-liner (the common case, sized big and centred).
  // A longer quote-style pun (like EP01's) needs a smaller size so it doesn't
  // grow tall enough to run into Xecxec's fixed bottom-right zone.
  const fontSize = pun.length > 60 ? 46 : 64;

  return (
    <SceneFrame
      colours={{ bg: palette.tomato, accent: palette.butter }}
      mascot={{ pose: "snap", size: 460, bottom: 30 }}
    >
      <AbsoluteFill
        style={{
          padding: "120px 120px 320px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: 48,
        }}
      >
        <div
          style={{
            scale: `${flipScaleX} 1`,
            opacity,
            fontFamily: fonts.title,
            fontSize,
            color: readableOn(palette.tomato),
            textAlign: "center",
            lineHeight: 1.3,
            maxWidth: "76%",
          }}
        >
          {pun}
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
