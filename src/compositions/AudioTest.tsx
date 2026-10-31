import { AbsoluteFill, useCurrentFrame } from "remotion";
import { MusicBed, Sfx, type FrameRange, type SfxName } from "../audio";

/** Frame (at 30 fps) where each sound plays. A fake "narration" window checks the ducking. */
const CUES: { name: SfxName; at: number }[] = [
  { name: "sting", at: 0 },
  { name: "claw-click", at: 105 },
  { name: "whoosh", at: 120 },
  { name: "thud", at: 135 },
  { name: "key-tick", at: 150 },
  { name: "key-tick", at: 156 },
  { name: "key-tick", at: 162 },
  { name: "marker-swipe", at: 180 },
  { name: "ding", at: 210 },
  { name: "buzzer", at: 240 },
  { name: "pop", at: 270 },
  { name: "stamp", at: 285 },
  { name: "chime", at: 300 },
  { name: "rimshot", at: 330 },
];

/** Pretend the narrator speaks from 2.0 s to 6.5 s: the bed must duck inside this window. */
export const AUDIO_TEST_DUCK: FrameRange[] = [{ from: 60, to: 195 }];
export const AUDIO_TEST_DURATION = 420;

export const AudioTest: React.FC = () => {
  const frame = useCurrentFrame();
  const last = [...CUES].reverse().find((c) => c.at <= frame);
  return (
    <AbsoluteFill
      style={{ background: "#FFD8BE", justifyContent: "center", alignItems: "center", gap: 24 }}
    >
      <div style={{ fontSize: 72, fontWeight: 900, fontFamily: "sans-serif" }}>AUDIO TEST</div>
      <div style={{ fontSize: 56, fontFamily: "monospace" }}>{last ? last.name : "bed only"}</div>
      <MusicBed duckRanges={AUDIO_TEST_DUCK} />
      {CUES.map((c, i) => (
        <Sfx key={i} name={c.name} at={c.at} />
      ))}
    </AbsoluteFill>
  );
};
