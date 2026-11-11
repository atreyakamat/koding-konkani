import { useCurrentFrame } from "remotion";
import type { Episode } from "../lib/episode";
import type { ShortBox, ShortVisual } from "../lib/shortVisual";
import { frameAt, frameStarts, type WordTime } from "../lib/shortFrames";
import { bugCulprit } from "../lib/bugCulprit";
import { chooseFontSize } from "../lib/codeLayout";
import { defaultHlCues, hlLineAt } from "../lib/cues";
import { typewriterChars } from "../lib/motion";
import { stripMarkdown } from "../lib/sanitize";
import { textTransformFor } from "../lib/textCase";
import { accentOn, readableOn } from "../theme/contrast";
import { fonts } from "../theme/fonts";
import { brutal, palette } from "../theme/palette";
import { CodeBlock, Panel } from "../ui";
import { SHORT_SLOT } from "../scenes/ShortLayout";

const { width: W, height: H } = SHORT_SLOT;

const reveal = (frame: number, start: number, len = 10): number =>
  Math.min(1, Math.max(0, (frame - start) / len));

/** Text size that keeps a block of `chars` characters inside the slot. */
const fitText = (chars: number, base = 72): number =>
  chars > 140
    ? Math.round(base * 0.55)
    : chars > 90
      ? Math.round(base * 0.7)
      : chars > 45
        ? Math.round(base * 0.85)
        : base;

/** Inner size of a Panel filling the slot (padding 32 + border 5, both sides). */
const CARD_INNER = { width: W - 74, height: H - 74 } as const;
const CARD_MIN_PX = 56;
const CARD_MAX_PX = 140;
const CARD_GAP = 28;

/** Largest title-font size (>= CARD_MIN_PX) at which every part, word-wrapped, fits the card.
 * Archivo Black caps average ~0.74em per character. A card of one or two short lines
 * therefore gets the biggest size; a long sentence steps down toward the 56px floor. */
const fitCardText = (parts: string[]): number => {
  const fits = (size: number): boolean => {
    const perRow = Math.max(1, Math.floor(CARD_INNER.width / (size * 0.74)));
    let rows = 0;
    for (const part of parts) {
      let row = 0;
      let used = 0;
      for (const word of part.split(/\s+/)) {
        const need = word.length + (used ? 1 : 0);
        if (used && used + need > perRow) {
          row++;
          used = word.length;
        } else used += need;
        if (word.length > perRow) row += Math.floor(word.length / perRow);
      }
      rows += row + 1;
    }
    return rows * size * 1.2 + (parts.length - 1) * CARD_GAP <= CARD_INNER.height;
  };
  for (let size = CARD_MAX_PX; size > CARD_MIN_PX; size -= 4) if (fits(size)) return size;
  return CARD_MIN_PX;
};

/** Big text card, filling its slot. " · " separated parts stack as their own lines (a list
 * reads as a list); long words wrap instead of clipping. */
const TextCard: React.FC<{ text: string; background?: string }> = ({
  text,
  background = palette.cream,
}) => {
  const parts = text
    .split(/\s·\s|\n/)
    .map((p) => p.trim())
    .filter(Boolean);
  const size = fitCardText(
    parts.map((p) => (textTransformFor(p) === "uppercase" ? p.toUpperCase() : p)),
  );
  return (
    <Panel
      background={background}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: CARD_GAP,
      }}
    >
      {parts.map((part, i) => (
        <div
          key={i}
          style={{
            fontFamily: fonts.title,
            fontSize: size,
            lineHeight: 1.2,
            textAlign: "center",
            color: readableOn(background),
            textTransform: textTransformFor(part),
            overflowWrap: "anywhere",
          }}
        >
          {part}
        </div>
      ))}
    </Panel>
  );
};

const PunVisual: React.FC<{ text: string }> = ({ text }) => {
  const frame = useCurrentFrame();
  const o = reveal(frame, 8, 8);
  return (
    <Panel
      background={palette.tomato}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          opacity: o,
          fontFamily: fonts.title,
          fontSize: fitText(text.length, 72),
          lineHeight: 1.25,
          textAlign: "center",
          color: readableOn(palette.tomato),
        }}
      >
        {text}
      </div>
    </Panel>
  );
};

