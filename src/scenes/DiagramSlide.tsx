import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { Panel } from "../ui";
import { enterProgress } from "../lib/motion";
import { layoutGraph } from "../lib/diagramLayout";
import type { Diagram } from "../lib/episode";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type DiagramSlideProps = BaseSceneProps & { diagram: Diagram };

/** The diagram area: the whole frame minus the padding, with the bottom third kept clear for Xecxec. */
const AREA_W = 1728;
const AREA_H = 700;

/** Reveal frame of item `i` of `n`: items spring in one by one over the first 65% of the scene. */
const revealAt = (i: number, n: number, duration: number): number =>
  10 + Math.round((i * Math.max(0, duration * 0.65 - 10)) / Math.max(1, n));

const Arrow: React.FC<{ size: number }> = ({ size }) => (
  <svg width={size} height={size} viewBox="0 0 40 40" style={{ flexShrink: 0 }}>
    <path
      d="M4 20 H28 M18 8 L32 20 L18 32"
      fill="none"
      stroke={palette.ink}
      strokeWidth={6}
      strokeLinecap="round"
      strokeLinejoin="round"
    />
  </svg>
);

const FlowView: React.FC<{ d: Extract<Diagram, { kind: "flow" }> } & BaseSceneProps> = ({
  d,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const n = d.steps.length;
  const cardW = Math.floor((AREA_W - (n - 1) * 90) / n);
  const labelSize = n >= 5 ? 38 : 48;
  const detailSize = n >= 5 ? 28 : 34;
  return (
    <div
      style={{
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        gap: 18,
        width: AREA_W,
        height: AREA_H,
      }}
    >
      {d.steps.map((s, i) => {
        const p = enterProgress(frame, revealAt(i, n, durationInFrames), 10);
        return (
          <div
            key={s.id}
            style={{
              display: "flex",
              alignItems: "center",
              gap: 18,
              opacity: p,
              translate: `0 ${(1 - p) * 40}px`,
            }}
          >
            <Panel background={palette.cream} padding={24} style={{ width: cardW, minHeight: 300 }}>
              <div
                style={{
                  width: 64,
                  height: 64,
                  borderRadius: "50%",
                  background: colours.accent,
                  border: `${brutal.border}px solid ${palette.ink}`,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                  fontFamily: fonts.title,
                  fontSize: 34,
                  color: readableOn(colours.accent),
                  marginBottom: 18,
                }}
              >
                {i + 1}
              </div>
              <div
                style={{
                  fontFamily: fonts.title,
                  fontSize: labelSize,
                  color: palette.ink,
                  lineHeight: 1.1,
                  textTransform: "uppercase",
                  wordBreak: "break-word",
                }}
              >
                {s.label}
              </div>
              <div
                style={{
                  fontFamily: fonts.body,
                  fontWeight: 700,
                  fontSize: detailSize,
                  color: palette.ink,
                  marginTop: 14,
                  lineHeight: 1.25,
                }}
              >
                {s.detail}
              </div>
            </Panel>
            {i < n - 1 ? <Arrow size={72} /> : null}
          </div>
        );
      })}
    </div>
  );
};

const TableView: React.FC<{ d: Extract<Diagram, { kind: "table" }> } & BaseSceneProps> = ({
  d,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const rows = d.rows.length;
  const size = rows >= 6 ? 34 : rows >= 4 ? 40 : 48;
  const headSize = size;
  const head = enterProgress(frame, 6, 10);
  return (
    <div style={{ width: AREA_W, height: AREA_H, display: "flex", alignItems: "center" }}>
      <Panel background={palette.cream} padding={0} style={{ width: "100%", overflow: "hidden" }}>
        <div
          style={{
            display: "grid",
            gridTemplateColumns: `repeat(${d.headers.length}, 1fr)`,
            opacity: head,
          }}
        >
          {d.headers.map((h) => (
            <div
              key={h}
              style={{
                background: colours.accent,
                color: readableOn(colours.accent),
                fontFamily: fonts.title,
                fontSize: headSize,
                textTransform: "uppercase",
                padding: "18px 24px",
                borderBottom: `${brutal.border}px solid ${palette.ink}`,
              }}
            >
              {h}
            </div>
          ))}
        </div>
        {d.rows.map((row, r) => {
          const p = enterProgress(frame, revealAt(r, rows, durationInFrames), 10);
          return (
            <div
              key={r}
              style={{
                display: "grid",
                gridTemplateColumns: `repeat(${d.headers.length}, 1fr)`,
                opacity: p,
                translate: `${(1 - p) * -50}px 0`,
                background: r % 2 === 0 ? palette.cream : palette.butter,
                borderTop: r === 0 ? undefined : `3px solid ${palette.ink}`,
              }}
            >
              {row.map((cell, c) => (
                <div
                  key={c}
                  style={{
                    fontFamily: c === 0 ? fonts.code : fonts.body,
                    fontWeight: 700,
                    fontSize: size,
                    color: palette.ink,
                    padding: "14px 24px",
                    lineHeight: 1.2,
                    wordBreak: "break-word",
                  }}
                >
                  {cell}
                </div>
              ))}
            </div>
          );
        })}
      </Panel>
    </div>
  );
};

const GraphView: React.FC<{ d: Extract<Diagram, { kind: "graph" }> } & BaseSceneProps> = ({
  d,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const layout = layoutGraph(d, AREA_W, AREA_H);
  const n = layout.nodes.length;
  const nodeStart = (index: number): number => revealAt(index, n, durationInFrames);
  const labelSize = layout.nodes[0] && layout.nodes[0].w < 240 ? 34 : 44;
  return (
    <div style={{ position: "relative", width: AREA_W, height: AREA_H }}>
      <svg width={AREA_W} height={AREA_H} style={{ position: "absolute", inset: 0 }}>
        <defs>
          <marker id="head" markerWidth="8" markerHeight="8" refX="6" refY="4" orient="auto">
            <path d="M0 0 L8 4 L0 8 Z" fill={palette.ink} />
          </marker>
        </defs>
        {layout.edges.map((e, i) => {
          const from = layout.nodes.find((x) => x.id === e.from)!;
          const to = layout.nodes.find((x) => x.id === e.to)!;
          const p = enterProgress(
            frame,
            Math.max(nodeStart(from.index), nodeStart(to.index)) + 8,
            10,
          );
          const mx = e.x1 + (e.x2 - e.x1) * p;
          const my = e.y1 + (e.y2 - e.y1) * p;
          return (
            <line
              key={i}
              x1={e.x1}
              y1={e.y1}
              x2={mx}
              y2={my}
              stroke={palette.ink}
              strokeWidth={6}
              markerEnd={p > 0.95 ? "url(#head)" : undefined}
            />
          );
        })}
      </svg>
      {layout.edges.map((e, i) =>
        e.label ? (
          <div
            key={`l${i}`}
            style={{
              position: "absolute",
              left: (e.x1 + e.x2) / 2,
              top: (e.y1 + e.y2) / 2,
              translate: "-50% -50%",
              background: palette.cream,
              border: `3px solid ${palette.ink}`,
              fontFamily: fonts.code,
              fontWeight: 700,
              fontSize: 28,
              padding: "2px 12px",
              color: palette.ink,
              opacity: enterProgress(
                frame,
                nodeStart(layout.nodes.find((x) => x.id === e.to)!.index) + 12,
                8,
              ),
            }}
          >
            {e.label}
          </div>
        ) : null,
      )}
      {layout.nodes.map((node) => {
        const p = enterProgress(frame, nodeStart(node.index), 10);
        return (
          <div
            key={node.id}
            style={{
              position: "absolute",
              left: node.x,
              top: node.y,
              width: node.w,
              height: node.h,
              opacity: p,
              scale: `${0.7 + 0.3 * p}`,
            }}
          >
            <Panel
              background={node.index === 0 ? colours.accent : palette.cream}
              padding={10}
              style={{
                width: "100%",
                height: "100%",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "center",
                textAlign: "center",
              }}
            >
              <div
                style={{
                  fontFamily: fonts.title,
                  fontSize: labelSize,
                  color: node.index === 0 ? readableOn(colours.accent) : palette.ink,
                  lineHeight: 1.05,
                  wordBreak: "break-word",
                }}
              >
                {node.label}
              </div>
              {node.sub ? (
                <div
                  style={{
                    fontFamily: fonts.body,
                    fontWeight: 700,
                    fontSize: 26,
                    color: node.index === 0 ? readableOn(colours.accent) : palette.ink,
                    marginTop: 6,
                    lineHeight: 1.15,
                  }}
                >
                  {node.sub}
                </div>
              ) : null}
            </Panel>
          </div>
        );
      })}
    </div>
  );
};

const StackView: React.FC<{ d: Extract<Diagram, { kind: "callstack" }> } & BaseSceneProps> = ({
  d,
  colours,
  durationInFrames,
}) => {
  const frame = useCurrentFrame();
  const n = d.steps.length;
  const per = Math.max(1, (durationInFrames * 0.7 - 10) / n);
  const current = Math.min(n - 1, Math.max(0, Math.floor((frame - 10) / per)));
  const step = d.steps[current];
  const stepStart = 10 + current * per;
  const frameH = Math.min(78, Math.floor(AREA_H / 9));
  return (
    <div style={{ display: "flex", gap: 56, width: AREA_W, height: AREA_H, alignItems: "center" }}>
      <div
        style={{
          flex: 1,
          display: "flex",
          flexDirection: "column-reverse",
          gap: 10,
          justifyContent: "flex-start",
          height: AREA_H - 40,
        }}
      >
        {step.frames.map((f, i) => {
          const isTop = i === step.frames.length - 1;
          const p = isTop ? enterProgress(frame, stepStart, 8) : 1;
          return (
            <div
              key={`${current}-${i}`}
              style={{
                height: frameH,
                background: isTop ? colours.accent : palette.cream,
                color: isTop ? readableOn(colours.accent) : palette.ink,
                border: `${brutal.border}px solid ${palette.ink}`,
                boxShadow: `6px 6px 0 0 ${palette.ink}`,
                fontFamily: fonts.code,
                fontWeight: 700,
                fontSize: 40,
                display: "flex",
                alignItems: "center",
                padding: "0 28px",
                opacity: p,
                translate: `0 ${(1 - p) * -60}px`,
              }}
            >
              {f}
            </div>
          );
        })}
      </div>
      <div style={{ flex: 1, alignSelf: "center" }}>
        <Panel background={palette.butter} padding={36}>
          <div
            style={{ fontFamily: fonts.title, fontSize: 44, color: palette.ink, marginBottom: 16 }}
          >
            STEP {current + 1} OF {n}
          </div>
          <div
            style={{
              fontFamily: fonts.body,
              fontWeight: 700,
              fontSize: 48,
              color: palette.ink,
              lineHeight: 1.25,
            }}
          >
            {step.note}
          </div>
        </Panel>
      </div>
    </div>
  );
};

/** Scene 4 of a C++ episode when it is not memory or bars: a flow, graph, table or call stack,
 * drawn from the structured data in the episode JSON (see docs/cpp-bible/ILLUSTRATIONS.md). */
export const DiagramSlide: React.FC<DiagramSlideProps> = ({
  diagram,
  colours,
  durationInFrames,
  cues,
}) => {
  const common = { colours, durationInFrames, cues };
  return (
    <SceneFrame colours={colours} mascot={{}}>
      <AbsoluteFill
        style={{
          padding: "70px 96px 0",
          display: "flex",
          alignItems: "flex-start",
          justifyContent: "center",
        }}
      >
        {diagram.kind === "flow" ? <FlowView d={diagram} {...common} /> : null}
        {diagram.kind === "table" ? <TableView d={diagram} {...common} /> : null}
        {diagram.kind === "graph" ? <GraphView d={diagram} {...common} /> : null}
        {diagram.kind === "callstack" ? <StackView d={diagram} {...common} /> : null}
      </AbsoluteFill>
    </SceneFrame>
  );
};
