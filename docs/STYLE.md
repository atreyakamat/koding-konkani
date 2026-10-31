# Koding Konkani: pacing, cuts and transitions

Audience: school and college students, and working professionals who want C done properly.
Feel: calm, confident and cinematic, with a neo-brutalist look. Friendly jokes stay, but they are
short and well timed, never silly for its own sake. This file is read together with CLAUDE.md.

## 1. Pace (slow on purpose)

- Narration is slow and clear: Piper `length_scale` 1.12 (about 125 to 135 words a minute).
  Settings live in `config/voice.json` under `pacing`.
- Pauses: 0.4 s after each sentence, 0.7 s between scenes, 1.0 s before the Bug of the Day reveal.
  Silence is part of the pacing; let the code and the animation breathe.
- Every code line gets its own beat: highlight, then speak, then 0.3 s hold before the next line.
- Episodes may run up to 9:00 because of the slower pace. If one goes over, report it and trim
  narration, do not speed the voice up.
- Speed tip: EP 01 says it out loud ("I speak slowly on purpose... set the speed to 1.5x"). Every
  episode also shows a small on-screen chip, `TIP: SET SPEED TO 1.5x`, for 3 seconds in the first
  10 seconds (component `SpeedTip`). It is never spoken again after EP 01.

## 2. Cuts and transitions

Vocabulary (use `@remotion/transitions` presentations where they exist; custom ones are built
from flat shapes, no blur, no gradients). Max length 12 frames (0.4 s). Every transition has a
sound effect that lands on the cut. Never use the same transition twice in a row.

| From to | Transition | Sound |
|---|---|---|
| Cold open to Title card | Hard cut with a 2-frame white impact frame | thud |
| Title card to anything | Ink wipe: a flat accent-colour block sweeps across and reveals the next scene | whoosh |
| Concept slide to Concept slide | Slide (alternate left and right) | whoosh |
| Concept slide to Code explain | Push-in: scale 1.06 to 1.0 with a vertical wipe | marker-swipe |
| Code explain to Terminal | Window pop: the terminal springs up from the code panel | key-tick |
| Any to Bug of the Day | Whip: fast horizontal slide with a 3-frame shake | buzzer (low) |
| Bug of the Day (wrong to fixed) | Split: the fixed panel slides over the wrong one | ding |
| Any to Pun card | Flip (Y axis) | pop |
| Pun card to Challenge | Clock wipe | stamp |
| Challenge to Outro | Fade to the module background | chime |

## 3. Camera moves (cinematic, still flat)

- Slow push: concept slides drift from scale 1.00 to 1.04 over the scene. Never static for more than 3 s.
- Focus pull on code: when a line is highlighted, dim the other lines to 35 percent and push in
  to scale 1.05 centred on that line; ease back out when the scene ends.
- Parallax: background shapes (circles, bars) move at 20 to 40 percent of the foreground speed.
- Impact frames: on stamps and crashes, hold one frame, shake for 2 frames, then settle.
- Punch-in: on a key word, scale the on-screen text 1.0 to 1.12 and back in 10 frames.
- Cut on action: cut while something is moving, never on a still frame.
- Xecxec reacts (eyes, claws) one beat after the narrator finishes a line, never over it.

## 4. Polish rules

- Hierarchy: one focal point per frame. If two things move, one of them is the background.
- No jump scares, no flashing faster than 3 times a second (accessibility).
- Captions are always burnt in (word-highlight style), lower third on long videos.
- Music bed under speech at about -24 dB, ducked; stop music for the Bug of the Day reveal.
- Every Short opens on its hook in the first 1.5 s: motion on frame 0, no logo intro.
- Professional tone: define a term once, precisely, then use it. Jokes land after the idea, not instead of it.

## 5. What not to do

Gradients, blur, emoji, drop shadows that are not the hard offset shadow, stock transitions with
glow or sparkle, text that moves while it is being read, and speeding up the voice to save time.
