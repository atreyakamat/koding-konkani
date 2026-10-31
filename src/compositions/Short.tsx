import { AbsoluteFill, Audio, Sequence, interpolate, staticFile, useCurrentFrame } from "remotion";
import type { CalculateMetadataFunction } from "remotion";
import type { Episode } from "../lib/episode";
import { ShortLayout } from "../scenes/ShortLayout";
import { coloursForModule } from "../theme/modules";
import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { readableOn } from "../theme/contrast";
import { Xecxec } from "../mascot/Xecxec";

const FPS = 30;
const END_CARD_SEC = 2;

export type ShortProps = {
  episodeNumber: number;
  shortId: string;
  episode?: Episode;
  short?: Episode["shorts"][number];
  durationInFrames?: number;
};

export const calculateMetadata: CalculateMetadataFunction<ShortProps> = async ({ props }) => {
  const epId = `ep${String(props.episodeNumber).padStart(3, "0")}`;
  const episode: Episode = await fetch(staticFile(`voice/${epId}/episode.json`)).then((r) => r.json());
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

/** The last 2 seconds of every Short, per docs/shorts-reels.md: FOLLOW / SUBSCRIBE + Full video badge.
 * Mounted inside a Sequence starting at that point, so frame 0 here is the card's own entrance. */
const EndCard: React.FC<{ ep: number }> = ({ ep }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 8], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill style={{ background: palette.ink, opacity, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", gap: 28 }}>
      <Xecxec pose="wave" size={160} />
      <div style={{ fontFamily: fonts.title, fontSize: 56, color: palette.white, textAlign: "center", padding: "0 60px" }}>
        FOLLOW @YOUR_IG_HANDLE
      </div>
      <div style={{ fontFamily: fonts.body, fontWeight: 700, fontSize: 36, color: palette.butter }}>
        SUBSCRIBE: Koding Konkani
      </div>
      <div
        style={{
          marginTop: 12,
          background: palette.tomato,
          border: `${brutal.border}px solid ${palette.ink}`,
          padding: "14px 28px",
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: 32,
          color: readableOn(palette.tomato),
        }}
      >
        Full video: EP {String(ep).padStart(2, "0")}
      </div>
    </AbsoluteFill>
  );
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
      />
      <Sequence from={Math.max(0, durationInFrames - END_CARD_SEC * FPS)} layout="none">
        <EndCard ep={episode.ep} />
      </Sequence>
    </AbsoluteFill>
  );
};
