/**
 * Draft review pass (default 720p): for each episode, one job at a time, render the long
 * video at --scale (default 2/3: 1280x720) and the 5 Shorts (720x1280) with fast draft
 * settings, master the audio, then build review aids: blackdetect on the long
 * video, ebur128 loudness for every file, and contact sheets (long: one frame
 * every 10 s, 6 columns; Shorts: one frame every 2.5 s). Nothing is skipped —
 * every draft must reflect the current code. Time per job is logged.
 * <out>/report.md (default out/draft720) is rebuilt after every episode from results.json, so a
 * restart carries earlier episodes' rows forward.
 *
 * Usage: node scripts/draft_queue.mts [episode-number...] [--only=S1,S2] [--no-long] [--no-shorts]
 *   [--scale=0.5] [--out=out/draft540]   (defaults: 2/3 scale, out/draft720; --scale=0.5 is 960x540)
 * (default: episodes 1..19, long + all Shorts; --only implies --no-long and merges into earlier results)
 */
import { execSync } from "node:child_process";
import {
  appendFileSync,
  copyFileSync,
  existsSync,
  mkdirSync,
  readFileSync,
  statSync,
  unlinkSync,
  writeFileSync,
} from "node:fs";
import { join, relative, resolve, sep } from "node:path";
import os from "node:os";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PYTHON = join(ROOT, ".venv", "Scripts", "python.exe");
// Optional --scale=<0..1] and --out=<dir>; defaults are the 720p review pass (out/draft720).
const cliFlag = (name: string): string | undefined =>
  process.argv
    .slice(2)
    .find((a) => a.startsWith(`--${name}=`))
    ?.slice(name.length + 3);
const DRAFT_DIR = cliFlag("out")
  ? resolve(ROOT, cliFlag("out") as string)
  : join(ROOT, "out", "draft720");
const LOG_PATH = join(DRAFT_DIR, "draft-queue.log");
const RESULTS_PATH = join(DRAFT_DIR, "results.json");
const REPORT_PATH = join(DRAFT_DIR, "report.md");

// 2/3 at full float precision: a rounded 0.6667 gives a non-integer frame size
// that Remotion's stitcher rejects (found the hard way on 31 Oct).
const SCALE = cliFlag("scale") ?? "0.6666666666666666";
const scaleNumber = Number(SCALE);
if (!(scaleNumber > 0 && scaleNumber <= 1)) {
  console.error(`--scale must be a number in (0, 1], got "${SCALE}"`);
  process.exit(1);
}
const scaled = (px: number): number => Math.round(px * scaleNumber);
// The stitcher needs whole-pixel frames: 1920x and 1080x must both land on integers.
if (
  Math.abs(1920 * scaleNumber - scaled(1920)) > 1e-6 ||
  Math.abs(1080 * scaleNumber - scaled(1080)) > 1e-6
) {
  console.error(
    `--scale=${SCALE} gives non-integer frame sizes; pick e.g. 0.5 or 0.6666666666666666`,
  );
  process.exit(1);
}
/** Real output sizes at this scale: long 16:9, Shorts 9:16. */
const LONG_W = scaled(1920);
const LONG_H = scaled(1080);
const SHORT_W = scaled(1080);
const SHORT_H = scaled(1920);
const LABEL = `${LONG_H}p`;
const DRAFT_FLAGS = [
  "--codec=h264",
  "--crf=20",
  `--scale=${SCALE}`,
  "--x264-preset=veryfast",
  "--audio-bitrate=192k",
  // Fonts are fetched from Google at render start; a DNS blip inside the default 30 s
  // delayRender window is what failed every "~37 s" job on 1 Nov (ERR_NAME_NOT_RESOLVED
  // for fonts.gstatic.com). Two minutes rides out a short outage.
  "--timeout=120000",
];
const SHORT_IDS = ["S1", "S2", "S3", "S4", "S5"] as const;

const flagArgs = process.argv.slice(2).filter((a) => a.startsWith("--"));
const only =
  flagArgs
    .find((a) => a.startsWith("--only="))
    ?.slice(7)
    .split(",") ?? [];
const skipLong = flagArgs.includes("--no-long") || only.length > 0;
const skipShorts = flagArgs.includes("--no-shorts");
const argEps = process.argv
  .slice(2)
  .filter((a) => !a.startsWith("--"))
  .map(Number);
const episodeNumbers = argEps.length ? argEps : Array.from({ length: 19 }, (_, i) => i + 1);
if (episodeNumbers.some((n) => !Number.isInteger(n) || n < 1)) {
  console.error(
    "usage: node scripts/draft_queue.mts [episode-number...] [--scale=0.5] [--out=out/draft540]",
  );
  process.exit(1);
}

