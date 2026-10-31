import { useCallback, useEffect, useState } from "react";
import { AbsoluteFill, Sequence, staticFile, useDelayRender, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import type { Caption } from "@remotion/captions";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { Sticker } from "../ui";
import { Xecxec } from "../mascot/Xecxec";
import { MusicBed } from "../audio/MusicBed";
import { VoiceTestCaptions } from "./VoiceTestCaptions";

export type VoiceTestProps = {
  voiceLabel: string;
  voiceSrc: string;
  captionsSrc: string;
};

const MUSIC_SRC = staticFile("voice-test/placeholder-pad.wav");
const SFX = [
  staticFile("voice-test/placeholder-whoosh.wav"),
  staticFile("voice-test/placeholder-tick.wav"),
  staticFile("voice-test/placeholder-chime.wav"),
];

/**
 * Phase 3 voice test harness: plays one narration sample over a ducked music
 * bed with 3 SFX accents and word-highlighted captions, so a voice can be
 * judged with the mix instead of in isolation.
 */
export const VoiceTest: React.FC<VoiceTestProps> = ({ voiceLabel, voiceSrc, captionsSrc }) => {
  const { durationInFrames } = useVideoConfig();
  const [captions, setCaptions] = useState<Caption[] | null>(null);
  const { delayRender, continueRender, cancelRender } = useDelayRender();
  const [handle] = useState(() => delayRender());

  const fetchCaptions = useCallback(async () => {
    try {
      const response = await fetch(staticFile(captionsSrc));
      const data = (await response.json()) as Caption[];
      setCaptions(data);
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [captionsSrc, continueRender, cancelRender, handle]);

  useEffect(() => {
    fetchCaptions();
  }, [fetchCaptions]);

  if (!captions) {
    return null;
  }

  return (
    <AbsoluteFill style={{ background: palette.peach }}>
      <Audio src={staticFile(voiceSrc)} />
      <MusicBed musicSrc={MUSIC_SRC} duckRanges={[{ from: 0, durationInFrames }]} />
      <Sequence>
        <Audio src={SFX[0]} volume={0.7} />
      </Sequence>
      <Sequence from={Math.round(durationInFrames * 0.45)}>
        <Audio src={SFX[1]} volume={0.6} />
      </Sequence>
      <Sequence from={Math.max(0, durationInFrames - 20)}>
        <Audio src={SFX[2]} volume={0.6} />
      </Sequence>

      <AbsoluteFill style={{ padding: 96 }}>
        <Sticker
          text={voiceLabel.replace(/_/g, " ")}
          background={palette.white}
          rotateDeg={-3}
          fontSize={40}
        />
        <div style={{ position: "absolute", bottom: 96, right: 110 }}>
          <Xecxec pose="idle" size={180} />
        </div>
        <div
          style={{
            position: "absolute",
            top: 96,
            right: 110,
            fontFamily: fonts.body,
            fontSize: 24,
            color: palette.ink,
            opacity: 0.6,
          }}
        >
          Voice test · Phase 3
        </div>
      </AbsoluteFill>

      <VoiceTestCaptions captions={captions} />
    </AbsoluteFill>
  );
};
