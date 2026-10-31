/**
 * Full per-episode overnight pipeline: GCC check -> narration -> render
 * (long 4K + 5 Shorts, one job at a time) -> QA, for a range of episodes.
 * An episode whose C samples don't compile/match is logged and skipped
 * (not fatal to the run). Resumable: a render step is skipped only when its
 * output already exists at the expected resolution (not just exists).
 *
 * Usage: node scripts/episode_pipeline.mts <start-ep> <end-ep>
 */
import { execFileSync } from "node:child_process";
import {
  appendFileSync,
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
  unlinkSync,
  writeFileSync,
} from "node:fs";
import { join } from "node:path";
import os from "node:os";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PYTHON = join(ROOT, ".venv", "Scripts", "python.exe");
const LOG_PATH = join(ROOT, "out", "render-queue.log");
const SKIP_LOG_PATH = join(ROOT, "out", "episode-skips.log");

const [startEp, endEp] = process.argv.slice(2).map(Number);
if (!Number.isInteger(startEp) || !Number.isInteger(endEp) || startEp > endEp) {
  console.error("usage: node scripts/episode_pipeline.mts <start-ep> <end-ep>");
  process.exit(1);
}

mkdirSync(join(ROOT, "out"), { recursive: true });

const log = (line: string): void => {
  const entry = `${new Date().toISOString()} ${line}`;
  appendFileSync(LOG_PATH, `${entry}\n`, "utf-8");
  console.log(entry);
};

const logSkip = (ep: number, reason: string): void => {
  const entry = `${new Date().toISOString()} ep${String(ep).padStart(3, "0")} SKIPPED-EPISODE reason="${reason}"`;
  appendFileSync(SKIP_LOG_PATH, `${entry}\n`, "utf-8");
  log(entry);
};

const usedMemGB = (): number => (os.totalmem() - os.freemem()) / 1e9;

const pickConcurrency = (base: number, label: string): number => {
  const used = usedMemGB();
  if (used > 12) {
    const lowered = Math.max(1, Math.floor(base / 2));
    log(`MEMORY ${label}: ${used.toFixed(1)}GB used, dropping concurrency ${base} -> ${lowered}`);
    return lowered;
  }
  return base;
};

const run = (cmd: string, args: string[]): void => {
  execFileSync(cmd, args, { cwd: ROOT, stdio: "inherit", shell: true });
};

const pyEval = (code: string): string =>
  execFileSync(PYTHON, ["-c", code], { cwd: ROOT, encoding: "utf-8" });

const probeDimensions = (path: string): { w: number; h: number } | null => {
  try {
    const raw = execFileSync(
      "ffprobe",
      [
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height",
        "-of",
        "csv=p=0",
        path,
      ],
      { encoding: "utf-8" },
    ).trim();
    const [w, h] = raw.split(",").map(Number);
    return { w, h };
  } catch {
    return null;
  }
};

type JobResult = "SKIPPED" | "DONE" | "FAILED";

const renderJob = (
  label: string,
  compositionId: string,
  outPath: string,
  extraFlags: string[],
  expectW: number,
  expectH: number,
): JobResult => {
  if (existsSync(outPath)) {
    const dims = probeDimensions(outPath);
    if (dims && dims.w === expectW && dims.h === expectH) {
      log(`SKIP  ${label} -> ${outPath} (already exists at ${expectW}x${expectH})`);
      return "SKIPPED";
    }
    log(
      `STALE ${label} -> ${outPath} (existing file is ${dims ? `${dims.w}x${dims.h}` : "unreadable"}, expected ${expectW}x${expectH} — re-rendering)`,
    );
  }
  mkdirSync(join(outPath, ".."), { recursive: true });
  const rawPath = outPath.replace(/\.mp4$/, ".raw.mp4");
  const t0 = Date.now();
  try {
    run("npx", ["remotion", "render", "src/index.ts", compositionId, rawPath, ...extraFlags]);
    pyEval(
      "import sys; sys.path.insert(0, 'scripts'); from loudness import master_video; " +
        `master_video(r"${rawPath}", r"${outPath}", target_tp=-1.5, audio_bitrate="320k")`,
    );
    unlinkSync(rawPath);
    const seconds = (Date.now() - t0) / 1000;
    const mb = statSync(outPath).size / 1e6;
    log(`DONE  ${label} -> ${outPath} ${seconds.toFixed(1)}s ${mb.toFixed(1)}MB`);
    return "DONE";
  } catch (err) {
    const seconds = (Date.now() - t0) / 1000;
    const message = err instanceof Error ? err.message.split("\n")[0] : String(err);
    log(`FAILED ${label} -> ${outPath} ${seconds.toFixed(1)}s error="${message.slice(0, 200)}"`);
    if (existsSync(rawPath)) unlinkSync(rawPath);
    return "FAILED";
  }
};

