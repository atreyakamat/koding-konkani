import { AbsoluteFill, Audio, staticFile } from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import type { Episode } from "../lib/episode";
import { ShortLayout } from "../scenes/ShortLayout";
import { coloursForModule } from "../theme/modules";
import { deriveShortVisuals } from "../lib/shortVisual";
import { ShortVisualView } from "./ShortVisuals";

const FPS = 30;

export type ShortProps = {
  episodeNumber: number;
  shortId: string;
  episode?: Episode;
  short?: Episode["shorts"][number];
  durationInFrames?: number;
};

export const calculateMetadata: CalculateMetadataFunction<ShortProps> = async ({ props }) => {
  const epId = `ep${String(props.episodeNumber).padStart(3, "0")}`;
  const episode: Episode = await fetch(staticFile(`voice/${epId}/episode.json`)).then((r) =>
    r.json(),
  );
  const manifest: { timings: { short?: string; durationSec: number }[] } = await fetch(
    staticFile(`voice/${epId}/manifest.json`),
  ).then((r) => r.json());

  const short = episode.shorts.find((s) => s.id === props.shortId);
  const timing = manifest.timings.find((t) => t.short === props.shortId);
  const durationInFrames = Math.round((timing?.durationSec ?? short?.lengthSec ?? 15) * FPS);

  return {
    durationInFrames,
    props: { ...props, episode, short, durationInFrames },
  };
};

export const Short: React.FC<ShortProps> = ({ episode, short, durationInFrames }) => {
  if (!episode || !short || !durationInFrames) {
    return null;
  }
  const colours = coloursForModule(episode.module);
  const epId = `ep${String(episode.ep).padStart(3, "0")}`;
  const visual = deriveShortVisuals(episode)[short.id];

  return (
    <AbsoluteFill style={{ background: colours.bg }}>
      <Audio src={staticFile(`voice/${epId}/${short.id}.wav`)} />
      <ShortLayout
        ep={episode.ep}
        hook={short.hook}
        visualLabel={short.onScreen}
        caption={short.caption}
        colours={colours}
        durationInFrames={durationInFrames}
        mascotPose={visual?.kind === "pun" ? "snap" : "dance"}
      >
        {visual ? (
          <ShortVisualView
            visual={visual}
            episode={episode}
            accent={colours.accent}
            durationInFrames={durationInFrames}
          />
        ) : undefined}
      </ShortLayout>
    </AbsoluteFill>
  );
};
