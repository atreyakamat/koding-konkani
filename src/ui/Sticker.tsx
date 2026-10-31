import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";

export type StickerProps = {
  text: string;
  background: string;
  color?: string;
  rotateDeg?: number;
  fontSize?: number;
};

/** A rotated badge, e.g. the "EP 01" sticker on a title card. */
export const Sticker: React.FC<StickerProps> = ({
  text,
  background,
  color = palette.ink,
  rotateDeg = -6,
  fontSize = 40,
}) => {
  return (
    <div
      style={{
        display: "inline-block",
        background,
        color,
        fontFamily: fonts.title,
        fontSize,
        letterSpacing: 2,
        padding: "10px 24px",
        border: `${brutal.borderThick}px solid ${palette.ink}`,
        boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
        rotate: `${rotateDeg}deg`,
        textTransform: "uppercase",
      }}
    >
      {text}
    </div>
  );
};
