import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn, readableOn } from "../theme/contrast";
import { Panel, Chip, CodeBlock } from "../ui";
import type { MascotConfig } from "../mascot/MascotCompanion";
import { typewriterChars } from "../lib/motion";
import { stripMarkdown as sanitizeText } from "../lib/sanitize";
import { chooseFontSize } from "../lib/codeLayout";
import { defaultHlCues, hlLineAt, trackValuesAt } from "../lib/cues";
import { layoutOutput, TAKEOVER_PANEL_WIDTH } from "../lib/outputFit";
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
/** With program output on screen Xecxec is 240px at the bottom-right (top of his head ~y 820,
 * his "It runs!" bubble above to ~y 720), so the right column ends at y 700 and the output
 * panel is sized to the room left under the explanation card and tracker. */
const MASCOT_SIZE_WITH_OUTPUT = 240;
const RIGHT_COLUMN_BOTTOM = 700;
/** In takeover the panel runs down to y 790: Xecxec's head tops out near y 840 and his bubble is
 * dropped, so nothing else needs the space. */
const TAKEOVER_BOTTOM = 790;
const OUTPUT_ROOM = RIGHT_COLUMN_BOTTOM - 96 - 160 - 24 - 90 - 24;

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

  const outputLayout = output
    ? layoutOutput(output, OUTPUT_ROOM, TAKEOVER_BOTTOM - 96)
    : undefined;
  // When the output will take over the right column, the code panel is narrower for the whole scene
  // (no mid-scene reflow) so the terminal gets TAKEOVER_PANEL_WIDTH.
  const codeWidth = outputLayout?.fullColumn
    ? 1920 - 192 - 48 - TAKEOVER_PANEL_WIDTH
    : CODE_COLUMN_WIDTH;
  const sourceLines = code.split("\n");
  const freeHeight = COLUMN_BOTTOM - PANEL_TOP;
  const codeFont = chooseFontSize(code, codeWidth, freeHeight);
  const defaultCues = defaultHlCues(sourceLines, durationInFrames - typingEnd).map((cue) => ({
    ...cue,
    frame: cue.frame + typingEnd,
  }));
  const activeCues = cues?.length ? cues : defaultCues;
  const highlightLine = hlLineAt(activeCues, frame);
  const trackedValues = trackValuesAt(activeCues, frame);
  // The explanation of the latest highlighted line that has one: the card holds that text
  // through lines without a label, and does not exist at all before the first label.
  const labelText = [...activeCues]
    .filter((cue) => cue.type === "hl" && cue.frame <= frame)
    .reverse()
    .map((cue) => (cue.type === "hl" ? labels?.[cue.line] : undefined))
    .find((text): text is string => !!text);

  const outputStart = Math.round(durationInFrames * 0.78);
  // Long outputs (EP20: 11 lines, EP25: 14) take the whole right column once they print, so the
  // text stays readable; the explanation card and tracker give way for the last 22% of the scene.
  const outputTakesColumn = !!outputLayout?.fullColumn && frame >= outputStart;
  const outputChars = outputLayout
    ? typewriterChars(outputLayout.text, frame, outputStart + 6, 1)
    : 0;
  const mascot: MascotConfig = output
    ? {
        size: MASCOT_SIZE_WITH_OUTPUT,
        bottom: 60,
        poses: [{ frame: outputStart, pose: "clawsUp" }],
        bubbles: outputLayout?.fullColumn ? [] : [{ at: outputStart + 10, text: "It runs!" }],
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
            flex: `0 0 ${codeWidth}px`,
            maxWidth: codeWidth,
            display: "flex",
            flexDirection: "column",
            gap: 20,
          }}
        >
          <Chip text={file} background={colours.accent} color={readableOn(colours.accent)} />
          {source ? (
            <CodeBlock
              source={source}
              width={codeWidth}
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
                {sanitizeText(onScreen ?? "")}
              </div>
            </Panel>
          )}
        </div>

        <div
          style={{
            flex: 1,
            minWidth: 0,
            display: "flex",
            flexDirection: "column",
            gap: 24,
            paddingBottom: output
              ? 1080 - 96 - (outputLayout?.fullColumn ? TAKEOVER_BOTTOM : RIGHT_COLUMN_BOTTOM)
              : 0,
          }}
        >
          {labelText && !outputTakesColumn ? (
            <Panel background={palette.cream} style={{ minHeight: 160 }}>
              <div
                style={{
                  fontFamily: fonts.body,
                  fontSize: 44,
                  color: palette.ink,
                  lineHeight: 1.35,
                }}
              >
                {sanitizeText(labelText)}
              </div>
            </Panel>
          ) : null}

          {Object.keys(trackedValues).length > 0 && !outputTakesColumn ? (
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
          {outputLayout ? (
            <div
              style={{
                opacity: frame >= outputStart ? 1 : 0,
                background: palette.darkBlue,
                border: `5px solid ${palette.ink}`,
                boxShadow: `8px 8px 0 0 ${palette.ink}`,
                padding: "20px 32px",
                ...(outputTakesColumn ? { flex: 1, minHeight: 0, overflow: "hidden" } : {}),
                fontFamily: fonts.code,
                fontSize: outputLayout.size,
                color: palette.mint,
                whiteSpace: "pre-wrap",
              }}
            >
              <span style={{ color: palette.white }}>{"$ ./program"}</span>
              {"\n"}
              {outputLayout.text.slice(0, outputChars)}
            </div>
          ) : null}
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
