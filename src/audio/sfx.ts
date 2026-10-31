/** Sound-effect names (files live in audio/sfx/<name>.wav) and their default mix level (0 to 1). */
export const SFX_VOLUME = {
  "claw-click": 0.9,
  thud: 0.9,
  whoosh: 0.6,
  "key-tick": 0.5,
  "marker-swipe": 0.6,
  ding: 0.8,
  buzzer: 0.4,
  pop: 0.8,
  stamp: 0.9,
  chime: 0.6,
  rimshot: 0.8,
  sting: 0.8,
} as const;

export type SfxName = keyof typeof SFX_VOLUME;

/** Music bed level: normal, and ducked while the narrator is talking (about -12 dB). */
export const MUSIC_VOLUME = { normal: 0.25, ducked: 0.06 } as const;
