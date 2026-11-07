/**
 * Full per-episode overnight pipeline: GCC check -> narration -> render
 * (long 4K + 5 Shorts, one job at a time) -> QA, for a range of episodes.
 * An episode whose C samples don't compile/match is logged and skipped
 * (not fatal to the run) — but 2 episode failures in a row (GCC check,
 * narration, or any QA/render failure of the episode) stop the whole run
 * deliberately (exit code 2, distinct from a crash) rather than silently
 * working through what might be a systemic problem. Resumable: a render step
 * is skipped only when its output already exists at the expected resolution.
 *
 * 4K re-render mode (this run): right before an episode renders, its old
 * out/epNNN folder is MOVED (never deleted) to out/old4k/epNNN, guarded by a
 * marker file so a restart after a crash never moves fresh files over old ones.
 * One render at a time is enforced by a process gate (waits while an ffmpeg, or
 * a node process whose command line mentions remotion/render/episode_pipeline/
 * draft_queue, is running). Per episode: blackdetect on the long video, loudness
 * of every file, contact sheets, verdict PASS / WARN / FAIL, qa.json + qa.md,
 * and out/morning-report.md rebuilt from disk after every episode.
 *
 * Usage: node scripts/episode_pipeline.mts <start-ep> <end-ep> [--no-timebox]
 */