// Two Shorts in one episode must never show the same visual (and none may fall back to the
// old generic printf("Hi"); card): fail before spending render time.
try {
  execSync(`node scripts/check_short_visuals.mts ${episodeNumbers.join(" ")}`, {
    cwd: ROOT,
    stdio: "inherit",
  });
} catch {
  console.error("check_short_visuals failed: duplicate or generic Short visuals. Not rendering.");
  process.exit(1);
}

mkdirSync(DRAFT_DIR, { recursive: true });

const log = (line: string): void => {
  const entry = `${new Date().toISOString()} ${line}`;
  appendFileSync(LOG_PATH, `${entry}\n`, "utf-8");
  console.log(entry);
};

const q = (s: string): string => JSON.stringify(s);
const sh = (cmd: string, capture = false): string =>
  execSync(cmd, {
    cwd: ROOT,
    stdio: capture ? ["ignore", "pipe", "pipe"] : "inherit",
    encoding: "utf-8",
  }) ?? "";

const usedMemGB = (): number => (os.totalmem() - os.freemem()) / 1e9;
const pickConcurrency = (label: string): number => {
  const used = usedMemGB();
  if (used > 12) {
    log(`MEMORY ${label}: ${used.toFixed(1)}GB used, dropping concurrency 2 -> 1`);
    return 1;
  }
  return 2;
};

type FileResult = {
  file: string;
  status: "DONE" | "FAILED";
  seconds: number;
  sizeMB?: number;
  dims?: string;
  lufs?: number;
  tp?: number;
  loudnessPass?: boolean;
  blackFrames?: string[];
  sheet?: string;
  note?: string;
};
type EpisodeResult = { ep: number; long: FileResult; shorts: FileResult[]; finishedAt: string };

const loadResults = (): Record<string, EpisodeResult> =>
  existsSync(RESULTS_PATH)
    ? (JSON.parse(readFileSync(RESULTS_PATH, "utf-8")) as Record<string, EpisodeResult>)
    : {};

const probe = (path: string): { w: number; h: number; duration: number } | null => {
  try {
    const out = sh(
      `ffprobe -v error -select_streams v:0 -show_entries stream=width,height:format=duration -of csv=p=0 ${q(path)}`,
      true,
    );
    const nums = out
      .trim()
      .split(/[\s,]+/)
      .map(Number);
    const [w, h] = nums;
    const duration = nums[nums.length - 1];
    return w && h ? { w, h, duration } : null;
  } catch {
    return null;
  }
};

const measureLoudness = (path: string): { lufs: number; tp: number; pass: boolean } | null => {
  try {
    const out = sh(
      `${q(PYTHON)} -c "import sys; sys.path.insert(0, 'scripts'); from loudness import measure; m = measure(r'${path}', -16, -1.5, 11); print(m['input_i'], m['input_tp'])"`,
      true,
    );
    const [lufs, tp] = out.trim().split(/\s+/).map(Number);
    return { lufs, tp, pass: Math.abs(lufs + 16) <= 1 && tp <= -1.5 };
  } catch {
    return null;
  }
};

const blackDetect = (path: string): string[] => {
  try {
    const out = sh(
      `ffmpeg -hide_banner -i ${q(path)} -vf blackdetect=d=0.03:pic_th=0.98 -an -f null - 2>&1`,
      true,
    );
    return [...out.matchAll(/black_start:([\d.]+) black_end:([\d.]+)/g)].map(
      (m) => `${Number(m[1]).toFixed(2)}s-${Number(m[2]).toFixed(2)}s`,
    );
  } catch {
    return ["blackdetect failed"];
  }
};

const contactSheet = (
  path: string,
  sheetPath: string,
  everySec: number,
  thumbWidth: number,
): boolean => {
  const info = probe(path);
  if (!info) return false;
  const frames = Math.max(1, Math.ceil(info.duration / everySec));
  const rows = Math.max(1, Math.ceil(frames / 6));
  try {
    sh(
      `ffmpeg -hide_banner -loglevel error -y -i ${q(path)} -vf "fps=1/${everySec},scale=${thumbWidth}:-1,tile=6x${rows}" -frames:v 1 ${q(sheetPath)}`,
    );
    return existsSync(sheetPath);
  } catch {
    return false;
  }
};

