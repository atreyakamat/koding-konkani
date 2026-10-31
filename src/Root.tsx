import { Composition } from "remotion";
import { LongVideo } from "./compositions/LongVideo";
import { Short } from "./compositions/Short";
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
        durationInFrames={FPS * 10}
        fps={FPS}
        width={1920}
        height={1080}
        defaultProps={{ ep: 1, title: "Welcome to Koding Konkani", module: 0 }}
      />
      <Composition
        id="Short"
        component={Short}
        durationInFrames={FPS * 10}
        fps={FPS}
        width={1080}
        height={1920}
        defaultProps={{ ep: 1, id: "S1", hook: "A crab will teach you C", module: 0 }}
      />
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
    </>
  );
};
