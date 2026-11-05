import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { CodeBlock, Panel, Sticker } from "../ui";
import { impactShakeX, springs } from "../lib/motion";
import { errorExcerpt } from "../lib/errorExcerpt";
import type { BugOverride } from "../lib/bugOverrides";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type BugOfTheDayProps = BaseSceneProps & {
  wrongCode: string;
  error: string;
  /** Hand-written panel for a bug whose Bible text has nothing to show (see lib/bugOverrides.ts). */
  errorOverride?: BugOverride;
  fixedCode: string;
  why?: string;
};

/** Real C reliably has `;`, `{` or `#include`; prose and paths do not. */
const looksLikeCode = (text: string): boolean => /[;{]|#include/.test(text);

const MIN_BODY_PX = 22;
/** The error panel shows at most two lines (errorExcerpt), so it can be big. */
const ERROR_SIZES = [44, 40, 36, 32, 28, 26, 24, MIN_BODY_PX];
const WHY_SIZES = [34, 32, 30, 28, 26, 24, MIN_BODY_PX];
/** Inner text width of a 1100px Panel (padding 32 + border 5, both sides). */
const PANEL_TEXT_WIDTH = 1100 - 74;

/** Largest size in the (descending) list that fits; the smallest (>= MIN_BODY_PX) otherwise. */
const pickFont = (sizes: number[], fits: (size: number) => boolean): number =>
  sizes.find(fits) ?? sizes[sizes.length - 1];

/** Rows the lines occupy when each wraps at `perRow` characters. */
const wrappedRows = (lines: string[], perRow: number): number =>
  lines.reduce((n, line) => n + Math.max(1, Math.ceil(line.length / Math.max(1, perRow))), 0);

/** Keeps every `error:` line (the teaching point), then the earliest other lines in order,
 * while the wrapped rows fit `maxRows`; whole lines only, with an ellipsis for anything dropped. */
const fitErrorLines = (lines: string[], perRow: number, maxRows: number): string[] => {
  if (wrappedRows(lines, perRow) <= maxRows) return lines;
  const keep = new Set<number>();
  lines.forEach((line, i) => {
    if (line.includes("error:")) keep.add(i);
  });
  for (let i = 0; i < lines.length; i++) {
    if (keep.has(i)) continue;
    const next = [...keep, i].sort((x, y) => x - y).map((k) => lines[k]);
    if (wrappedRows(next, perRow) + 1 > maxRows) break;
    keep.add(i);
  }
  return [...[...keep].sort((x, y) => x - y).map((k) => lines[k]), "…"];
};

/** Butter banner drops in; wrong code shakes and the GCC error appears; then the fix lands in mint. */
export const BugOfTheDay: React.FC<BugOfTheDayProps> = ({
  wrongCode,
  error,
  errorOverride,
  fixedCode,
  why,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const isFixed = frame >= Math.round(durationInFrames * 0.68);
  // Not every bug slot holds C: EP02's "wrong" is a quoted claim, EP03's a path, and EP05's
  // "fixed" is a sentence. Each side is judged on its own, so prose becomes a text card and
  // only real code goes through CodeBlock's C highlighting.
  const wrongIsCode = looksLikeCode(wrongCode);
  const fixedIsCode = looksLikeCode(fixedCode);
  const shownIsCode = isFixed ? fixedIsCode : wrongIsCode;
  const lineCount = (text: string, isCode: boolean): number =>
    isCode ? text.split("\n").length : 3;
  const codeLines = Math.max(lineCount(wrongCode, wrongIsCode), lineCount(fixedCode, fixedIsCode));
  const allErrorLines = errorOverride ? errorOverride.lines : errorExcerpt(error);
  // The error panel has to fit under the code panel and above the caption band. Budget:
  // 1080 - 80 top - 200 bottom = 800, minus banner (~70), two gaps (48), the code panel
  // (min(codeLines, 8) rows at 40px*1.5 + chrome), and the panel's own 64px padding + 10px
  // border. Text is never shrunk below MIN_BODY_PX: long lines WRAP (counted here, so the
  // budget sees every wrapped row) and only whole lines are dropped.
  const codePanelHeight = Math.min(codeLines * 60 + 50, 410);
  const errorTextBudget = 800 - 70 - 48 - codePanelHeight - 74;
  const errorFontSize = pickFont(ERROR_SIZES, (f) => {
    const perRow = Math.floor(PANEL_TEXT_WIDTH / (f * 0.6));
    return wrappedRows(allErrorLines, perRow) * f * 1.3 <= errorTextBudget;
  });
  const errorPerRow = Math.floor(PANEL_TEXT_WIDTH / (errorFontSize * 0.6));
  const maxErrorRows = Math.max(2, Math.floor(errorTextBudget / (errorFontSize * 1.3)));
  const errorText = fitErrorLines(allErrorLines, errorPerRow, maxErrorRows).join("\n");
  // "Why" sits under the FIXED chip (~110px) once the fix lands.
  const whyBudget = 800 - 70 - 48 - codePanelHeight - 110 - 16;
  const whyFontSize = pickFont(WHY_SIZES, (f) => {
    const perRow = Math.floor((1100 - 8) / (f * 0.52));
    return wrappedRows((why ?? "").split("\n"), perRow) * f * 1.4 <= whyBudget;
  });
  const phase2 = Math.round(durationInFrames * 0.4);
  const phase3 = Math.round(durationInFrames * 0.68);
  // A hang prints nothing: the cursor blinks for about 2s, then the viewer presses Ctrl+C.
  const ctrlCFrame = phase2 + 60;

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
            {shownIsCode ? (
              <CodeBlock
                source={isFixed ? fixedCode : wrongCode}
                width={1100}
                fontSize={40}
                maxHeight={410}
              />
            ) : (
              <Panel background={isFixed ? palette.mint : palette.cream} borderColor={palette.ink}>
                <div
                  style={{
                    fontFamily: fonts.body,
                    fontWeight: 700,
                    fontSize: 44,
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
                  overflowWrap: "anywhere",
                }}
              >
                {errorOverride?.hang ? (
                  <>
                    <span style={{ color: palette.white }}>{"$ ./program"}</span>
                    {"\n"}
                    {frame >= ctrlCFrame ? "^C" : ""}
                    {Math.floor((frame - phase2) / 15) % 2 === 0 ? "█" : " "}
                  </>
                ) : (
                  errorText
                )}
              </div>
            </Panel>
            {errorOverride?.caption ? (
              <div
                style={{
                  marginTop: 16,
                  fontFamily: fonts.body,
                  fontWeight: 700,
                  fontSize: 36,
                  color: readableOn(colours.bg),
                }}
              >
                {errorOverride.caption}
              </div>
            ) : null}
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
            {why && why.trim() !== fixedCode.trim() ? (
              <div
                style={{
                  fontFamily: fonts.body,
                  fontSize: whyFontSize,
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
