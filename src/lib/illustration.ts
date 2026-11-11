import { z } from "zod";

/** Structured illustration spec (docs/python-bible/ILLUSTRATIONS.md). Pure data + pure layout and state functions,
 * so scripts can check a spec under Node without React. Validated in Python by scripts/check_illustrations.py. */
export const GRID_COLS = 12;
export const GRID_ROWS = 6;

export const COLOUR_TOKENS = [
  "tomato",
  "peach",
  "apricot",
  "butter",
  "cream",
  "pastelBlue",
  "mint",
  "lilac",
  "darkBlue",
  "ink",
  "white",
] as const;
export const VERBS = [
  "show",
  "hide",
  "move",
  "draw",
  "glow",
  "dim",
  "shake",
  "stamp",
  "tick",
  "cross",
  "flip",
] as const;
export const SFX_NAMES = [
  "buzzer",
  "chime",
  "claw-click",
  "ding",
  "key-tick",
  "marker-swipe",
  "pop",
  "rimshot",
  "stamp",
  "sting",
  "thud",
  "whoosh",
] as const;

const ObjectSchema = z.object({
  id: z.string().min(1),
  shape: z.enum(["box", "card", "label", "token", "arrow"]),
  text: z.string(),
  colour: z.enum(COLOUR_TOKENS),
  col: z
    .number()
    .int()
    .min(0)
    .max(GRID_COLS - 1)
    .optional(),
  row: z
    .number()
    .int()
    .min(0)
    .max(GRID_ROWS - 1)
    .optional(),
  w: z.number().int().min(1).max(GRID_COLS).optional(),
  h: z.number().int().min(1).max(GRID_ROWS).optional(),
  from: z.string().optional(),
  to: z.string().optional(),
});

const StepSchema = z.object({
  t: z.number().min(0).max(1),
  do: z.enum(VERBS),
  target: z.string().min(1),
  sfx: z.enum(SFX_NAMES).optional(),
  to: z.tuple([z.number().int(), z.number().int()]).optional(),
});

export const IllustrationSchema = z.object({
  ep: z.number().int().optional(),
  scene: z.number().int().optional(),
  grid: z.object({ cols: z.literal(GRID_COLS), rows: z.literal(GRID_ROWS) }).optional(),
  objects: z.array(ObjectSchema).min(1),
  steps: z.array(StepSchema),
});
export type IllustrationSpec = z.infer<typeof IllustrationSchema>;
export type IllObject = z.infer<typeof ObjectSchema>;
export type IllStep = z.infer<typeof StepSchema>;

/** Drawing area in the 1920x1080 composition: clear of the top-right mascot and the caption band at the bottom. */
export const AREA = { x: 96, y: 200, width: 1728, height: 660 } as const;
export const CELL_W = AREA.width / GRID_COLS;
export const CELL_H = AREA.height / GRID_ROWS;
const GAP = 22;
export const MOVE_FRAMES = 12;
export const DRAW_FRAMES = 12;

export type Rect = { x: number; y: number; w: number; h: number };

/** Pixel rectangle of a grid position (fractional cells allowed while a move is in progress). */
export const rectAt = (col: number, row: number, w: number, h: number): Rect => ({
  x: AREA.x + col * CELL_W + GAP / 2,
  y: AREA.y + row * CELL_H + GAP / 2,
  w: w * CELL_W - GAP,
  h: h * CELL_H - GAP,
});

const clamp01 = (v: number): number => Math.min(1, Math.max(0, v));

export type ObjectState = {
  visible: boolean;
  appearAt: number;
  hideAt: number | null;
  drawAt: number | null;
  col: number;
  row: number;
  glowAt: number | null;
  dimmed: boolean;
  shakeAt: number | null;
  stampAt: number | null;
  tickAt: number | null;
  crossAt: number | null;
  flipAt: number | null;
};

/** Frame at which a step fires, for a scene of `duration` frames. */
export const stepFrame = (t: number, duration: number): number =>
  Math.round(t * Math.max(0, duration - 1));

