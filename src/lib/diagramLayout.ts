import type { Diagram } from "./episode";

type GraphDiagram = Extract<Diagram, { kind: "graph" }>;

export type PlacedNode = {
  id: string;
  label: string;
  sub: string;
  x: number;
  y: number;
  w: number;
  h: number;
  index: number;
};
export type PlacedEdge = {
  from: string;
  to: string;
  label: string;
  x1: number;
  y1: number;
  x2: number;
  y2: number;
};
export type GraphLayout = {
  width: number;
  height: number;
  nodes: PlacedNode[];
  edges: PlacedEdge[];
};

/** Depth of each node: the first node is depth 0, a child sits one level below its deepest parent.
 * Edges that would form a cycle are ignored, so a bad diagram still lays out instead of looping. */
const depths = (g: GraphDiagram): Map<string, number> => {
  const depth = new Map<string, number>(g.nodes.map((n) => [n.id, 0]));
  for (let pass = 0; pass < g.nodes.length; pass++) {
    let changed = false;
    for (const e of g.edges) {
      const next = (depth.get(e.from) ?? 0) + 1;
      if (next > (depth.get(e.to) ?? 0) && next < g.nodes.length) {
        depth.set(e.to, next);
        changed = true;
      }
    }
    if (!changed) break;
  }
  return depth;
};

/** Places the nodes of a graph diagram inside a width x height box. Pure: same input, same boxes. */
export const layoutGraph = (g: GraphDiagram, width: number, height: number): GraphLayout => {
  const levelOf = new Map<string, number>();
  if (g.layout === "row") g.nodes.forEach((n) => levelOf.set(n.id, 0));
  else if (g.layout === "column") g.nodes.forEach((n, i) => levelOf.set(n.id, i));
  else depths(g).forEach((d, id) => levelOf.set(id, d));

  const levelCount = Math.max(...levelOf.values()) + 1;
  const perLevel: string[][] = Array.from({ length: levelCount }, () => []);
  for (const n of g.nodes) perLevel[levelOf.get(n.id) ?? 0].push(n.id);
  const widest = Math.max(...perLevel.map((l) => l.length));

  const gapX = 56;
  const w = Math.min(340, Math.floor((width - (widest - 1) * gapX) / widest));
  const rowH = height / levelCount;
  const h = Math.min(150, Math.floor(rowH - (levelCount > 1 ? 64 : 0)));

  const nodes: PlacedNode[] = [];
  perLevel.forEach((ids, level) => {
    const slot = width / ids.length;
    ids.forEach((id, i) => {
      const n = g.nodes.find((x) => x.id === id)!;
      nodes.push({
        id,
        label: n.label,
        sub: n.sub,
        x: slot * (i + 0.5) - w / 2,
        y: rowH * (level + 0.5) - h / 2,
        w,
        h,
        index: g.nodes.indexOf(n),
      });
    });
  });

  const byId = new Map(nodes.map((n) => [n.id, n]));
  const edges: PlacedEdge[] = [];
  for (const e of g.edges) {
    const a = byId.get(e.from);
    const b = byId.get(e.to);
    if (!a || !b) continue;
    if (g.layout === "row") {
      edges.push({ ...e, x1: a.x + a.w, y1: a.y + a.h / 2, x2: b.x, y2: b.y + b.h / 2 });
    } else {
      edges.push({ ...e, x1: a.x + a.w / 2, y1: a.y + a.h, x2: b.x + b.w / 2, y2: b.y });
    }
  }
  return { width, height, nodes, edges };
};