/** Render -> master (loudnorm, video copied) -> final. Always re-renders: drafts must reflect the current code. */
const renderJob = (
  label: string,
  compositionId: string,
  propsFile: string,
  outPath: string,
  expectW: number,
  expectH: number,
): FileResult => {
  const started = Date.now();
  const file = outPath.split(/[\\/]/).pop()!;
  const rawPath = outPath.replace(/\.mp4$/, ".raw.mp4");
  for (const p of [outPath, rawPath]) if (existsSync(p)) unlinkSync(p);
  const concurrency = pickConcurrency(label);
  try {
    sh(
      `npx remotion render src/index.ts ${compositionId} ${q(rawPath)} --props=${q(propsFile)} ${DRAFT_FLAGS.join(" ")} --concurrency=${concurrency}`,
    );
    sh(
      `${q(PYTHON)} -c "import sys; sys.path.insert(0, 'scripts'); from loudness import master_video; master_video(r'${rawPath}', r'${outPath}', target_tp=-1.7, audio_bitrate='192k')"`,
    );
    unlinkSync(rawPath);
    const seconds = (Date.now() - started) / 1000;
    const info = probe(outPath);
    const dims = info ? `${info.w}x${info.h}` : "unknown";
    const note =
      info && (info.w !== expectW || info.h !== expectH)
        ? `expected ${expectW}x${expectH}`
        : undefined;
    const sizeMB = statSync(outPath).size / 1e6;
    log(
      `DONE  ${label} -> ${file} ${seconds.toFixed(1)}s ${sizeMB.toFixed(1)}MB ${dims}${note ? ` (${note})` : ""}`,
    );
    return { file, status: "DONE", seconds, sizeMB, dims, note };
  } catch (err) {
    const seconds = (Date.now() - started) / 1000;
    const message = err instanceof Error ? err.message.slice(0, 160) : String(err);
    log(`FAILED ${label} -> ${file} ${seconds.toFixed(1)}s error=${JSON.stringify(message)}`);
    return { file, status: "FAILED", seconds, note: message };
  }
};

const fmtSec = (s: number): string =>
  s >= 60
    ? `${Math.floor(s / 60)}m${Math.round(s % 60)
        .toString()
        .padStart(2, "0")}s`
    : `${s.toFixed(0)}s`;
const fmtLoud = (r: FileResult): string =>
  r.lufs === undefined || r.tp === undefined
    ? "—"
    : `${r.lufs.toFixed(1)} LUFS / ${r.tp.toFixed(2)} dBTP ${r.loudnessPass ? "ok" : "FAIL"}`;

const writeReport = (results: Record<string, EpisodeResult>): void => {
  const eps = Object.values(results).sort((a, b) => a.ep - b.ep);
  const lines: string[] = [
    `# ${LABEL} draft review pass — report`,
    "",
    `Last updated ${new Date().toISOString()}. Drafts in ${relative(ROOT, DRAFT_DIR).split(sep).join("/")}/epNNN/ (long: ${LONG_W}x${LONG_H}, Shorts: ${SHORT_W}x${SHORT_H}; crf 20, veryfast, 192k AAC, audio mastered to -16 LUFS / -1.7 dBTP target). Contact sheets next to each file (*.sheet.png).`,
    "",
    "| Episode | Long (time, size) | Black frames | Long loudness | Shorts (time each) | Shorts loudness | Anything odd |",
    "| --- | --- | --- | --- | --- | --- | --- |",
  ];
  for (const r of eps) {
    const odd: string[] = [];
    if (r.long.status === "FAILED") odd.push(`long FAILED: ${r.long.note ?? ""}`);
    if (r.long.note && r.long.status === "DONE") odd.push(`long dims: ${r.long.note}`);
    if (r.long.blackFrames?.length) odd.push(`black frame(s) at ${r.long.blackFrames.join(", ")}`);
    if (r.long.loudnessPass === false) odd.push("long loudness out of spec");
    for (const s of r.shorts) {
      if (s.status === "FAILED") odd.push(`${s.file} FAILED: ${s.note ?? ""}`);
      else if (s.note) odd.push(`${s.file} dims: ${s.note}`);
      if (s.loudnessPass === false) odd.push(`${s.file} loudness out of spec`);
      if (s.sheet === undefined) odd.push(`${s.file} no contact sheet`);
    }
    if (r.long.sheet === undefined && r.long.status === "DONE") odd.push("long: no contact sheet");
    const longCell =
      r.long.status === "DONE"
        ? `${fmtSec(r.long.seconds)}, ${r.long.sizeMB?.toFixed(1)} MB`
        : `FAILED after ${fmtSec(r.long.seconds)}`;
    const black =
      r.long.status !== "DONE"
        ? "—"
        : r.long.blackFrames?.length
          ? `${r.long.blackFrames.length}`
          : "none";
    const shortTimes = r.shorts
      .map((s) => (s.status === "DONE" ? fmtSec(s.seconds) : "FAIL"))
      .join(" / ");
    const shortLoud = r.shorts.every((s) => s.loudnessPass)
      ? "all ok"
      : r.shorts.map((s) => (s.loudnessPass ? "ok" : "FAIL")).join("/");
    lines.push(
      `| ep${String(r.ep).padStart(3, "0")} | ${longCell} | ${black} | ${fmtLoud(r.long)} | ${shortTimes} | ${shortLoud} | ${odd.length ? odd.join("; ") : "—"} |`,
    );
  }
  const total = eps.reduce(
    (acc, r) => acc + r.long.seconds + r.shorts.reduce((a, s) => a + s.seconds, 0),
    0,
  );
  lines.push(
    "",
    `${eps.length} episode(s) in this report; ${fmtSec(total)} of render time in total.`,
    "",
  );
  writeFileSync(REPORT_PATH, lines.join("\n"), "utf-8");
};