/** State of one object at `frame`: replays every step that has already fired, in order. */
export const stateAt = (
  spec: IllustrationSpec,
  id: string,
  frame: number,
  duration: number,
): ObjectState => {
  const o = spec.objects.find((x) => x.id === id);
  const st: ObjectState = {
    visible: false,
    appearAt: 0,
    hideAt: null,
    drawAt: null,
    col: o?.col ?? 0,
    row: o?.row ?? 0,
    glowAt: null,
    dimmed: false,
    shakeAt: null,
    stampAt: null,
    tickAt: null,
    crossAt: null,
    flipAt: null,
  };
  let fromCol = st.col;
  let fromRow = st.row;
  let moveAt = -1;
  let toCol = st.col;
  let toRow = st.row;
  for (const s of spec.steps) {
    if (s.target !== id) continue;
    const sf = stepFrame(s.t, duration);
    if (sf > frame) break;
    switch (s.do) {
      case "show":
        st.visible = true;
        st.appearAt = sf;
        st.hideAt = null;
        break;
      case "draw":
        st.visible = true;
        st.appearAt = sf;
        st.drawAt = sf;
        st.hideAt = null;
        break;
      case "hide":
        st.visible = false;
        st.hideAt = sf;
        break;
      case "glow":
        st.glowAt = sf;
        st.dimmed = false;
        break;
      case "dim":
        st.dimmed = true;
        break;
      case "shake":
        st.shakeAt = sf;
        break;
      case "stamp":
        st.stampAt = sf;
        break;
      case "tick":
        st.tickAt = sf;
        break;
      case "cross":
        st.crossAt = sf;
        break;
      case "flip":
        st.flipAt = sf;
        break;
      case "move":
        if (s.to) {
          // A new move starts from wherever the previous one ended.
          fromCol = toCol;
          fromRow = toRow;
          toCol = s.to[0];
          toRow = s.to[1];
          moveAt = sf;
        }
        break;
    }
  }
  if (moveAt >= 0) {
    const p = clamp01((frame - moveAt) / MOVE_FRAMES);
    st.col = fromCol + (toCol - fromCol) * p;
    st.row = fromRow + (toRow - fromRow) * p;
  }
  return st;
};

/** Where an arrow runs: from the edge of one rectangle to the edge of the other, along the centre line. */
export const arrowPoints = (
  a: Rect,
  b: Rect,
): { x1: number; y1: number; x2: number; y2: number } => {
  const ca = { x: a.x + a.w / 2, y: a.y + a.h / 2 };
  const cb = { x: b.x + b.w / 2, y: b.y + b.h / 2 };
  const edge = (r: Rect, c: { x: number; y: number }, towards: { x: number; y: number }) => {
    const dx = towards.x - c.x;
    const dy = towards.y - c.y;
    if (dx === 0 && dy === 0) return c;
    const sx = dx === 0 ? Infinity : r.w / 2 / Math.abs(dx);
    const sy = dy === 0 ? Infinity : r.h / 2 / Math.abs(dy);
    const k = Math.min(sx, sy);
    return { x: c.x + dx * k, y: c.y + dy * k };
  };
  const p1 = edge(a, ca, cb);
  const p2 = edge(b, cb, ca);
  return { x1: p1.x, y1: p1.y, x2: p2.x, y2: p2.y };
};

/** Largest font size (descending list) at which `text` wraps into the box; smallest otherwise. */
export const fitFont = (
  text: string,
  width: number,
  height: number,
  sizes: number[] = [40, 36, 32, 28, 24, 22],
): number => {
  for (const size of sizes) {
    const perRow = Math.max(1, Math.floor((width - 28) / (size * 0.56)));
    const rows = text
      .split("\n")
      .reduce((n, line) => n + Math.max(1, Math.ceil(line.length / perRow)), 0);
    if (rows * size * 1.2 <= height - 14) return size;
  }
  return sizes[sizes.length - 1];
};
