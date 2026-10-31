import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { CodeBlock, Panel, Sticker } from "../ui";
import { impactShakeX, springs } from "../lib/motion";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type BugOfTheDayProps = BaseSceneProps & {
  wrongCode: string;
  error: string;
  fixedCode: string;
  why?: string;
};

/** Butter banner drops in; wrong code shakes and the GCC error appears; then the fix lands in mint. */
export const BugOfTheDay: React.FC<BugOfTheDayProps> = ({
  wrongCode,
  error,
  fixedCode,
  why,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  // Not every "bug" is broken code — some are a wrong mental model (EP02: a quoted
  // claim) or a config/path value (EP03). Rendering those through CodeBlock's C
  // syntax highlighting looked wrong and didn't wrap long lines. A real C snippet
  // reliably has `;`, `{` or `#include`; prose/paths don't.
  const isCode = /[;{]|#include/.test(wrongCode) || /[;{]|#include/.test(fixedCode);
  const codeLines = Math.max(wrongCode.split("\n").length, fixedCode.split("\n").length);
  const errorLines = error.split("\n").length;
  // GCC output can run long (EP01: 10 lines) — a compact size keeps the full, real error
  // visible (truncating a teaching moment would be worse) while clearing the caption band.
  const errorFontSize = errorLines > 6 ? 22 : 28;
  const phase2 = Math.round(durationInFrames * 0.4);
  const phase3 = Math.round(durationInFrames * 0.68);
  const isFixed = frame >= phase3;

  const bannerY = interpolate(frame, [0, 10], [-140, 0], {
    easing: springs.slam,
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const shakeX = impactShakeX(frame, 8, 14);
  const errorOpacity = interpolate(frame, [phase2, phase2 + 8], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });
  const fixOpacity = interpolate(frame, [phase3, phase3 + 10], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <SceneFrame
      colours={colours}
      mascot={{
        poses: [
          { frame: phase2, pose: "shellShake" },
          { frame: phase3, pose: "clawsUp" },
        ],
        bubbles: [
          { at: phase2, text: "Oops!" },
          { at: phase3, text: "Fixed!" },
        ],
      }}
    >
      <AbsoluteFill
        style={{
          padding: "80px 96px 200px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          gap: 24,
        }}
      >
        <div style={{ translate: `0px ${bannerY}px` }}>
          <Sticker text="Bug of the Day" background={palette.butter} rotateDeg={0} fontSize={40} />
        </div>

        <div style={{ display: "flex", gap: 48, width: "100%", justifyContent: "center" }}>
          <div
            style={{ translate: `${isFixed ? 0 : shakeX}px 0px`, width: "100%", maxWidth: 1100 }}
          >
            {isCode ? (
              <CodeBlock
                source={isFixed ? fixedCode : wrongCode}
                width={1100}
                fontSize={32}
                maxVisibleLines={Math.min(codeLines, 8)}
              />
            ) : (
              <Panel background={isFixed ? palette.mint : palette.cream} borderColor={palette.ink}>
                <div
                  style={{
                    fontFamily: fonts.body,
                    fontWeight: 700,
                    fontSize: 36,
                    lineHeight: 1.4,
                    color: palette.ink,
                    whiteSpace: "pre-wrap",
                  }}
                >
                  {isFixed ? fixedCode : wrongCode}
                </div>
              </Panel>
            )}
          </div>
        </div>

        {!isFixed ? (
          <div style={{ opacity: errorOpacity, width: "100%", maxWidth: 1100 }}>
            <Panel background={palette.darkBlue} borderColor={palette.ink}>
              <div
                style={{
                  fontFamily: fonts.code,
                  fontSize: errorFontSize,
                  lineHeight: 1.3,
                  color: palette.tomato,
                  whiteSpace: "pre-wrap",
                }}
              >
                {error}
              </div>
            </Panel>
          </div>
        ) : (
          <div
            style={{
              opacity: fixOpacity,
              width: "100%",
              maxWidth: 1100,
              display: "flex",
              flexDirection: "column",
              gap: 16,
            }}
          >
            <Panel background={palette.mint} borderColor={palette.ink}>
              <div style={{ fontFamily: fonts.title, fontSize: 28, color: palette.ink }}>FIXED</div>
            </Panel>
            {why ? (
              <div
                style={{
                  fontFamily: fonts.body,
                  fontSize: 32,
                  color: palette.ink,
                  lineHeight: 1.4,
                }}
              >
                {why}
              </div>
            ) : null}
          </div>
        )}
      </AbsoluteFill>
    </SceneFrame>
  );
};
