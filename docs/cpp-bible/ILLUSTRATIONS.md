# Illustration data (scene 4)

Scene 4 of every episode has one illustration. It is **data, not a picture**. Remotion reads the JSON block in the episode's "Illustrations" section and draws it. All numbers in the JSON come from real code or from the tools in `scripts/cpp_bible/lib.py`, so they cannot drift from the code on screen.

`scripts/preflight_cpp.py` checks every block against the rules below. A block that fails stops the render.

Every block has `"scene": 4`, a `"kind"` and a `"caption"`.

| kind | Scene template | Used for |
| --- | --- | --- |
| `memory` | Memory boxes | variables, pointers, arrays, heap blocks |
| `flow` | Concept slide | ordered steps (build steps, exception path, thread life) |
| `graph` | Concept slide | trees, inheritance, links between objects (`layout`: row, column, tree) |
| `table` | Concept slide | comparisons, anatomy, reference lists |
| `callstack` | Concept slide | recursion and function calls |
| `trace` | Algorithm bars | bubble, selection, insertion sort |

## memory

```json
{ "kind": "memory", "addressesAreIllustrative": true, "caption": "...",
  "boxes": [ { "id": "p", "name": "p", "type": "int*", "value": "0x2000", "bytes": 8, "addr": "0x1008", "region": "stack" } ],
  "arrows": [ { "from": "p", "to": "x", "label": "points to" } ] }
```

- 1 to 12 boxes. Each box has `id`, `name`, `type`, `value`, `bytes`, `addr` and `region`. `id` values are unique.
- `region` is `stack`, `heap` or `static`. Addresses are hex, aligned to the size (at most 8), and boxes in one region never overlap.
- `bytes` follows the type: char 1, short 2, int 4, float 4, long long 8, double 8, pointer 8. The generator fills it in.
- An array of N items becomes N boxes named `name[0]` to `name[N-1]`.
- A pointer box must have an arrow, or the value `nullptr`. Its `value` equals the address of the box it points to.
- Addresses are for teaching. The flag `addressesAreIllustrative` is always true. Do not print them as real addresses.

## flow

`{ "kind": "flow", "steps": [ { "id": "s1", "label": "throw", "detail": "divide throws" } ] }`

2 to 6 steps. Draw them in order, left to right.

## graph

`{ "kind": "graph", "layout": "tree", "nodes": [ { "id": "n5", "label": "5", "sub": "root" } ], "edges": [ { "from": "n5", "to": "n3", "label": "left" } ] }`

Every edge names two node ids that exist. With `tree`, the first node is the root, and the order of the edges decides left and right.

## table

`{ "kind": "table", "headers": ["Stream", "Direction"], "rows": [ ["ofstream", "program to file"] ] }`

Each row has as many cells as there are headers. Draw one row at a time, and glow the row the narrator names.

## callstack

`{ "kind": "callstack", "steps": [ { "step": 1, "frames": ["main()", "factorial(n=3)"], "note": "main calls factorial" } ] }`

`frames` lists the stack from bottom to top. Each step is one push or one pop.

## trace

`{ "kind": "trace", "algorithm": "bubble", "steps": [ { "step": 1, "array": [5, 2, 4], "compare": [0, 1], "swap": [0, 1], "sorted": [] } ] }`

The generator makes every step by running the real algorithm on the real array, and it keeps the counters (passes, compares, swaps). Colours: compare is butter, swap is tomato, sorted is mint. Do not change a trace by hand.
