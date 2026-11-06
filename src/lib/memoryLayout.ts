import type { MemoryFrame } from "./memory.ts";

/** Pure layout for the MemoryBoxes `memory` frames (no React, so scripts/check_boxes.mts can run it under Node).
 * Everything is in the 1920x1080 composition space. The free band is what is left clear of the top-right
 * Xecxec, the label strip at the top and the burnt-in caption bar at the bottom (starts near y 905). */
export const BAND = { x: 96, width: 1728, top: 270, bottom: 880 } as const;
export const MAX_CELL_WIDTH = 220;
/** A frame whose largest group has at most SMALL_GROUP_CELLS cells scales its boxes up to this width. */
export const SMALL_CELL_WIDTH = 320;
export const SMALL_GROUP_CELLS = 3;
export const MIN_CELL_WIDTH = 64;
/** Cell height as a fraction of its width (the value and the address line sit inside). */
export const CELL_ASPECT = 0.8;
const HEADER = 54;
const INDEX_ROW = 36;
const RULER_ROW = 86;
const GROUP_GAP = 36;
const JOINER_GAP = 90;
/** Gap between rows of a grid; a group with an index under each cell needs room for that label. */
const rowGapFor = (indexed: boolean): number => (indexed ? INDEX_ROW + 22 : 26);

export type PlacedGroup = {
  x: number;
  y: number;
  width: number;
  height: number;
  cols: number;
  rows: number;
  gapX: number;
  headerHeight: number;
  hasIndex: boolean;
  rowGap: number;
};

export type FrameLayout = {
  cellWidth: number;
  cellHeight: number;
  groups: PlacedGroup[];
  /** x of the centre of the gap before group k (k >= 1), for the joiners. */
  joinerX: number[];
  fits: boolean;
};

const gapFor = (w: number): number => Math.max(14, Math.round(w * 0.12));

type Shape = { cols: number; rows: number; header: boolean; index: boolean; ruler: boolean };

const shapes = (frame: MemoryFrame): Shape[] =>
  frame.groups.map((g) => ({
    cols: Math.min(g.cols ?? g.cells.length, g.cells.length),
    rows: Math.ceil(g.cells.length / Math.min(g.cols ?? g.cells.length, g.cells.length)),
    header: !!(g.name || g.tags?.length),
    index: g.cells.some((c) => c.index !== undefined),
    ruler: !!g.ruler,
  }));

const sizeOf = (s: Shape, w: number): { width: number; height: number } => {
  const h = Math.round(w * CELL_ASPECT);
  const gap = gapFor(w);
  return {
    width: s.cols * w + (s.cols - 1) * gap,
    height: (s.header ? HEADER : 0) + s.rows * h + (s.rows - 1) * rowGapFor(s.index) + (s.index ? INDEX_ROW : 0) + (s.ruler ? RULER_ROW : 0),
  };
};

/** The largest cell width (up to MAX_CELL_WIDTH) at which every group of the frame fits the free band. */
export const layoutFrame = (frame: MemoryFrame): FrameLayout => {
  const sh = shapes(frame);
  const row = frame.arrange === "row";
  const areaHeight = BAND.bottom - BAND.top;
  const fitsAt = (w: number): boolean => {
    const sizes = sh.map((s) => sizeOf(s, w));
    if (row) {
      const total = sizes.reduce((n, s) => n + s.width, 0) + (sizes.length - 1) * JOINER_GAP;
      return total <= BAND.width && Math.max(...sizes.map((s) => s.height)) <= areaHeight;
    }
    const total = sizes.reduce((n, s) => n + s.height, 0) + (sizes.length - 1) * GROUP_GAP;
    return Math.max(...sizes.map((s) => s.width)) <= BAND.width && total <= areaHeight;
  };
  const small = frame.groups.every((g) => g.cells.length <= SMALL_GROUP_CELLS);
  let w = small ? SMALL_CELL_WIDTH : MAX_CELL_WIDTH;
  while (w > MIN_CELL_WIDTH && !fitsAt(w)) w -= 2;
  const fits = fitsAt(w);
  const cellHeight = Math.round(w * CELL_ASPECT);
  const sizes = sh.map((s) => sizeOf(s, w));
  const placed: PlacedGroup[] = [];
  const joinerX: number[] = [];
  if (row) {
    const total = sizes.reduce((n, s) => n + s.width, 0) + (sizes.length - 1) * JOINER_GAP;
    let x = BAND.x + (BAND.width - total) / 2;
    const maxH = Math.max(...sizes.map((s) => s.height));
    const y = BAND.top + (areaHeight - maxH) / 2;
    sizes.forEach((s, k) => {
      placed.push({ x, y, ...s, cols: sh[k].cols, rows: sh[k].rows, gapX: gapFor(w), headerHeight: sh[k].header ? HEADER : 0, hasIndex: sh[k].index, rowGap: rowGapFor(sh[k].index) });
      x += s.width;
      if (k < sizes.length - 1) joinerX.push(x + JOINER_GAP / 2);
      x += JOINER_GAP;
    });
  } else {
    const total = sizes.reduce((n, s) => n + s.height, 0) + (sizes.length - 1) * GROUP_GAP;
    let y = BAND.top + (areaHeight - total) / 2;
    sizes.forEach((s, k) => {
      const x = BAND.x + (BAND.width - s.width) / 2;
      placed.push({ x, y, ...s, cols: sh[k].cols, rows: sh[k].rows, gapX: gapFor(w), headerHeight: sh[k].header ? HEADER : 0, hasIndex: sh[k].index, rowGap: rowGapFor(sh[k].index) });
      y += s.height + GROUP_GAP;
    });
  }
  return { cellWidth: w, cellHeight, groups: placed, joinerX, fits };
};

/** Top-left of cell `i` of a placed group. */
export const cellOrigin = (layout: FrameLayout, g: number, i: number): { x: number; y: number } => {
  const p = layout.groups[g];
  const col = i % p.cols;
  const row = Math.floor(i / p.cols);
  return {
    x: p.x + col * (layout.cellWidth + p.gapX),
    y: p.y + p.headerHeight + row * (layout.cellHeight + p.rowGap),
  };
};

/** Frame index shown at `frame`: frames share the scene evenly. */
export const frameIndexAt = (frame: number, count: number, durationInFrames: number): number =>
  Math.min(count - 1, Math.max(0, Math.floor((frame * count) / Math.max(1, durationInFrames))));

/** First frame (in the scene) at which frame `k` is shown. */
export const frameStart = (k: number, count: number, durationInFrames: number): number =>
  Math.ceil((k * durationInFrames) / count);
