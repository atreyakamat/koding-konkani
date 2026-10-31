import { Html5Audio, interpolate, staticFile, useCurrentFrame } from "remotion";
import { MUSIC_VOLUME } from "./sfx-levels";

export type FrameRange = { from: number; to: number };
export type MusicBedProps = { src?: string; duckRanges?: FrameRange[]; rampFrames?: number };

/** Volume (0 to 1) of the bed at `frame`: ducked inside any narration range, with short ramps. */
export const musicVolumeAt = (frame: number, duckRanges: FrameRange[], rampFrames = 8): number => {
  let duck = 0;
  for (const { from, to } of duckRanges) {
    const d = interpolate(frame, [from - rampFrames, from, to, to + rampFrames], [0, 1, 1, 0], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    duck = Math.max(duck, d);
  }
  return MUSIC_VOLUME.normal + (MUSIC_VOLUME.ducked - MUSIC_VOLUME.normal) * duck;
};

/** Looping music bed that ducks under the narrator. Phase 5 passes the narration ranges. */
export const MusicBed: React.FC<MusicBedProps> = ({
  src = "music/bed-01.wav",
  duckRanges = [],
  rampFrames = 8,
}) => {
  const frame = useCurrentFrame();
  return (
    <Html5Audio src={staticFile(src)} loop volume={musicVolumeAt(frame, duckRanges, rampFrames)} />
  );
};
