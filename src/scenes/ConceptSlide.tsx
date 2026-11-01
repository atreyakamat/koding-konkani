import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { accentOn, readableOn } from "../theme/contrast";
import { Panel } from "../ui";
import { enterProgress } from "../lib/motion";
import { textTransformFor } from "../lib/textCase";
import { defaultRevealCues, revealFrame } from "../lib/cues";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type ConceptSlideProps = BaseSceneProps & {
  heading?: string;
  lines: string[];
  analogy?: { title: string; body: string };
};

/** Concept slide: 1-3 numbered lines spring in one by one; an analogy card slides in on the right. */
export const ConceptSlide: React.FC<ConceptSlideProps> = ({
  heading,
  lines,
  analogy,
  colours,
  durationInFrames,
  cues,
}) => {
  const frame = useCurrentFrame();
  const revealCues = cues?.length ? cues : defaultRevealCues(lines.length, durationInFrames * 0.6);
  const lastReveal = revealFrame(
    revealCues,
    lines.length - 1,
    lines.length,
    durationInFrames * 0.6,
  );
  // Analogy card shows from the start (item 3, 31 Oct v2 review) — it illustrates the
  // whole point, not just a payoff after the bullets finish. Xecxec's claws-up beat
  // still lands on the last bullet reveal, independent of the card's own timing.
  const analogyStart = 14;

  return (
    <SceneFrame
      colours={colours}
      mascot={{
        poses: [
          { frame: lastReveal + 8, pose: "clawsUp" },
          { frame: lastReveal + 44, pose: "idle" },
        ],
      }}
    >
      {/* Xecxec only uses the bottom-right corner (right: 72, ~300px square), so only the
          analogy column reserves space for him; the bullets column uses the full height
          instead of leaving the lower third of the frame empty. */}
      <AbsoluteFill
        style={{
          padding: "96px 96px 140px",
          display: "flex",
          flexDirection: "row",
          gap: 56,
          alignItems: "center",
        }}
      >
        <div
          style={{
            flex: analogy ? 1.3 : 1,
            display: "flex",
            flexDirection: "column",
            justifyContent: "center",
            gap: analogy ? 44 : 56,
          }}
        >
          {heading ? (
            <div
              style={{
                fontFamily: fonts.title,
                fontSize: 56,
                color: accentOn(colours.bg, colours.accent),
                textTransform: textTransformFor(heading),
              }}
            >
              {heading}
            </div>
          ) : null}
          {lines.map((line, index) => {
            const start = revealFrame(revealCues, index, lines.length, durationInFrames * 0.6);
            const progress = enterProgress(frame, start, 10);
            return (
              <div
                key={index}
                style={{
                  display: "flex",
                  alignItems: "flex-start",
                  gap: 24,
                  opacity: progress,
                  translate: `${(1 - progress) * -48}px 0`,
                }}
              >
                <div
                  style={{
                    flexShrink: 0,
                    width: 56,
                    height: 56,
                    borderRadius: "50%",
                    background: colours.accent,
                    border: `${brutal.border}px solid ${palette.ink}`,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontFamily: fonts.title,
                    fontSize: 32,
                    color: readableOn(colours.accent),
                  }}
                >
                  {index + 1}
                </div>
                <div
                  style={{
                    fontFamily: fonts.body,
                    fontWeight: 700,
                    fontSize: analogy ? 64 : 72,
                    color: readableOn(colours.bg),
                    lineHeight: 1.25,
                  }}
                >
                  {line}
                </div>
              </div>
            );
          })}
          {!analogy ? (
            <div style={{ display: "flex", gap: 28, marginTop: 24 }}>
              {["{ }", "#", "01"].map((glyph, i) => {
                const start = lastReveal + 10 + i * 8;
                const progress = enterProgress(frame, start, 10);
                return (
                  <div
                    key={glyph}
                    style={{
                      width: 120,
                      height: 120,
                      borderRadius: "50%",
                      background: colours.accent,
                      border: `${brutal.border}px solid ${palette.ink}`,
                      boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
                      display: "flex",
                      alignItems: "center",
                      justifyContent: "center",
                      fontFamily: fonts.code,
                      fontWeight: 700,
                      fontSize: 40,
                      color: readableOn(colours.accent),
                      scale: `${progress} ${progress}`,
                    }}
                  >
                    {glyph}
                  </div>
                );
              })}
            </div>
          ) : null}
        </div>

        {analogy
          ? (() => {
              const progress = enterProgress(frame, analogyStart, 12);
              return (
                <div
                  style={{
                    flex: 1,
                    alignSelf: "stretch",
                    display: "flex",
                    alignItems: "center",
                    paddingBottom: 260,
                    opacity: progress,
                    translate: `${(1 - progress) * 60}px 0`,
                  }}
                >
                  <Panel background={palette.cream} padding={40} style={{ width: "100%" }}>
                    <div
                      style={{
                        fontFamily: fonts.title,
                        fontSize: 36,
                        color: accentOn(palette.cream, colours.accent),
                        marginBottom: 20,
                        textTransform: textTransformFor(analogy.title),
                      }}
                    >
                      {analogy.title}
                    </div>
                    <div
                      style={{
                        fontFamily: fonts.body,
                        fontSize: 40,
                        color: palette.ink,
                        lineHeight: 1.4,
                      }}
                    >
                      {analogy.body}
                    </div>
                  </Panel>
                </div>
              );
            })()
          : null}
      </AbsoluteFill>
    </SceneFrame>
  );
};
