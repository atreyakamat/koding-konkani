/**
 * Reports which tools each course needs and whether they are on PATH.
 *
 *   node scripts/check_toolchain.mts            # all courses
 *   node scripts/check_toolchain.mts java       # one course (exit 1 if a required tool is missing)
 *
 * Only checks that the tool runs (`<tool> --version`). It does not run any course sample.
 */
import { spawnSync } from "node:child_process";
import { COURSE_INFO, COURSE_KEYS, type Course } from "./lib/course.mts";

const VERSION_ARGS: Record<string, string[]> = {
  gcc: ["--version"],
  "g++": ["--version"],
  python3: ["--version"],
  javac: ["-version"],
  java: ["-version"],
  docker: ["--version"],
  kubectl: ["version", "--client"],
};

const hasTool = (tool: string): { ok: boolean; detail: string } => {
  // java and javac print their version to stderr, so read both streams.
  const run = spawnSync(tool, VERSION_ARGS[tool] ?? ["--version"], {
    encoding: "utf-8",
    timeout: 15000,
  });
  if (run.error || run.status !== 0) return { ok: false, detail: "not found" };
  const text = `${run.stdout}\n${run.stderr}`;
  return {
    ok: true,
    detail:
      text
        .split("\n")
        .find((l) => l.trim() !== "")
        ?.trim() ?? "",
  };
};

const arg = process.argv[2];
if (arg !== undefined && !(COURSE_KEYS as readonly string[]).includes(arg)) {
  console.error(`Unknown course "${arg}". Use one of: ${COURSE_KEYS.join(", ")}`);
  process.exit(2);
}
const courses: readonly Course[] = arg ? [arg as Course] : COURSE_KEYS;
const cache = new Map<string, { ok: boolean; detail: string }>();

let missingForRequested = false;
for (const course of courses) {
  console.log(`== ${course}`);
  for (const tool of COURSE_INFO[course].tools) {
    if (!cache.has(tool)) cache.set(tool, hasTool(tool));
    const r = cache.get(tool)!;
    console.log(`  ${r.ok ? "OK     " : "MISSING"} ${tool}${r.ok ? `  (${r.detail})` : ""}`);
    if (!r.ok && arg) missingForRequested = true;
  }
}
process.exit(missingForRequested ? 1 : 0);
