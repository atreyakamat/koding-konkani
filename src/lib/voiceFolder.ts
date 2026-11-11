import { epFolder, type Lang } from "./episode";

/** Folder (inside the Remotion public dir, audio/) that holds one episode's generated narration, e.g. "voice/python-ep005". */
export const voiceFolder = (lang: Lang | undefined, ep: number): string => `voice/${epFolder(lang, ep)}`;
