import { useCurrentFrame, interpolate, useVideoConfig } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";

const SHOW_FOR_SECONDS = 3;

/**
 * "TIP: SET SPEED TO 1.5x" chip, shown for 3s somewhere in the first 10s of
 * every episode (docs/STYLE.md section 1). Mount it at the point in the
 * timeline where it should appear; it manages its own fade in/out.
 */
export const SpeedTip: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const showFrames = SHOW_FOR_SECONDS * fps;

  const opacity = interpolate(frame, [0, 8, showFrames - 10, showFrames], [0, 1, 1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  if (frame >= showFrames) {
    return null;
  }

  return (
    <div
      style={{
        position: "absolute",
        bottom: 56,
        right: 56,
        opacity,
        background: palette.butter,
        color: palette.ink,
        fontFamily: fonts.body,
        fontWeight: 700,
        fontSize: 26,
        letterSpacing: 1,
        padding: "12px 20px",
        border: `${brutal.border}px solid ${palette.ink}`,
        boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
      }}
    >
      TIP: SET SPEED TO 1.5x
    </div>
  );
};
