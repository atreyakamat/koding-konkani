import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { tokenizeLine } from "../lib/highlight";

export type CodeBlockProps = {
  source: string;
  /** 1-indexed line to highlight in butter, as if `[HL n]` fired. */
  highlightLine?: number;
  /** Total characters to reveal, for the typewriter effect. Defaults to the full source. */
  visibleChars?: number;
  /** Upper bound; shrinks so the longest line fits `width` (JetBrains Mono, ~0.6em per char). */
  fontSize?: number;
  width?: number;
  /** Caps the panel to this many visible lines and auto-scrolls to keep `highlightLine` in view. */
  maxVisibleLines?: number;
  /** A trailing `// comment` is cut with an ellipsis so the line stays within this many chars. */
  maxLineChars?: number;
};

const PADDING_X = 28;
const PADDING_Y = 20;
const GUTTER_GAP = 20;
const CHAR_EM = 0.6;
const GUTTER_CH = 2.5;
const MIN_FONT_SIZE = 20;

/** Index of a `//` that starts a comment (i.e. not inside a string literal), or -1. */
const commentStart = (line: string): number => {
  let inString = false;
  for (let i = 0; i < line.length - 1; i++) {
    const ch = line[i];
    if (ch === "\\" && inString) {
      i++;
      continue;
    }
    if (ch === '"') inString = !inString;
    if (!inString && ch === "/" && line[i + 1] === "/") return i;
  }
  return -1;
};

/** Shortens only the comment part of an over-long line, never the code before it. */
const shortenComment = (line: string, maxChars: number): string => {
  if (line.length <= maxChars) return line;
  const at = commentStart(line);
  if (at === -1) return line;
  const keep = maxChars - 1;
  if (keep <= at + 3) return `${line.slice(0, at + 2)}…`;
  return `${line.slice(0, keep).trimEnd()}…`;
};

/** Code panel: cream background, JetBrains Mono, line numbers, token colours, butter line highlight. */
export const CodeBlock: React.FC<CodeBlockProps> = ({
  source,
  highlightLine,
  visibleChars,
  fontSize: maxFontSize = 38,
  width,
  maxVisibleLines,
  maxLineChars = 58,
}) => {
  const lines = source.split("\n").map((line) => shortenComment(line, maxLineChars));
  const longest = Math.max(1, ...lines.map((line) => line.length));

  // Fit: gutter (2.5ch + gap) + longest line must sit inside the padded, bordered width.
  let fontSize = maxFontSize;
  if (width) {
    const available = width - 2 * PADDING_X - 2 * brutal.borderThick - GUTTER_GAP;
    const perEm = GUTTER_CH * CHAR_EM + longest * CHAR_EM;
    fontSize = Math.max(MIN_FONT_SIZE, Math.min(maxFontSize, Math.floor(available / perEm)));
  }
  const lineHeightPx = fontSize * 1.5;

  const budget = visibleChars ?? Infinity;
  let remaining = budget;

  const scrollLines = maxVisibleLines
    ? Math.min(
        Math.max(0, lines.length - maxVisibleLines),
        Math.max(0, (highlightLine ?? 1) - 1 - Math.floor(maxVisibleLines / 2)),
      )
    : 0;

  return (
    <div
      style={{
        background: palette.cream,
        border: `${brutal.borderThick}px solid ${palette.ink}`,
        boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
        padding: `${PADDING_Y}px ${PADDING_X}px`,
        width,
        // Whole lines only: padding and the border are added on top of N full line heights.
        height: maxVisibleLines
          ? maxVisibleLines * lineHeightPx + 2 * PADDING_Y + 2 * brutal.borderThick
          : undefined,
        overflow: maxVisibleLines || width ? "hidden" : undefined,
        boxSizing: "border-box",
        fontFamily: fonts.code,
        fontSize,
        lineHeight: 1.5,
      }}
    >
      <div style={{ translate: `0px ${-scrollLines * lineHeightPx}px` }}>
        {lines.map((line, index) => {
          const lineNumber = index + 1;
          const visibleInLine = Math.max(0, Math.min(line.length, remaining));
          remaining = Math.max(0, remaining - line.length - 1);
          const shown = line.slice(0, visibleInLine);
          const isHighlighted = highlightLine === lineNumber;
          return (
            <div
              key={lineNumber}
              style={{
                display: "flex",
                background: isHighlighted ? palette.butter : "transparent",
                height: lineHeightPx,
              }}
            >
              <span
                style={{
                  color: "rgba(17, 17, 17, 0.4)",
                  width: `${GUTTER_CH}ch`,
                  textAlign: "right",
                  marginRight: GUTTER_GAP,
                  userSelect: "none",
                  flexShrink: 0,
                }}
              >
                {lineNumber}
              </span>
              <span style={{ whiteSpace: "pre" }}>
                {tokenizeLine(shown).map((token, tokenIndex) => (
                  <span
                    key={tokenIndex}
                    style={{ color: token.color, fontWeight: token.bold ? 700 : 500 }}
                  >
                    {token.text}
                  </span>
                ))}
              </span>
            </div>
          );
        })}
      </div>
    </div>
  );
};
