import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { Chip } from "../ui";
import { enterProgress } from "../lib/motion";
import { cellOrigin, frameIndexAt, frameStart, layoutFrame, type FrameLayout } from "../lib/memoryLayout";
import type { MemoryData, MemoryFrame, MemoryGroup } from "../lib/memory";
import { MemoryCellView } from "./MemoryCell";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type MemoryFramesProps = BaseSceneProps & { memory: MemoryData };

/** The first frame's cells all appear within this many frames of the scene start (1 s at 30 fps). */
const REVEAL_WINDOW = 24;
/** A group that is new in a frame (other size or shape) appears faster. */
const REGROUP_WINDOW = 12;
const ARROW_DELAY = 20;
const ARROW_STEP = 10;

/** Does cell `i` of `group` differ from the same cell of the previous frame (value, mark or lost value)? */
const cellChanged = (group: MemoryGroup, prev: MemoryGroup | undefined, i: number): boolean => {
  const a = group.cells[i];
  const b = prev?.cells[i];
  return !b || a.value !== b.value || a.mark !== b.mark || a.lost !== b.lost;
};

/** Is group `g` of this frame a different group (cell count or columns) than in the previous frame? */
const regrouped = (frame: MemoryFrame, prev: MemoryFrame | undefined, g: number): boolean => {
  const a = frame.groups[g];
  const b = prev?.groups[g];
  return !b || a.cells.length !== b.cells.length || a.cols !== b.cols;
};

type ArrowViewProps = { from: string; to: string; layout: FrameLayout; start: number; frame: number; ink: string };

const ArrowView: React.FC<ArrowViewProps> = ({ from, to, layout, start, frame, ink }) => {
  const [fg, fc] = from.split(":").map(Number);
  const [tg, tc] = to.split(":").map(Number);
  const a = cellOrigin(layout, fg, fc);
  const b = cellOrigin(layout, tg, tc);
  const h = layout.cellHeight;
  const w = layout.cellWidth;
  const down = b.y > a.y;
  const x1 = a.x + w / 2;
  const y1 = down ? a.y + h + 40 : a.y - 8;
  const x2 = b.x + w / 2;
  const y2 = down ? b.y - 12 : b.y + h + 40;
  const length = Math.hypot(x2 - x1, y2 - y1) + 20;
  const draw = enterProgress(frame, start, 14);
  return (
    <path
      d={`M ${x1} ${y1} Q ${(x1 + x2) / 2 + (x2 > x1 ? -30 : 30)} ${(y1 + y2) / 2} ${x2} ${y2}`}
      fill="none"
      stroke={ink}
      strokeWidth={8}
      strokeLinecap="round"
      markerEnd="url(#memory-cell-arrow)"
      strokeDasharray={length}
      strokeDashoffset={length * (1 - draw)}
    />
  );
};

const GroupHeader: React.FC<{ group: MemoryGroup; x: number; y: number; ink: string; accent: string }> = ({ group, x, y, ink, accent }) => (
  <g>
    {group.name ? (
      <text x={x} y={y + 38} fontFamily={fonts.title} fontSize={36} fill={ink}>
        {group.name}
      </text>
    ) : null}
    {(group.tags ?? []).map((tag, k) => {
      const tx = x + (group.name ? group.name.length * 24 + 40 : 0) + k * 330;
      return (
        <g key={tag}>
          <rect x={tx} y={y + 4} width={300} height={42} rx={8} fill={accent} stroke={palette.ink} strokeWidth={brutal.border} />
          <text x={tx + 150} y={y + 34} textAnchor="middle" fontFamily={fonts.body} fontWeight={700} fontSize={26} fill={readableOn(accent)}>
            {tag}
          </text>
        </g>
      );
    })}
  </g>
);

const Ruler: React.FC<{ group: MemoryGroup; x: number; y: number; cellWidth: number; gap: number; ink: string }> = ({ group, x, y, cellWidth, gap, ink }) => {
  if (!group.ruler) return null;
  const n = group.cells.length;
  const total = n * cellWidth + (n - 1) * gap;
  return (
    <g stroke={ink} strokeWidth={4} fill="none">
      {group.cells.map((c, i) => {
        const cx = x + i * (cellWidth + gap);
        return (
          <g key={`${c.value}-${cx}`}>
            <path d={`M ${cx} ${y} v 12 h ${cellWidth} v -12`} />
            <text x={cx + cellWidth / 2} y={y + 40} textAnchor="middle" fontFamily={fonts.code} fontSize={24} fill={ink} stroke="none">
              {group.ruler?.each}
            </text>
          </g>
        );
      })}
      <path d={`M ${x} ${y + 52} v 12 h ${total} v -12`} />
      <text x={x + total / 2} y={y + 62} textAnchor="middle" fontFamily={fonts.title} fontSize={30} fill={ink} stroke="none" dy={22}>
        {group.ruler.total}
      </text>
    </g>
  );
};

