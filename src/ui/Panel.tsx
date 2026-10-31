import type { CSSProperties, PropsWithChildren } from "react";
import { palette, brutal } from "../theme/palette";

export type PanelProps = PropsWithChildren<{
  background: string;
  borderColor?: string;
  shadowColor?: string;
  borderWidth?: number;
  shadowOffset?: number;
  padding?: number;
  style?: CSSProperties;
}>;

/** Neo-brutalist block: flat colour, thick ink border, hard offset shadow. No gradients, no blur. */
export const Panel: React.FC<PanelProps> = ({
  children,
  background,
  borderColor = palette.ink,
  shadowColor = palette.ink,
  borderWidth = brutal.borderThick,
  shadowOffset = brutal.shadow,
  padding = 32,
  style,
}) => {
  return (
    <div
      style={{
        background,
        border: `${borderWidth}px solid ${borderColor}`,
        boxShadow: `${shadowOffset}px ${shadowOffset}px 0 0 ${shadowColor}`,
        padding,
        boxSizing: "border-box",
        ...style,
      }}
    >
      {children}
    </div>
  );
};
