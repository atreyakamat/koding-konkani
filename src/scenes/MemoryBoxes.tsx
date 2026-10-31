import { AbsoluteFill, useCurrentFrame } from "remotion";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { enterProgress } from "../lib/motion";
import { defaultRevealCues, revealFrame } from "../lib/cues";
import type { BaseSceneProps } from "./types";

export type MemoryBox = {
  name: string;
  value: string;
  address: string;
  isPointer?: boolean;
  pointsTo?: string;
};

export type MemoryBoxesProps = BaseSceneProps & {
  boxes: MemoryBox[];
};

const BOX_WIDTH = 240;
const BOX_HEIGHT = 190;
const GAP = 48;
const ROW_Y = 460;

/** Variables as labelled boxes with addresses; pointers as thick arrows that draw on. */
export const MemoryBoxes: React.FC<MemoryBoxesProps> = ({
  boxes,
  colours,
  durationInFrames,
  cues,
}) => {
  const frame = useCurrentFrame();
  const revealCues = cues?.length ? cues : defaultRevealCues(boxes.length, durationInFrames * 0.5);

  const totalWidth = boxes.length * BOX_WIDTH + (boxes.length - 1) * GAP;
  const startX = Math.max(96, (1920 - totalWidth) / 2);

  const centerX = (index: number) => startX + index * (BOX_WIDTH + GAP) + BOX_WIDTH / 2;
  const indexOf = (name: string) => boxes.findIndex((box) => box.name === name);
  const boxInk = (box: { isPointer?: boolean }) =>
    readableOn(box.isPointer ? colours.accent : palette.cream);

  return (
    <AbsoluteFill style={{ background: colours.bg }}>
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
          const dipY = ROW_Y + BOX_HEIGHT + 70;
          const pathLength = Math.abs(toX - fromX) + 160;
          const start =
            Math.max(
              revealFrame(revealCues, index, boxes.length, durationInFrames * 0.5),
              revealFrame(revealCues, targetIndex, boxes.length, durationInFrames * 0.5),
            ) + 8;
          const draw = enterProgress(frame, start, 14);
          return (
            <path
              key={`arrow-${index}`}
              d={`M ${fromX} ${ROW_Y + BOX_HEIGHT} Q ${(fromX + toX) / 2} ${dipY} ${toX} ${ROW_Y + BOX_HEIGHT}`}
              fill="none"
              stroke={readableOn(colours.bg)}
              strokeWidth={8}
              strokeLinecap="round"
              markerEnd="url(#memory-arrow)"
              strokeDasharray={pathLength}
              strokeDashoffset={pathLength * (1 - draw)}
            />
          );
        })}

        {boxes.map((box, index) => {
          const start = revealFrame(revealCues, index, boxes.length, durationInFrames * 0.5);
          const progress = enterProgress(frame, start, 10);
          const x = startX + index * (BOX_WIDTH + GAP);
          const scale = 0.8 + progress * 0.2;
          const cx = x + BOX_WIDTH / 2;
          const cy = ROW_Y + BOX_HEIGHT / 2;
          return (
            <g
              key={box.name}
              opacity={progress}
              transform={`translate(${cx} ${cy}) scale(${scale}) translate(${-cx} ${-cy})`}
            >
              <rect
                x={x + brutal.shadow}
                y={ROW_Y + brutal.shadow}
                width={BOX_WIDTH}
                height={BOX_HEIGHT}
                fill={palette.ink}
              />
              <rect
                x={x}
                y={ROW_Y}
                width={BOX_WIDTH}
                height={BOX_HEIGHT}
                fill={box.isPointer ? colours.accent : palette.cream}
                stroke={palette.ink}
                strokeWidth={brutal.borderThick}
              />
              <text
                x={cx}
                y={ROW_Y + 42}
                textAnchor="middle"
                fontFamily={fonts.title}
                fontSize={28}
                fill={boxInk(box)}
              >
                {box.name}
              </text>
              <text
                x={cx}
                y={ROW_Y + 108}
                textAnchor="middle"
                fontFamily={fonts.code}
                fontSize={44}
                fontWeight={700}
                fill={boxInk(box)}
              >
                {box.value}
              </text>
              <text
                x={cx}
                y={ROW_Y + 158}
                textAnchor="middle"
                fontFamily={fonts.code}
                fontSize={22}
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
  );
};
