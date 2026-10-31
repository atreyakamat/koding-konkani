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
          padding: 96,
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
                    fontSize: 34,
                    color: colourFor(line.kind),
                    whiteSpace: "pre",
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
