import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn } from "../theme/contrast";
import { Sticker, Chip } from "../ui";
import { enterProgress, springs } from "../lib/motion";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type TitleCardProps = BaseSceneProps & {
  ep: number;
  title: string;
  moduleLabel?: string;
};

/** Title card: EP sticker, huge outlined title that slams in, underline wipe, Xecxec scuttles in. */
export const TitleCard: React.FC<TitleCardProps> = ({ ep, title, moduleLabel, colours }) => {
  const frame = useCurrentFrame();
  const titleScale = interpolate(enterProgress(frame, 0, 12), [0, 1], [1.2, 1]);
  const titleOpacity = interpolate(frame, [0, 6], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const underlineWidth = interpolate(frame, [6, 16], [0, 1], {
    easing: springs.slam,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <SceneFrame colours={colours} mascot={{ pose: "dance", size: 520, bottom: 40 }}>
      <AbsoluteFill
        style={{
          padding: 96,
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "center",
          gap: 32,
        }}
      >
        <div style={{ position: "absolute", top: 96, left: 96, display: "flex", gap: 20 }}>
          <Sticker text={`EP ${String(ep).padStart(2, "0")}`} background={palette.butter} />
          {moduleLabel ? <Chip text={moduleLabel} background={palette.white} /> : null}
        </div>

        <div
          style={{
            fontFamily: fonts.title,
            fontSize: 128,
            lineHeight: 1.05,
            color: colours.bg,
            WebkitTextStroke: `4px ${accentOn(colours.bg, colours.accent)}`,
            paintOrder: "stroke fill",
            textTransform: "uppercase",
            textAlign: "center",
            scale: `${titleScale} ${titleScale}`,
            opacity: titleOpacity,
            maxWidth: "90%",
          }}
        >
          {title}
        </div>
        <div
          style={{
            width: `${underlineWidth * 60}%`,
            height: 10,
            background: colours.accent,
          }}
        />
      </AbsoluteFill>
    </SceneFrame>
  );
};
