import { useCurrentFrame, interpolate } from "remotion";
import { Audio } from "@remotion/media";

const dbToLinear = (db: number): number => Math.pow(10, db / 20);

export type DuckRange = { from: number; durationInFrames: number };

export type MusicBedProps = {
  musicSrc: string;
  /** Frame ranges (relative to this component) where narration plays; the bed ducks under these. */
  duckRanges: DuckRange[];
  /** dB level while nothing is talking (e.g. a pure-music intro). Default -14. */
  bedVolumeDb?: number;
  /** dB level under narration, per CLAUDE.md's "music bed ~-24dB under speech". Default -24. */
  duckedVolumeDb?: number;
  /** Frames to crossfade between bed and ducked levels. Default 15 (0.5s @30fps). */
  fadeFrames?: number;
  loop?: boolean;
};

/**
 * Background music bed that ducks under narration. Plays at `bedVolumeDb` by
 * default and dips to `duckedVolumeDb` for each range in `duckRanges`, with a
 * short crossfade so the duck isn't an audible jump cut.
 */
export const MusicBed: React.FC<MusicBedProps> = ({
  musicSrc,
  duckRanges,
  bedVolumeDb = -14,
  duckedVolumeDb = -24,
  fadeFrames = 15,
  loop = true,
}) => {
  const frame = useCurrentFrame();
  const bedLinear = dbToLinear(bedVolumeDb);
  const duckedLinear = dbToLinear(duckedVolumeDb);

  let target = bedLinear;
  for (const range of duckRanges) {
    const rampIn = interpolate(
      frame,
      [range.from - fadeFrames, range.from],
      [bedLinear, duckedLinear],
      {
        extrapolateLeft: "clamp",
        extrapolateRight: "clamp",
      },
    );
    const rampOutStart = range.from + range.durationInFrames;
    const rampOut = interpolate(
      frame,
      [rampOutStart, rampOutStart + fadeFrames],
      [duckedLinear, bedLinear],
      { extrapolateLeft: "clamp", extrapolateRight: "clamp" },
    );
    if (frame >= range.from - fadeFrames && frame < rampOutStart) {
      target = Math.min(target, rampIn);
    } else if (frame >= rampOutStart && frame < rampOutStart + fadeFrames) {
      target = Math.min(target, rampOut);
    }
  }

  return <Audio src={musicSrc} volume={target} loop={loop} />;
};
