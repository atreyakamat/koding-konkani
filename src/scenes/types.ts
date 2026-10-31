import type { Cue } from "../lib/cues";

export type SceneColours = { bg: string; accent: string };

/** Every scene template shares these: its own length, its colour pair, and optional timing cues. */
export type BaseSceneProps = {
  durationInFrames: number;
  colours: SceneColours;
  cues?: Cue[];
};

export type SceneTemplateName =
  | "TitleCard"
  | "ConceptSlide"
  | "CodeExplain"
  | "MemoryBoxes"
  | "Terminal"
  | "AlgorithmBars"
  | "BugOfTheDay"
  | "PunCard"
  | "Challenge"
  | "Outro"
  | "ShortLayout";
