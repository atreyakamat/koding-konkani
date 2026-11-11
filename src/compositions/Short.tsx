import { AbsoluteFill, Audio, staticFile } from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import { epFolder, type Episode, type Lang } from "../lib/episode";
import { ShortLayout } from "../scenes/ShortLayout";
import { coloursForModule } from "../theme/modules";
import { stripMarkdown } from "../lib/sanitize";
import { deriveShortVisuals } from "../lib/shortVisual";
import type { WordTime } from "../lib/shortFrames";
import { ShortVisualView } from "./ShortVisuals";

const FPS = 30;

export type ShortProps = {
  episodeNumber: number;
  /** Course language; omitted for the C course. Picks the narration folder (see epFolder). */
  lang?: Lang;
  shortId: string;
  episode?: Episode;
  short?: Episode["shorts"][number];
  durationInFrames?: number;
  /** Narration word times (S<n>.captions.json), for visuals that step in sync with the script. */
  words?: WordTime[];
};

export const calculateMetadata: CalculateMetadataFunction<ShortProps> = async ({ props }) => {
  const epId = epFolder(props.lang, props.episodeNumber);
  const episode: Episode = await fetch(staticFile(`voice/${epId}/episode.json`)).then((r) =>
    r.json(),
  );
  const manifest: { timings: { short?: string; durationSec: number }[] } = await fetch(
    staticFile(`voice/${epId}/manifest.json`),
  ).then((r) => r.json());

  const short = episode.shorts.find((s) => s.id === props.shortId);
  const timing = manifest.timings.find((t) => t.short === props.shortId);
  const durationInFrames = Math.round((timing?.durationSec ?? short?.lengthSec ?? 15) * FPS);

  const captions: { text: string; startMs: number }[] = await fetch(
    staticFile(`voice/${epId}/${props.shortId}.captions.json`),
  )
    .then((r) => r.json())
    .catch(() => []);
  const words = captions.map((c) => ({ text: c.text, startMs: c.startMs }));

  return {
    durationInFrames,
    props: { ...props, episode, short, durationInFrames, words },
  };
};

export const Short: React.FC<ShortProps> = ({ episode, short, durationInFrames, words }) => {
  if (!episode || !short || !durationInFrames) {
    return null;
  }
  const colours = coloursForModule(episode.module);
  const epId = epFolder(episode.lang, episode.ep);
  const visual = deriveShortVisuals(episode)[short.id];

  return (
    <AbsoluteFill style={{ background: colours.bg }}>
      <Audio src={staticFile(`voice/${epId}/${short.id}.wav`)} />
      <ShortLayout
        ep={episode.ep}
        hook={stripMarkdown(short.hook)}
        visualLabel={stripMarkdown(short.onScreen)}
        caption={stripMarkdown(short.caption)}
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
            words={words ?? []}
          />
        ) : undefined}
      </ShortLayout>
    </AbsoluteFill>
  );
};
