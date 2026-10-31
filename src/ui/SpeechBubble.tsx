import type { CSSProperties, PropsWithChildren } from "react";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";

export type SpeechBubbleProps = PropsWithChildren<{
  background?: string;
  tailSide?: "left" | "right";
  fontSize?: number;
  style?: CSSProperties;
}>;

/** Xecxec never speaks, but reacts with a speech bubble (e.g. "It's Sheck Sheck."). */
export const SpeechBubble: React.FC<SpeechBubbleProps> = ({
  children,
  background = palette.white,
  tailSide = "left",
  fontSize = 32,
  style,
}) => {
  return (
    <div style={{ position: "relative", ...style }}>
      <div
        style={{
          background,
          color: palette.ink,
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize,
          padding: "16px 24px",
          border: `${brutal.border}px solid ${palette.ink}`,
          boxShadow: `6px 6px 0 0 ${palette.ink}`,
          borderRadius: 20,
        }}
      >
        {children}
      </div>
      <div
        style={{
          position: "absolute",
          bottom: -14,
          [tailSide]: 28,
          width: 0,
          height: 0,
          borderLeft: "14px solid transparent",
          borderRight: "14px solid transparent",
          borderTop: `18px solid ${palette.ink}`,
        }}
      />
      <div
        style={{
          position: "absolute",
          bottom: -9,
          [tailSide]: 32,
          width: 0,
          height: 0,
          borderLeft: "10px solid transparent",
          borderRight: "10px solid transparent",
          borderTop: `14px solid ${background}`,
        }}
      />
    </div>
  );
};
