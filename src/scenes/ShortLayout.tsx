import React, { type PropsWithChildren } from "react";
import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn, readableOn } from "../theme/contrast";
import { BRAND } from "../brand";
import { Backdrop, Panel, Sticker } from "../ui";
import { Xecxec } from "../mascot/Xecxec";
import { enterProgress } from "../lib/motion";
import type { BaseSceneProps } from "./types";

export type ShortLayoutProps = PropsWithChildren<
  BaseSceneProps & {
    ep: number;
    hook: string;
    /** Fallback text for the visual slot when no `children` visual is supplied. */
    visualLabel?: string;
    caption?: string;
    /** Frames the follow/subscribe end card is on screen (default 66 = 2.2 s at 30 fps). */
    endCardFrames?: number;
  }
>;

/** Frames each caption word stays highlighted. */
const FRAMES_PER_WORD = 10;
const CAPTION_START = 18;

/**
 * Short layout, 1080x1920. Safe zones: nothing right of x=940 (platform buttons) or
 * below y=1640 (platform caption overlay).
 *   y  60  progress bar
 *   y 110  hook (pops in on frame 0)
 *   y 500  visual slot: `children` (animated code, bug, memory) or a label card
 *   y1090  Xecxec dancing, plus the "Full video" sticker
 *   y1440  word-by-word caption, current word highlighted
 * The last `endCardFrames` replace the visual slot with the follow/subscribe card.
 */
export const ShortLayout: React.FC<ShortLayoutProps> = ({
  ep,
  hook,
  visualLabel,
  caption,
  colours,
  durationInFrames,
  endCardFrames = 66,
  children,
}) => {
  const frame = useCurrentFrame();
  const epLabel = String(ep).padStart(2, "0");

  // Frame 0 is already visible and moving: the hook starts at 55% scale, not blank.
  const hookScale = interpolate(enterProgress(frame, 0, 10), [0, 1], [0.55, 1]);
  const visualProgress = enterProgress(frame, 6, 12);
  const progress = Math.min(1, frame / Math.max(1, durationInFrames));

  const endStart = durationInFrames - endCardFrames;
  const showEnd = frame >= endStart;
  const endProgress = enterProgress(frame, endStart, 10);

  const words = (caption ?? "").split(/\s+/).filter(Boolean);
  const activeWord = Math.floor((frame - CAPTION_START) / FRAMES_PER_WORD);
  const hookInk = readableOn(colours.bg);

  return (
    <AbsoluteFill>
      <Backdrop background={colours.bg} accent={colours.accent} />

      {/* progress bar */}
      <div
        style={{
          position: "absolute",
          top: 56,
          left: 60,
          width: 860,
          height: 22,
          background: palette.white,
          border: `${brutal.border}px solid ${palette.ink}`,
        }}
      >
        <div style={{ width: `${progress * 100}%`, height: "100%", background: colours.accent }} />
      </div>

      {/* hook */}
      <div
        style={{
          position: "absolute",
          top: 120,
          left: 60,
          width: 860,
          scale: `${hookScale} ${hookScale}`,
          transformOrigin: "top left",
        }}
      >
        <div
          style={{
            fontFamily: fonts.title,
            fontSize: 76,
            color: hookInk,
            lineHeight: 1.12,
            textTransform: "uppercase",
          }}
        >
          {hook}
        </div>
      </div>

      {/* visual slot */}
      <div
        style={{
          position: "absolute",
          top: 440,
          left: 60,
          width: 860,
          height: 540,
          scale: `${visualProgress} ${visualProgress}`,
          opacity: showEnd ? 0 : 1,
          transformOrigin: "center top",
        }}
      >
        {children ?? (
          <Panel background={palette.cream} style={{ width: "100%", height: "100%" }}>
            <div
              style={{
                fontFamily: fonts.title,
                fontSize: 56,
                color: palette.ink,
                textAlign: "center",
                textTransform: "uppercase",
                lineHeight: 1.2,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                height: "100%",
              }}
            >
              {visualLabel ?? ""}
            </div>
          </Panel>
        )}
      </div>

      {/* end card: follow + subscribe, replaces the visual slot (no full-frame dimming) */}
      {showEnd ? (
        <div
          style={{
            position: "absolute",
            top: 440,
            left: 60,
            width: 860,
            height: 540,
            scale: `${endProgress} ${endProgress}`,
            transformOrigin: "center top",
          }}
        >
          <Panel
            background={palette.cream}
            style={{
              width: "100%",
              height: "100%",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              justifyContent: "center",
              gap: 28,
            }}
          >
            <div
              style={{
                fontFamily: fonts.title,
                fontSize: 84,
                color: palette.ink,
                textTransform: "uppercase",
              }}
            >
              Follow
            </div>
            <Sticker
              text={BRAND.instagramHandle}
              background={colours.accent}
              rotateDeg={-2}
              fontSize={64}
            />
            <div
              style={{
                fontFamily: fonts.body,
                fontWeight: 700,
                fontSize: 40,
                color: accentOn(palette.cream, colours.accent),
              }}
            >
              Subscribe: {BRAND.channelName}
            </div>
          </Panel>
        </div>
      ) : null}

      {/* mascot, always dancing, always in frame */}
      <div style={{ position: "absolute", top: 1085, left: 40 }}>
        <Xecxec pose="dance" size={420} />
      </div>
      <div style={{ position: "absolute", top: 1170, left: 520 }}>
        <Sticker
          text={`Full video: EP ${epLabel}`}
          background={palette.butter}
          rotateDeg={3}
          fontSize={40}
        />
      </div>

      {/* word-by-word caption */}
      {words.length > 0 ? (
        <div style={{ position: "absolute", top: 1440, left: 60, width: 860 }}>
          <div
            style={{
              background: colours.accent,
              border: `${brutal.border}px solid ${palette.ink}`,
              boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
              padding: "20px 28px",
              fontFamily: fonts.body,
              fontWeight: 700,
              fontSize: 56,
              lineHeight: 1.3,
              color: readableOn(colours.accent),
            }}
          >
            {words.map((word, i) => (
              <React.Fragment key={i}>
                <span
                  style={{
                    background: i === activeWord ? palette.butter : "transparent",
                    color: i === activeWord ? palette.ink : "inherit",
                    padding: "0 6px",
                  }}
                >
                  {word}
                </span>{" "}
              </React.Fragment>
            ))}
          </div>
        </div>
      ) : null}
    </AbsoluteFill>
  );
};