const results = loadResults();

for (const ep of episodeNumbers) {
  const epId = `ep${String(ep).padStart(3, "0")}`;
  const outDir = join(DRAFT_DIR, epId);
  mkdirSync(outDir, { recursive: true });
  log(`=== ${epId}: starting ===`);

  const voiceDir = join(ROOT, "audio", "voice", epId);
  if (!existsSync(join(voiceDir, "manifest.json"))) {
    log(`SKIP  ${epId}: no narration in audio/voice/${epId} — run render_episode_audio.py first`);
    continue;
  }
  // Compositions read the voice-dir copy of the episode JSON; keep it current.
  copyFileSync(join(ROOT, "episodes", `${epId}.json`), join(voiceDir, "episode.json"));

  const longProps = join(outDir, ".props-longvideo.json");
  writeFileSync(longProps, JSON.stringify({ episodeNumber: ep }), "utf-8");
  const longOut = join(outDir, `${epId}-${LABEL}.mp4`);
  const prev = results[epId];
  const long: FileResult =
    skipLong && prev
      ? prev.long
      : renderJob(`${epId} long ${LABEL}`, "LongVideo", longProps, longOut, LONG_W, LONG_H);
  if (!(skipLong && prev) && long.status === "DONE") {
    long.blackFrames = blackDetect(longOut);
    const loud = measureLoudness(longOut);
    if (loud) Object.assign(long, { lufs: loud.lufs, tp: loud.tp, loudnessPass: loud.pass });
    const sheet = longOut.replace(/\.mp4$/, ".sheet.png");
    if (contactSheet(longOut, sheet, 10, 320)) long.sheet = sheet;
    log(
      `AIDS  ${epId} long: black=${long.blackFrames.length ? long.blackFrames.join(",") : "none"} loudness=${fmtLoud(long)} sheet=${long.sheet ? "ok" : "FAILED"}`,
    );
  }

  const shorts: FileResult[] = prev ? [...prev.shorts] : [];
  for (const shortId of SHORT_IDS) {
    if (skipShorts || (only.length > 0 && !only.includes(shortId))) continue;
    const props = join(outDir, `.props-short-${shortId}.json`);
    writeFileSync(props, JSON.stringify({ episodeNumber: ep, shortId }), "utf-8");
    const shortOut = join(outDir, `${epId}-${shortId}-${LABEL}.mp4`);
    const result = renderJob(
      `${epId} ${shortId}`,
      `Short-${shortId}`,
      props,
      shortOut,
      SHORT_W,
      SHORT_H,
    );
    if (result.status === "DONE") {
      const loud = measureLoudness(shortOut);
      if (loud) Object.assign(result, { lufs: loud.lufs, tp: loud.tp, loudnessPass: loud.pass });
      const sheet = shortOut.replace(/\.mp4$/, ".sheet.png");
      if (contactSheet(shortOut, sheet, 2.5, 180)) result.sheet = sheet;
    }
    const at = shorts.findIndex((x) => x.file === result.file);
    if (at >= 0) shorts[at] = result;
    else shorts.push(result);
  }

  results[epId] = { ep, long, shorts, finishedAt: new Date().toISOString() };
  writeFileSync(RESULTS_PATH, JSON.stringify(results, null, 2), "utf-8");
  writeReport(results);
  log(`=== ${epId}: done, report updated ===`);
}

log(`=== draft_queue: finished ${episodeNumbers.join(",")} ===`);
