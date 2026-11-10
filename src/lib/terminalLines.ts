import type { Episode } from "./episode";
import { stripMarkdown } from "./sanitize.ts";

type Scene = Episode["scenes"][number];

export type TerminalLineKind = "input" | "output" | "success" | "error";
export type TerminalLine = { text: string; kind?: TerminalLineKind };

/** Most program-output rows a terminal window shows (it must clear Xecxec's zone). */
const MAX_OUTPUT_ROWS = 6;

const COMMAND = /^(gcc|clang|cc|make|cd|ls|dir|echo|type|pacman|code|notepad|\.\/|\.\\)/;
const RUN = /^(\.\/|\.\\)/;

/** Terminal onScreen text is a shot description, never a transcript. This builds what the
 * window really shows: the commands it names, then real output. Real output is only ever
 * (a) a reply quoted/ticked in the description, or (b) the output of the episode's own
 * code-explain scene, which check_c.py verified against GCC. The description itself is never
 * printed. With no commands and no output at all, the window shows a bare prompt. */
export const terminalLinesFor = (episode: Episode, scene: Scene): TerminalLine[] => {
  const text = scene.onScreen.replace(/sticky note\s+"[^"]*"/gi, "");
  const lower = text.toLowerCase();
  const replyKind: TerminalLineKind =
    lower.includes("tomato") || lower.includes("error")
      ? "error"
      : lower.includes("mint") || lower.includes("success")
        ? "success"
        : "output";

  const found: TerminalLine[] = [];
  for (const m of text.matchAll(/`([^`]+)`|"([^"]+)"/g)) {
    const tick = m[1];
    const quoted = m[2];
    if (tick !== undefined) {
      // A ticked non-command is output only when the description says the program prints it;
      // otherwise it is a word being pointed at (`main` appears), not terminal text.
      const before = text.slice(Math.max(0, (m.index ?? 0) - 16), m.index ?? 0);
      if (COMMAND.test(tick)) found.push({ text: tick, kind: "input" });
      else if (/(prints?|replies|reply|says|shows|output)\s*:?\s*$/i.test(before))
        found.push({ text: tick, kind: replyKind });
    } else if (quoted !== undefined && quoted.trim().length > 2) {
      found.push({ text: quoted, kind: replyKind });
    }
  }
  // Commands written without backticks ("gcc ep41_arrays.c -o ep41 then ./ep41").
  if (!found.some((l) => l.kind === "input")) {
    const plain = [...text.matchAll(/\bgcc\s+[\w.-]+(?:\s+-o\s+[\w.-]+)?|\.\/[\w.-]+/g)];
    for (const p of plain.reverse()) found.unshift({ text: p[0], kind: "input" });
  }

  const inputs = found.filter((l) => l.kind === "input");
  const replies = found.filter((l) => l.kind !== "input");
  const runs = inputs.filter((l) => RUN.test(l.text));

  const programs = episode.scenes.filter((s) => s.template === "code-explain" && s.code?.output);
  const wanted = inputs.map((l) => l.text.match(/([\w-]+)(?:\.c)?\s*$/)?.[1] ?? "").filter(Boolean);
  const program =
    programs.find((s) => wanted.some((w) => s.code?.file.replace(/\.c$/, "") === w)) ?? programs[0];
  const realOutput: TerminalLine[] = (program?.code?.output ?? "")
    .split("\n")
    .map((t) => t.replace(/\s+$/, ""))
    .filter((t, i, all) => t.length > 0 || i < all.length - 1)
    .slice(0, MAX_OUTPUT_ROWS)
    .map((t) => ({ text: t, kind: "output" as const }));

  let lines: TerminalLine[];
  if (inputs.length === 0) {
    // "Program prints ..." with no command: compile + run the episode's own program.
    if (program?.code) {
      const name = program.code.file.replace(/\.c$/, "");
      lines = [
        { text: `gcc ${program.code.file} -o ${name}`, kind: "input" },
        { text: `./${name}`, kind: "input" },
        ...realOutput,
      ];
    } else {
      lines = replies.length ? replies : [{ text: "", kind: "input" }];
    }
  } else if (replies.length > 0) {
    lines = [...found];
  } else if (runs.length > 0 && realOutput.length > 0) {
    lines = [...inputs, ...realOutput];
  } else {
    lines = inputs; // compile-only, or nothing real to show: just the command(s)
  }
  return lines.map((l) => ({ ...l, text: stripMarkdown(l.text) || l.text }));
};
