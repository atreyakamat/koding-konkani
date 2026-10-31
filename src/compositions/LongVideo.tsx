import { Fragment } from "react";
import { AbsoluteFill, Sequence, staticFile, Audio } from "remotion";
import { TransitionSeries, linearTiming } from "@remotion/transitions";
import type { CalculateMetadataFunction } from "remotion";
import type { Episode, Scene, SceneTemplate } from "../lib/episode";
import type { Cue } from "../lib/cues";
import {
  resolveTransition,
  presentationForTransition,
  sfxForTransition,
  TRANSITION_FRAMES,
  type TransitionName,
} from "../transitions";
import { scenePropsFor } from "./sceneProps";
import {
  TitleCard,
  ConceptSlide,
  CodeExplain,
  MemoryBoxes,
  Terminal,
  AlgorithmBars,
  BugOfTheDay,
  PunCard,
  Challenge,
  Outro,
} from "../scenes";
import { MusicBed, Sfx } from "../audio";
import type { SfxName } from "../audio/sfx-levels";
import { SpeedTip } from "../ui/SpeedTip";
import { coloursForModule } from "../theme/modules";
import { LongVideoCaptions } from "./LongVideoCaptions";

const FPS = 30;
const msToFrame = (ms: number): number => Math.round((ms / 1000) * FPS);

type ResolvedCue = { type: "HL" | "TRACK"; raw: string; atMs: number };

export type SceneTiming = {
  scene: Scene;
  startFrame: number;
  durationInFrames: number;
  transitionIn: TransitionName | null;
  cues: Cue[];
  wavPath: string;
};

export type LongVideoProps = {
  episodeNumber: number;
  episode?: Episode;
  sceneTimings?: SceneTiming[];
};

const TEMPLATE_COMPONENTS: Record<SceneTemplate, React.FC<Record<string, unknown>>> = {
  "title-card": TitleCard as React.FC<Record<string, unknown>>,
  "concept-slide": ConceptSlide as React.FC<Record<string, unknown>>,
  "code-explain": CodeExplain as React.FC<Record<string, unknown>>,
  "memory-boxes": MemoryBoxes as React.FC<Record<string, unknown>>,
  terminal: Terminal as React.FC<Record<string, unknown>>,
  "algorithm-bars": AlgorithmBars as React.FC<Record<string, unknown>>,
  "bug-of-the-day": BugOfTheDay as React.FC<Record<string, unknown>>,
  "pun-card": PunCard as React.FC<Record<string, unknown>>,
  challenge: Challenge as React.FC<Record<string, unknown>>,
  outro: Outro as React.FC<Record<string, unknown>>,
};

const cueFromResolved = (r: ResolvedCue): Cue => {
  const frame = msToFrame(r.atMs);
  if (r.type === "HL") {
    return { type: "hl", line: Number(r.raw) || 0, frame };
  }
  const [name, value] = r.raw.split("=");
  return { type: "track", name: name ?? r.raw, value: value ?? "", frame };
};

export const calculateMetadata: CalculateMetadataFunction<LongVideoProps> = async ({ props }) => {
  const epId = `ep${String(props.episodeNumber).padStart(3, "0")}`;
  const episode: Episode = await fetch(staticFile(`voice/${epId}/episode.json`)).then((r) => r.json());
  const manifest: { timings: { scene?: number; durationSec: number }[] } = await fetch(
    staticFile(`voice/${epId}/manifest.json`),
  ).then((r) => r.json());

  let frame = 0;
  let previousName: TransitionName | null = null;
  let slideGoesLeft = true;
  let previousTemplate: SceneTemplate | null = null;

  const sceneTimings: SceneTiming[] = [];

  for (const scene of episode.scenes) {
    const timing = manifest.timings.find((t) => t.scene === scene.id);
    const durationInFrames = Math.round((timing?.durationSec ?? scene.lengthSec) * FPS);

    let transitionIn: TransitionName | null = null;
    if (previousTemplate) {
      const resolved = resolveTransition(previousTemplate, scene.template, {
        isColdOpen: previousTemplate === null,
        previousName,
        slideGoesLeft,
      });
      transitionIn = resolved.name;
      previousName = resolved.name;
      slideGoesLeft = resolved.nextSlideGoesLeft;
      frame -= TRANSITION_FRAMES; // TransitionSeries overlaps consecutive sequences by this much.
    }

    const resolvedCues: ResolvedCue[] = await fetch(staticFile(`voice/${epId}/scene${scene.id}.cues.json`))
      .then((r) => r.json())
      .catch(() => []);

    sceneTimings.push({
      scene,
      startFrame: Math.max(0, frame),
      durationInFrames,
      transitionIn,
      cues: resolvedCues.map(cueFromResolved),
      wavPath: `voice/${epId}/scene${scene.id}.wav`,
    });

    frame += durationInFrames;
    previousTemplate = scene.template;
  }

  return {
    durationInFrames: frame,
    props: { ...props, episode, sceneTimings },
  };
};

