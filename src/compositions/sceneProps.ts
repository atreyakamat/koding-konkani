import type { Episode, Scene } from "../lib/episode";

const CUE_RE = /\[(HL|TRACK)\s+[^\]]*\]/g;
const MAX_LINE_CHARS = 48;
const MAX_LINES = 3;

/** Splits narration into sentences, strips [HL]/[TRACK] cues, and takes up to
 * MAX_LINES short ones for ConceptSlide's numbered points — the episode JSON
 * has no separately-authored "bullet point" text, so the spoken narration
 * (not the onScreen stage direction, which describes the shot, not viewer
 * text) is the best available source. Long or very wordy scenes (e.g. a
 * cold-open monologue) will only surface their first few short sentences;
 * see review.md for scenes where this under-represents the full narration. */
const linesFromNarration = (narration: string): string[] => {
  const clean = narration.replace(CUE_RE, "").replace(/\s+/g, " ").trim();
  const sentences = clean.split(/(?<=[.?!])\s+/).filter(Boolean);
  const lines: string[] = [];
  for (const sentence of sentences) {
    if (sentence.length > MAX_LINE_CHARS) continue; // skip run-on sentences, not truncate mid-word
    lines.push(sentence);
    if (lines.length >= MAX_LINES) break;
  }
  if (lines.length === 0 && sentences.length > 0) {
    const first = sentences[0];
    lines.push(first.length > MAX_LINE_CHARS ? `${first.slice(0, MAX_LINE_CHARS - 1)}…` : first);
  }
  return lines;
};

/** Many (not all) concept-slide onScreen directions are shaped "Title": description
 * (e.g. '"Why C?": laptop, washing machine, Python logo...') — a natural analogy
 * card. Cold-open-style concept slides (no colon in their direction) get none,
 * which is correct: they're narrative, not a numbered-point + analogy layout. */
export const analogyFromOnScreen = (
  onScreen: string,
): { title: string; body: string } | undefined => {
  const m = onScreen.match(/^"?([^":]{2,40})"?:\s*(.+)$/);
  if (!m) return undefined;
  return { title: m[1].trim(), body: m[2].trim() };
};

const HL_CUE_RE = /\[HL\s+(\d+)\]/g;
const MAX_LABEL_CHARS = 140;

/** Builds CodeExplain's { line -> short explanation } map by taking the
 * narration text right after each [HL n] marker, up to the next sentence
 * end or the next cue — i.e. what the narrator is saying while that line
 * is highlighted. There's no separately-authored label text in the Bible. */
const labelsFromNarration = (narration: string): Record<number, string> => {
  const labels: Record<number, string> = {};
  const matches = [...narration.matchAll(HL_CUE_RE)];
  for (let i = 0; i < matches.length; i++) {
    const m = matches[i];
    const line = Number(m[1]);
    const start = m.index! + m[0].length;
    const end = i + 1 < matches.length ? matches[i + 1].index! : narration.length;
    let segment = narration.slice(start, end).replace(/\s+/g, " ").trim();
    const sentenceEnd = segment.search(/[.?!](\s|$)/);
    if (sentenceEnd !== -1) segment = segment.slice(0, sentenceEnd + 1);
    if (segment.length > MAX_LABEL_CHARS) segment = `${segment.slice(0, MAX_LABEL_CHARS - 1)}…`;
    if (segment) labels[line] = segment;
  }
  return labels;
};

/**
 * Adapts one generic episode scene (+ the episode it belongs to) into the
 * specific props each scene template component expects. The Bible's
 * `onScreen` text is free prose, not pre-split into each template's
 * structured shape, so most of these are a best-effort single-line mapping.
 * Solid for the 7 templates EP01 actually uses (title-card, concept-slide,
 * code-explain, pun-card, bug-of-the-day, challenge, outro); terminal,
 * memory-boxes and algorithm-bars fall back to scene.trace/scene.code where
 * present and a single onScreen line otherwise — flagged in review.md as
 * needing real refinement once Module 6+ episodes are rendered.
 */
export const scenePropsFor = (episode: Episode, scene: Scene): Record<string, unknown> => {
  switch (scene.template) {
    case "title-card":
      return {
        ep: episode.ep,
        title: episode.title,
        moduleLabel: `M${String(episode.module).padStart(2, "0")}`,
      };
    case "concept-slide":
      return {
        lines: linesFromNarration(scene.narration),
        analogy: analogyFromOnScreen(scene.onScreen),
      };
    case "code-explain":
      return {
        file: scene.code?.file ?? "code.c",
        source: scene.code?.source ?? scene.onScreen,
        labels: labelsFromNarration(scene.narration),
        output: scene.code?.output,
      };
    case "terminal":
      return { lines: [{ text: scene.onScreen }] };
    case "algorithm-bars":
      return { trace: scene.trace ?? [] };
    case "memory-boxes":
      return { boxes: [] };
    case "bug-of-the-day":
      return {
        wrongCode: episode.bug.wrong,
        error: episode.bug.error,
        fixedCode: episode.bug.fixed,
        why: episode.bug.why,
      };
    case "pun-card":
      return { pun: episode.pun };
    case "challenge":
      return { task: episode.challenge };
    case "outro": {
      const m = scene.onScreen.match(/EP\s*(\d+)\s*[·-]\s*(.+?)(?:\s*\+|$)/);
      return {
        nextEp: m ? Number(m[1]) : episode.ep + 1,
        nextTitle: m ? m[2].trim() : "Next episode",
      };
    }
    default:
      return {};
  }
};