const PronunciationVisual: React.FC<{ written: string; spoken: string; accent: string }> = ({
  written,
  spoken,
  accent,
}) => {
  const frame = useCurrentFrame();
  const sweep = reveal(frame, 20, 14);
  return (
    <Panel
      background={palette.cream}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        gap: 28,
      }}
    >
      <div style={{ fontFamily: fonts.code, fontWeight: 700, fontSize: 80, color: palette.ink }}>
        {written}
      </div>
      <div
        style={{ fontFamily: fonts.title, fontSize: 52, color: accentOn(palette.cream, accent) }}
      >
        ↓ say it like
      </div>
      <div
        style={{
          fontFamily: fonts.title,
          fontSize: 84,
          color: palette.ink,
          background: accent,
          border: `${brutal.border}px solid ${palette.ink}`,
          padding: "10px 32px",
          clipPath: `inset(0 ${(1 - sweep) * 100}% 0 0)`,
        }}
      >
        {spoken.toUpperCase()}
      </div>
    </Panel>
  );
};

const AnalogyVisual: React.FC<{ title: string; body: string; accent: string }> = ({
  title,
  body,
  accent,
}) => {
  const frame = useCurrentFrame();
  return (
    <Panel
      background={palette.cream}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      <div
        style={{
          fontFamily: fonts.title,
          fontSize: 56,
          color: accentOn(palette.cream, accent),
          marginBottom: 28,
          textTransform: textTransformFor(title),
        }}
      >
        {title}
      </div>
      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: body.length > 90 ? 48 : 58,
          color: palette.ink,
          lineHeight: 1.35,
          opacity: reveal(frame, 16, 10),
        }}
      >
        {body}
      </div>
    </Panel>
  );
};

const TERMINAL_SIZES = [80, 72, 64, 56, 48, 44, 40];
const TERMINAL_GAP = 18;

/** Largest mono size at which every "$ line", wrapped, fits the card (JetBrains Mono ~0.6em/char),
 * so one or two short commands fill the card instead of sitting small in a corner. */
const fitTerminalFont = (lines: string[]): number => {
  const fits = (size: number): boolean => {
    const perRow = Math.max(1, Math.floor(CARD_INNER.width / (size * 0.6)));
    const rows = lines.reduce((n, l) => n + Math.ceil((l.length + 2) / perRow), 0);
    return rows * size * 1.3 + (lines.length - 1) * TERMINAL_GAP <= CARD_INNER.height;
  };
  return TERMINAL_SIZES.find(fits) ?? TERMINAL_SIZES[TERMINAL_SIZES.length - 1];
};

const TerminalVisual: React.FC<{ lines: string[] }> = ({ lines }) => {
  const frame = useCurrentFrame();
  const font = fitTerminalFont(lines);
  return (
    <Panel
      background={palette.darkBlue}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        gap: TERMINAL_GAP,
      }}
    >
      {lines.map((line, i) => (
        <div
          key={i}
          style={{
            fontFamily: fonts.code,
            fontWeight: 700,
            fontSize: font,
            color: palette.white,
            whiteSpace: "pre-wrap",
            overflowWrap: "anywhere",
            opacity: reveal(frame, 8 + i * 14, 8),
          }}
        >
          <span style={{ color: palette.mint }}>{"$ "}</span>
          {line}
        </div>
      ))}
    </Panel>
  );
};

const CodeVisual: React.FC<{
  source: string;
  mode: "advance" | "static";
  durationInFrames: number;
}> = ({ source, mode, durationInFrames }) => {
  const frame = useCurrentFrame();
  // Short snippets (one or two lines) get a much larger font to fill the slot.
  const numbered = source.includes("\n");
  const font = chooseFontSize(source, W, H, 120, numbered);
  const visibleChars = typewriterChars(source, frame, 6, Math.max(1, source.length / 36));
  const typed = visibleChars >= source.length;
  const hl =
    mode === "advance" && typed
      ? hlLineAt(defaultHlCues(source.split("\n"), durationInFrames - 60), frame)
      : undefined;
  return (
    <CodeBlock
      source={source}
      width={W}
      fontSize={font}
      maxHeight={H}
      fillHeight={H}
      visibleChars={visibleChars}
      highlightLine={hl}
      lineNumbers={numbered}
    />
  );
};