type QaRow = { file: string; status: JobResult; ffprobe: string; loudness: string; pass: boolean };

const qaCheck = (
  outPath: string,
  expectW: number,
  expectH: number,
): { ffprobe: string; loudness: string; pass: boolean } => {
  if (!existsSync(outPath)) {
    return { ffprobe: "n/a", loudness: "n/a", pass: false };
  }
  let ffprobeLine = "error";
  let pass = true;
  try {
    const raw = execFileSync(
      "ffprobe",
      [
        "-v",
        "error",
        "-select_streams",
        "v:0",
        "-show_entries",
        "stream=width,height,r_frame_rate",
        "-of",
        "csv=p=0",
        outPath,
      ],
      { encoding: "utf-8" },
    ).trim();
    const audioRaw = execFileSync(
      "ffprobe",
      [
        "-v",
        "error",
        "-select_streams",
        "a:0",
        "-show_entries",
        "stream=sample_rate",
        "-of",
        "csv=p=0",
        outPath,
      ],
      { encoding: "utf-8" },
    ).trim();
    const [w, h, fps] = raw.split(",");
    ffprobeLine = `${w}x${h} @ ${fps} fps, ${audioRaw}Hz audio`;
    if (Number(w) !== expectW || Number(h) !== expectH) pass = false;
    if (!fps.startsWith("30")) pass = false;
    if (audioRaw !== "48000") pass = false;
  } catch {
    pass = false;
  }

  let loudnessLine = "error";
  try {
    const result = pyEval(
      "import sys; sys.path.insert(0, 'scripts'); from loudness import measure; " +
        `m = measure(r"${outPath}", -16, -1.5, 11); print(m['input_i'], m['input_tp'])`,
    ).trim();
    const [i, tp] = result.split(" ").map(Number);
    loudnessLine = `${i.toFixed(2)} LUFS, ${tp.toFixed(2)} dBTP`;
    if (Math.abs(i - -16) > 1) pass = false;
    if (tp > -1.5) pass = false;
  } catch {
    pass = false;
  }

  return { ffprobe: ffprobeLine, loudness: loudnessLine, pass };
};

/** GCC-checks one episode. Returns true (proceed) or false (log + skip episode). */
const gccCheckPasses = (ep: number): boolean => {
  try {
    run(PYTHON, [join("scripts", "check_c.py"), "--episode", String(ep)]);
  } catch (err) {
    logSkip(
      ep,
      `check_c.py itself failed to run: ${err instanceof Error ? err.message.slice(0, 150) : String(err)}`,
    );
    return false;
  }
  const report = readFileSync(join(ROOT, "out", "c-check-report.md"), "utf-8");
  if (/## Non-PASS results \((?!0\))/.test(report)) {
    logSkip(ep, "GCC check found non-PASS results — see out/c-check-report.md for this run");
    return false;
  }
  return true;
};

/** Don't start a new episode's job after 05:30 local time (overnight run
 * time-box). Uses local system time, which this machine already reports as
 * IST. The run starts in the evening and crosses midnight, so "past cutoff"
 * must mean specifically the 05:30-11:59 morning window — NOT every hour
 * from 05:00 through 23:59, which would immediately (and wrongly) trip the
 * very first check at e.g. 21:30 (caught live: this exact bug killed the
 * first overnight run before it started EP05). */
