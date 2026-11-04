import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { fitPun, PUN_BOX } from "../lib/punFit";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type PunCardProps = BaseSceneProps & {
  pun: string;
};

/** Full tomato screen, one pun, Xecxec snaps. The card flips in, rimshot on landing. */
export const PunCard: React.FC<PunCardProps> = ({ pun }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 6], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  const { size } = fitPun(pun);

  return (
    <SceneFrame
      colours={{ bg: palette.tomato, accent: palette.butter }}
      mascot={{ pose: "snap", size: 460, bottom: 30 }}
    >
      <AbsoluteFill
        style={{
          // Bottom padding keeps the text above Xecxec's corner (460px mascot, 30px up).
          padding: "120px 120px 340px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          gap: 48,
        }}
      >
        <div
          style={{
            opacity,
            fontFamily: fonts.title,
            fontSize: size,
            color: readableOn(palette.tomato),
            textAlign: "center",
            lineHeight: 1.3,
            maxWidth: PUN_BOX.width,
            overflowWrap: "anywhere",
          }}
        >
          {pun}
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
