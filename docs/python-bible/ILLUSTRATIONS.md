# Illustration specs (Remotion-ready)

Complex drawings are data, not prose. Each one is a JSON file in `docs/python-bible/illustrations/epNNN.json`.
Source of truth: `scripts/python_bible/illustrations.py`. Validator: `python3 scripts/check_illustrations.py` (add `--write` to export the JSON).
38 episodes have a spec: EP 13, 15, 19, 22, 41, 43, 44, 46-50, 52-61, 67, 68, 70, 74-80, 85-90. Memory boxes for other episodes come from the real run (see the checker).

## Format

```json
{ "ep": 13, "scene": 4, "grid": {"cols": 12, "rows": 6},
  "objects": [ {"id":"q","shape":"box","text":"temperature > 30 ?","colour":"butter","col":4,"row":0,"w":4,"h":1},
               {"id":"a1","shape":"arrow","text":"True","colour":"ink","from":"q","to":"yes"} ],
  "steps":   [ {"t":0.0,"do":"show","target":"q","sfx":"pop"} ] }
```

| Field | Rule |
|---|---|
| grid | 12 columns (0-11) by 6 rows (0-5). Map to the 1920x1080 canvas. One cell is 160x180 px with a margin. |
| shape | `box`, `card`, `label`, `token`, `arrow` |
| colour | tomato, peach, apricot, butter, cream, pastelBlue, mint, lilac, darkBlue, ink, white (theme tokens only) |
| col, row, w, h | Integers. The object must fit inside the grid. |
| arrow | Has `from` and `to` (ids of non-arrow objects). No position fields. |
| t | A number from 0 to 1. Fraction of the scene length. Steps stay in time order. |
| do | show, hide, move, draw, glow, dim, shake, stamp, tick, cross, flip |
| move | Needs `to=[col,row]`. The moved object must stay inside the grid. |
| draw | Arrows only. Other verbs on arrows: show, hide, glow, dim. |
| sfx | buzzer, chime, claw-click, ding, key-tick, marker-swipe, pop, rimshot, stamp, sting, thud, whoosh |

## Zero-error rules (the validator enforces all of them)

- Every id is unique. Every `target`, `from` and `to` exists.
- Every object is shown or drawn at least once.
- An arrow is not drawn before both of its ends are shown.
- No two boxes overlap, except full nesting: the outer box comes first in the list, the inner box lies completely inside it.
- Only the listed verbs, colours, shapes and sound names. No extra keys in a step.

## Remotion mapping

- Read `t * sceneFrames` to get the start frame. Use a spring of 8-12 frames for show, move, flip.
- `show`: pop in. `hide`: scale out. `glow`: butter outline, 8 frames. `dim`: opacity 0.35. `shake`: 2-frame shake. `stamp`: scale 1.4 to 1 with thud.
- `draw`: stroke-dashoffset from full length to 0 in 10 frames. Arrow runs from the edge of `from` to the edge of `to`. `text` sits on the middle of the arrow.
- Play the `sfx` file at the start frame of the step.
- If the narration audio is longer or shorter than the plan, keep `t` as a fraction. The steps stretch with the scene.
- All boxes use a 4 px ink border and an 8 px hard shadow. Text is Space Grotesk 700; code text is JetBrains Mono.

## Memory scenes

Memory boxes (names, objects, aliasing) are not in these files. `check_py.py` derives them from a real run of the code, with no addresses. Use the Memory section of each episode in `m*.md`.
