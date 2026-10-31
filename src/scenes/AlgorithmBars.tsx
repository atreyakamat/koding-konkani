import { AbsoluteFill, useCurrentFrame, interpolate } from "remotion";
import { palette, brutal } from "../theme/palette";
import { algorithmBarColours } from "../theme/modules";
import { fonts } from "../theme/fonts";
import { Chip } from "../ui";
import { springs } from "../lib/motion";
import type { BaseSceneProps } from "./types";

export type TraceStep = {
  step: number | string;
  array: number[];
  compare?: [number, number];
  swap?: [number, number];
  sorted?: number[];
};

export type AlgorithmBarsProps = BaseSceneProps & {
  trace: TraceStep[];
};

const BAR_AREA_TOP = 220;
const BASELINE_Y = 860;
const MAX_BAR_HEIGHT = BASELINE_Y - BAR_AREA_TOP;

/** Bars driven by a step-trace table: compare in butter, swap in tomato, sorted in mint. */
export const AlgorithmBars: React.FC<AlgorithmBarsProps> = ({
  trace,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const framesPerStep = durationInFrames / trace.length;
  const stepIndex = Math.min(trace.length - 1, Math.floor(frame / framesPerStep));
  const step = trace[stepIndex];
  const previous = stepIndex > 0 ? trace[stepIndex - 1].array : trace[0].array;

  const n = step.array.length;
  const maxValue = Math.max(...trace.flatMap((s) => s.array));
  const available = 1920 - 192;
  const gap = 24;
  const barWidth = (available - gap * (n - 1)) / n;

  const localFrame = frame - stepIndex * framesPerStep;
  const transitionFrames = Math.min(framesPerStep * 0.6, 14);

  const comparesSoFar = trace.slice(0, stepIndex + 1).filter((s) => s.compare).length;
  const swapsSoFar = trace.slice(0, stepIndex + 1).filter((s) => s.swap).length;
  const passLabel = typeof step.step === "string" ? step.step.split(".")[0] : String(step.step);

  return (
    <AbsoluteFill style={{ background: colours.bg, padding: 96 }}>
      <div style={{ display: "flex", gap: 20, marginBottom: 32 }}>
        <Chip text={`Pass ${passLabel}`} background={colours.accent} color={palette.white} />
        <Chip text={`Compares: ${comparesSoFar}`} background={palette.white} />
        <Chip text={`Swaps: ${swapsSoFar}`} background={palette.white} />
      </div>

      <svg
        viewBox="0 0 1920 1080"
        width="100%"
        height="100%"
        style={{ position: "absolute", inset: 0 }}
      >
        {step.array.map((value, index) => {
          const previousValue = previous[index] ?? value;
          const height =
            interpolate(localFrame, [0, transitionFrames], [previousValue, value], {
              easing: springs.pop,
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            }) *
            (MAX_BAR_HEIGHT / maxValue);

          const isSorted = step.sorted?.includes(index);
          const isSwap = step.swap?.includes(index);
          const isCompare = step.compare?.includes(index);
          const fill = isSorted
            ? algorithmBarColours.sorted
            : isSwap
              ? algorithmBarColours.swap
              : isCompare
                ? algorithmBarColours.compare
                : algorithmBarColours.idle;

          const x = 96 + index * (barWidth + gap);
          const y = BASELINE_Y - height;

          return (
            <g key={index}>
              <rect
                x={x}
                y={y}
                width={barWidth}
                height={height}
                fill={fill}
                stroke={palette.ink}
                strokeWidth={brutal.border}
              />
              <text
                x={x + barWidth / 2}
                y={y - 18}
                textAnchor="middle"
                fontFamily={fonts.code}
                fontSize={32}
                fontWeight={700}
                fill={palette.ink}
              >
                {value}
              </text>
            </g>
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};
