import { AbsoluteFill, useCurrentFrame, useVideoConfig } from "remotion";
import { palette } from "../theme/palette";

export type BackdropProps = {
  background: string;
  accent: string;
  /** Overrides useCurrentFrame(), for stills and tests. */
  frame?: number;
};

type Shape = {
  x: number;
  y: number;
  size: number;
  kind: "circle" | "square" | "ring" | "plus";
  tone: "accent" | "white" | "butter";
  phase: number;
};

/** Fixed layout, hugging the edges so it never sits behind the main content. */
const SHAPES: Shape[] = [
  { x: 3, y: 8, size: 70, kind: "circle", tone: "accent", phase: 0 },
  { x: 90, y: 6, size: 54, kind: "plus", tone: "white", phase: 1.2 },
  { x: 94, y: 40, size: 40, kind: "ring", tone: "accent", phase: 2.1 },
  { x: 2, y: 46, size: 46, kind: "square", tone: "butter", phase: 0.7 },
  { x: 5, y: 82, size: 60, kind: "ring", tone: "white", phase: 3.3 },
  { x: 48, y: 3, size: 36, kind: "square", tone: "accent", phase: 2.6 },
  { x: 62, y: 90, size: 44, kind: "plus", tone: "accent", phase: 4.1 },
  { x: 36, y: 93, size: 32, kind: "circle", tone: "butter", phase: 1.8 },
];

const GRID = 56;

/**
 * Ambient background shared by every scene: a slowly drifting dot grid and flat pastel
 * shapes that bob and spin at the edges. Flat fills only (no gradients, no blur).
 */
export const Backdrop: React.FC<BackdropProps> = ({ background, accent, frame: frameProp }) => {
  const currentFrame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const frame = frameProp ?? currentFrame;
  const t = frame / fps;
  const drift = (frame * 0.5) % GRID;
  const tones = { accent, white: palette.white, butter: palette.butter };

  return (
    <AbsoluteFill style={{ background, overflow: "hidden", pointerEvents: "none" }}>
      <svg width={width} height={height} style={{ position: "absolute", inset: 0 }}>
        <defs>
          <pattern
            id="kk-dots"
            width={GRID}
            height={GRID}
            patternUnits="userSpaceOnUse"
            patternTransform={`translate(${drift} ${drift})`}
          >
            <circle cx={GRID / 2} cy={GRID / 2} r={3} fill={palette.ink} opacity={0.12} />
          </pattern>
        </defs>
        <rect width={width} height={height} fill="url(#kk-dots)" />
        {SHAPES.map((shape, i) => {
          const cx = (shape.x / 100) * width;
          const cy = (shape.y / 100) * height + Math.sin(t * 1.4 + shape.phase) * 14;
          const spin = (t * 24 + shape.phase * 40) % 360;
          const s = shape.size;
          const fill = tones[shape.tone];
          const common = { opacity: 0.55, stroke: palette.ink, strokeWidth: 4 } as const;
          return (
            <g key={i} transform={`translate(${cx} ${cy}) rotate(${spin})`}>
              {shape.kind === "circle" ? <circle r={s / 2} fill={fill} {...common} /> : null}
              {shape.kind === "square" ? (
                <rect x={-s / 2} y={-s / 2} width={s} height={s} fill={fill} {...common} />
              ) : null}
              {shape.kind === "ring" ? (
                <circle r={s / 2} fill="none" {...common} stroke={fill} strokeWidth={10} />
              ) : null}
              {shape.kind === "plus" ? (
                <path
                  d={`M${-s / 6} ${-s / 2}h${s / 3}v${s / 3}h${s / 3}v${s / 3}h${-s / 3}v${s / 3}h${-s / 3}v${-s / 3}h${-s / 3}v${-s / 3}h${s / 3}z`}
                  fill={fill}
                  {...common}
                />
              ) : null}
            </g>
          );
        })}
      </svg>
    </AbsoluteFill>
  );
};
