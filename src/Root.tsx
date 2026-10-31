import { Composition } from "remotion";
import { LongVideo } from "./compositions/LongVideo";
import { Short } from "./compositions/Short";
import { AudioTest, AUDIO_TEST_DURATION } from "./compositions/AudioTest";
import { SceneGallery, SCENE_GALLERY_DURATION } from "./compositions/SceneGallery";

export const FPS = 30;

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