const pastCutoff = (): boolean => {
  const now = new Date();
  const h = now.getHours();
  const m = now.getMinutes();
  return (h === 5 && m >= 30) || (h > 5 && h < 12);
};

for (let ep = startEp; ep <= endEp; ep++) {
  if (pastCutoff()) {
    log(`=== TIME-BOX: past 05:30, not starting ep${String(ep).padStart(3, "0")} or later ===`);
    break;
  }
  const epId = `ep${String(ep).padStart(3, "0")}`;
  log(`=== ${epId}: starting ===`);

  if (!gccCheckPasses(ep)) {
    log(`=== ${epId}: SKIPPED (GCC check failed) ===`);
    continue;
  }

  // Narration: skip if already generated (manifest.json present) for a cheap resume.
  const manifestPath = join(ROOT, "audio", "voice", epId, "manifest.json");
  if (!existsSync(manifestPath)) {
    try {
      run(PYTHON, [join("scripts", "render_episode_audio.py"), String(ep)]);
    } catch (err) {
      logSkip(
        ep,
        `narration generation failed: ${err instanceof Error ? err.message.slice(0, 150) : String(err)}`,
      );
      continue;
    }
  } else {
    log(`SKIP  ${epId} narration (manifest.json already exists)`);
  }

  const outDir = join(ROOT, "out", epId);
  mkdirSync(outDir, { recursive: true });
  const rows: QaRow[] = [];

  const propsFile = join(outDir, ".props-longvideo.json");
  writeFileSync(propsFile, JSON.stringify({ episodeNumber: ep }), "utf-8");

  const longConcurrency = pickConcurrency(2, `${epId} long`);
  const longOut = join(outDir, `${epId}-4k.mp4`);
  const longStatus = renderJob(
    `${epId} long 4K`,
    "LongVideo",
    longOut,
    [
      `--props=${propsFile}`,
      "--codec=h264",
      "--crf=18",
      "--scale=2",
      "--x264-preset=medium",
      "--audio-bitrate=320k",
      `--concurrency=${longConcurrency}`,
    ],
    3840,
    2160,
  );
  rows.push({ file: `${epId}-4k.mp4`, status: longStatus, ...qaCheck(longOut, 3840, 2160) });

  for (const shortId of ["S1", "S2", "S3", "S4", "S5"]) {
    const shortPropsFile = join(outDir, `.props-short-${shortId}.json`);
    writeFileSync(shortPropsFile, JSON.stringify({ episodeNumber: ep, shortId }), "utf-8");
    const shortConcurrency = pickConcurrency(2, `${epId} ${shortId}`);
    const shortOut = join(outDir, `${epId}-${shortId}.mp4`);
    const shortStatus = renderJob(
      `${epId} ${shortId}`,
      `Short-${shortId}`,
      shortOut,
      [
        `--props=${shortPropsFile}`,
        "--codec=h264",
        "--crf=18",
        "--x264-preset=medium",
        "--audio-bitrate=320k",
        `--concurrency=${shortConcurrency}`,
      ],
      1080,
      1920,
    );
    rows.push({
      file: `${epId}-${shortId}.mp4`,
      status: shortStatus,
      ...qaCheck(shortOut, 1080, 1920),
    });
  }

  const qaLines = [
    `# QA — ${epId}`,
    "",
    "| File | Status | ffprobe | Loudness | QA |",
    "| --- | --- | --- | --- | --- |",
    ...rows.map(
      (r) =>
        `| ${r.file} | ${r.status} | ${r.ffprobe} | ${r.loudness} | ${r.pass ? "PASS" : "FAIL"} |`,
    ),
  ];
  writeFileSync(join(outDir, "qa.md"), qaLines.join("\n") + "\n", "utf-8");
  log(`=== ${epId}: done, QA written to out/${epId}/qa.md ===`);
}

log(`=== episode_pipeline: finished range ep${startEp}-ep${endEp} ===`);
