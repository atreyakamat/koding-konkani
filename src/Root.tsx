import { Composition } from "remotion";
import { LongVideo } from "./compositions/LongVideo";
import { Short } from "./compositions/Short";

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
    </>
  );
};
