import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { Panel, Chip } from "../ui";
import { enterProgress, typewriterChars } from "../lib/motion";
import type { BaseSceneProps } from "./types";

export type ShortLayoutProps = BaseSceneProps & {
  ep: number;
  hook: string;
  visualLabel?: string;
  caption?: string;
};

/**
 * Short layout, 1080x1920: hook top, visual middle, captions in the upper part of the
 * bottom third. Nothing sits right of x=940 (platform like/comment/share column) or
 * below y=1640 (platform caption/username overlay).
 */
export const ShortLayout: React.FC<ShortLayoutProps> = ({
  ep,
  hook,
  visualLabel,
  caption,
  colours,
}) => {
  const frame = useCurrentFrame();
  const hookProgress = enterProgress(frame, 0, 10);
  const visualProgress = enterProgress(frame, 8, 12);
  const captionVisible = typewriterChars(caption ?? "", frame, 20, 1.4);

  return (
    <AbsoluteFill style={{ background: colours.bg }}>
      <div
        style={{
          position: "absolute",
          top: 100,
          left: 60,
          width: 860,
          opacity: hookProgress,
          translate: `0px ${(1 - hookProgress) * -30}px`,
        }}
      >
        <div
          style={{
            fontFamily: fonts.title,
            fontSize: 64,
            color: readableOn(colours.bg),
            lineHeight: 1.15,
            textTransform: "uppercase",
          }}
        >
          {hook}
        </div>
      </div>

      <div
        style={{
          position: "absolute",
          top: 680,
          left: 60,
          width: 860,
          height: 560,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          scale: `${visualProgress} ${visualProgress}`,
          opacity: visualProgress,
        }}
      >
        <Panel background={palette.cream} style={{ width: "100%", height: "100%" }}>
          <div
            style={{
              fontFamily: fonts.body,
              fontSize: 36,
              color: palette.ink,
              textAlign: "center",
              display: "flex",
              alignItems: "center",
              justifyContent: "center",
              height: "100%",
            }}
          >
            {visualLabel ?? ""}
          </div>
        </Panel>
      </div>

      {caption ? (
        <div style={{ position: "absolute", top: 1340, left: 60, width: 820 }}>
          <div
            style={{
              background: colours.accent,
              border: `${brutal.border}px solid ${palette.ink}`,
              padding: "16px 24px",
              fontFamily: fonts.body,
              fontWeight: 700,
              fontSize: 42,
              color: readableOn(colours.accent),
              lineHeight: 1.3,
            }}
          >
            {caption.slice(0, captionVisible)}
          </div>
        </div>
      ) : null}

      <div style={{ position: "absolute", top: 1560, left: 60 }}>
        <Chip
          text={`Full video: EP ${String(ep).padStart(2, "0")}`}
          background={palette.white}
          fontSize={26}
        />
      </div>
    </AbsoluteFill>
  );
};
