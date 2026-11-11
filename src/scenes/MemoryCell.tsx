import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { enterProgress } from "../lib/motion";
import { CELL_ASPECT } from "../lib/memoryLayout";
import type { CellMark, MemoryCell } from "../lib/memory";

export type MemoryCellViewProps = {
  cell: MemoryCell;
  x: number;
  y: number;
  width: number;
  frame: number;
  /** Frame at which this cell pops in. */
  start: number;
  /** Ink for the text that sits on the scene background (the index under the cell). */
  labelInk: string;
};

const FILL: Record<CellMark, string> = {
  zero: palette.cream,
  stop: palette.tomato,
  taken: palette.mint,
  hl: palette.butter,
};

const valueScale = (value: string): number => (value.length > 6 ? 0.55 : value.length > 3 ? 0.75 : 1);

/** One memory box of the `memory` layout: the existing box look (cream fill, thick ink border, hard shadow),
 * a value, an optional variable name on top and address inside, and the index below. */
export const MemoryCellView: React.FC<MemoryCellViewProps> = ({ cell, x, y, width, frame, start, labelInk }) => {
  const height = Math.round(width * CELL_ASPECT);
  const progress = enterProgress(frame, start, 10);
  const scale = 0.8 + progress * 0.2;
  const cx = x + width / 2;
  const cy = y + height / 2;
  const fill = cell.mark ? FILL[cell.mark] : palette.cream;
  const ink = readableOn(fill);
  const faded = cell.mark === "zero";
  const hasName = !!cell.name;
  const showAddress = !!cell.address && width >= 120;
  const valueSize = Math.round(width * 0.34 * valueScale(cell.value));
  const index = cell.index === undefined ? undefined : typeof cell.index === "number" ? `[${cell.index}]` : cell.index;
  return (
    <g
      opacity={progress}
      transform={`translate(${cx} ${cy}) scale(${scale}) translate(${-cx} ${-cy})`}
    >
      <rect x={x + brutal.shadow} y={y + brutal.shadow} width={width} height={height} fill={palette.ink} />
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        fill={fill}
        fillOpacity={faded ? 0.5 : 1}
        stroke={palette.ink}
        strokeWidth={brutal.borderThick}
      />
      {hasName ? (
        <text
          x={cx}
          y={y + height * 0.24}
          textAnchor="middle"
          fontFamily={fonts.title}
          fontSize={Math.round(width * 0.15)}
          fill={ink}
        >
          {cell.name}
        </text>
      ) : null}
      <text
        x={cx}
        y={y + height * (hasName ? 0.62 : showAddress ? 0.56 : 0.64)}
        textAnchor="middle"
        fontFamily={fonts.code}
        fontSize={valueSize}
        fontWeight={700}
        fill={ink}
        fillOpacity={faded ? 0.55 : 1}
      >
        {cell.value}
      </text>
      {showAddress ? (
        <text
          x={cx}
          y={y + height * 0.9}
          textAnchor="middle"
          fontFamily={fonts.code}
          fontSize={Math.max(14, Math.round(width * 0.075))}
          fill={ink}
          fillOpacity={0.7}
        >
          {cell.address}
        </text>
      ) : null}
      {index ? (
        <text
          x={cx}
          y={y + height + 30}
          textAnchor="middle"
          fontFamily={fonts.code}
          fontSize={26}
          fontWeight={700}
          fill={labelInk}
          fillOpacity={0.85}
        >
          {index}
        </text>
      ) : null}
      {cell.lost ? (
        <text
          x={cx}
          y={y - 12}
          textAnchor="middle"
          fontFamily={fonts.code}
          fontSize={Math.round(width * 0.2)}
          fontWeight={700}
          fill={palette.tomato}
          textDecoration="line-through"
        >
          {cell.lost}
        </text>
      ) : null}
    </g>
  );
};