const QuizVisual: React.FC<{ visual: Extract<ShortVisual, { kind: "quiz" }>; accent: string }> = ({
  visual,
  accent,
}) => {
  const frame = useCurrentFrame();
  // No code to run, so no OUTPUT panel: the question and its options are the whole card.
  if (visual.code.length === 0) {
    return <TextCard text={visual.card} />;
  }
  const outputH = visual.options.length ? 120 : 170;
  const optionsH = visual.options.length ? 150 : 0;
  const codeMax = H - outputH - optionsH - 32;
  const source = visual.code.join("\n");
  const font = chooseFontSize(source, W, codeMax);
  const text = [...visual.options, visual.question].filter(Boolean);
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, height: "100%" }}>
      {visual.code.length ? (
        <CodeBlock
          source={source}
          width={W}
          fontSize={font}
          maxHeight={codeMax}
          fillHeight={codeMax}
          visibleChars={typewriterChars(source, frame, 4, Math.max(1, source.length / 24))}
        />
      ) : (
        <Panel
          background={palette.cream}
          style={{ flex: 1, display: "flex", alignItems: "center", justifyContent: "center" }}
        >
          <div
            style={{
              fontFamily: fonts.title,
              fontSize: fitText(text.join(" ").length, 60),
              textAlign: "center",
              lineHeight: 1.2,
              color: palette.ink,
            }}
          >
            {text.join("\n")}
          </div>
        </Panel>
      )}
      {visual.code.length && text.length ? (
        <div
          style={{
            fontFamily: fonts.body,
            fontWeight: 700,
            fontSize: text.join(" ").length > 60 ? 38 : 46,
            lineHeight: 1.2,
            color: palette.ink,
          }}
        >
          {text.join(" · ")}
        </div>
      ) : null}
      <Panel
        background={palette.darkBlue}
        padding={16}
        style={{ display: "flex", alignItems: "center", gap: 24, minHeight: outputH }}
      >
        <div
          style={{ fontFamily: fonts.code, fontSize: 36, fontWeight: 700, color: palette.white }}
        >
          OUTPUT
        </div>
        <div
          style={{
            fontFamily: fonts.title,
            fontSize: 96,
            lineHeight: 1,
            color: accent,
            opacity: Math.floor(frame / 12) % 2 === 0 ? 1 : 0.55,
          }}
        >
          ?
        </div>
      </Panel>
    </div>
  );
};

type BoxesVisualProps = {
  boxes: ShortBox[];
  frames?: { label?: string; boxes: ShortBox[] }[];
  words: WordTime[];
  durationInFrames: number;
};

/** The label under the boxes is code, so it is set big enough to read on a phone. */
const STEP_LABEL_FONT = 44;

/** Boxes of a memory scene. With several frames it steps through them in sync with the narration (frameStarts);
 * only the boxes whose value changed pop again. */
const BoxesVisual: React.FC<BoxesVisualProps> = ({ boxes: first, frames, words, durationInFrames }) => {
  const frame = useCurrentFrame();
  const steps = frames ?? [{ boxes: first }];
  const starts = frameStarts(
    steps.map((st) => st.label),
    words,
    30,
    durationInFrames,
  );
  const k = frameAt(starts, frame);
  const boxes = steps[k].boxes;
  const label = steps[k].label;
  const n = boxes.length;
  const gap = 20;
  const boxW = Math.floor((W - gap * (n - 1)) / n);
  const boxH = Math.min(340, Math.round(boxW * 1.25));
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 36, height: "100%", alignItems: "center", justifyContent: "center" }}>
      <div style={{ display: "flex", gap }}>
        {boxes.map((box, i) => {
          // The frame in which this box last changed its value decides when it pops.
          let born = 0;
          for (let j = 1; j <= k; j++) if (steps[j].boxes[i]?.value !== steps[j - 1].boxes[i]?.value) born = j;
          const p = reveal(frame, born === 0 ? 6 + i * 5 : starts[born], 8);
          const valueFont = Math.max(
            28,
            Math.min(72, Math.floor((boxW - 24) / (Math.max(2, box.value.length) * 0.6))),
          );
          const nameFont = Math.max(
            28,
            Math.min(40, Math.floor((boxW - 16) / (Math.max(3, box.name.length) * 0.62))),
          );
          return (
            <div
              key={`${box.name}-${i}`}
              style={{
                width: boxW,
                height: boxH,
                background: box.mark === "hl" ? palette.butter : palette.cream,
                border: `${brutal.borderThick}px solid ${palette.ink}`,
                boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
                boxSizing: "border-box",
                display: "flex",
                flexDirection: "column",
                alignItems: "center",
                justifyContent: "space-evenly",
                opacity: p,
                scale: `${0.85 + 0.15 * p}`,
              }}
            >
              <div style={{ fontFamily: fonts.title, fontSize: nameFont, color: palette.ink }}>{box.name}</div>
              <div style={{ fontFamily: fonts.code, fontWeight: 700, fontSize: valueFont, color: palette.ink }}>{box.value}</div>
            </div>
          );
        })}
      </div>
      {label && steps.length > 1 ? (
        <div
          style={{
            fontFamily: fonts.code,
            fontWeight: 700,
            fontSize: STEP_LABEL_FONT,
            color: palette.ink,
            textAlign: "center",
            maxWidth: W,
            overflowWrap: "anywhere",
          }}
        >
          {label}
        </div>
      ) : null}
    </div>
  );
};

