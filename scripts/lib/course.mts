/**
 * Which course a script works on. Default is the C course (episodes/).
 * Set KK_LANG=python or KK_LANG=cpp (KK_COURSE also works) for the other courses (episodes-python/, episodes-cpp/).
 * Narration always lives in audio/voice/; the folder name follows epFolder() in src/lib/episode.ts
 * (ep005 for C, cpp-ep005, python-ep005).
 */
import { join } from "node:path";

export type Course = "c" | "cpp" | "python";

const ENV_COURSE = process.env.KK_LANG ?? process.env.KK_COURSE; // KK_LANG is the name render_queue.mts uses; KK_COURSE still works
export const COURSE: Course = ENV_COURSE === "python" ? "python" : ENV_COURSE === "cpp" ? "cpp" : "c";

const EPISODE_FOLDERS: Record<Course, string> = { c: "episodes", cpp: "episodes-cpp", python: "episodes-python" };

/** Folder with epNNN.json for the selected course. */
export const episodesDir = (root: string): string => join(root, EPISODE_FOLDERS[COURSE]);

/** Sub-folder of the Remotion public dir (audio/) that holds generated narration. */
export const voiceSubdir = "voice";

export const episodeJsonPath = (root: string, epId: string): string => join(episodesDir(root), `${epId}.json`);
