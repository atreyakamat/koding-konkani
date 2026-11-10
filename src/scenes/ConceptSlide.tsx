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

/** Free height beside the analogy card; without a card the stack also stays above Xecxec's corner. */
const FREE_HEIGHT_WITH_ANALOGY = 1080 - 96 - 140;
const FREE_HEIGHT_NO_ANALOGY = 1080 - 96 - 340;
const LINE_GAP = 44;

/** Largest body size in [64, maxSize] at which the wrapped lines fit `width` and the free height. */
const fitBodySize = (
  lines: string[],
  width: number,
  maxSize: number,
  freeHeight: number,
): number => {
  const fits = (size: number): boolean => {
    const badge = Math.round(size * 0.9);
    const perRow = Math.max(4, Math.floor((width - badge - 24) / (size * 0.52)));
    const rows = lines.reduce((n, l) => n + Math.max(1, Math.ceil(l.length / perRow)), 0);
    return rows * size * 1.25 + Math.max(0, lines.length - 1) * LINE_GAP <= freeHeight;
  };
  for (let size = maxSize; size > 64; size -= 4) if (fits(size)) return size;
  return 64;
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
  // Fill the frame: pick the largest type at which every numbered line fits its column (wrapped)
  // and the whole stack fits the free height. With no analogy card the lines own the full width
  // (a lone short line gets huge type); with one they share it, at 64-80px.
  const columnWidth = analogy ? 945 : 1728;
  const bodySize = fitBodySize(
    lines,
    columnWidth,
    analogy ? 80 : 140,
    analogy ? FREE_HEIGHT_WITH_ANALOGY : FREE_HEIGHT_NO_ANALOGY,
  );
  const badge = analogy ? 56 : Math.round(bodySize * 0.9);

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
          padding: analogy ? "96px 96px 140px" : "96px 96px 340px",
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
                    width: badge,
                    height: badge,
                    borderRadius: "50%",
                    background: colours.accent,
                    border: `${brutal.border}px solid ${palette.ink}`,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                    fontFamily: fonts.title,
                    fontSize: Math.round(badge * 0.57),
                    color: readableOn(colours.accent),
                  }}
                >
                  {index + 1}
                </div>
                <div
                  style={{
                    fontFamily: fonts.body,
                    fontWeight: 700,
                    fontSize: bodySize,
                    color: readableOn(colours.bg),
                    lineHeight: 1.25,
                  }}
                >
                  {line}
                </div>
              </div>
            );
          })}
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
                  <Panel background={palette.cream} padding={44} style={{ width: "100%" }}>
                    <div
                      style={{
                        fontFamily: fonts.title,
                        fontSize: 48,
                        color: accentOn(palette.cream, colours.accent),
                        marginBottom: 24,
                        textTransform: textTransformFor(analogy.title),
                      }}
                    >
                      {analogy.title}
                    </div>
                    <div
                      style={{
                        fontFamily: fonts.body,
                        fontSize: analogy.body.length > 70 ? 56 : 64,
                        fontWeight: 700,
                        color: palette.ink,
                        lineHeight: 1.3,
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
