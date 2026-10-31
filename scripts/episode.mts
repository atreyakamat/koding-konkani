/**
 * Full per-episode pipeline, reusable for all 86 episodes:
 *   1. Narration (scripts/render_episode_audio.py): one WAV + word timestamps
 *      + resolved cues per scene and per Short.
 *   2. GCC check (scripts/check_c.py --episode N): every code sample compiles
 *      and its output matches the episode JSON.
 *   3. Render: LongVideo at 1080p, then 4K (--scale=2), then the 5 Shorts at
 *      1080x1920 — all into out/epNNN/.
 * Logs how long each step took and the real-time ratio (render time / output
 * video length) for the two LongVideo renders, and writes out/epNNN/render-log.json
 * for review.md to read.
 *
 * Usage: npm run episode -- <episode-number>
 *     or: node scripts/episode.mts <episode-number>
 */
import { execFileSync } from "node:child_process";
import { mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PYTHON = join(ROOT, ".venv", "Scripts", "python.exe");

const epNum = Number(process.argv[2]);
if (!Number.isInteger(epNum) || epNum < 1) {
  console.error("usage: npm run episode -- <episode-number>");
  process.exit(1);
}
const epId = `ep${String(epNum).padStart(3, "0")}`;
const outDir = join(ROOT, "out", epId);
mkdirSync(outDir, { recursive: true });
mkdirSync(join(outDir, "shorts"), { recursive: true });

type StepTiming = { step: string; seconds: number };
const timings: StepTiming[] = [];

const timed = <T,>(step: string, fn: () => T): T => {
  console.log(`\n=== ${step} ===`);
  const t0 = Date.now();
  const result = fn();
  const seconds = (Date.now() - t0) / 1000;
  timings.push({ step, seconds: Math.round(seconds * 10) / 10 });
  console.log(`--- ${step}: ${seconds.toFixed(1)}s ---`);
  return result;
};

const run = (cmd: string, args: string[]) => {
  // shell:true because `npx` resolves to npx.cmd on Windows, which Node
  // cannot spawn directly without a shell.
  execFileSync(cmd, args, { cwd: ROOT, stdio: "inherit", shell: true });
};

/** Writes JSON to a temp props file and returns its path — avoids passing
 * inline JSON (quotes, braces) as a shell argument on Windows. */
const propsFile = (name: string, data: unknown): string => {
  const p = join(outDir, `.props-${name}.json`);
  writeFileSync(p, JSON.stringify(data), "utf-8");
  return p;
};

/** Renders to a `.raw.mp4` intermediate, then masters its audio in place (two-pass
 * loudnorm, -c:v copy) to the real output path. A single clip's narration/SFX/music
 * are each normalised on their own, but the combined mix can still peak hotter than
 * any one of them — confirmed on EP01 (-15.86 LUFS / -0.59 dBTP pre-master, docs/reviews/
 * ep001-pilot-review.md). Mastering the final render is what actually guarantees the
 * CLAUDE.md target on the delivered file. */
const renderAndMaster = (renderArgs: string[], outPath: string) => {
  const rawPath = outPath.replace(/\.mp4$/, ".raw.mp4");
  run("npx", [
    "remotion",
    "render",
    "src/index.ts",
    ...renderArgs,
    rawPath,
    "--codec=h264",
    "--crf=18",
    "--concurrency=2",
  ]);
  run(PYTHON, [
    "-c",
    "import sys; sys.path.insert(0, 'scripts'); from loudness import master_video; " +
      `print(master_video(r"${rawPath}", r"${outPath}", target_tp=-1.5))`,
  ]);
  rmSync(rawPath);
};

// 1. Narration
timed("narration", () => run(PYTHON, [join("scripts", "render_episode_audio.py"), String(epNum)]));

// 2. GCC check (never silently skipped — a failing sample should stop the pipeline,
// since CLAUDE.md requires every code sample verified before rendering).
timed("gcc-check", () => run(PYTHON, [join("scripts", "check_c.py"), "--episode", String(epNum)]));
const ccheckReport = readFileSync(join(ROOT, "out", "c-check-report.md"), "utf-8");
const nonPassMatch = ccheckReport.match(/PASS:\s*(\d+)/);
if (!nonPassMatch) {
  console.error("Could not parse out/c-check-report.md; aborting.");
  process.exit(1);
}
if (/## Non-PASS results \((?!0\))/.test(ccheckReport)) {
  console.error(
    `GCC check found non-PASS results for ${epId} — see out/c-check-report.md. Aborting render.`,
  );
  process.exit(1);
}

// Total narration audio length, for the real-time-ratio figures below.
const manifest = JSON.parse(
  readFileSync(join(ROOT, "audio", "voice", epId, "manifest.json"), "utf-8"),
) as { timings: { durationSec: number }[] };
const totalAudioSec = manifest.timings.reduce((sum, t) => sum + t.durationSec, 0);
const longVideoSec = manifest.timings
  .filter((t) => "scene" in t)
  .reduce((sum, t) => sum + t.durationSec, 0);

// 3. Render: LongVideo 1080p, then 4K.
const longVideoPropsFile = propsFile("longvideo", { episodeNumber: epNum });

timed("render-long-1080p", () =>
  renderAndMaster(
    ["LongVideo", `--props=${longVideoPropsFile}`],
    join(outDir, `${epId}-1080p.mp4`),
  ),
);
timed("render-long-4k", () =>
  renderAndMaster(
    ["LongVideo", `--props=${longVideoPropsFile}`, "--scale=2"],
    join(outDir, `${epId}-4k.mp4`),
  ),
);

// 4. Render: the 5 Shorts, 1080x1920.
const shortIds = ["S1", "S2", "S3", "S4", "S5"];
for (const shortId of shortIds) {
  const shortPropsFile = propsFile(`short-${shortId}`, { episodeNumber: epNum, shortId });
  timed(`render-short-${shortId}`, () =>
    renderAndMaster(
      [`Short-${shortId}`, `--props=${shortPropsFile}`],
      join(outDir, "shorts", `${epId}-${shortId}.mp4`),
    ),
  );
}

const render1080 = timings.find((t) => t.step === "render-long-1080p")!;
const realTimeRatio1080 = render1080.seconds / longVideoSec;

const log = {
  ep: epNum,
  longVideoSec: Math.round(longVideoSec * 10) / 10,
  totalAudioSec: Math.round(totalAudioSec * 10) / 10,
  realTimeRatio1080: Math.round(realTimeRatio1080 * 100) / 100,
  timings,
};
writeFileSync(join(outDir, "render-log.json"), JSON.stringify(log, null, 2), "utf-8");

console.log(
  `\nDone. Episode ${epId}: ${longVideoSec.toFixed(1)}s video, 1080p render took ${render1080.seconds.toFixed(1)}s (${realTimeRatio1080.toFixed(2)}x real time).`,
);
console.log(`Log written to out/${epId}/render-log.json`);
