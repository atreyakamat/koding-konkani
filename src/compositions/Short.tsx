import { AbsoluteFill, Audio, staticFile } from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import type { CourseName, Episode } from "../lib/episode";
import { voiceFolder } from "../lib/voiceFolder";
import { ShortLayout } from "../scenes/ShortLayout";
import { coloursForModule } from "../theme/modules";
import { stripMarkdown } from "../lib/sanitize";
import { deriveShortVisuals } from "../lib/shortVisual";
import type { WordTime } from "../lib/shortFrames";
import { ShortVisualView } from "./ShortVisuals";

const FPS = 30;

export type ShortProps = {
  episodeNumber: number;
  /** Which course: picks the narration folder (default C). */
  course?: CourseName;
  shortId: string;
  episode?: Episode;
  short?: Episode["shorts"][number];
  durationInFrames?: number;
  /** Narration word times (S<n>.captions.json), for visuals that step in sync with the script. */
  words?: WordTime[];
};

export const calculateMetadata: CalculateMetadataFunction<ShortProps> = async ({ props }) => {
  const epId = voiceFolder(props.course, props.episodeNumber);
  const episode: Episode = await fetch(staticFile(`${epId}/episode.json`)).then((r) =>
    r.json(),
  );
  const manifest: { timings: { short?: string; durationSec: number }[] } = await fetch(
    staticFile(`${epId}/manifest.json`),
  ).then((r) => r.json());

  const short = episode.shorts.find((s) => s.id === props.shortId);
  const timing = manifest.timings.find((t) => t.short === props.shortId);
  const durationInFrames = Math.round((timing?.durationSec ?? short?.lengthSec ?? 15) * FPS);

  const captions: { text: string; startMs: number }[] = await fetch(
    staticFile(`${epId}/${props.shortId}.captions.json`),
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
  const epId = voiceFolder(episode.course, episode.ep);
  const visual = deriveShortVisuals(episode)[short.id];

  return (
    <AbsoluteFill style={{ background: colours.bg }}>
      <Audio src={staticFile(`${epId}/${short.id}.wav`)} />
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
