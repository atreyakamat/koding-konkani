import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn, readableOn } from "../theme/contrast";
import { Panel, Chip, CodeBlock } from "../ui";
import type { MascotConfig } from "../mascot/MascotCompanion";
import { typewriterChars } from "../lib/motion";
import { defaultHlCues, hlLineAt, trackValuesAt } from "../lib/cues";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type CodeExplainProps = BaseSceneProps & {
  file: string;
  source: string;
  /** Short explanation shown for a given highlighted line, e.g. {4: "function · text · end of statement"}. */
  labels?: Record<number, string>;
  /** Program output. Prints in a terminal under the code near the end of the scene. */
  output?: string;
};

/** Code explain: code types itself, then the active line gets a butter highlight with a live variable tracker. */
export const CodeExplain: React.FC<CodeExplainProps> = ({
  file,
  source,
  labels,
  output,
  colours,
  durationInFrames,
  cues,
}) => {
  const frame = useCurrentFrame();

  const typingEnd = Math.round(durationInFrames * 0.35);
  const charsPerFrame = Math.max(0.5, source.length / typingEnd);
  const visibleChars = typewriterChars(source, frame, 0, charsPerFrame);

  const sourceLines = source.split("\n");
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
        <div style={{ flex: 1.5, display: "flex", flexDirection: "column", gap: 20 }}>
          <Chip text={file} background={colours.accent} color={readableOn(colours.accent)} />
          <CodeBlock
            source={source}
            highlightLine={highlightLine}
            visibleChars={visibleChars}
            maxVisibleLines={Math.min(sourceLines.length, 13)}
          />
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

        <div style={{ flex: 1, display: "flex", flexDirection: "column", gap: 24 }}>
          <Panel background={palette.cream} style={{ minHeight: 160 }}>
            <div
              style={{ fontFamily: fonts.body, fontSize: 36, color: palette.ink, lineHeight: 1.4 }}
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
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
