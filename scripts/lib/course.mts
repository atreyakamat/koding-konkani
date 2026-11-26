/**
 * Which course a script works on. Default is the C course (episodes/).
 * Set KK_LANG=<course> (KK_COURSE also works) to pick another course. Every course has its own
 * episode folder (see COURSE_INFO below). Narration always lives in audio/voice/; the folder name
 * follows epFolder() in src/lib/episode.ts (ep005 for C, cpp-ep005, python-ep005, java-ep005, ...).
 */
import { join } from "node:path";

export const COURSE_KEYS = [
  "c",
  "cpp",
  "python",
  "java",
  "docker",
  "kubernetes",
  "jenkins",
  "sonarqube",
] as const;
export type Course = (typeof COURSE_KEYS)[number];

type CourseInfo = {
  /** Folder under the repo root that holds epNNN.json. */
  folder: string;
  /** Number of episodes in the course. The five new courses are provisional until their plans are approved. */
  episodeCount: number;
  /** Highlighter language used for code panels. */
  codeLang: "c" | "python" | "java" | "yaml" | "shell" | "dockerfile";
  /** Real toolchain the course needs (names as checked by scripts/check_toolchain.mts). */
  tools: readonly string[];
};

export const COURSE_INFO: Record<Course, CourseInfo> = {
  c: { folder: "episodes", episodeCount: 86, codeLang: "c", tools: ["gcc"] },
  cpp: { folder: "episodes-cpp", episodeCount: 90, codeLang: "c", tools: ["g++"] },
  python: { folder: "episodes-python", episodeCount: 90, codeLang: "python", tools: ["python3"] },
  java: { folder: "episodes-java", episodeCount: 90, codeLang: "java", tools: ["javac", "java"] },
  docker: {
    folder: "episodes-docker",
    episodeCount: 80,
    codeLang: "dockerfile",
    tools: ["docker"],
  },
  kubernetes: {
    folder: "episodes-kubernetes",
    episodeCount: 80,
    codeLang: "yaml",
    tools: ["docker", "kubectl"],
  },
  jenkins: { folder: "episodes-jenkins", episodeCount: 60, codeLang: "shell", tools: ["docker"] },
  sonarqube: {
    folder: "episodes-sonarqube",
    episodeCount: 60,
    codeLang: "shell",
    tools: ["docker", "java"],
  },
};

const ENV_COURSE = process.env.KK_LANG ?? process.env.KK_COURSE;
export const COURSE: Course = (COURSE_KEYS as readonly string[]).includes(ENV_COURSE ?? "")
  ? (ENV_COURSE as Course)
  : "c";

/** Folder with epNNN.json for the selected course. */
export const episodesDir = (root: string): string => join(root, COURSE_INFO[COURSE].folder);

/** Sub-folder of the Remotion public dir (audio/) that holds generated narration. */
export const voiceSubdir = "voice";

export const episodeJsonPath = (root: string, epId: string): string =>
  join(episodesDir(root), `${epId}.json`);
