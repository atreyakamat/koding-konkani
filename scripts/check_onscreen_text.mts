/**
 * Fails (exit 1) if any on-screen string — long-video scene props or Short visuals/hook/caption —
 * still carries Markdown (`**`, paired backticks, `# ` headings) after the shared sanitiser.
 *
 * Usage: node scripts/check_onscreen_text.mts [episode-number...]   (default: every episode)
 */
import { readdirSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { scenePropsFor } from "../src/compositions/sceneProps.ts";
import { deriveShortVisuals } from "../src/lib/shortVisual.ts";
import { hasMarkdown, stripMarkdown } from "../src/lib/sanitize.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const dir = join(ROOT, "episodes");
const wanted = process.argv.slice(2).map(Number);
const files = readdirSync(dir)
  .filter((f) => /^ep\d{3}\.json$/.test(f))
  .filter((f) => wanted.length === 0 || wanted.includes(Number(f.slice(2, 5))));

/** Source-code fields keep their characters (a `#include` is not a heading). */
const CODE_KEYS = new Set(["source", "wrongCode", "fixedCode", "code", "lines"]);

const strings = (value: unknown, key = ""): [string, string][] => {
  if (typeof value === "string") return CODE_KEYS.has(key) ? [] : [[key, value]];
  if (Array.isArray(value)) return value.flatMap((v) => strings(v, key));
  if (value && typeof value === "object")
    return Object.entries(value).flatMap(([k, v]) => strings(v, k));
  return [];
};

let failed = 0;
const report = (where: string, text: string): void => {
  failed++;
  console.error(`FAIL ${where}: ${JSON.stringify(text.slice(0, 80))}`);
};

for (const file of files) {
  const ep = JSON.parse(readFileSync(join(dir, file), "utf-8"));
  const id = file.slice(0, 5);
  for (const scene of ep.scenes) {
    const props = scenePropsFor(ep, scene);
    for (const [key, text] of strings(props))
      if (hasMarkdown(text)) report(`${id} scene ${scene.id} ${key}`, text);
    if (scene.template === "terminal")
      for (const l of (props.lines as { text: string }[]) ?? [])
        if (hasMarkdown(l.text)) report(`${id} scene ${scene.id} terminal`, l.text);
  }
  for (const short of ep.shorts) {
    for (const [key, text] of [
      ["hook", short.hook],
      ["onScreen", short.onScreen],
      ["caption", short.caption],
    ] as const)
      if (hasMarkdown(stripMarkdown(text))) report(`${id} ${short.id} ${key}`, text);
  }
  for (const [sid, v] of Object.entries(deriveShortVisuals(ep)))
    for (const [key, text] of strings(v))
      if (hasMarkdown(text)) report(`${id} ${sid} visual ${key}`, text);
}
console.log(
  failed ? `${failed} on-screen string(s) still contain Markdown` : "on-screen text: clean",
);
process.exit(failed ? 1 : 0);
