import { Html5Audio, Sequence, staticFile } from "remotion";
import { SFX_VOLUME, type SfxName } from "./sfx-levels";

export type SfxProps = { name: SfxName; at: number; volume?: number };

/** Plays one sound effect starting at frame `at` of the surrounding composition or sequence. */
export const Sfx: React.FC<SfxProps> = ({ name, at, volume }) => (
  <Sequence from={at} layout="none">
    <Html5Audio src={staticFile(`sfx/${name}.wav`)} volume={volume ?? SFX_VOLUME[name]} />
  </Sequence>
);
