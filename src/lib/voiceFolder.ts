import type { CourseName } from "./episode";

/** Folder (inside the Remotion public dir, audio/) that holds one episode's generated narration:
 * "voice/ep005" for the C course, "voice-py/ep005" for the Python course. Both courses number episodes from 1. */
export const voiceFolder = (course: CourseName | undefined, ep: number): string =>
  `${course === "python" ? "voice-py" : "voice"}/ep${String(ep).padStart(3, "0")}`;
