import { AbsoluteFill, interpolate, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { enterProgress, impactShakeX } from "../lib/motion";
import { Sfx } from "../audio";
import {
  arrowPoints,
  fitFont,
  rectAt,
  stateAt,
  stepFrame,
  DRAW_FRAMES,
  type IllObject,
  type IllustrationSpec,
  type Rect,
} from "../lib/illustration";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type IllustrationProps = BaseSceneProps & { spec: IllustrationSpec };

/** Frames a flip takes. */
const MOVE_FLIP = 12;

const colourOf = (token: string): string =>
  (palette as Record<string, string>)[token] ?? palette.cream;

/** One drawn explanation (docs/python-bible/ILLUSTRATIONS.md): boxes, cards, labels, tokens and arrows on a 12x6 grid,
 * revealed by timed steps. All positions, colours and timings come from the spec; nothing is guessed. */
export const Illustration: React.FC<IllustrationProps> = ({ spec, colours, durationInFrames }) => {
  const frame = useCurrentFrame();
  const byId = new Map(spec.objects.map((o) => [o.id, o]));
  const nodes = spec.objects.filter((o) => o.shape !== "arrow");
  const arrows = spec.objects.filter((o) => o.shape === "arrow");

  const rectOf = (o: IllObject): Rect => {
    const s = stateAt(spec, o.id, frame, durationInFrames);
    return rectAt(s.col, s.row, o.w ?? 1, o.h ?? 1);
  };

  return (
    <SceneFrame colours={colours} mascot={{ top: 24, size: 150 }}>
      <AbsoluteFill>
        {nodes.map((o) => {
          const s = stateAt(spec, o.id, frame, durationInFrames);
          const hiding = s.hideAt !== null && !s.visible;
          if (!s.visible && !hiding) return null;
          const r = rectOf(o);
          const enter = enterProgress(frame, s.appearAt, 10);
          let opacity = hiding
            ? interpolate(frame, [s.hideAt ?? 0, (s.hideAt ?? 0) + 8], [1, 0], {
                extrapolateLeft: "clamp",
                extrapolateRight: "clamp",
              })
            : enter;
          if (s.dimmed) opacity *= 0.35;
          let scale = 0.85 + 0.15 * (hiding ? 1 : enter);
          if (s.stampAt !== null)
            scale *= interpolate(frame, [s.stampAt, s.stampAt + 8], [1.35, 1], {
              extrapolateLeft: "clamp",
              extrapolateRight: "clamp",
            });
          const shake = s.shakeAt !== null ? impactShakeX(frame, s.shakeAt, 8) : 0;
          const flipX =
            s.flipAt !== null
              ? Math.abs(
                  Math.cos(
                    interpolate(frame, [s.flipAt, s.flipAt + MOVE_FLIP], [0, Math.PI], {
                      extrapolateLeft: "clamp",
                      extrapolateRight: "clamp",
                    }),
                  ),
                )
              : 1;
          const fill = colourOf(o.colour);
          const ink = readableOn(fill);
          const isLabel = o.shape === "label";
          const isToken = o.shape === "token";
          const font = fitFont(o.text, r.w, r.h);
          const glowing = s.glowAt !== null && frame - s.glowAt < 24;
          const glowed = s.glowAt !== null;
          return (
            <div
              key={o.id}
              style={{
                position: "absolute",
                left: r.x,
                top: r.y,
                width: r.w,
                height: r.h,
                opacity,
                transform: `translateX(${shake}px) scale(${scale * 1}) scaleX(${flipX})`,
                background: isLabel ? "transparent" : fill,
                border: isLabel ? "none" : `${brutal.borderThick}px solid ${palette.ink}`,
                borderRadius: isToken ? r.h / 2 : 0,
                boxShadow: isLabel
                  ? "none"
                  : `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
                outline: glowing
                  ? `8px solid ${palette.butter}`
                  : glowed && !isLabel
                    ? `4px solid ${palette.butter}`
                    : "none",
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                textAlign: "center",
                padding: "0 14px",
                fontFamily:
                  o.text.includes("(") || o.text.includes("=") || o.text.includes("[")
                    ? fonts.code
                    : fonts.body,
                fontWeight: 700,
                fontSize: font,
                lineHeight: 1.2,
                color: isLabel ? readableOn(colours.bg) : ink,
                whiteSpace: "pre-wrap",
                overflowWrap: "anywhere",
                boxSizing: "border-box",
              }}
            >
              {o.text}
              {s.tickAt !== null ? (
                <span
                  style={{
                    position: "absolute",
                    right: -18,
                    top: -22,
                    fontSize: 56,
                    color: palette.ink,
                    background: palette.mint,
                    border: `4px solid ${palette.ink}`,
                    borderRadius: 999,
                    width: 56,
                    height: 56,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  ✓
                </span>
              ) : null}
              {s.crossAt !== null ? (
                <span
                  style={{
                    position: "absolute",
                    right: -18,
                    top: -22,
                    fontSize: 52,
                    color: palette.ink,
                    background: palette.tomato,
                    border: `4px solid ${palette.ink}`,
                    borderRadius: 999,
                    width: 56,
                    height: 56,
                    display: "flex",
                    alignItems: "center",
                    justifyContent: "center",
                  }}
                >
                  ✕
                </span>
              ) : null}
            </div>
          );
        })}
        <svg
          viewBox="0 0 1920 1080"
          width="100%"
          height="100%"
          style={{ position: "absolute", inset: 0 }}
        >
          <defs>
            <marker
              id="ill-arrow"
              markerUnits="userSpaceOnUse"
              markerWidth="26"
              markerHeight="26"
              refX="20"
              refY="13"
              orient="auto"
            >
              <path d="M0,0 L24,13 L0,26 Z" fill={palette.ink} />
            </marker>
          </defs>
          {arrows.map((a) => {
            const s = stateAt(spec, a.id, frame, durationInFrames);
            if (!s.visible) return null;
            const from = byId.get(a.from ?? "");
            const to = byId.get(a.to ?? "");
            if (!from || !to) return null;
            const p = arrowPoints(rectOf(from), rectOf(to));
            const progress =
              s.drawAt === null
                ? 1
                : interpolate(frame, [s.drawAt, s.drawAt + DRAW_FRAMES], [0, 1], {
                    extrapolateLeft: "clamp",
                    extrapolateRight: "clamp",
                  });
            const stroke = a.colour === "ink" ? palette.ink : colourOf(a.colour);
            const mid = { x: (p.x1 + p.x2) / 2, y: (p.y1 + p.y2) / 2 };
            const opacity = s.dimmed ? 0.35 : 1;
            return (
              <g key={a.id} opacity={opacity}>
                <line
                  x1={p.x1}
                  y1={p.y1}
                  x2={p.x1 + (p.x2 - p.x1) * progress}
                  y2={p.y1 + (p.y2 - p.y1) * progress}
                  stroke={stroke}
                  strokeWidth={s.glowAt !== null ? 9 : 7}
                  strokeLinecap="round"
                  markerEnd={progress >= 1 ? "url(#ill-arrow)" : undefined}
                />
                {a.text && progress >= 1 ? (
                  <g>
                    <rect
                      x={mid.x - (a.text.length * 9 + 20)}
                      y={mid.y - 22}
                      width={a.text.length * 18 + 40}
                      height={44}
                      fill={palette.cream}
                      stroke={palette.ink}
                      strokeWidth={4}
                    />
                    <text
                      x={mid.x}
                      y={mid.y + 11}
                      textAnchor="middle"
                      fontFamily={fonts.body}
                      fontWeight={700}
                      fontSize={30}
                      fill={palette.ink}
                    >
                      {a.text}
                    </text>
                  </g>
                ) : null}
              </g>
            );
          })}
        </svg>
        {spec.steps
          .filter((s) => s.sfx)
          .map((s, i) => (
            <Sfx key={`${s.target}-${i}`} name={s.sfx!} at={stepFrame(s.t, durationInFrames)} />
          ))}
      </AbsoluteFill>
    </SceneFrame>
  );
};
