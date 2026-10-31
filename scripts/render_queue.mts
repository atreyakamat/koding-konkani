/**
 * Phase C render queue: EP01 long 4K -> EP01 Shorts -> EP02 -> EP03 -> EP04,
 * strictly one job at a time. Resumable (skips a file that already exists),
 * continues past a failed job rather than aborting the whole queue, masters
 * every file's audio (two-pass loudnorm) before QA-checking it, and lowers
 * concurrency if system memory is tight.
 *
 * Usage: node scripts/render_queue.mts 1 2 3 4
 */
import { execFileSync } from "node:child_process";
import {
  appendFileSync,
  existsSync,
  mkdirSync,
  statSync,
  unlinkSync,
  writeFileSync,
} from "node:fs";
import { join } from "node:path";
import os from "node:os";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PYTHON = join(ROOT, ".venv", "Scripts", "python.exe");
const LOG_PATH = join(ROOT, "out", "render-queue.log");

const episodeNumbers = process.argv.slice(2).map(Number);
if (episodeNumbers.length === 0 || episodeNumbers.some((n) => !Number.isInteger(n) || n < 1)) {
  console.error("usage: node scripts/render_queue.mts <episode-number...>");
  process.exit(1);
}

mkdirSync(join(ROOT, "out"), { recursive: true });

const log = (line: string): void => {
  const entry = `${new Date().toISOString()} ${line}`;
  appendFileSync(LOG_PATH, `${entry}\n`, "utf-8");
  console.log(entry);
};

const usedMemGB = (): number => (os.totalmem() - os.freemem()) / 1e9;

/** Drops to a lower concurrency when system memory is already tight, per the
 * explicit "lower it if RAM goes above ~13GB" instruction (used, not free). */
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

type JobResult = "SKIPPED" | "DONE" | "FAILED";

/** Dimensions of an existing file's video stream, or null if it can't be read. */
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

/** Renders to a .raw.mp4, masters its audio onto the final path, deletes the raw.
 * Skips only if the final output already exists *and* is at the expected resolution —
 * a same-named file from an earlier, different-resolution pass must not be mistaken
 * for a finished job (caught live: 720x1280 pilot Shorts sitting at the same path the
 * 1080x1920 production Shorts need). */
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
        // -1.7 not -1.5: loudnorm's linear-gain pass has ~0.05dB precision slop on a
        // long, complex multi-layer mix, and -1.5 was landing just over the ceiling
        // on most long-video renders (confirmed across EP04/07/08/09/10) — -1.7
        // reliably clears the actual -1.5 dBTP requirement with margin.
        `master_video(r"${rawPath}", r"${outPath}", target_tp=-1.7, audio_bitrate="320k")`,
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

/** ffprobe dimensions/fps/sample-rate + ebur128-style loudness measurement (reusing
 * loudness.py's two-pass loudnorm measure() — the same tool that masters the file). */
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

const allResults: { ep: number; rows: QaRow[] }[] = [];

for (const ep of episodeNumbers) {
  const epId = `ep${String(ep).padStart(3, "0")}`;
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
  const longQa = qaCheck(longOut, 3840, 2160);
  rows.push({ file: `${epId}-4k.mp4`, status: longStatus, ...longQa });

  for (const shortId of ["S1", "S2", "S3", "S4", "S5"]) {
    const shortPropsFile = join(outDir, `.props-short-${shortId}.json`);
    writeFileSync(shortPropsFile, JSON.stringify({ episodeNumber: ep, shortId }), "utf-8");
    // Lowered from 4 after a live OOM kill mid-queue; 2/2 for both long and
    // Shorts per the owner's explicit instruction following that.
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
    const shortQa = qaCheck(shortOut, 1080, 1920);
    rows.push({ file: `${epId}-${shortId}.mp4`, status: shortStatus, ...shortQa });
  }

  allResults.push({ ep, rows });

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
  log(`QA written: out/${epId}/qa.md`);
}

console.log("\n=== Render queue summary ===");
for (const { ep, rows } of allResults) {
  const epId = `ep${String(ep).padStart(3, "0")}`;
  for (const r of rows) {
    console.log(`${epId} ${r.file.padEnd(20)} ${r.status.padEnd(8)} ${r.pass ? "PASS" : "FAIL"}`);
  }
}
