import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn, readableOn } from "../theme/contrast";
import { Panel, Chip, CodeBlock } from "../ui";
import type { MascotConfig } from "../mascot/MascotCompanion";
import { typewriterChars } from "../lib/motion";
import { chooseFontSize } from "../lib/codeLayout";
import { defaultHlCues, hlLineAt, trackValuesAt } from "../lib/cues";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type CodeExplainProps = BaseSceneProps & {
  file: string;
  /** The code to type in. Absent for a scene whose JSON has no `code` field; then
   * `onScreen` is shown as a text card instead of being mistaken for code. */
  source?: string;
  onScreen?: string;
  /** Short explanation shown for a given highlighted line, e.g. {4: "function · text · end of statement"}. */
  labels?: Record<number, string>;
  /** Program output. Prints in a terminal under the code near the end of the scene. */
  output?: string;
};

/** 58% of the 1728px content width: the code panel never grows past this, so the
 * explanation card on the right is always fully on screen. */
const CODE_COLUMN_WIDTH = 1002;
/** Free height for the code column below the file chip: the frame is 1080 tall, 96px top
 * padding + ~64px chip + gap, and the burnt-in caption bar starts near y=905. */
const COLUMN_BOTTOM = 900;
const PANEL_TOP = 96 + 64 + 20;

/** Code explain: code types itself, then the active line gets a butter highlight with a live variable tracker. */
export const CodeExplain: React.FC<CodeExplainProps> = ({
  file,
  source,
  onScreen,
  labels,
  output,
  colours,
  durationInFrames,
  cues,
}) => {
  const frame = useCurrentFrame();
  const code = source ?? "";

  const typingEnd = Math.round(durationInFrames * 0.35);
  const charsPerFrame = Math.max(0.5, code.length / typingEnd);
  const visibleChars = typewriterChars(code, frame, 0, charsPerFrame);

  const sourceLines = code.split("\n");
  const freeHeight = COLUMN_BOTTOM - PANEL_TOP;
  const codeFont = chooseFontSize(code, CODE_COLUMN_WIDTH, freeHeight);
  const defaultCues = defaultHlCues(sourceLines, durationInFrames - typingEnd).map((cue) => ({
    ...cue,
    frame: cue.frame + typingEnd,
  }));
  const activeCues = cues?.length ? cues : defaultCues;
  const highlightLine = hlLineAt(activeCues, frame);
  const trackedValues = trackValuesAt(activeCues, frame);

  const outputStart = Math.round(durationInFrames * 0.78);
  const outputChars = output ? typewriterChars(output, frame, outputStart + 6, 1) : 0;
  const mascot: MascotConfig = output
    ? {
        poses: [{ frame: outputStart, pose: "clawsUp" }],
        bubbles: [{ at: outputStart + 10, text: "It runs!" }],
      }
    : {};

  return (
    <SceneFrame colours={colours} mascot={mascot}>
      <AbsoluteFill
        style={{
          padding: 96,
          display: "flex",
          flexDirection: "row",
          gap: 48,
          alignItems: "stretch",
        }}
      >
        <div
          style={{
            flex: `0 0 ${CODE_COLUMN_WIDTH}px`,
            maxWidth: CODE_COLUMN_WIDTH,
            display: "flex",
            flexDirection: "column",
            gap: 20,
          }}
        >
          <Chip text={file} background={colours.accent} color={readableOn(colours.accent)} />
          {source ? (
            <CodeBlock
              source={source}
              width={CODE_COLUMN_WIDTH}
              fontSize={codeFont}
              maxHeight={freeHeight}
              fillHeight={freeHeight}
              highlightLine={highlightLine}
              visibleChars={visibleChars}
            />
          ) : (
            <Panel background={palette.cream}>
              <div
                style={{
                  fontFamily: fonts.body,
                  fontWeight: 700,
                  fontSize: 40,
                  lineHeight: 1.4,
                  color: palette.ink,
                  whiteSpace: "pre-wrap",
                }}
              >
                {onScreen ?? ""}
              </div>
            </Panel>
          )}
        </div>

        <div style={{ flex: 1, minWidth: 0, display: "flex", flexDirection: "column", gap: 24 }}>
          <Panel background={palette.cream} style={{ minHeight: 160 }}>
            <div
              style={{ fontFamily: fonts.body, fontSize: 44, color: palette.ink, lineHeight: 1.35 }}
            >
              {highlightLine && labels?.[highlightLine] ? labels[highlightLine] : ""}
            </div>
          </Panel>

          {Object.keys(trackedValues).length > 0 ? (
            <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
              <div
                style={{
                  fontFamily: fonts.title,
                  fontSize: 24,
                  color: accentOn(colours.bg, colours.accent),
                  textTransform: "uppercase",
                }}
              >
                Tracker
              </div>
              <div style={{ display: "flex", flexWrap: "wrap", gap: 12 }}>
                {Object.entries(trackedValues).map(([name, value]) => (
                  <Chip
                    key={name}
                    text={`${name} = ${value}`}
                    background={palette.white}
                    fontSize={26}
                  />
                ))}
              </div>
            </div>
          ) : null}
          {output ? (
            <div
              style={{
                opacity: frame >= outputStart ? 1 : 0,
                background: palette.darkBlue,
                border: `5px solid ${palette.ink}`,
                boxShadow: `8px 8px 0 0 ${palette.ink}`,
                padding: "20px 32px",
                fontFamily: fonts.code,
                fontSize: 34,
                color: palette.mint,
                whiteSpace: "pre-wrap",
              }}
            >
              <span style={{ color: palette.white }}>{"$ ./program"}</span>
              {"\n"}
              {output.slice(0, outputChars)}
            </div>
          ) : null}
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
