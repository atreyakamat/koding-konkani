/**
 * Validates every episodes/epNNN.json against the zod Episode schema
 * (src/lib/episode.ts). Run after scripts/bible_to_json.py.
 *
 * Usage: node scripts/validate_episodes.ts   (KK_COURSE=python for the Python course)
 */
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { EpisodeSchema, sceneTemplateFromBibleName } from "../src/lib/episode.ts";
import { COURSE, episodesDir } from "./lib/course.mts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const EPISODES_DIR = episodesDir(ROOT);
/** The C course has 86 episodes, the Python and C++ courses 90. */
const EPISODE_COUNT = COURSE === "c" ? 86 : 90;

// Sanity-check the Bible-name -> slug mapping fails loudly on garbage input,
// since bible_to_json.py relies on duplicating this same mapping in Python.
try {
  sceneTemplateFromBibleName("Not a real template");
  console.error("sceneTemplateFromBibleName did not throw on an unknown name");
  process.exit(1);
} catch {
  // expected
}

const files = readdirSync(EPISODES_DIR)
  .filter((f) => /^ep\d{3}\.json$/.test(f))
  .sort();

let failures = 0;
const seenEp = new Set<number>();

for (const file of files) {
  const raw = readFileSync(join(EPISODES_DIR, file), "utf-8");
  let data: unknown;
  try {
    data = JSON.parse(raw);
  } catch (e) {
    console.error(`${file}: invalid JSON: ${(e as Error).message}`);
    failures++;
    continue;
  }

  const result = EpisodeSchema.safeParse(data);
  if (!result.success) {
    failures++;
    console.error(`${file}: FAILED validation`);
    for (const issue of result.error.issues) {
      console.error(`  - ${issue.path.join(".")}: ${issue.message}`);
    }
    continue;
  }

  const ep = result.data.ep;
  if (seenEp.has(ep)) {
    console.error(`${file}: duplicate ep number ${ep}`);
    failures++;
  }
  seenEp.add(ep);

  const expectedFile = `ep${String(ep).padStart(3, "0")}.json`;
  if (file !== expectedFile) {
    console.error(`${file}: ep ${ep} should live in ${expectedFile}`);
    failures++;
  }
}

const missing: number[] = [];
for (let i = 1; i <= EPISODE_COUNT; i++) {
  if (!seenEp.has(i)) missing.push(i);
}
if (missing.length > 0) {
  console.error(`Missing episodes: ${missing.join(", ")}`);
  failures += missing.length;
}

console.log(`Validated ${files.length} files, ${seenEp.size} distinct episodes, ${failures} failures.`);
if (failures > 0) {
  process.exit(1);
}