const BitRow: React.FC<{
  label: string;
  bits: string;
  cell: number;
  accent: string;
  frame: number;
  at: number;
}> = ({ label, bits, cell, accent, frame, at }) => (
  <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
    <div
      style={{
        width: 150,
        fontFamily: fonts.title,
        fontSize: 44,
        color: palette.ink,
        textAlign: "right",
      }}
    >
      {label}
    </div>
    {[...bits].map((b, i) => {
      const p = reveal(frame, at + i * 3, 6);
      return (
        <div
          key={i}
          style={{
            width: cell,
            height: cell,
            boxSizing: "border-box",
            background: b === "1" ? accent : palette.cream,
            border: `${brutal.border}px solid ${palette.ink}`,
            boxShadow: `${brutal.shadow - 3}px ${brutal.shadow - 3}px 0 0 ${palette.ink}`,
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            fontFamily: fonts.code,
            fontWeight: 700,
            fontSize: Math.round(cell * 0.6),
            color: b === "1" ? readableOn(accent) : palette.ink,
            opacity: p,
          }}
        >
          {b}
        </div>
      );
    })}
  </div>
);

const BitsVisual: React.FC<{ visual: Extract<ShortVisual, { kind: "bits" }>; accent: string }> = ({
  visual,
  accent,
}) => {
  const frame = useCurrentFrame();
  const width = visual.rows[0].bits.length;
  const cell = Math.min(150, Math.floor((W - 150 - 14 * width - 40) / width));
  const places = [...visual.rows[0].bits].map((_, i) => 2 ** (width - 1 - i));
  return (
    <Panel
      background={palette.cream}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        gap: 20,
        padding: 20,
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 14 }}>
        <div style={{ width: 150 }} />
        {places.map((p) => (
          <div
            key={p}
            style={{
              width: cell,
              textAlign: "center",
              fontFamily: fonts.code,
              fontWeight: 700,
              fontSize: 40,
              color: accentOn(palette.cream, accent),
            }}
          >
            {p}
          </div>
        ))}
      </div>
      {visual.rows.map((row, i) => (
        <BitRow
          key={row.label}
          label={row.label}
          bits={row.bits}
          cell={cell}
          accent={accent}
          frame={frame}
          at={8 + i * 14}
        />
      ))}
      {visual.result ? (
        <>
          <div style={{ height: 6, background: palette.ink, marginLeft: 164 }} />
          <BitRow
            label={`= ${visual.result.label}`}
            bits={visual.result.bits}
            cell={cell}
            accent={palette.mint}
            frame={frame}
            at={44}
          />
        </>
      ) : null}
      {visual.sum ? (
        <div
          style={{
            fontFamily: fonts.code,
            fontWeight: 700,
            fontSize: 48,
            color: palette.ink,
            textAlign: "center",
            opacity: reveal(frame, 40, 10),
          }}
        >
          {visual.sum}
        </div>
      ) : null}
    </Panel>
  );
};

const briefErrorLines = (error: string, wrong: string, isCode: boolean): string => {
  if (isCode) {
    const gcc = error.split("\n").filter((l) => l.includes("error:"));
    if (gcc.length > 0) return gcc.join("\n");
  }
  const wrongLines = new Set(wrong.split("\n").map((l) => l.trim()));
  return error
    .split("\n")
    .filter((l) => l.trim() && !wrongLines.has(l.trim()))
    .slice(0, 3)
    .join("\n");
};

const ERROR_SIZES = [44, 40, 36, 32, 30];
const ERROR_MAX_HEIGHT = 380;
const ERROR_PAD = 74;

/** The error text for the Bug Short's card: the largest size (30px at the least, so it reads on a phone) at which
 * every error line fits ERROR_MAX_HEIGHT; when even 30px is too much, only the first error line is kept. */