/** Spreads a scene's sfx names across its duration: first near the entrance, the rest evenly after. */
const sfxSpread = (names: string[], durationInFrames: number): { name: SfxName; at: number }[] =>
  names.map((name, i) => ({
    name: name as SfxName,
    at: Math.round((i === 0 ? 0.1 : (i + 0.3) / names.length) * durationInFrames),
  }));

export const LongVideo: React.FC<LongVideoProps> = ({ episode, sceneTimings }) => {
  if (!episode || !sceneTimings) {
    return null;
  }
  const epId = `ep${String(episode.ep).padStart(3, "0")}`;

  const bugTiming = sceneTimings.find((t) => t.scene.template === "bug-of-the-day");
  const titleTiming = sceneTimings.find((t) => t.scene.template === "title-card");

  const duckRanges = sceneTimings
    .filter((t) => t.scene.template !== "bug-of-the-day")
    .map((t) => ({ from: t.startFrame, to: t.startFrame + t.durationInFrames }));
  const silenceRanges = bugTiming
    ? [{ from: bugTiming.startFrame, to: bugTiming.startFrame + bugTiming.durationInFrames }]
    : [];

  return (
    <AbsoluteFill style={{ background: "black" }}>
      <TransitionSeries>
        {sceneTimings.map((timing, index) => {
          const { scene } = timing;
          const Component = TEMPLATE_COMPONENTS[scene.template];
          const colours = coloursForModule(episode.module);
          const sceneProps = scenePropsFor(episode, scene);

          return (
            <Fragment key={scene.id}>
              {index > 0 && timing.transitionIn ? (
                <TransitionSeries.Transition
                  presentation={presentationForTransition(timing.transitionIn)}
                  timing={linearTiming({ durationInFrames: TRANSITION_FRAMES })}
                />
              ) : null}
              <TransitionSeries.Sequence durationInFrames={timing.durationInFrames}>
                <AbsoluteFill>
                  <Audio src={staticFile(timing.wavPath)} />
                  {index > 0 && timing.transitionIn ? (
                    // SFX lands on the cut: fires right as this scene's sequence mounts.
                    <Sfx name={sfxForTransition(timing.transitionIn)} at={0} />
                  ) : null}
                  {sfxSpread(scene.sfx, timing.durationInFrames).map(({ name, at }) => (
                    <Sfx key={`${scene.id}-${name}-${at}`} name={name} at={at} />
                  ))}
                  <Component
                    {...sceneProps}
                    durationInFrames={timing.durationInFrames}
                    colours={colours}
                    cues={timing.cues}
                  />
                </AbsoluteFill>
              </TransitionSeries.Sequence>
            </Fragment>
          );
        })}
      </TransitionSeries>

      <MusicBed duckRanges={duckRanges} silenceRanges={silenceRanges} />

      {/* 3s channel sting on the title card. */}
      {titleTiming ? (
        <Sequence from={titleTiming.startFrame} durationInFrames={90} layout="none">
          <Sfx name="sting" at={0} volume={0.7} />
        </Sequence>
      ) : null}

      <Sequence durationInFrames={90} layout="none">
        <SpeedTip />
      </Sequence>

      <LongVideoCaptions epId={epId} sceneTimings={sceneTimings} />
    </AbsoluteFill>
  );
};
