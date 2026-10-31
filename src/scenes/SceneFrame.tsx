import type { PropsWithChildren } from "react";
import { AbsoluteFill } from "remotion";
import { Backdrop } from "../ui/Backdrop";
import { MascotCompanion, type MascotConfig } from "../mascot/MascotCompanion";
import type { SceneColours } from "./types";

export type SceneFrameProps = PropsWithChildren<{
  colours: SceneColours;
  /** Xecxec's behaviour in this scene. Pass `false` only where the layout reserves the space. */
  mascot?: MascotConfig | false;
}>;

/** Every scene sits in this: animated backdrop, content, and Xecxec in his corner. */
export const SceneFrame: React.FC<SceneFrameProps> = ({ colours, mascot = {}, children }) => (
  <AbsoluteFill>
    <Backdrop background={colours.bg} accent={colours.accent} />
    {children}
    {mascot === false ? null : <MascotCompanion {...mascot} />}
  </AbsoluteFill>
);
