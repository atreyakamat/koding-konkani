import { useCurrentFrame } from "remotion";
import { AbsoluteFill, Audio, staticFile } from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import type { Episode } from "../lib/episode";
import { ShortLayout } from "../scenes/ShortLayout";
import { coloursForModule } from "../theme/modules";
import { palette, brutal } from "../theme/palette";
import { accentOn } from "../theme/contrast";
import { CodeBlock, Panel } from "../ui";
import { fonts } from "../theme/fonts";
import { typewriterChars } from "../lib/motion";
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

/** For a real GCC bug (EP01), the actual `error:` lines (not the "GCC output:" header
 * or the caret-pointer lines). Not every bug compiles, though — EP02's is a wrong
 * mental model, EP03's is a PATH problem — neither has a literal "error:" line, so
 * fall back to the explanation's first few non-empty lines not already shown in the
 * wrong-value panel above (EP03's error text repeats those same path lines first). */
const briefErrorLines = (error: string, wrong: string, isCode: boolean): string => {
  if (isCode) {
    const gccLines = error.split("\n").filter((l) => l.includes("error:"));
    if (gccLines.length > 0) return gccLines.join("\n");
  }
  const wrongLines = new Set(wrong.split("\n").map((l) => l.trim()));
  return error
    .split("\n")
    .filter((l) => l.trim() && !wrongLines.has(l.trim()))
    .slice(0, 3)
    .join("\n");
};

/** The bug reveal: the wrong code/claim/value, then the explanation typing in
 * underneath. A real C snippet reliably has `;`, `{` or `#include`; a wrong mental
 * model or a config value (EP02/EP03) doesn't, and reads better as a text card
 * than C-syntax-highlighted code. */
const BugVisual: React.FC<{ episode: Episode }> = ({ episode }) => {
  const frame = useCurrentFrame();
  const isCode = /[;{]|#include/.test(episode.bug.wrong);
  const errorText = briefErrorLines(episode.bug.error, episode.bug.wrong, isCode);
  const errorChars = typewriterChars(errorText, frame, 24, 1.1);
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, height: "100%" }}>
      {isCode ? (
        <CodeBlock source={episode.bug.wrong} width={860} fontSize={34} maxVisibleLines={6} />
      ) : (
        <Panel background={palette.cream} borderColor={palette.ink}>
          <div
            style={{
              fontFamily: fonts.body,
              fontWeight: 700,
              fontSize: 30,
              lineHeight: 1.4,
              color: palette.ink,
              whiteSpace: "pre-wrap",
            }}
          >
            {episode.bug.wrong}
          </div>
        </Panel>
      )}
      <Panel background={palette.darkBlue} borderColor={palette.ink}>
        <div
          style={{
            fontFamily: isCode ? fonts.code : fonts.body,
            fontWeight: isCode ? 400 : 700,
            fontSize: 22,
            lineHeight: 1.3,
            color: palette.tomato,
            whiteSpace: "pre-wrap",
            minHeight: 60,
          }}
        >
          {errorText.slice(0, errorChars)}
        </div>
      </Panel>
    </div>
  );
};

/** A code scene's source, typing in, with its taught line highlighted once typing reaches it. */
const CodeVisual: React.FC<{ source: string; highlightLine?: number }> = ({
  source,
  highlightLine,
}) => {
  const frame = useCurrentFrame();
  const visibleChars = typewriterChars(source, frame, 10, source.length / 40);
  const typingDone = visibleChars >= source.length;
  return (
    <CodeBlock
      source={source}
      width={860}
      fontSize={36}
      visibleChars={visibleChars}
      highlightLine={typingDone ? highlightLine : undefined}
      maxVisibleLines={8}
    />
  );
};

/** A single line of code typing in — for the intro Short, where the hero is Xecxec
 * (already dancing in ShortLayout's own fixed spot) and the visual slot shows what
 * he's about to teach, not a second copy of him. */
const TypedLineVisual: React.FC<{ line: string }> = ({ line }) => {
  const frame = useCurrentFrame();
  const visibleChars = typewriterChars(line, frame, 14, 0.6);
  return (
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
      <div
        style={{
          fontFamily: fonts.code,
          fontWeight: 700,
          fontSize: 56,
          color: palette.ink,
        }}
      >
        {line.slice(0, visibleChars)}
        <span style={{ opacity: Math.floor(frame / 15) % 2 === 0 ? 1 : 0 }}>|</span>
      </div>
    </Panel>
  );
};

/** The source scene's analogy (same "Title": description onScreen pattern ConceptSlide
 * reads), for a Short whose hook is a concept rather than code. Title sweeps in first,
 * then the body — the "highlight sweep" motion for a Short with no code to type. */
const AnalogyVisual: React.FC<{ title: string; body: string; accent: string }> = ({
  title,
  body,
  accent,
}) => {
  const frame = useCurrentFrame();
  const bodyOpacity = Math.min(1, Math.max(0, (frame - 16) / 10));
  return (
    <Panel background={palette.cream} style={{ width: "100%", height: "100%" }}>
      <div
        style={{
          fontFamily: fonts.title,
          fontSize: 46,
          color: accentOn(palette.cream, accent),
          marginBottom: 24,
          textTransform: "uppercase",
        }}
      >
        {title}
      </div>
      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: 48,
          color: palette.ink,
          lineHeight: 1.4,
          opacity: bodyOpacity,
        }}
      >
        {body}
      </div>
    </Panel>
  );
};

/** Pronunciation card: the written name, an arrow, and how it's actually said — for the
 * "it's pronounced ___" Short, which has no code to show. */
const PronunciationVisual: React.FC<{ accent: string }> = ({ accent }) => {
  const frame = useCurrentFrame();
  const saySweep = Math.min(1, Math.max(0, (frame - 20) / 14));
  return (
    <Panel
      background={palette.cream}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: 24,
      }}
    >
      <div style={{ fontFamily: fonts.code, fontWeight: 700, fontSize: 64, color: palette.ink }}>
        Xecxec
      </div>
      <div
        style={{ fontFamily: fonts.title, fontSize: 40, color: accentOn(palette.cream, accent) }}
      >
        ↓ say it like
      </div>
      <div
        style={{
          fontFamily: fonts.title,
          fontSize: 72,
          color: palette.ink,
          background: accent,
          border: `${brutal.border}px solid ${palette.ink}`,
          padding: "10px 28px",
          clipPath: `inset(0 ${(1 - saySweep) * 100}% 0 0)`,
        }}
      >
        SHECK SHECK
      </div>
    </Panel>
  );
};

/** Per-Short real visuals (animated code / bug / mascot / diagram), where the Short's
 * source scene has content to show. */
const visualFor = (
  episode: Episode,
  shortId: string,
  accent: string,
): React.ReactNode | undefined => {
  if (shortId === "S1") {
    return <TypedLineVisual line='printf("Hi");' />;
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
  if (shortId === "S4") {
    return <PronunciationVisual accent={accent} />;
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
