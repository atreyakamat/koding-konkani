/**
 * System-ready check for rendering the C++ course on this PC. Read-only: it only runs
 * `--version` style commands and looks for files. It never installs or changes anything.
 *
 *   npm run system:check
 *
 * Exit code 1 if anything required is missing; each line says how to fix it.
 */
import { execFileSync } from "node:child_process";
import { existsSync, readFileSync, statfsSync } from "node:fs";
import { join } from "node:path";

const ROOT = new URL("..", import.meta.url).pathname.replace(/^\/([a-zA-Z]:)/, "$1");
const PY = join(ROOT, ".venv", "Scripts", "python.exe");

type Row = { name: string; ok: boolean; detail: string; fix: string };
const rows: Row[] = [];

const run = (cmd: string, args: string[]): string | null => {
  try {
    return execFileSync(cmd, args, {
      encoding: "utf-8",
      stdio: ["ignore", "pipe", "pipe"],
      timeout: 20000,
    }).trim();
  } catch {
    return null;
  }
};
const add = (name: string, ok: boolean, detail: string, fix: string): void => {
  rows.push({ name, ok, detail, fix });
};

const node = process.versions.node;
add("Node 20 or newer", Number(node.split(".")[0]) >= 20, node, "Install Node LTS from nodejs.org");

add(
  "node_modules installed",
  existsSync(join(ROOT, "node_modules", "remotion")),
  "",
  "Run: npm install",
);

const py = existsSync(PY) ? run(PY, ["--version"]) : null;
add(
  "Python venv (.venv)",
  py !== null,
  py ?? "not found",
  "Run: py -3.13 -m venv .venv, then .venv\\Scripts\\python.exe -m pip install -r scripts\\requirements.txt",
);

if (py) {
  const piper = run(PY, ["-c", "import piper; print('ok')"]);
  add(
    "Python package: piper",
    piper === "ok",
    piper ?? "missing",
    "Run: .venv\\Scripts\\python.exe -m pip install -r scripts\\requirements.txt",
  );
}

const ff = (run("ffmpeg", ["-version"]) ?? "").split("\n")[0] ?? "";
add(
  "ffmpeg on PATH",
  ff.startsWith("ffmpeg"),
  ff || "not found",
  "Install FFmpeg and add it to PATH",
);
const fp = (run("ffprobe", ["-version"]) ?? "").split("\n")[0] ?? "";
add("ffprobe on PATH", fp.startsWith("ffprobe"), fp || "not found", "Comes with FFmpeg");

const gpp = (run("g++", ["--version"]) ?? "").split("\n")[0] ?? "";
add(
  "g++ (GCC) on PATH",
  gpp.length > 0,
  gpp || "not found",
  "Install MSYS2 GCC and add its bin folder to PATH",
);
if (gpp) {
  const major = Number(/(\d+)\.\d+\.\d+/.exec(gpp)?.[1] ?? 0);
  add(
    "GCC 13 or newer (C++20)",
    major >= 13,
    `major ${major}`,
    "Update GCC: pacman -S mingw-w64-ucrt-x86_64-gcc",
  );
}

try {
  const cfg = JSON.parse(readFileSync(join(ROOT, "config", "voice.json"), "utf-8")) as {
    model: string;
  };
  const model = join(ROOT, cfg.model);
  add(
    "Narrator voice model",
    existsSync(model),
    cfg.model,
    "Copy the Piper voice files into .cache/piper-voices/ (same as for the C course)",
  );
  add(
    "Narrator voice config (.json)",
    existsSync(`${model}.json`),
    `${cfg.model}.json`,
    "The .onnx.json file must sit next to the .onnx file",
  );
} catch {
  add("config/voice.json", false, "unreadable", "Restore config/voice.json from git");
}

add(
  "Fonts (audio/fonts)",
  existsSync(join(ROOT, "audio", "fonts")),
  "",
  "Run: git checkout -- audio/fonts",
);
add(
  "Episode files (episodes-cpp)",
  existsSync(join(ROOT, "episodes-cpp", "ep090.json")),
  "",
  "Run: npm run cpp:build",
);

try {
  const s = statfsSync(ROOT);
  const freeGb = Math.round((Number(s.bavail) * Number(s.bsize)) / 1e9);
  add(
    "Free disk 60 GB or more",
    freeGb >= 60,
    `${freeGb} GB`,
    "Free space: one module of 4K videos needs about 60 GB",
  );
} catch {
  add("Free disk", true, "could not read, skipped", "");
}

let failed = 0;
for (const r of rows) {
  if (!r.ok) failed++;
  console.log(
    `${r.ok ? "OK  " : "FAIL"} ${r.name}${r.detail ? ` (${r.detail})` : ""}${r.ok ? "" : `\n       fix: ${r.fix}`}`,
  );
}
console.log(
  failed === 0 ? "\nSYSTEM READY" : `\n${failed} problem(s). Fix them, then run this check again.`,
);
process.exit(failed === 0 ? 0 : 1);
