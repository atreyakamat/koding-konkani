import { useCurrentFrame } from "remotion";
import type { Episode } from "../lib/episode";
import type { ShortVisual } from "../lib/shortVisual";
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

/** Big text card. "s·s" separated parts stack as their own lines (a list reads as a list),
 * sized to fill the slot; long words wrap instead of clipping. */
const TextCard: React.FC<{ text: string; background?: string }> = ({
  text,
  background = palette.cream,
}) => {
  const parts = text
    .split(/\s·\s|\n/)
    .map((p) => p.trim())
    .filter(Boolean);
  const longest = Math.max(...parts.map((p) => p.length), 1);
  const base = parts.length >= 3 ? 76 : parts.length === 2 ? 88 : 96;
  const size = Math.min(
    fitText(parts.join(" ").length, base),
    Math.floor(W / (longest * 0.62)) + 40,
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
        gap: 28,
      }}
    >
      {parts.map((part, i) => (
        <div
          key={i}
          style={{
            fontFamily: fonts.title,
            fontSize: Math.max(56, size),
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

const TerminalVisual: React.FC<{ lines: string[] }> = ({ lines }) => {
  const frame = useCurrentFrame();
  return (
    <Panel
      background={palette.darkBlue}
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        gap: 18,
      }}
    >
      {lines.map((line, i) => (
        <div
          key={i}
          style={{
            fontFamily: fonts.code,
            fontWeight: 700,
            fontSize: line.length > 24 ? 40 : 48,
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
  const font = chooseFontSize(source, W, H);
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
    return <TextCard text={[...visual.options, visual.question].filter(Boolean).join("s·s")} />;
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
          {text.join(" s·s ")}
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

const BoxesVisual: React.FC<{
  boxes: { name: string; value: string; address?: string }[];
}> = ({ boxes }) => {
  const frame = useCurrentFrame();
  const n = boxes.length;
  const gap = 20;
  const boxW = Math.floor((W - gap * (n - 1)) / n);
  const boxH = Math.min(340, Math.round(boxW * 1.25));
  return (
    <div
      style={{
        display: "flex",
        gap,
        height: "100%",
        alignItems: "center",
        justifyContent: "center",
      }}
    >
      {boxes.map((box, i) => {
        const p = reveal(frame, 6 + i * 5, 8);
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
              background: palette.cream,
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
            <div style={{ fontFamily: fonts.title, fontSize: nameFont, color: palette.ink }}>
              {box.name}
            </div>
            <div
              style={{
                fontFamily: fonts.code,
                fontWeight: 700,
                fontSize: valueFont,
                color: palette.ink,
              }}
            >
              {box.value}
            </div>
          </div>
        );
      })}
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

/** The bug reveal: the wrong code/claim/value, then the key error line underneath. */
const BugVisual: React.FC<{ episode: Episode }> = ({ episode }) => {
  const frame = useCurrentFrame();
  const isCode = /[;{]|#include/.test(episode.bug.wrong);
  const wrongText = isCode ? episode.bug.wrong : stripMarkdown(episode.bug.wrong);
  const errorText = stripMarkdown(
    briefErrorLines(stripMarkdown(episode.bug.error), episode.bug.wrong, isCode),
  );
  const errorChars = typewriterChars(errorText, frame, 24, 1.1);
  const errorH = 200;
  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 16, height: "100%" }}>
      {isCode ? (
        <CodeBlock source={wrongText} width={W} fontSize={40} maxHeight={H - errorH - 16} />
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
            fontSize: 30,
            lineHeight: 1.3,
            color: palette.tomato,
            whiteSpace: "pre-wrap",
            overflowWrap: "anywhere",
          }}
        >
          {errorText.slice(0, errorChars)}
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
}> = ({ visual, episode, accent, durationInFrames }) => {
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
      return <BoxesVisual boxes={visual.boxes} />;
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
