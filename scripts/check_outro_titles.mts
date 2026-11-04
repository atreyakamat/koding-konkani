/**
 * Prints, for every episode, the Bible's outro line and what the Outro scene is given
 * (next episode number and title, via the real scenePropsFor). Exits 1 if any episode has no title,
 * or if the number named in the outro line differs from the number passed on.
 * Usage: node scripts/check_outro_titles.mts [from] [to]   (default 1 86)
 */
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { scenePropsFor } from "../src/compositions/sceneProps.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const from = Number(process.argv[2] ?? 1);
const to = Number(process.argv[3] ?? 86);
let bad = 0;
for (let n = from; n <= to; n++) {
  const episode = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  const scene = episode.scenes.find((s: { template: string }) => s.template === "outro");
  const props = scenePropsFor(episode, scene) as { nextEp: number; nextTitle?: string };
  const named = /next:?\s*(?:Module[^,]*,\s*)?EP\s*(\d+)/i.exec(scene.onScreen)?.[1];
  const last = n === 86;
  const problem = last
    ? props.nextTitle !== undefined
      ? "finale should have no next title"
      : ""
    : !props.nextTitle
      ? "NO TITLE"
      : named && Number(named) !== props.nextEp
        ? `outro names EP ${named}`
        : "";
  if (problem) bad++;
  const shown = last ? "(finale: thank-you card)" : `EP ${props.nextEp} · ${props.nextTitle}`;
  console.log(`EP${String(n).padStart(2, "0")} | ${scene.onScreen.slice(0, 62).padEnd(62)} | ${shown}${problem ? `   <-- ${problem}` : ""}`);
}
console.log(bad ? `${bad} problem(s)` : `all ${to - from + 1} outros show a title`);
process.exit(bad ? 1 : 0);
