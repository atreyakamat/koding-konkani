/**
 * Which course a script works on. Default is the C course (episodes/, audio/voice/).
 * Set KK_COURSE=python for the Python course (episodes-python/, audio/voice-py/).
 */
import { join } from "node:path";

export type Course = "c" | "python";

export const COURSE: Course = process.env.KK_COURSE === "python" ? "python" : "c";

/** Folder with epNNN.json for the selected course. */
export const episodesDir = (root: string): string =>
  join(root, COURSE === "python" ? "episodes-python" : "episodes");

/** Sub-folder of the Remotion public dir (audio/) that holds generated narration. */
export const voiceSubdir: string = COURSE === "python" ? "voice-py" : "voice";

export const episodeJsonPath = (root: string, epId: string): string =>
  join(episodesDir(root), `${epId}.json`);
