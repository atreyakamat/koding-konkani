/**
 * One command for the C++ course: checks, narration, render and QA for every episode, in order.
 * Safe to stop and start again: finished work is skipped.
 *
 *   npm run cpp:all                      all 90 episodes
 *   npm run cpp:all -- 5 12              episodes 5 to 12
 *   npm run cpp:all -- --4k              force 4K (default is 1080p on a PC with less than 20 GB RAM)
 *   npm run cpp:all -- --check           run the checks only, render nothing
 *
 * Order for each run: system check -> episode data check -> for each episode: narration (only if
 * missing, silent dry-run audio, or made at a different pace) -> render_queue (long video, 5 Shorts,
 * QA with black-frame check). One episode at a time. A failed episode is logged and the run goes on
 * with the next one; the report at the end lists every failure and the exit code is 1.
 * Output goes to out/ only. Report: out/render-all-report.md
 */
import { spawnSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import os from "node:os";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PYTHON = join(ROOT, ".venv", "Scripts", "python.exe");
const OUT = join(ROOT, "out");
const REPORT = join(OUT, "render-all-report.md");

const args = process.argv.slice(2);
const flag = (name: string): boolean => {
  const i = args.indexOf(name);
  if (i >= 0) args.splice(i, 1);
  return i >= 0;
};
const force4k = flag("--4k");
const checkOnly = flag("--check");
const numbers = args.map(Number);
if (numbers.some((n) => !Number.isInteger(n) || n < 1 || n > 90) || numbers.length > 2) {
  console.error("usage: npm run cpp:all -- [from [to]] [--4k] [--check]   (episodes 1 to 90)");
  process.exit(1);
}
const from = numbers[0] ?? 1;
const to = numbers[1] ?? (numbers.length === 1 ? from : 90);

const totalGb = os.totalmem() / 1e9;
const hd = !force4k && totalGb < 20;
console.log(
  `RAM ${totalGb.toFixed(1)} GB: rendering long videos at ${hd ? "1080p (less than 20 GB RAM; use --4k to force 4K)" : "4K"}.`,
);

const runNode = (script: string, scriptArgs: string[]): boolean =>
  spawnSync(process.execPath, [script, ...scriptArgs], { cwd: ROOT, stdio: "inherit" }).status ===
  0;
const runPython = (script: string, scriptArgs: string[]): boolean =>
  spawnSync(PYTHON, [script, ...scriptArgs], { cwd: ROOT, stdio: "inherit" }).status === 0;

console.log("\n== 1. System check ==");
if (!runNode("scripts/check_system.mts", [])) {
  console.error("\nSystem check failed. Fix the lines marked FAIL, then run this command again.");
  process.exit(1);
}
console.log("\n== 2. Episode data check ==");
if (!runNode("scripts/check_render_ready.mts", ["--lang", "cpp"])) {
  console.error("\nEpisode data check failed. Do not render. Send the problem lines to Claude.");
  process.exit(1);
}
if (checkOnly) {
  console.log("\nChecks passed. Nothing was rendered (--check).");
  process.exit(0);
}

const currentPace = (): string => {
  const cfg = JSON.parse(readFileSync(join(ROOT, "config", "voice.json"), "utf-8")) as {
    pacing: { lengthScale: number };
    pacingOverrides?: { cpp?: { lengthScale?: number } };
  };
  return String(cfg.pacingOverrides?.cpp?.lengthScale ?? cfg.pacing.lengthScale);
};

const needsNarration = (voiceDir: string): string | null => {
  if (!existsSync(join(voiceDir, "manifest.json"))) return "no narration yet";
  if (existsSync(join(voiceDir, ".fake"))) return "silent dry-run audio";
  const marker = join(voiceDir, ".pace");
  if (!existsSync(marker)) return "narration made before pace tracking";
  if (readFileSync(marker, "utf-8").trim() !== currentPace())
    return "narration made at a different pace";
  return null;
};

type Result = { ep: number; status: "ok" | "failed"; note: string; seconds: number };
const results: Result[] = [];
mkdirSync(OUT, { recursive: true });

const writeReport = (): void => {
  const failed = results.filter((r) => r.status === "failed");
  const lines = [
    `# C++ render-all report`,
    ``,
    `${results.length} episodes run, ${results.length - failed.length} ok, ${failed.length} failed. Long video: ${hd ? "1080p" : "4K"}.`,
    ``,
    `| Episode | Result | Minutes | Note |`,
    `| --- | --- | --- | --- |`,
    ...results.map((r) => `| ${r.ep} | ${r.status} | ${(r.seconds / 60).toFixed(1)} | ${r.note} |`),
    ``,
    failed.length
      ? `Run the same command again to retry only what is missing. Details: out/render-queue.log`
      : `All done.`,
  ];
  writeFileSync(REPORT, lines.join("\n"), "utf-8");
};

for (let ep = from; ep <= to; ep++) {
  const started = Date.now();
  const id = `cpp-ep${String(ep).padStart(3, "0")}`;
  console.log(`\n== EP ${ep} of ${to} (${id}) ==`);
  const why = needsNarration(join(ROOT, "audio", "voice", id));
  let ok = true;
  let note = "";
  if (why) {
    console.log(`Narration: ${why}. Generating real narration...`);
    ok = runPython("scripts/render_episode_audio.py", [String(ep), "--lang", "cpp"]);
    if (!ok) note = "narration failed";
  }
  if (ok) {
    ok = runNode("scripts/render_queue.mts", [
      "--lang",
      "cpp",
      ...(hd ? ["--1080"] : []),
      String(ep),
    ]);
    if (!ok) note = "render or QA failed (see out/render-queue.log)";
  }
  results.push({
    ep,
    status: ok ? "ok" : "failed",
    note: ok ? (why ?? "") : note,
    seconds: (Date.now() - started) / 1000,
  });
  writeReport();
}

const failed = results.filter((r) => r.status === "failed");
console.log(
  `\n== Done: ${results.length - failed.length} ok, ${failed.length} failed. Report: ${REPORT} ==`,
);
process.exit(failed.length ? 1 : 0);
