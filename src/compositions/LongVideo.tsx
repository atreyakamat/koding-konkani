import { AbsoluteFill } from "remotion";
import { coloursForModule, fonts, palette } from "../theme";

export type LongVideoProps = { ep: number; title: string; module: number };

/** Placeholder: scenes are added in Phase 2, episode data in Phase 4. */
export const LongVideo: React.FC<LongVideoProps> = ({ ep, title, module }) => {
  const { bg, accent } = coloursForModule(module);
  return (
    <AbsoluteFill
      style={{ background: bg, justifyContent: "center", alignItems: "center", gap: 24 }}
    >
      <div style={{ fontFamily: fonts.title, fontSize: 64, color: accent }}>
        EP {String(ep).padStart(2, "0")}
      </div>
      <div style={{ fontFamily: fonts.title, fontSize: 96, color: palette.ink }}>{title}</div>
    </AbsoluteFill>
  );
};
