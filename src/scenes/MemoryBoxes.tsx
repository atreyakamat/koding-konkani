import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { enterProgress } from "../lib/motion";
import { defaultRevealCues, revealFrame } from "../lib/cues";
import type { MemoryData } from "../lib/memory";
import { MemoryFrames } from "./MemoryFrames";
import { SceneFrame } from "./SceneFrame";
import type { BaseSceneProps } from "./types";

export type MemoryBox = {
  name: string;
  value: string;
  address: string;
  isPointer?: boolean;
  pointsTo?: string;
};

/** A scene has `memory` (frames of groups of cells: arrays, strings, grids, steps; see lib/memory.ts) or the older
 * flat `boxes` (variables with addresses and pointer arrows). */
export type MemoryBoxesProps = BaseSceneProps & {
  boxes?: MemoryBox[];
  memory?: MemoryData;
};

const CONTENT_WIDTH = 1920 - 2 * 96;
const GAP = 56;
const MIN_BOX_WIDTH = 260;
const MAX_BOX_WIDTH = 520;
/** Vertical centre of the band free of the top-right mascot and the lower-third captions. */
const BAND_CENTER_Y = 560;
const ARROW_DIP = 70;
/** All boxes are on screen within this many frames of the scene start (1 s at 30 fps). */
const REVEAL_WINDOW = 24;

/** Variables as labelled boxes with addresses; pointers as thick arrows that draw on.
 * Box size adapts to the count: 2-3 boxes get ~2x the original 240px, 5 boxes stay at
 * the 260px floor so the row still fits. The row (plus any arrow dip) is centred in
 * the free band, and every box has appeared within the first second. */
const FlatBoxes: React.FC<BaseSceneProps & { boxes: MemoryBox[] }> = ({ boxes, colours }) => {
  const frame = useCurrentFrame();
  const count = Math.max(1, boxes.length);
  const boxWidth = Math.round(
    Math.min(MAX_BOX_WIDTH, Math.max(MIN_BOX_WIDTH, (CONTENT_WIDTH - (count - 1) * GAP) / count)),
  );
  const boxHeight = Math.round(boxWidth * 0.8);
  const hasArrows = boxes.some((box) => box.isPointer && box.pointsTo);
  const rowY = Math.round(BAND_CENTER_Y - boxHeight / 2 - (hasArrows ? ARROW_DIP / 2 : 0));

  const nameSize = Math.round(boxWidth * 0.11);
  const addressSize = Math.max(28, Math.round(boxWidth * 0.075));
  const valueSize = (value: string) => {
    const base = boxWidth * 0.18;
    const factor = value.length > 7 ? 0.55 : value.length > 5 ? 0.75 : 1;
    return Math.round(base * factor);
  };

  const revealCues = defaultRevealCues(count, REVEAL_WINDOW);
  const totalWidth = count * boxWidth + (count - 1) * GAP;
  const startX = Math.max(96, (1920 - totalWidth) / 2);
  const centerX = (index: number) => startX + index * (boxWidth + GAP) + boxWidth / 2;
  const indexOf = (name: string) => boxes.findIndex((box) => box.name === name);
  const boxInk = (box: { isPointer?: boolean }) =>
    readableOn(box.isPointer ? colours.accent : palette.cream);

  return (
    <SceneFrame colours={colours} mascot={{ top: 24, size: 190 }}>
      <AbsoluteFill>
        <svg viewBox="0 0 1920 1080" width="100%" height="100%">
          <defs>
            <marker
              id="memory-arrow"
              markerWidth="12"
              markerHeight="12"
              refX="9"
              refY="5"
              orient="auto"
            >
              <path d="M0,0 L10,5 L0,10 Z" fill={readableOn(colours.bg)} />
            </marker>
          </defs>

          {boxes.map((box, index) => {
            if (!box.isPointer || !box.pointsTo) {
              return null;
            }
            const targetIndex = indexOf(box.pointsTo);
            if (targetIndex === -1) {
              return null;
            }
            const fromX = centerX(index);
            const toX = centerX(targetIndex);
            const bottomY = rowY + boxHeight;
            const pathLength = Math.abs(toX - fromX) + 160;
            const start =
              Math.max(
                revealFrame(revealCues, index, count, REVEAL_WINDOW),
                revealFrame(revealCues, targetIndex, count, REVEAL_WINDOW),
              ) + 6;
            const draw = enterProgress(frame, start, 14);
            return (
              <path
                key={`arrow-${index}`}
                d={`M ${fromX} ${bottomY} Q ${(fromX + toX) / 2} ${bottomY + ARROW_DIP} ${toX} ${bottomY}`}
                fill="none"
                stroke={readableOn(colours.bg)}
                strokeWidth={10}
                strokeLinecap="round"
                markerEnd="url(#memory-arrow)"
                strokeDasharray={pathLength}
                strokeDashoffset={pathLength * (1 - draw)}
              />
            );
          })}

          {boxes.map((box, index) => {
            const start = revealFrame(revealCues, index, count, REVEAL_WINDOW);
            const progress = enterProgress(frame, start, 10);
            const x = startX + index * (boxWidth + GAP);
            const scale = 0.8 + progress * 0.2;
            const cx = x + boxWidth / 2;
            const cy = rowY + boxHeight / 2;
            return (
              <g
                key={box.name}
                opacity={progress}
                transform={`translate(${cx} ${cy}) scale(${scale}) translate(${-cx} ${-cy})`}
              >
                <rect
                  x={x + brutal.shadow}
                  y={rowY + brutal.shadow}
                  width={boxWidth}
                  height={boxHeight}
                  fill={palette.ink}
                />
                <rect
                  x={x}
                  y={rowY}
                  width={boxWidth}
                  height={boxHeight}
                  fill={box.isPointer ? colours.accent : palette.cream}
                  stroke={palette.ink}
                  strokeWidth={brutal.borderThick}
                />
                <text
                  x={cx}
                  y={rowY + boxHeight * 0.24}
                  textAnchor="middle"
                  fontFamily={fonts.title}
                  fontSize={nameSize}
                  fill={boxInk(box)}
                >
                  {box.name}
                </text>
                <text
                  x={cx}
                  y={rowY + boxHeight * 0.6}
                  textAnchor="middle"
                  fontFamily={fonts.code}
                  fontSize={valueSize(box.value)}
                  fontWeight={700}
                  fill={boxInk(box)}
                >
                  {box.value}
                </text>
                <text
                  x={cx}
                  y={rowY + boxHeight * 0.86}
                  textAnchor="middle"
                  fontFamily={fonts.code}
                  fontSize={addressSize}
                  fill={boxInk(box)}
                  fillOpacity={0.75}
                >
                  {box.address}
                </text>
              </g>
            );
          })}
        </svg>
      </AbsoluteFill>
    </SceneFrame>
  );
};

export const MemoryBoxes: React.FC<MemoryBoxesProps> = ({ boxes, memory, ...rest }) =>
  memory ? <MemoryFrames memory={memory} {...rest} /> : <FlatBoxes boxes={boxes ?? []} {...rest} />;
