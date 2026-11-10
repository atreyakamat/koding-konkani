import { AbsoluteFill } from "remotion";
import type { Episode } from "../lib/episode";
import { coloursForModule } from "../theme/modules";
import { TEMPLATE_COMPONENTS } from "./LongVideo";
import { scenePropsFor } from "./sceneProps";

export type ScenePreviewProps = { episode?: Episode; sceneId?: number };

/** One scene of an episode on its own, at the scene's planned length (`lengthSec`), with no narration, manifest or audio.
 * For stills of scenes whose episode has no generated narration yet (--props carries the whole episode JSON). */
export const ScenePreview: React.FC<ScenePreviewProps> = ({ episode, sceneId }) => {
  const scene = episode?.scenes.find((s) => s.id === sceneId);
  if (!episode || !scene) return null;
  const Component = TEMPLATE_COMPONENTS[scene.template];
  return (
    <AbsoluteFill>
      <Component
        {...scenePropsFor(episode, scene)}
        durationInFrames={Math.round(scene.lengthSec * 30)}
        colours={coloursForModule(episode.module)}
        cues={[]}
      />
    </AbsoluteFill>
  );
};
