import { Composition } from "remotion";
import { LongVideo, calculateMetadata as calculateLongVideoMetadata } from "./compositions/LongVideo";
import { Short, calculateMetadata as calculateShortMetadata } from "./compositions/Short";
import { AudioTest, AUDIO_TEST_DURATION } from "./compositions/AudioTest";
import { SceneGallery, SCENE_GALLERY_DURATION } from "./compositions/SceneGallery";
import { VoiceTest } from "./compositions/VoiceTest";

export const FPS = 30;

/** Phase 3 voice test: one composition per candidate voice, sized to its own measured duration. */
const VOICE_TEST_SAMPLES = [
  { id: "VoiceTest-am-michael", label: "am_michael (Kokoro)", seconds: 29.95, file: "am_michael" },
  { id: "VoiceTest-am-adam", label: "am_adam (Kokoro)", seconds: 25.4, file: "am_adam" },
  { id: "VoiceTest-bm-george", label: "bm_george (Kokoro)", seconds: 26.85, file: "bm_george" },
  { id: "VoiceTest-bm-lewis", label: "bm_lewis (Kokoro)", seconds: 28.7, file: "bm_lewis" },
  {
    id: "VoiceTest-en-US-ryan",
    label: "en_US-ryan-high (Piper)",
    seconds: 26.59,
    file: "en_US-ryan-high",
  },
] as const;

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="LongVideo"
        component={LongVideo}
        calculateMetadata={calculateLongVideoMetadata}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{ episodeNumber: 1 }}
      />
      {/* Every episode has 5 Shorts, S1-S5 (CLAUDE.md). One composition id per slot; the
          episode to render is picked via defaultProps / --props, same as LongVideo. */}
      {(["S1", "S2", "S3", "S4", "S5"] as const).map((shortId) => (
        <Composition
          key={shortId}
          id={`Short-${shortId}`}
          component={Short}
          calculateMetadata={calculateShortMetadata}
          fps={FPS}
          width={1080}
          height={1920}
          defaultProps={{ episodeNumber: 1, shortId }}
        />
      ))}
      <Composition
        id="SceneGallery"
        component={SceneGallery}
        durationInFrames={SCENE_GALLERY_DURATION}
        fps={FPS}
        width={1920}
        height={1080}
      />
      {VOICE_TEST_SAMPLES.map((sample) => (
        <Composition
          key={sample.id}
          id={sample.id}
          component={VoiceTest}
          durationInFrames={Math.round(sample.seconds * FPS) + 15}
          fps={FPS}
          width={1920}
          height={1080}
          defaultProps={{
            voiceLabel: sample.label,
            voiceSrc: `voice-test/${sample.file}.wav`,
            captionsSrc: `voice-test/${sample.file}.captions.json`,
          }}
        />
      ))}
      <Composition
        id="AudioTest"
        component={AudioTest}
        durationInFrames={AUDIO_TEST_DURATION}
        fps={FPS}
        width={1280}
        height={720}
      />
    </>
  );
};
