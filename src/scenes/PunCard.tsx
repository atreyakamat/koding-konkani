import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { Xecxec } from "../mascot/Xecxec";
import { springs } from "../lib/motion";
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

  return (
    <AbsoluteFill
      style={{
        background: palette.tomato,
        padding: 120,
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
          fontSize: 64,
          color: readableOn(palette.tomato),
          textAlign: "center",
          lineHeight: 1.3,
          maxWidth: "85%",
        }}
      >
        {pun}
      </div>
      <Xecxec pose="snap" size={160} />
    </AbsoluteFill>
  );
};
