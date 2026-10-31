import { AbsoluteFill } from "remotion";
import { coloursForModule, fonts, palette } from "../theme";

export type ShortProps = { ep: number; id: string; hook: string; module: number };

/** Placeholder 1080x1920 layout: hook top, visual middle, captions bottom third. */
export const Short: React.FC<ShortProps> = ({ ep, id, hook, module }) => {
  const { bg, accent } = coloursForModule(module);
  return (
    <AbsoluteFill style={{ background: bg, padding: 80 }}>
      <div style={{ fontFamily: fonts.title, fontSize: 72, color: palette.ink }}>{hook}</div>
      <div style={{ marginTop: "auto", fontFamily: fonts.body, fontSize: 40, color: accent }}>
        Full video: EP {String(ep).padStart(2, "0")} ({id})
      </div>
    </AbsoluteFill>
  );
};
