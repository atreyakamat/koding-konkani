import { AbsoluteFill, Audio, staticFile } from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import type { Episode } from "../lib/episode";
import { ShortLayout } from "../scenes/ShortLayout";
import { Xecxec } from "../mascot/Xecxec";
import { coloursForModule } from "../theme/modules";
import { palette } from "../theme/palette";
import { accentOn } from "../theme/contrast";
import { CodeBlock, Panel } from "../ui";
import { fonts } from "../theme/fonts";
import { analogyFromOnScreen } from "./sceneProps";

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

/** The bug reveal (wrong code + GCC's first error line), for the "copy-paste bug" Short. */
const BugVisual: React.FC<{ episode: Episode }> = ({ episode }) => (
  <div style={{ display: "flex", flexDirection: "column", gap: 16, height: "100%" }}>
    <CodeBlock source={episode.bug.wrong} width={860} fontSize={34} maxVisibleLines={6} />
    <Panel background={palette.darkBlue} borderColor={palette.ink}>
      <div
        style={{
          fontFamily: fonts.code,
          fontSize: 24,
          color: palette.tomato,
          whiteSpace: "pre-wrap",
        }}
      >
        {episode.bug.error.split("\n")[0]}
      </div>
    </Panel>
  </div>
);

/** A code scene's source with its taught line highlighted, for a "what does X mean" Short. */
const CodeVisual: React.FC<{ source: string; highlightLine?: number }> = ({
  source,
  highlightLine,
}) => (
  <CodeBlock
    source={source}
    width={860}
    fontSize={36}
    highlightLine={highlightLine}
    maxVisibleLines={8}
  />
);

/** A big Xecxec close-up for the intro Short — he *is* the hook. */
const XecxecVisual: React.FC = () => (
  <Panel
    background={palette.cream}
    style={{
      width: "100%",
      height: "100%",
      display: "flex",
      alignItems: "center",
      justifyContent: "center",
    }}
  >
    <Xecxec pose="wave" size={440} />
  </Panel>
);

/** The source scene's analogy (same "Title": description onScreen pattern ConceptSlide
 * reads), for a Short whose hook is a concept rather than code. */
const AnalogyVisual: React.FC<{ title: string; body: string; accent: string }> = ({
  title,
  body,
  accent,
}) => (
  <Panel background={palette.cream} style={{ width: "100%", height: "100%" }}>
    <div
      style={{
        fontFamily: fonts.title,
        fontSize: 36,
        color: accentOn(palette.cream, accent),
        marginBottom: 20,
        textTransform: "uppercase",
      }}
    >
      {title}
    </div>
    <div style={{ fontFamily: fonts.body, fontSize: 40, color: palette.ink, lineHeight: 1.4 }}>
      {body}
    </div>
  </Panel>
);

/** Per-Short real visuals (animated code / bug / mascot / diagram), where the Short's
 * source scene has content to show. */
const visualFor = (
  episode: Episode,
  shortId: string,
  accent: string,
): React.ReactNode | undefined => {
  if (shortId === "S1") {
    return <XecxecVisual />;
  }
  if (shortId === "S2") {
    const short = episode.shorts.find((s) => s.id === "S2");
    const sceneId = short?.fromScenes[0];
    const scene = episode.scenes.find((s) => s.id === sceneId);
    const analogy = scene ? analogyFromOnScreen(scene.onScreen) : undefined;
    if (analogy) {
      return <AnalogyVisual title={analogy.title} body={analogy.body} accent={accent} />;
    }
  }
  if (shortId === "S3") {
    return <BugVisual episode={episode} />;
  }
  if (shortId === "S5") {
    const short = episode.shorts.find((s) => s.id === "S5");
    const sceneId = short?.fromScenes[0];
    const scene = episode.scenes.find((s) => s.id === sceneId);
    if (scene?.code) {
      return <CodeVisual source={scene.code.source} highlightLine={4} />;
    }
  }
  return undefined;
};

export const Short: React.FC<ShortProps> = ({ episode, short, durationInFrames }) => {
  if (!episode || !short || !durationInFrames) {
    return null;
  }
  const colours = coloursForModule(episode.module);
  const epId = `ep${String(episode.ep).padStart(3, "0")}`;

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
      >
        {visualFor(episode, short.id, colours.accent)}
      </ShortLayout>
    </AbsoluteFill>
  );
};
