import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn } from "../theme/contrast";
import { typewriterChars } from "../lib/motion";
import { defaultRevealCues, revealFrame } from "../lib/cues";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type TerminalLineKind = "input" | "output" | "success" | "error";
export type TerminalLine = { text: string; kind?: TerminalLineKind };

export type TerminalProps = BaseSceneProps & {
  lines: TerminalLine[];
};

/** Vertical space kept clear at the bottom for the mascot and his bubble. */
const MASCOT_ZONE = 410;

/** Free height inside the window (frame minus 96 top, mascot zone, header 55, padding 64). */
const WINDOW_TEXT_HEIGHT = 1080 - 96 - 410 - 55 - 64;
const WINDOW_TEXT_WIDTH = 1500 - 80 - 10;

const pickTerminalFont = (texts: string[]): number => {
  const sizes = [40, 36, 34, 30, 28, 26, 24, 22];
  const fits = (size: number): boolean => {
    const perRow = Math.floor(WINDOW_TEXT_WIDTH / (size * 0.6));
    const rows = texts.reduce(
      (n, t) => n + Math.max(1, Math.ceil((t.length + 2) / Math.max(1, perRow))),
      0,
    );
    return rows * (size * 1.3 + 14) <= WINDOW_TEXT_HEIGHT;
  };
  return sizes.find(fits) ?? 22;
};

const colourFor = (kind: TerminalLineKind | undefined): string => {
  if (kind === "success") return palette.mint;
  if (kind === "error") return palette.tomato;
  return palette.white;
};

/** Dark terminal window: commands type in, output prints line by line. Mint for success, tomato for errors. */
export const Terminal: React.FC<TerminalProps> = ({ lines, colours, durationInFrames, cues }) => {
  const frame = useCurrentFrame();
  const revealCues = cues?.length ? cues : defaultRevealCues(lines.length, durationInFrames * 0.8);
  const finalFrame = revealFrame(
    revealCues,
    lines.length - 1,
    lines.length,
    durationInFrames * 0.8,
  );
  const hasError = lines.some((line) => line.kind === "error");
  // The window must fit the zone above Xecxec: pick the largest size at which every row
  // (long lines wrap) fits both the width and the height of that zone, never below 22px.
  const fontSize = pickTerminalFont(lines.map((l) => l.text));

  return (
    <SceneFrame
      colours={colours}
      mascot={{
        size: 260,
        poses: [{ frame: finalFrame, pose: hasError ? "shellShake" : "clawsUp" }],
        bubbles: [{ at: finalFrame, text: hasError ? "Oops!" : "Nice!" }],
      }}
    >
      <AbsoluteFill
        style={{
          // Reserve Xecxec's zone (bottom-right: 260px mascot + his speech bubble above him,
          // ~y 680 down) so the window never sits behind him (EP14).
          padding: `96px 96px ${MASCOT_ZONE}px`,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <div
          style={{
            width: "100%",
            maxWidth: 1500,
            background: palette.darkBlue,
            border: `${brutal.borderThick}px solid ${palette.ink}`,
            boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
          }}
        >
          <div
            style={{
              display: "flex",
              gap: 12,
              padding: "16px 24px",
              borderBottom: `3px solid ${palette.ink}`,
            }}
          >
            <div
              style={{ width: 18, height: 18, borderRadius: "50%", background: palette.tomato }}
            />
            <div
              style={{ width: 18, height: 18, borderRadius: "50%", background: palette.butter }}
            />
            <div style={{ width: 18, height: 18, borderRadius: "50%", background: palette.mint }} />
          </div>
          <div style={{ padding: "32px 40px", display: "flex", flexDirection: "column", gap: 14 }}>
            {lines.map((line, index) => {
              const start = revealFrame(revealCues, index, lines.length, durationInFrames * 0.8);
              const visibleChars = typewriterChars(line.text, frame, start, 1.2);
              const shown = line.text.slice(0, visibleChars);
              const isInput = line.kind === "input";
              return (
                <div
                  key={index}
                  style={{
                    fontFamily: fonts.code,
                    fontSize,
                    lineHeight: 1.3,
                    color: colourFor(line.kind),
                    whiteSpace: "pre-wrap",
                    wordBreak: "break-word",
                  }}
                >
                  {isInput ? (
                    <span style={{ color: accentOn(palette.darkBlue, colours.accent) }}>
                      {"$ "}
                    </span>
                  ) : null}
                  {shown}
                </div>
              );
            })}
          </div>
        </div>
      </AbsoluteFill>
    </SceneFrame>
  );
};