export const fitError = (text: string, mono: boolean): { text: string; size: number; height: number } => {
  const width = W - ERROR_PAD;
  const rowsAt = (t: string, size: number): number =>
    t.split("\n").reduce((n, l) => n + Math.max(1, Math.ceil(l.length / Math.max(1, Math.floor(width / (size * (mono ? 0.6 : 0.55)))))), 0);
  const heightOf = (t: string, size: number): number => rowsAt(t, size) * size * 1.3 + ERROR_PAD;
  const lines = text.split("\n").filter((l) => l.trim() !== "");
  for (const candidate of [lines.join("\n"), lines[0] ?? ""]) {
    const size = ERROR_SIZES.find((sz) => heightOf(candidate, sz) <= ERROR_MAX_HEIGHT);
    if (size) return { text: candidate, size, height: Math.max(200, Math.round(heightOf(candidate, size))) };
  }
  const first = lines[0] ?? "";
  const size = ERROR_SIZES[ERROR_SIZES.length - 1];
  return { text: first, size, height: ERROR_MAX_HEIGHT };
};

/** The bug reveal: the wrong code/claim/value, then the key error line underneath. */
const BugVisual: React.FC<{ episode: Episode }> = ({ episode }) => {
  const frame = useCurrentFrame();
  const isCode = /[;{]|#include/.test(episode.bug.wrong);
  const wrongText = isCode ? episode.bug.wrong : stripMarkdown(episode.bug.wrong);
  const errorText = stripMarkdown(
    briefErrorLines(stripMarkdown(episode.bug.error), episode.bug.wrong, isCode),
  );
  // The code window centres on the culprit line, like the long video's Bug of the Day.
  const culprit = isCode ? bugCulprit(episode.ep, episode.bug.wrong, episode.bug.fixed, episode.bug.error).wrong : undefined;
  const fitted = fitError(errorText, isCode);
  const errorChars = typewriterChars(fitted.text, frame, 24, 1.1);
  const errorH = fitted.height;
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, height: "100%" }}>
      {isCode ? (
        <CodeBlock
          source={wrongText}
          width={W}
          fontSize={chooseFontSize(wrongText, W, H - errorH - 16, 64)}
          maxHeight={H - errorH - 16}
          fillHeight={H - errorH - 16}
          highlightLine={culprit}
        />
      ) : (
        <Panel background={palette.cream} style={{ flex: 1 }}>
          <div
            style={{
              fontFamily: fonts.body,
              fontWeight: 700,
              fontSize: 40,
              lineHeight: 1.35,
              color: palette.ink,
              whiteSpace: "pre-wrap",
            }}
          >
            {wrongText}
          </div>
        </Panel>
      )}
      <Panel background={palette.darkBlue} style={{ minHeight: errorH - 20 }}>
        <div
          style={{
            fontFamily: isCode ? fonts.code : fonts.body,
            fontWeight: isCode ? 500 : 700,
            fontSize: fitted.size,
            lineHeight: 1.3,
            color: palette.tomato,
            whiteSpace: "pre-wrap",
            overflowWrap: "anywhere",
          }}
        >
          {fitted.text.slice(0, errorChars)}
        </div>
      </Panel>
    </div>
  );
};

export const ShortVisualView: React.FC<{
  visual: ShortVisual;
  episode: Episode;
  accent: string;
  durationInFrames: number;
  words?: WordTime[];
}> = ({ visual, episode, accent, durationInFrames, words }) => {
  switch (visual.kind) {
    case "pun":
      return <PunVisual text={visual.text} />;
    case "quiz":
      return <QuizVisual visual={visual} accent={accent} />;
    case "pron":
      return (
        <PronunciationVisual written={visual.written} spoken={visual.spoken} accent={accent} />
      );
    case "boxes":
      return <BoxesVisual boxes={visual.boxes} frames={visual.frames} words={words ?? []} durationInFrames={durationInFrames} />;
    case "bits":
      return <BitsVisual visual={visual} accent={accent} />;
    case "code":
      return (
        <CodeVisual source={visual.source} mode={visual.mode} durationInFrames={durationInFrames} />
      );
    case "bug":
      return <BugVisual episode={episode} />;
    case "analogy":
      return <AnalogyVisual title={visual.title} body={visual.body} accent={accent} />;
    case "terminal":
      return <TerminalVisual lines={visual.lines} />;
    case "text":
      return <TextCard text={visual.text} />;
  }
};
