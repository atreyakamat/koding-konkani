/**
 * Phase C render queue: EP01 long 4K -> EP01 Shorts -> EP02 -> EP03 -> EP04,
 * strictly one job at a time. Resumable (skips a file that already exists),
 * continues past a failed job rather than aborting the whole queue, masters
 * every file's audio (two-pass loudnorm) before QA-checking it, and lowers
 * concurrency if system memory is tight.
 *
 * Usage: node scripts/render_queue.mts 1 2 3 4
 *        KK_LANG=cpp node scripts/render_queue.mts 1 2 3     (C++ course: episodes-cpp/, audio/voice/cpp-epNNN/, out/cpp-epNNN/)
 */
import { execFileSync, spawnSync } from "node:child_process";
import {
  appendFileSync,
  copyFileSync,
  existsSync,
  mkdirSync,
  statSync,
  unlinkSync,
  writeFileSync,
} from "node:fs";
import { join } from "node:path";
import os from "node:os";
import { epFolder } from "../src/lib/episode.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PYTHON = join(ROOT, ".venv", "Scripts", "python.exe");
const LOG_PATH = join(ROOT, "out", "render-queue.log");

/** Course language: c (default), cpp or python. Picks the episode folder, the narration folder and the output folder. */
const argv = process.argv.slice(2);
const langFlag = argv.indexOf("--lang");
const LANG = langFlag >= 0 ? (argv[langFlag + 1] ?? "") : (process.env.KK_LANG ?? "c");
if (langFlag >= 0) argv.splice(langFlag, 2);
if (!["c", "cpp", "python"].includes(LANG)) {
  console.error(`--lang must be c, cpp or python (got ${LANG})`);
  process.exit(1);
}
const EPISODES_DIRNAME = LANG === "cpp" ? "episodes-cpp" : LANG === "python" ? "episodes-python" : "episodes";
const langProps = LANG === "c" ? {} : { lang: LANG };

const episodeNumbers = argv.map(Number);
if (episodeNumbers.length === 0 || episodeNumbers.some((n) => !Number.isInteger(n) || n < 1)) {
  console.error("usage: node scripts/render_queue.mts [--lang c|cpp] <episode-number...>");
  process.exit(1);
}

// Two Shorts in one episode must never show the same visual (and none may fall back to the
// old generic printf("Hi"); card): fail before spending render time.
if (LANG === "c") {
  try {
    execFileSync(
      process.execPath,
      ["scripts/check_short_visuals.mts", ...episodeNumbers.map(String)],
      { cwd: ROOT, stdio: "inherit" },
    );
  } catch {
    console.error("check_short_visuals failed: duplicate or generic Short visuals. Not rendering.");
    process.exit(1);
  }
} else {
  // Other courses: every scene must have the data it draws (no empty or black scenes). Static, takes seconds.
  try {
    execFileSync(process.execPath, ["scripts/check_render_ready.mts", "--lang", LANG], { cwd: ROOT, stdio: "inherit" });
  } catch {
    console.error("check_render_ready failed: an episode is missing data a scene needs. Not rendering.");
    process.exit(1);
  }
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

/** Black stretches (>= 0.2 s) inside the video, ignoring the first and last 0.3 s. Uses ffmpeg blackdetect on a small copy. */
const blackSegmentsOf = (path: string): { start: number; end: number }[] => {
  const r = spawnSync("ffmpeg", ["-hide_banner", "-i", path, "-vf", "scale=320:-2,blackdetect=d=0.2:pix_th=0.05", "-an", "-f", "null", "-"], {
    encoding: "utf-8",
  });
  const text = `${r.stderr ?? ""}`;
  const dur = Number(text.match(/Duration: (\d+):(\d+):(\d+\.\d+)/)?.slice(1).reduce((a, v, i) => a + Number(v) * [3600, 60, 1][i], 0) ?? 0);
  const out: { start: number; end: number }[] = [];
  for (const m of text.matchAll(/black_start:(\d+(?:\.\d+)?) black_end:(\d+(?:\.\d+)?)/g)) {
    const start = Number(m[1]);
    const end = Number(m[2]);
    if (start < 0.3 && start === 0) continue; // a fade-in from black at the very start is intended
    if (dur > 0 && end >= dur - 0.3) continue; // and a fade-out at the very end
    out.push({ start, end });
  }
  return out;
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

  // A black frame anywhere inside the video (not the first/last fraction of a second) is a failed render.
  const blackSegments = blackSegmentsOf(outPath);
  if (blackSegments.length > 0) {
    ffprobeLine += ` | BLACK at ${blackSegments.slice(0, 3).map((b) => `${b.start.toFixed(1)}s`).join(", ")}`;
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
  const epId = epFolder(LANG, ep);
  const jsonName = `ep${String(ep).padStart(3, "0")}.json`;
  const outDir = join(ROOT, "out", epId);
  mkdirSync(outDir, { recursive: true });
  const rows: QaRow[] = [];

  // The compositions read audio/voice/<ep>/episode.json, a copy taken when narration
  // was generated. Narration is skipped once it exists, so without this refresh any
  // later edit to episodes/<ep>.json (box data, code fields, outputs) never reaches a
  // render — which is exactly how EP07-09 rendered empty memory-boxes scenes on 1 Nov.
  // Only the JSON is refreshed; the audio, cues and captions are untouched.
  const voiceDir = join(ROOT, "audio", "voice", epId);
  if (existsSync(join(voiceDir, ".fake"))) {
    console.error(`${epId}: audio is silent dry-run audio. Run: python scripts/render_episode_audio.py ${ep} --lang ${LANG}`);
    process.exit(1);
  }
  if (!existsSync(join(voiceDir, "manifest.json"))) {
    console.error(`${epId}: no narration yet. Run: python scripts/render_episode_audio.py ${ep} --lang ${LANG}`);
    process.exit(1);
  }
  if (existsSync(voiceDir)) {
    copyFileSync(join(ROOT, EPISODES_DIRNAME, jsonName), join(voiceDir, "episode.json"));
    log(`REFRESH ${epId} episode.json -> audio/voice/${epId}/episode.json`);
  }

  const propsFile = join(outDir, ".props-longvideo.json");
  writeFileSync(propsFile, JSON.stringify({ episodeNumber: ep, ...langProps }), "utf-8");

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
      // Fonts are fetched from Google at render start; a DNS blip inside the default
      // 30 s delayRender window failed every "~37 s" job on 1 Nov. Give it 2 minutes.
      "--timeout=120000",
      `--concurrency=${longConcurrency}`,
    ],
    3840,
    2160,
  );
  const longQa = qaCheck(longOut, 3840, 2160);
  rows.push({ file: `${epId}-4k.mp4`, status: longStatus, ...longQa });

  for (const shortId of ["S1", "S2", "S3", "S4", "S5"]) {
    const shortPropsFile = join(outDir, `.props-short-${shortId}.json`);
    writeFileSync(shortPropsFile, JSON.stringify({ episodeNumber: ep, shortId, ...langProps }), "utf-8");
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
        "--timeout=120000",
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
  const epId = epFolder(LANG, ep);
  for (const r of rows) {
    console.log(`${epId} ${r.file.padEnd(20)} ${r.status.padEnd(8)} ${r.pass ? "PASS" : "FAIL"}`);
  }
}
