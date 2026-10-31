import { Composition, registerRoot } from "remotion";
import { AudioTest, AUDIO_TEST_DURATION } from "./compositions/AudioTest";

/** Audio-only entry: no Google Fonts, so it renders offline (CI, sandboxes). npm run test:audio */
registerRoot(() => (
  <Composition
    id="AudioTest"
    component={AudioTest}
    durationInFrames={AUDIO_TEST_DURATION}
    fps={30}
    width={1280}
    height={720}
  />
));
