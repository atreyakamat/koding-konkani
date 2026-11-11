/**
 * Prints, for every episode, the Bug-of-the-Day error excerpt the panel will show (what the real
 * scenePropsFor passes to errorExcerpt), its kind, and flags the ones that are prose-only or empty.
 * With --old=<path to an older errorExcerpt.ts> it also marks the episodes whose excerpt changes.
 * Read-only: reads episodes/*.json and src/lib only.
 * Usage: node scripts/bug_excerpts.mts [--old=../koding-konkani/src/lib/errorExcerpt.ts]
 */
import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { pathToFileURL } from "node:url";
import { stripMarkdown } from "../src/lib/sanitize.ts";
import { bugPanel } from "../src/lib/bugOverrides.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const oldArg = process.argv.find((a) => a.startsWith("--old="))?.slice(6);
const oldFn: ((e: string) => string[]) | undefined = oldArg
  ? (await import(pathToFileURL(resolve(oldArg)).href)).errorExcerpt
  : undefined;

const flagged: string[] = [];
const changed: string[] = [];
for (let n = 1; n <= 86; n++) {
  const ep = JSON.parse(readFileSync(join(ROOT, "episodes", `ep${String(n).padStart(3, "0")}.json`), "utf-8"));
  // The episode's bug, then any bug a scene carries itself (EP10's bonus bug).
  const records = [{ tag: "", bug: ep.bug }, ...(ep.scenes as { id: number; bug?: typeof ep.bug }[]).filter((s) => s.bug).map((s) => ({ tag: ` s${s.id}`, bug: s.bug }))];
  for (const r of records) {
  const error = stripMarkdown(r.bug?.error ?? "");
  const shown = r.bug?.wrong ?? "";
  const { kind, lines } = bugPanel(n, error, stripMarkdown(shown));
  const flag = kind === "prose" || kind === "empty" ? "FLAG" : "";
  const old = oldFn ? JSON.stringify(oldFn(error)) : null;
  const differs = old !== null && old !== JSON.stringify(lines);
  if (flag) flagged.push(`EP${n}`);
  if (differs) changed.push(`EP${n}`);
  console.log(
    `EP${String(n).padStart(2, "0")}${r.tag.padEnd(4)} ${kind.padEnd(10)} ${flag.padEnd(4)} ${differs ? "CHANGED" : "       "} | ${lines.join("  ⏎  ").slice(0, 150)}`,
  );
  if (differs) console.log(`     was: ${old!.slice(0, 150)}`);
  }
}
console.log(`\nflagged (prose-only or empty): ${flagged.join(", ") || "none"}`);
if (oldFn) console.log(`changed vs old: ${changed.length ? changed.join(", ") : "none"}`);
