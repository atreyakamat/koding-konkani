import type { CSSProperties } from "react";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";

export type ChipProps = {
  text: string;
  background: string;
  color?: string;
  fontSize?: number;
  style?: CSSProperties;
};

/** A small pill-shaped label: module badges, example chips, YouTube-chapter style tags. */
export const Chip: React.FC<ChipProps> = ({
  text,
  background,
  color = palette.ink,
  fontSize = 28,
  style,
}) => {
  return (
    <div
      style={{
        display: "inline-block",
        background,
        color,
        fontFamily: fonts.body,
        fontWeight: 700,
        fontSize,
        padding: "8px 20px",
        border: `${brutal.border}px solid ${palette.ink}`,
        boxShadow: `4px 4px 0 0 ${palette.ink}`,
        borderRadius: 8,
        ...style,
      }}
    >
      {text}
    </div>
  );
};
