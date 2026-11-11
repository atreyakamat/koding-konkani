/**
 * Smoke test of the real render path, without spending hours on full renders.
 * For each episode it loads the real LongVideo and the five Short compositions (so calculateMetadata,
 * the narration files, cues and captions are all exercised), renders still frames inside every scene
 * and every Short, and fails on:
 *   - any render error or timeout (missing file, bad data, crash);
 *   - a blank frame: one flat colour, or black (checked with ffmpeg signalstats).
 * It does NOT check narration quality. With --fake-voice files (silent) it proves the video side.
 *
 * Usage: node scripts/smoke_render.mts --lang cpp 1 40 90        (episode numbers)
 *        node scripts/smoke_render.mts --lang cpp all
 * Env:   BROWSER_EXECUTABLE=/path/to/chrome  (optional)   SMOKE_SCALE=0.35 (default)
 * Output: out/smoke/<lang>/report.md and the stills; exit 1 on any failure.
 */
import { execFileSync } from "node:child_process";
import { existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { bundle } from "@remotion/bundler";
import { openBrowser, renderStill, selectComposition } from "@remotion/renderer";
import { epFolder } from "../src/lib/episode.ts";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const FPS = 30;
const OVERLAP = 12; // TRANSITION_FRAMES: scenes overlap by this many frames in LongVideo

const args = process.argv.slice(2);
const langIdx = args.indexOf("--lang");
const lang = langIdx >= 0 ? args[langIdx + 1] : "c";
const rest = args.filter((_, i) => i !== langIdx && i !== langIdx + 1);
const episodesDir = join(
  ROOT,
  lang === "cpp" ? "episodes-cpp" : lang === "python" ? "episodes-python" : "episodes",
);
const all = rest[0] === "all";
const episodeNumbers = all
  ? Array.from({ length: lang === "cpp" ? 90 : lang === "python" ? 90 : 86 }, (_, i) => i + 1)
  : rest.map(Number);
if (episodeNumbers.length === 0 || episodeNumbers.some((n) => !Number.isInteger(n) || n < 1)) {
  console.error("usage: node scripts/smoke_render.mts --lang cpp <episode-number...|all>");
  process.exit(1);
}
const scale = Number(process.env.SMOKE_SCALE ?? "0.35");
const outDir = join(ROOT, "out", "smoke", lang);
mkdirSync(outDir, { recursive: true });

type Row = { what: string; ok: boolean; note: string };
const rows: Row[] = [];

/** Luma range of a still: a flat or black frame has almost no spread between darkest and brightest pixel. */
const lumaRange = (file: string): { min: number; max: number } => {
  const out = execFileSync(
    "ffmpeg",
    ["-v", "error", "-i", file, "-vf", "signalstats,metadata=print:file=-", "-f", "null", "-"],
    { encoding: "utf-8", stdio: ["ignore", "pipe", "pipe"] },
  );
  const num = (key: string): number =>
    Number(out.match(new RegExp(`lavfi.signalstats.${key}=(\\d+(?:\\.\\d+)?)`))?.[1] ?? NaN);
  return { min: num("YMIN"), max: num("YMAX") };
};

const bundleUrl = await bundle({
  entryPoint: join(ROOT, "src", "index.ts"),
  publicDir: join(ROOT, "audio"),
});
const browser = await openBrowser("chrome", {
  browserExecutable: process.env.BROWSER_EXECUTABLE ?? null,
  chromeMode: process.env.BROWSER_EXECUTABLE ? "chrome-for-testing" : undefined,
  chromiumOptions: { gl: "swangle" },
});

const still = async (
  id: string,
  props: Record<string, unknown>,
  frame: number,
  name: string,
): Promise<void> => {
  const what = `${name}`;
  try {
    const composition = await selectComposition({
      serveUrl: bundleUrl,
      id,
      inputProps: props,
      puppeteerInstance: browser,
      timeoutInMilliseconds: 120000,
    });
    const at = Math.min(Math.max(0, frame), composition.durationInFrames - 1);
    const output = join(outDir, `${name}.jpg`);
    await renderStill({
      composition,
      serveUrl: bundleUrl,
      output,
      frame: at,
      inputProps: props,
      imageFormat: "jpeg",
      jpegQuality: 75,
      scale,
      puppeteerInstance: browser,
      timeoutInMilliseconds: 120000,
    });
    const { min, max } = lumaRange(output);
    const flat = !(max - min >= 40);
    rows.push({
      what,
      ok: !flat,
      note: flat ? `BLANK frame (luma ${min}-${max})` : `luma ${min}-${max}`,
    });
  } catch (error) {
    rows.push({
      what,
      ok: false,
      note: `RENDER ERROR: ${String((error as Error).message)
        .split("\n")[0]
        .slice(0, 200)}`,
    });
  }
};

for (const ep of episodeNumbers) {
  const epId = epFolder(lang, ep);
  const voice = join(ROOT, "audio", "voice", epId);
  if (!existsSync(join(voice, "manifest.json"))) {
    rows.push({
      what: `${epId}`,
      ok: false,
      note: `no narration in audio/voice/${epId} (run render_episode_audio.py ${ep} --lang ${lang} first)`,
    });
    continue;
  }
  const episode = JSON.parse(
    readFileSync(join(episodesDir, `ep${String(ep).padStart(3, "0")}.json`), "utf-8"),
  );
  const manifest = JSON.parse(readFileSync(join(voice, "manifest.json"), "utf-8"));
  // Always test against the current episode JSON, never a stale copy (the 1 Nov EP07-09 black-scene bug).
  writeFileSync(join(voice, "episode.json"), JSON.stringify(episode, null, 2));
  const props = { episodeNumber: ep, ...(lang === "c" ? {} : { lang }) };

  let frame = 0;
  episode.scenes.forEach(
    (scene: { id: number; template: string; lengthSec: number }, i: number) => {
      const sec =
        manifest.timings.find((t: { scene?: number }) => t.scene === scene.id)?.durationSec ??
        scene.lengthSec;
      const length = Math.round(sec * FPS);
      if (i > 0) frame -= OVERLAP;
      scene.start = Math.max(0, frame);
      scene.frames = length;
      frame += length;
    },
  );
  for (const scene of episode.scenes) {
    for (const frac of [0.25, 0.85]) {
      await still(
        "LongVideo",
        props,
        scene.start + Math.round(scene.frames * frac),
        `${epId}-s${String(scene.id).padStart(2, "0")}-${scene.template}-${frac}`,
      );
    }
  }
  for (const short of episode.shorts) {
    for (const frac of [0.2, 0.8]) {
      const sec =
        manifest.timings.find((t: { short?: string }) => t.short === short.id)?.durationSec ??
        short.lengthSec;
      await still(
        `Short-${short.id}`,
        { ...props, shortId: short.id },
        Math.round(sec * FPS * frac),
        `${epId}-${short.id}-${frac}`,
      );
    }
  }
  const bad = rows.filter((r) => r.what.startsWith(epId) && !r.ok).length;
  console.log(`${epId}: ${bad === 0 ? "ok" : `${bad} problem(s)`}`);
}

await browser.close({ silent: true });
const failed = rows.filter((r) => !r.ok);
writeFileSync(
  join(outDir, "report.md"),
  [
    `# Smoke render (${lang}) — ${rows.length} frames, ${failed.length} problems`,
    "",
    ...failed.map((r) => `- ${r.what}: ${r.note}`),
    "",
    "## All frames",
    "",
    ...rows.map((r) => `- ${r.ok ? "ok" : "FAIL"} ${r.what}: ${r.note}`),
  ].join("\n") + "\n",
);
console.log(
  `${rows.length} frames checked, ${failed.length} problems. Report: out/smoke/${lang}/report.md`,
);
process.exit(failed.length ? 1 : 0);
