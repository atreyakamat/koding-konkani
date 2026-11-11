/**
 * Fills scene.code (file, source, output?) for specific code-explain scenes
 * whose Bible content (docs/bible/*.md) was never ported into episodes/*.json.
 * Dry-run by default (prints the plan, writes nothing); pass --write to
 * actually modify the episode files. Keeps each file's existing line-ending
 * style. Never guesses: any scene or episode it can't confidently match to a
 * Bible block is skipped and reported, not written.
 *
 * Matching rule: for each target scene, extract the `xxx.c` filename quoted
 * in that scene's onScreen text; collect these filenames (in scene order)
 * and the episode's "### Code shown" fenced code/output pairs (in document
 * order). If every target scene has a filename and the counts match, zip
 * them positionally (filename -> that pair). If filenames are missing for
 * every target scene but the counts still match, fall back to pure
 * positional pairing. Anything else is a mismatch: the whole episode is
 * skipped. A small table of hardcoded cross-episode special cases covers
 * scenes whose content lives in a different episode's section entirely.
 *
 * Usage: node scripts/add_scene_code.mts [--write]
 */
import { readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const ROOT = process.cwd();
const WRITE = process.argv.includes("--write");

/** `pick`: when the Bible's "Code shown" has more pairs than target scenes, the 1-based pair each
 * target scene shows (same order as `scenes`; a pair may repeat, e.g. EP71 shows binread.c twice).
 * `names`: file name to show for a scene whose onScreen text does not name a `x.c` file. */
type Target = {
  ep: number;
  scenes: number[];
  pick?: number[];
  names?: Record<number, string>;
};
const TARGETS: Target[] = [
  { ep: 26, scenes: [5, 8] },
  { ep: 28, scenes: [1, 3, 4, 6] },
  { ep: 29, scenes: [5, 8] },
  { ep: 30, scenes: [4, 6] },
  { ep: 31, scenes: [4, 5, 7] },
  { ep: 32, scenes: [4, 5, 7] },
  // Fix pass 4. EP41/EP44: scene names the file without backticks; the Bible has several programs.
  { ep: 41, scenes: [5], pick: [1] },
  // EP44 scene 6 narrates lines 4-25 of the first program (swap + one bubble pass).
  { ep: 44, scenes: [6], pick: [1] },
  { ep: 59, scenes: [5], pick: [1] },
  { ep: 61, scenes: [7], pick: [2], names: { 7: "ep61copy.c" } },
  { ep: 69, scenes: [6, 9] },
  { ep: 70, scenes: [4, 6] },
  { ep: 71, scenes: [4, 5, 7, 8], pick: [1, 2, 2, 3] },
];

/** The module file that holds an episode's "## EP n" heading. */
const bibleFor = (ep: number): { path: string; text: string } => {
  const dir = join(ROOT, "docs", "bible");
  for (const name of readdirSync(dir).filter((f) => /^m\d+\.md$/.test(f))) {
    // Some module files are CRLF; the fence regexes below expect LF.
    const text = readFileSync(join(dir, name), "utf-8").split("\r\n").join("\n");
    if (new RegExp(`^## EP ${ep} — `, "m").test(text)) return { path: join(dir, name), text };
  }
  throw new Error(`EP ${ep} heading not found in docs/bible`);
};

// Cross-episode special cases: scene content that lives in a different
// episode's Bible section (e.g. "EP 27 challenge answer" recapped at the
// start of EP 28). Keyed by "ep:sceneId".
const SPECIAL: Record<string, { file: string; source: string }> = {
  "28:1": {
    file: "ep27_table7.c",
    source: [
      "#include <stdio.h>",
      "",
      "int main(void) {",
      "    int n;",
      '    printf("Enter a number: ");',
      '    scanf("%d", &n);',
      "    for (int i = 1; i <= 10; i++) {",
      '        printf("%d x %d = %d\\n", n, i, n * i);',
      "    }",
      "    return 0;",
      "}",
      "",
    ].join("\n"),
  },
};

const getEpSection = (ep: number): string => {
  const bible = bibleFor(ep).text;
  const re = new RegExp(`^## EP ${ep} — .*$`, "m");
  const m = re.exec(bible);
  if (!m) throw new Error(`EP ${ep} heading not found`);
  const start = m.index + m[0].length;
  const rest = bible.slice(start);
  const next = /^## EP \d+/m.exec(rest);
  return rest.slice(0, next ? next.index : undefined);
};

const getCodeShownPairs = (section: string): { code: string; output?: string }[] => {
  const marker = "### Code shown";
  const csIdx = section.indexOf(marker);
  if (csIdx === -1) return [];
  const rest = section.slice(csIdx + marker.length);
  const nextHeading = /^### /m.exec(rest);
  const body = rest.slice(0, nextHeading ? nextHeading.index : undefined);
  const blocks: { lang: string; text: string }[] = [];
  const fenceRe = /```(c|text)\n([\s\S]*?)```/g;
  let m: RegExpExecArray | null;
  while ((m = fenceRe.exec(body))) {
    blocks.push({ lang: m[1], text: m[2].replace(/\n$/, "") });
  }
  const pairs: { code: string; output?: string }[] = [];
  for (let i = 0; i < blocks.length; i++) {
    if (blocks[i].lang !== "c") continue;
    const next = blocks[i + 1];
    if (next && next.lang === "text") {
      pairs.push({ code: blocks[i].text, output: next.text });
      i++;
    } else {
      pairs.push({ code: blocks[i].text });
    }
  }
  return pairs;
};

const extractFilename = (onScreen: string): string | null => {
  // Backticked (`sorry.c`) or bare at the start of the text (ep41_arrays.c types itself).
  const m = /`([\w-]+\.c)`/.exec(onScreen) ?? /^([\w-]+\.c)/.exec(onScreen);
  return m ? m[1] : null;
};

type SceneResult = { scene: number; file: string; source: string; output?: string };
type EpisodeReport = {
  ep: number;
  status: "ok" | "mismatch";
  reason?: string;
  usedFallback?: boolean;
  results: SceneResult[];
};

const reports: EpisodeReport[] = [];

for (const { ep, scenes, pick, names } of TARGETS) {
  const epPath = join(ROOT, "episodes", `ep${String(ep).padStart(3, "0")}.json`);
  const data = JSON.parse(readFileSync(epPath, "utf-8"));
  const section = getEpSection(ep);
  const allPairs = getCodeShownPairs(section);
  const pairs = pick ? pick.map((n) => allPairs[n - 1]) : allPairs;
  if (pairs.some((p) => p === undefined)) throw new Error(`ep${ep}: pick ${pick} is outside ${allPairs.length} pairs`);

  const normalScenes = scenes.filter((sid) => !SPECIAL[`${ep}:${sid}`]);
  const specialScenes = scenes.filter((sid) => SPECIAL[`${ep}:${sid}`]);

  const sceneObjs = normalScenes.map((sid) => {
    const s = data.scenes.find((x: any) => x.id === sid);
    if (!s) throw new Error(`ep${ep} scene ${sid} not found in episode JSON`);
    return s;
  });
  const filenames = sceneObjs.map((s: any) => names?.[s.id] ?? extractFilename(s.onScreen));

  let mismatch: string | undefined;
  let usedFallback = false;
  const results: SceneResult[] = [];

  const allHaveFilenames = filenames.every((f) => f !== null);
  const noneHaveFilenames = filenames.every((f) => f === null);

  if (allHaveFilenames && filenames.length === pairs.length) {
    for (let i = 0; i < sceneObjs.length; i++) {
      results.push({ scene: sceneObjs[i].id, file: filenames[i]!, source: pairs[i].code, output: pairs[i].output });
    }
  } else if (noneHaveFilenames && normalScenes.length > 0 && normalScenes.length === pairs.length) {
    usedFallback = true;
    for (let i = 0; i < sceneObjs.length; i++) {
      results.push({
        scene: sceneObjs[i].id,
        file: `scene${sceneObjs[i].id}.c`,
        source: pairs[i].code,
        output: pairs[i].output,
      });
    }
  } else if (normalScenes.length > 0) {
    mismatch = `${normalScenes.length} target scene(s) (filenames found: ${filenames.filter((f) => f).length}) vs ${pairs.length} Code shown pair(s) in docs/bible/m04.md`;
  }

  if (!mismatch) {
    for (const sid of specialScenes) {
      const sp = SPECIAL[`${ep}:${sid}`];
      results.push({ scene: sid, file: sp.file, source: sp.source });
    }
    results.sort((a, b) => a.scene - b.scene);
  }

  reports.push({ ep, status: mismatch ? "mismatch" : "ok", reason: mismatch, usedFallback, results });
}

// --- report ---
console.log(`=== add_scene_code.mts ${WRITE ? "(WRITE)" : "(DRY RUN)"} ===`);
for (const r of reports) {
  if (r.status === "mismatch") {
    console.log(`ep${String(r.ep).padStart(3, "0")}: MISMATCH — ${r.reason} — SKIPPED, not written`);
    continue;
  }
  console.log(`ep${String(r.ep).padStart(3, "0")}: ok${r.usedFallback ? " (positional fallback)" : ""}`);
  for (const res of r.results) {
    console.log(`  scene ${res.scene}: file=${res.file} source=${res.source.split("\n").length} lines output=${res.output ? "yes" : "no"}`);
  }
}

if (!WRITE) {
  console.log("\nDry run only — pass --write to apply.");
  process.exit(0);
}

// --- apply ---
for (const r of reports) {
  if (r.status !== "ok") continue;
  const epPath = join(ROOT, "episodes", `ep${String(r.ep).padStart(3, "0")}.json`);
  const raw = readFileSync(epPath, "utf-8");
  const eol = raw.includes("\r\n") ? "\r\n" : "\n";
  const data = JSON.parse(raw);
  for (const res of r.results) {
    const scene = data.scenes.find((s: any) => s.id === res.scene);
    scene.code = res.output !== undefined ? { file: res.file, source: res.source, output: res.output } : { file: res.file, source: res.source };
  }
  let out = JSON.stringify(data, null, 2) + "\n";
  if (eol === "\r\n") out = out.replace(/\n/g, "\r\n");
  writeFileSync(epPath, out, "utf-8");
  console.log(`wrote ${epPath}`);
}