import { sceneProblems } from "./check_scenes.mts";
import { execFileSync, spawnSync } from "node:child_process";
import {
  appendFileSync,
  existsSync,
  mkdirSync,
  readFileSync,
  renameSync,
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
const OLD_DIR = join(ROOT, "out", "old4k");
const REPORT_PATH = join(ROOT, "out", "morning-report.md");
const REPORT_TITLE = "# 4K re-render EP01-EP19 — morning report";
/** Names this re-render run; the per-episode marker file is `.rerender-4k-<tag>`. */
const RERENDER_TAG = "2026-11-03";
const EPISODE_MARKER = `.rerender-4k-${RERENDER_TAG}`;

/** Verdict thresholds (owner's decision, 3 Nov 2026). */
const LUFS_TARGET = -16;
const LUFS_TOLERANCE = 1;
const TP_FAIL_ABOVE = -1.0;
const TP_WARN_ABOVE = -1.5;

const args = process.argv.slice(2);
const noTimebox = args.includes("--no-timebox");
const [startEp, endEp] = args.filter((a) => a !== "--no-timebox").map(Number);
if (!Number.isInteger(startEp) || !Number.isInteger(endEp) || startEp > endEp) {
  console.error("usage: node scripts/episode_pipeline.mts <start-ep> <end-ep> [--no-timebox]");
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

const sleepSync = (ms: number): void => {
  Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, ms);
};

/** Other render work on this machine: any ffmpeg, or a node whose command line mentions
 * remotion / render / episode_pipeline / draft_queue. Our own process is excluded; idle tooling
 * node processes (editor/plugin servers) do not match, so they never block the queue. */
const rivalRenders = (): string[] => {
  const filter = "Name='node.exe' OR Name='ffmpeg.exe'";
  const ps =
    `Get-CimInstance Win32_Process -Filter "${filter}" | ` +
    "Select-Object ProcessId,Name,CommandLine | ConvertTo-Json -Compress";
  let raw = "";
  try {
    raw = execFileSync("powershell", ["-NoProfile", "-Command", ps], { encoding: "utf-8" }).trim();
  } catch {
    return [];
  }
  if (!raw) return [];
  const parsed: unknown = JSON.parse(raw);
  const list = (Array.isArray(parsed) ? parsed : [parsed]) as {
    ProcessId: number;
    Name: string;
    CommandLine: string | null;
  }[];
  const renderish = /remotion|render|episode_pipeline|draft_queue/i;
  return list
    .filter((p) => p.ProcessId !== process.pid)
    .filter((p) => p.Name.toLowerCase() === "ffmpeg.exe" || renderish.test(p.CommandLine ?? ""))
    .map((p) => `${p.Name}#${p.ProcessId}`);
};

/** Blocks until no other render process is running (never start a second render). */
const waitForQuietMachine = (label: string): void => {
  let waited = 0;
  for (;;) {
    const rivals = rivalRenders();
    if (rivals.length === 0) return;
    if (waited % 10 === 0)
      log(`GATE  ${label}: waiting, another render is running (${rivals.join(", ")})`);
    waited++;
    sleepSync(30_000);
  }
};

const epName = (ep: number): string => `ep${String(ep).padStart(3, "0")}`;

/** One-time per run: park the previous run's report + skip log in out/old4k (moved, not deleted). */
const initRun = (): void => {
  mkdirSync(OLD_DIR, { recursive: true });
  const marker = join(OLD_DIR, `.run-init-${RERENDER_TAG}`);
  if (existsSync(marker)) return;
  for (const [from, name] of [
    [REPORT_PATH, "morning-report.md"],
    [SKIP_LOG_PATH, "episode-skips.log"],
  ] as const) {
    if (existsSync(from) && !existsSync(join(OLD_DIR, name))) {
      renameSync(from, join(OLD_DIR, name));
      log(`MOVED ${from} -> ${join(OLD_DIR, name)}`);
    }
  }
  writeFileSync(marker, new Date().toISOString(), "utf-8");
};

/** Moves this episode's old out/epNNN to out/old4k/epNNN, once. The marker file in the NEW
 * folder records that the move happened, so a restart never moves fresh renders over old ones. */
const archiveOldEpisode = (ep: number): void => {
  const outDir = join(ROOT, "out", epName(ep));
  const marker = join(outDir, EPISODE_MARKER);
  if (existsSync(marker)) return;
  if (existsSync(outDir)) {
    const target = join(OLD_DIR, epName(ep));
    if (existsSync(target)) {
      throw new Error(
        `${target} already exists; refusing to overwrite old files. Resolve by hand.`,
      );
    }
    renameSync(outDir, target);
    log(`MOVED ${outDir} -> ${target}`);
  }
  mkdirSync(outDir, { recursive: true });
  writeFileSync(marker, new Date().toISOString(), "utf-8");
};

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
type JobOutcome = { result: JobResult; seconds: number | null };

const renderJob = (
  label: string,
  compositionId: string,
  outPath: string,
  extraFlags: string[],
  expectW: number,
  expectH: number,
): JobOutcome => {
  if (existsSync(outPath)) {
    const dims = probeDimensions(outPath);
    if (dims && dims.w === expectW && dims.h === expectH) {
      log(`SKIP  ${label} -> ${outPath} (already exists at ${expectW}x${expectH})`);
      return { result: "SKIPPED", seconds: null };
    }
    log(
      `STALE ${label} -> ${outPath} (existing file is ${dims ? `${dims.w}x${dims.h}` : "unreadable"}, expected ${expectW}x${expectH} — re-rendering)`,
    );
  }
  waitForQuietMachine(label);
  mkdirSync(join(outPath, ".."), { recursive: true });
  const rawPath = outPath.replace(/\.mp4$/, ".raw.mp4");
  const t0 = Date.now();
  try {
    run("npx", ["remotion", "render", "src/index.ts", compositionId, rawPath, ...extraFlags]);
    pyEval(
      "import sys; sys.path.insert(0, 'scripts'); from loudness import master_video; " +
        // -1.7 not -1.5: loudnorm's linear-gain pass has ~0.05dB precision slop on a
        // long, complex multi-layer mix, and -1.5 was landing just over the ceiling
        // on most long-video renders (confirmed across EP04/07/08/09/10 tonight) —
        // -1.7 reliably clears the actual -1.5 dBTP requirement with margin.
        `master_video(r"${rawPath}", r"${outPath}", target_tp=-1.7, audio_bitrate="320k")`,
    );
    unlinkSync(rawPath);
    const seconds = (Date.now() - t0) / 1000;
    const mb = statSync(outPath).size / 1e6;
    log(`DONE  ${label} -> ${outPath} ${seconds.toFixed(1)}s ${mb.toFixed(1)}MB`);
    return { result: "DONE", seconds };
  } catch (err) {
    const seconds = (Date.now() - t0) / 1000;
    const message = err instanceof Error ? err.message.split("\n")[0] : String(err);
    log(`FAILED ${label} -> ${outPath} ${seconds.toFixed(1)}s error="${message.slice(0, 200)}"`);
    if (existsSync(rawPath)) unlinkSync(rawPath);
    return { result: "FAILED", seconds };
  }
};

type Verdict = "PASS" | "WARN" | "FAIL";

type FileQa = {
  file: string;
  status: JobResult;
  seconds: number | null;
  mb: number | null;
  ffprobe: string;
  lufs: number | null;
  tp: number | null;
  /** Black-frame intervals (long video only); null = not checked. */
  black: string[] | null;
  verdict: Verdict;
  notes: string[];
};

const blackDetect = (path: string): string[] | null => {
  // Scaled down first: black frames are black at any size, and this is far faster at 4K.
  const r = spawnSync(
    "ffmpeg",
    [
      "-hide_banner",
      "-i",
      path,
      "-vf",
      "scale=480:-2,blackdetect=d=0.03:pic_th=0.98",
      "-an",
      "-f",
      "null",
      "-",
    ],
    { encoding: "utf-8", maxBuffer: 64 * 1024 * 1024 },
  );
  if (r.status !== 0) return null;
  return [...r.stderr.matchAll(/black_start:([\d.]+) black_end:([\d.]+)/g)].map(
    (m) => `${Number(m[1]).toFixed(2)}s-${Number(m[2]).toFixed(2)}s`,
  );
};

const contactSheet = (path: string, sheetPath: string, everySec: number, width: number): void => {
  try {
    const dur = Number(
      execFileSync(
        "ffprobe",
        ["-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path],
        { encoding: "utf-8" },
      ).trim(),
    );
    const rows = Math.max(1, Math.ceil(Math.ceil(dur / everySec) / 6));
    execFileSync(
      "ffmpeg",
      [
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        path,
        "-vf",
        `fps=1/${everySec},scale=${width}:-1,tile=6x${rows}`,
        "-frames:v",
        "1",
        sheetPath,
      ],
      { stdio: "ignore" },
    );
  } catch {
    log(`CONTACT-SHEET failed for ${path}`);
  }
};

const qaFile = (
  outPath: string,
  outcome: JobOutcome,
  expectW: number,
  expectH: number,
  isLong: boolean,
): FileQa => {
  const file = outPath.split(/[\\/]/).pop() ?? outPath;
  const qa: FileQa = {
    file,
    status: outcome.result,
    seconds: outcome.seconds,
    mb: null,
    ffprobe: "n/a",
    lufs: null,
    tp: null,
    black: null,
    verdict: "PASS",
    notes: [],
  };
  const fail = (note: string): void => {
    qa.verdict = "FAIL";
    qa.notes.push(note);
  };
  if (outcome.result === "FAILED") fail("render failed");
  if (!existsSync(outPath)) {
    if (outcome.result !== "FAILED") fail("file missing");
    return qa;
  }
  qa.mb = statSync(outPath).size / 1e6;

  try {
    const v = execFileSync(
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
    const audioRate = execFileSync(
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
    const [w, h, fps] = v.split(",");
    qa.ffprobe = `${w}x${h} @ ${fps} fps, ${audioRate}Hz audio`;
    if (Number(w) !== expectW || Number(h) !== expectH) fail(`resolution ${w}x${h}`);
    if (!fps.startsWith("30")) fail(`fps ${fps}`);
    if (audioRate !== "48000") fail(`audio ${audioRate}Hz`);
  } catch {
    fail("ffprobe failed");
  }

  try {
    const result = pyEval(
      "import sys; sys.path.insert(0, 'scripts'); from loudness import measure; " +
        `m = measure(r"${outPath}", -16, -1.5, 11); print(m['input_i'], m['input_tp'])`,
    ).trim();
    const [i, tp] = result.split(" ").map(Number);
    qa.lufs = i;
    qa.tp = tp;
    if (Math.abs(i - LUFS_TARGET) > LUFS_TOLERANCE) fail(`loudness ${i.toFixed(2)} LUFS`);
    if (tp > TP_FAIL_ABOVE) fail(`true peak ${tp.toFixed(2)} dBTP`);
    else if (tp > TP_WARN_ABOVE) {
      qa.notes.push(`WARN true peak ${tp.toFixed(2)} dBTP`);
      if (qa.verdict === "PASS") qa.verdict = "WARN";
    }
  } catch {
    fail("loudness measurement failed");
  }

  if (isLong) {
    qa.black = blackDetect(outPath);
    if (qa.black === null) fail("blackdetect failed");
    else if (qa.black.length > 0) fail(`black frames at ${qa.black.join(", ")}`);
  }
  return qa;
};

/** Non-PASS check_c rows approved as checker limits by the owner (4 Nov 2026): the episode still renders. */
const KNOWN_CHECKER_LIMITS: Record<number, { files: string[]; why: string }> = {
  41: { files: ["file3.c"], why: "file3.c (copy.c) is a deliberate compile-error teaching example" },
  48: { files: ["file1.c"], why: "file1.c needs typed stdin; the checker gives none" },
  // EP51-86 (8 Nov 2026). Each program below was compiled and run by hand with the right stdin / files and its
  // output matched the episode JSON (see docs/RUNBOOK-ep51-86.md, section "Checker limits"). Owner to confirm in the PR.
  51: { files: ["file1.c"], why: "needs a typed line on stdin" },
  52: { files: ["file1.c"], why: "prints real %p addresses, different every run" },
  53: { files: ["file1.c"], why: "prints real %p addresses" },
  56: { files: ["file1.c"], why: "prints real %p addresses" },
  57: { files: ["file1.c"], why: "prints real %p addresses" },
  65: { files: ["file1.c"], why: "prints real stack/heap/global %p addresses" },
  66: { files: ["file1.c"], why: "needs typed stdin (count and marks)" },
  70: { files: ["file1.c", "file2.c"], why: "read diary.txt / marks.txt that earlier episodes create" },
  71: { files: ["file2.c", "file3.c"], why: "read students.dat that file1.c writes" },
  73: { files: ["wrong.c"], why: "the bug IS an infinite loop (binary search hangs); the checker times out as expected" },
  81: { files: ["file1.c"], why: "prints measured milliseconds, different every run" },
  84: { files: ["students.c", "wrong.c", "fixed.c"], why: "interactive menu program: needs typed stdin" },
  85: { files: ["atm.c"], why: "interactive menu program: needs typed stdin" },
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
    // Checker limits the owner has approved (not defects in the episode): only these exact files.
    const known = KNOWN_CHECKER_LIMITS[ep];
    if (known) {
      const rows = report.split("\n").filter((l) => l.startsWith(`| ${ep} |`));
      const unexpected = rows.filter((l) => !known.files.some((f) => l.includes(`| ${f} |`)));
      if (unexpected.length === 0) {
        log(`GCC   ep${String(ep).padStart(3, "0")}: non-PASS accepted (checker limit: ${known.why})`);
        return true;
      }
    }
    logSkip(ep, "GCC check found non-PASS results — see out/c-check-report.md for this run");
    return false;
  }
  return true;
};

/** Don't start a new episode's job after 05:30 local time (overnight run
 * time-box). Disabled with --no-timebox (supervised run). */
const pastCutoff = (): boolean => {
  if (noTimebox) return false;
  const now = new Date();
  const h = now.getHours();
  const m = now.getMinutes();
  return (h === 5 && m >= 30) || (h > 5 && h < 12);
};

const fmtTime = (seconds: number | null): string => {
  if (seconds === null) return "n/a";
  const s = Math.round(seconds);
  const h = Math.floor(s / 3600);
  const m = Math.floor((s % 3600) / 60);
  const sec = s % 60;
  const two = (n: number): string => String(n).padStart(2, "0");
  return h > 0 ? `${h}:${two(m)}:${two(sec)}` : `${m}:${two(sec)}`;
};

type EpisodeQa = { ep: number; verdict: Verdict; files: FileQa[]; updated: string };

const readEpisodeQa = (ep: number): EpisodeQa | null => {
  const path = join(ROOT, "out", epName(ep), "qa.json");
  if (!existsSync(path)) return null;
  try {
    return JSON.parse(readFileSync(path, "utf-8")) as EpisodeQa;
  } catch {
    return null;
  }
};

/** Rebuilds out/morning-report.md from every episode's qa.json (current disk state). */
const writeMorningReport = (consecutiveFailures: number, stoppedReason: string | null): void => {
  const lines: string[] = [
    REPORT_TITLE,
    "",
    `Last updated ${new Date().toISOString()} (rebuilt after every episode). Old 4K files were moved to out/old4k/epNNN, not deleted.`,
    "",
    "Verdict rules: FAIL = any black frame in the long video, loudness outside -16 +/- 1 LUFS, true peak above -1.0 dBTP, wrong resolution/fps/audio rate, or a failed render. WARN = true peak between -1.5 and -1.0 dBTP.",
    "",
    "| Episode | Long video time | Shorts times (S1-S5) | Size (long + Shorts) | Loudness (LUFS / dBTP) | Black frames | Result / FAIL notes |",
    "| --- | --- | --- | --- | --- | --- | --- |",
  ];
  for (let ep = 1; ep <= 19; ep++) {
    const qa = readEpisodeQa(ep);
    if (!qa) {
      lines.push(`| ${epName(ep)} | not rendered | — | — | — | — | — |`);
      continue;
    }
    const long = qa.files.find((f) => f.file.endsWith("-4k.mp4"));
    const shorts = qa.files.filter((f) => !f.file.endsWith("-4k.mp4"));
    const sizeShorts = shorts.reduce((n, f) => n + (f.mb ?? 0), 0);
    const lufsAll = qa.files.map((f) => f.lufs).filter((v): v is number => v !== null);
    const tpAll = qa.files.map((f) => f.tp).filter((v): v is number => v !== null);
    const loud =
      lufsAll.length > 0
        ? `${Math.min(...lufsAll).toFixed(1)} to ${Math.max(...lufsAll).toFixed(1)} / max ${Math.max(...tpAll).toFixed(2)}`
        : "—";
    const black = long?.black ? (long.black.length === 0 ? "0" : long.black.join(", ")) : "n/a";
    const notes = qa.files
      .filter((f) => f.notes.length > 0)
      .map((f) => `${f.file}: ${f.notes.join("; ")}`)
      .join(" | ");
    lines.push(
      `| ${epName(ep)} | ${fmtTime(long?.seconds ?? null)} | ${shorts.map((f) => fmtTime(f.seconds)).join(" / ") || "—"} | ${(long?.mb ?? 0).toFixed(0)} MB + ${sizeShorts.toFixed(0)} MB | ${loud} | ${black} | **${qa.verdict}**${notes ? ` — ${notes}` : ""} |`,
    );
  }
  lines.push("");
  if (existsSync(SKIP_LOG_PATH)) {
    lines.push("## Episode-level skips (GCC check or narration failure)", "");
    lines.push("```", readFileSync(SKIP_LOG_PATH, "utf-8").trim(), "```", "");
  }
  lines.push(`## Status: ${stoppedReason ?? "in progress"}`, "");
  if (consecutiveFailures > 0) {
    lines.push(`Consecutive episode failures right now: ${consecutiveFailures}.`, "");
  }
  writeFileSync(REPORT_PATH, lines.join("\n"), "utf-8");
};

const stopIfTwoInARow = (epId: string, consecutiveFailures: number): void => {
  if (consecutiveFailures >= 2) {
    log(`=== STOPPING: 2 episodes in a row failed (${epId} and the one before it) ===`);
    writeMorningReport(consecutiveFailures, "stopped: 2 consecutive episode failures");
    process.exit(2); // 2 = deliberate stop (2 episodes in a row failed), not a crash to retry
  }
};

initRun();
let consecutiveFailures = 0;

for (let ep = startEp; ep <= endEp; ep++) {
  if (pastCutoff()) {
    log(`=== TIME-BOX: past 05:30, not starting ${epName(ep)} or later ===`);
    writeMorningReport(consecutiveFailures, "stopped at the 05:30 time-box");
    break;
  }
  const epId = epName(ep);
  log(`=== ${epId}: starting ===`);

  // Preflight: blank or crashing scenes (memory-boxes with no boxes, algorithm-bars with no trace). The episode is skipped.
  // This does not count toward the two-failures-in-a-row stop: it is a data gap, the next episode may be fine.
  const sceneProblemsFound = sceneProblems(ep);
  if (sceneProblemsFound.length > 0) {
    for (const p of sceneProblemsFound) log(`SCENES ${epId} scene ${p.scene} [${p.template}]: ${p.problem}`);
    logSkip(ep, `scene data missing: ${sceneProblemsFound.map((p) => `s${p.scene} ${p.template}`).join(", ")}`);
    log(`=== ${epId}: SKIPPED (scene check failed) ===`);
    writeMorningReport(consecutiveFailures, null);
    continue;
  }

  if (!gccCheckPasses(ep)) {
    log(`=== ${epId}: SKIPPED (GCC check failed) ===`);
    consecutiveFailures++;
    writeMorningReport(consecutiveFailures, null);
    stopIfTwoInARow(epId, consecutiveFailures);
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
      consecutiveFailures++;
      writeMorningReport(consecutiveFailures, null);
      stopIfTwoInARow(epId, consecutiveFailures);
      continue;
    }
  } else {
    log(`SKIP  ${epId} narration (manifest.json already exists)`);
  }

  // Old 4K files out of the way (moved, once), so the skip-if-exists logic re-renders them.
  archiveOldEpisode(ep);
  const outDir = join(ROOT, "out", epId);
  const previous = readEpisodeQa(ep);
  const files: FileQa[] = [];

  // A skipped (already re-rendered in an earlier attempt) job keeps its recorded render time.
  const withPriorTime = (outcome: JobOutcome, fileName: string): JobOutcome =>
    outcome.result === "SKIPPED"
      ? {
          result: "SKIPPED",
          seconds: previous?.files.find((f) => f.file === fileName)?.seconds ?? null,
        }
      : outcome;

  const propsFile = join(outDir, ".props-longvideo.json");
  writeFileSync(propsFile, JSON.stringify({ episodeNumber: ep }), "utf-8");

  const longOut = join(outDir, `${epId}-4k.mp4`);
  const longOutcome = withPriorTime(
    renderJob(
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
        "--timeout=120000",
        `--concurrency=${pickConcurrency(2, `${epId} long`)}`,
      ],
      3840,
      2160,
    ),
    `${epId}-4k.mp4`,
  );
  files.push(qaFile(longOut, longOutcome, 3840, 2160, true));
  contactSheet(longOut, join(outDir, `${epId}-contact-long.png`), 10, 320);

  for (const shortId of ["S1", "S2", "S3", "S4", "S5"]) {
    const shortPropsFile = join(outDir, `.props-short-${shortId}.json`);
    writeFileSync(shortPropsFile, JSON.stringify({ episodeNumber: ep, shortId }), "utf-8");
    const shortOut = join(outDir, `${epId}-${shortId}.mp4`);
    const shortOutcome = withPriorTime(
      renderJob(
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
          `--concurrency=${pickConcurrency(2, `${epId} ${shortId}`)}`,
        ],
        1080,
        1920,
      ),
      `${epId}-${shortId}.mp4`,
    );
    files.push(qaFile(shortOut, shortOutcome, 1080, 1920, false));
    if (existsSync(shortOut)) {
      contactSheet(shortOut, join(outDir, `${epId}-${shortId}-contact.png`), 2.5, 180);
    }
  }

  const verdict: Verdict = files.some((f) => f.verdict === "FAIL")
    ? "FAIL"
    : files.some((f) => f.verdict === "WARN")
      ? "WARN"
      : "PASS";
  const episodeQa: EpisodeQa = { ep, verdict, files, updated: new Date().toISOString() };
  writeFileSync(join(outDir, "qa.json"), JSON.stringify(episodeQa, null, 2), "utf-8");
  const qaLines = [
    `# QA — ${epId}: ${verdict}`,
    "",
    "| File | Status | Time | ffprobe | LUFS | dBTP | Black | Verdict | Notes |",
    "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ...files.map(
      (f) =>
        `| ${f.file} | ${f.status} | ${fmtTime(f.seconds)} | ${f.ffprobe} | ${f.lufs?.toFixed(2) ?? "—"} | ${f.tp?.toFixed(2) ?? "—"} | ${f.black ? f.black.length : "n/a"} | ${f.verdict} | ${f.notes.join("; ")} |`,
    ),
  ];
  writeFileSync(join(outDir, "qa.md"), qaLines.join("\n") + "\n", "utf-8");
  log(`=== ${epId}: done, verdict ${verdict}, QA written to out/${epId}/qa.md ===`);

  if (verdict === "FAIL") consecutiveFailures++;
  else consecutiveFailures = 0;
  writeMorningReport(consecutiveFailures, null);
  stopIfTwoInARow(epId, consecutiveFailures);
}

log(`=== episode_pipeline: finished range ep${startEp}-ep${endEp} ===`);
writeMorningReport(consecutiveFailures, `finished range ep${startEp}-ep${endEp}`);
