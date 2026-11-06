import { z } from "zod";

/** The `memory` scene field of a memory-boxes scene: a list of frames, each frame a few groups of cells.
 * It covers arrays, strings, grids, matrices, scalar swaps with steps and aliases. The older flat `boxes`
 * list (name / value / address boxes, pointer arrows) is unchanged and still used by EP7-18.
 *
 *  - cell: one memory box. `name` is the variable name (scalars), `index` the position under an array cell.
 *    `mark` styles it: zero (grey, filled with zero by the compiler), stop (the \0 stop sign), taken (mint,
 *    consumed), hl (butter highlight). `lost` is the value that was just overwritten, drawn struck through.
 *  - group: a row of cells, or a grid when `cols` is smaller than the cell count. `tags` are extra name tags
 *    on the same row (an alias); `ruler` draws a byte ruler under the cells.
 *  - frame: what is on screen between two moments; frames are spread evenly over the scene. A cell that
 *    differs from the previous frame pops in; the arrows draw on. `arrange: "row"` puts the groups side by
 *    side with `joiners` ("+", "=") between them; the default stacks them.
 *  - arrow refs are "group:cell" (zero based). */
export const MAX_CELLS_PER_GROUP = 13;
export const MAX_GROUPS_PER_FRAME = 3;

export const CellMarkSchema = z.enum(["zero", "stop", "taken", "hl"]);

export const MemoryCellSchema = z.object({
  value: z.string().min(1),
  name: z.string().min(1).optional(),
  index: z.union([z.number().int().nonnegative(), z.string().min(1)]).optional(),
  address: z.string().min(1).optional(),
  mark: CellMarkSchema.optional(),
  lost: z.string().min(1).optional(),
});

export const MemoryGroupSchema = z.object({
  name: z.string().min(1).optional(),
  tags: z.array(z.string().min(1)).max(3).optional(),
  cols: z.number().int().positive().optional(),
  ruler: z.object({ each: z.string().min(1), total: z.string().min(1) }).optional(),
  cells: z.array(MemoryCellSchema).min(1).max(MAX_CELLS_PER_GROUP),
});

const ArrowRefSchema = z.string().regex(/^\d+:\d+$/);

export const MemoryFrameSchema = z.object({
  label: z.string().min(1).optional(),
  badges: z.array(z.string().min(1)).max(3).optional(),
  arrange: z.enum(["stack", "row"]).optional(),
  joiners: z.array(z.string().min(1)).max(2).optional(),
  groups: z.array(MemoryGroupSchema).min(1).max(MAX_GROUPS_PER_FRAME),
  arrows: z.array(z.object({ from: ArrowRefSchema, to: ArrowRefSchema })).optional(),
});

export const MemoryDataSchema = z.object({
  frames: z.array(MemoryFrameSchema).min(1).max(6),
});

export type CellMark = z.infer<typeof CellMarkSchema>;
export type MemoryCell = z.infer<typeof MemoryCellSchema>;
export type MemoryGroup = z.infer<typeof MemoryGroupSchema>;
export type MemoryFrame = z.infer<typeof MemoryFrameSchema>;
export type MemoryData = z.infer<typeof MemoryDataSchema>;
