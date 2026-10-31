import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { tokenizeLine } from "../lib/highlight";

export type CodeBlockProps = {
  source: string;
  /** 1-indexed line to highlight in butter, as if `[HL n]` fired. */
  highlightLine?: number;
  /** Total characters to reveal, for the typewriter effect. Defaults to the full source. */
  visibleChars?: number;
  fontSize?: number;
  width?: number;
  /** Caps the panel to this many visible lines and auto-scrolls to keep `highlightLine` in view. */
  maxVisibleLines?: number;
};

/** Code panel: cream background, JetBrains Mono, line numbers, token colours, butter line highlight. */
export const CodeBlock: React.FC<CodeBlockProps> = ({
  source,
  highlightLine,
  visibleChars,
  fontSize = 38,
  width,
  maxVisibleLines,
}) => {
  const lines = source.split("\n");
  const budget = visibleChars ?? Infinity;
  let remaining = budget;
  const lineHeightPx = fontSize * 1.5;

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
        padding: "20px 28px",
        width,
        height: maxVisibleLines ? maxVisibleLines * lineHeightPx + 40 : undefined,
        overflow: maxVisibleLines ? "hidden" : undefined,
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
                minHeight: "1.5em",
              }}
            >
              <span
                style={{
                  color: "rgba(17, 17, 17, 0.4)",
                  width: "2.5ch",
                  textAlign: "right",
                  marginRight: 20,
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