/** The `memory` layout of MemoryBoxes: frames of groups of cells, with joiners, arrows, a byte ruler and name tags.
 * Frames share the scene evenly; the first frame's cells stagger in, later frames only pop the cells that changed. */
export const MemoryFrames: React.FC<MemoryFramesProps> = ({ memory, colours, durationInFrames }) => {
  const frame = useCurrentFrame();
  const count = memory.frames.length;
  const k = frameIndexAt(frame, count, durationInFrames);
  const current = memory.frames[k];
  const prev = k > 0 ? memory.frames[k - 1] : undefined;
  const layout = layoutFrame(current);
  const t0 = frameStart(k, count, durationInFrames);
  const ink = readableOn(colours.bg);
  const total = current.groups.reduce((n, g) => n + g.cells.length, 0);
  let seen = 0;

  return (
    <SceneFrame colours={colours} mascot={{ top: 24, size: 190 }}>
      <AbsoluteFill>
        <div style={{ position: "absolute", left: 96, top: 120, width: 1540, display: "flex", flexDirection: "column", gap: 16 }}>
          {current.label ? (
            <div style={{ fontFamily: fonts.body, fontWeight: 700, fontSize: current.label.length > 60 ? 34 : 42, lineHeight: 1.25, color: ink }}>
              {current.label}
            </div>
          ) : null}
          {current.badges?.length ? (
            <div style={{ display: "flex", gap: 20, flexWrap: "wrap" }}>
              {current.badges.map((text) => (
                <Chip key={text} text={text} background={palette.white} fontSize={30} />
              ))}
            </div>
          ) : null}
        </div>
        <svg viewBox="0 0 1920 1080" width="100%" height="100%" style={{ position: "absolute", inset: 0 }}>
          <defs>
            <marker id="memory-cell-arrow" markerWidth="12" markerHeight="12" refX="9" refY="5" orient="auto">
              <path d="M0,0 L10,5 L0,10 Z" fill={ink} />
            </marker>
          </defs>
          {current.groups.map((group, g) => {
            const placed = layout.groups[g];
            const fresh = k === 0 || regrouped(current, prev, g);
            const window = k === 0 ? REVEAL_WINDOW : REGROUP_WINDOW;
            const base = seen;
            seen += group.cells.length;
            return (
              <g key={`g-${group.name ?? g}`}>
                <GroupHeader group={group} x={placed.x} y={placed.y} ink={ink} accent={colours.accent} />
                {group.cells.map((cell, i) => {
                  const origin = cellOrigin(layout, g, i);
                  const start = fresh
                    ? t0 + Math.floor(((base + i) * window) / Math.max(1, total))
                    : cellChanged(group, prev?.groups[g], i)
                      ? t0
                      : -100;
                  return (
                    <MemoryCellView
                      key={`c-${g}-${i}`}
                      cell={cell}
                      x={origin.x}
                      y={origin.y}
                      width={layout.cellWidth}
                      frame={frame}
                      start={start}
                      labelInk={ink}
                    />
                  );
                })}
                <Ruler
                  group={group}
                  x={placed.x}
                  y={placed.y + placed.headerHeight + placed.rows * layout.cellHeight + (placed.rows - 1) * 26 + 40}
                  cellWidth={layout.cellWidth}
                  gap={placed.gapX}
                  ink={ink}
                />
              </g>
            );
          })}
          {(current.joiners ?? []).map((text, j) => (
            <text
              key={`join-${text}-${j}`}
              x={layout.joinerX[j]}
              y={layout.groups[0].y + layout.groups[0].headerHeight + layout.cellHeight / 2 + 26}
              textAnchor="middle"
              fontFamily={fonts.title}
              fontSize={76}
              fill={ink}
            >
              {text}
            </text>
          ))}
          {(current.arrows ?? []).map((arrow, j) => (
            <ArrowView
              key={`arrow-${arrow.from}-${arrow.to}`}
              from={arrow.from}
              to={arrow.to}
              layout={layout}
              start={t0 + ARROW_DELAY + j * ARROW_STEP}
              frame={frame}
              ink={ink}
            />
          ))}
        </svg>
      </AbsoluteFill>
    </SceneFrame>
  );
};
