import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { tokenizeLine } from "../lib/highlight";
import {
  BORDER,
  GUTTER_CH,
  GUTTER_GAP,
  PADDING_X,
  PADDING_Y,
  chromePx,
  layoutRows,
  rowHeightPx,
} from "../lib/codeLayout";

export type CodeBlockProps = {
  source: string;
  /** 1-indexed line to highlight in butter, as if `[HL n]` fired. */
  highlightLine?: number;
  /** Total characters to reveal, for the typewriter effect. Defaults to the full source. */
  visibleChars?: number;
  /** Fixed font size; long lines wrap onto extra rows instead of shrinking the text. */
  fontSize?: number;
  /** Panel width in px (the source wraps to fit it). */
  width?: number;
  /** Caps the panel to this many rows; scrolls by whole rows to keep `highlightLine` in view. */
  maxVisibleLines?: number;
  /** Caps the panel height in px (rounded down to whole rows). */
  maxHeight?: number;
  /** Stretch the panel up to this height (code centred) so it uses the free space. */
  fillHeight?: number;
};

/** Code panel: cream background, JetBrains Mono, line numbers, token colours, butter line highlight.
 * Rows are whole: the panel height is exactly N row heights plus chrome, so no line is ever cut. */
export const CodeBlock: React.FC<CodeBlockProps> = ({
  source,
  highlightLine,
  visibleChars,
  fontSize = 40,
  width = 860,
  maxVisibleLines,
  maxHeight,
  fillHeight,
}) => {
  const rows = layoutRows(source, width, fontSize);
  const rowH = rowHeightPx(fontSize);
  const chrome = chromePx();

  const byHeight = maxHeight ? Math.max(1, Math.floor((maxHeight - chrome) / rowH)) : Infinity;
  const capRows = Math.min(rows.length, maxVisibleLines ?? Infinity, byHeight);
  const contentHeight = capRows * rowH + chrome;
  const panelHeight = fillHeight
    ? Math.max(contentHeight, Math.min(fillHeight, maxHeight ?? fillHeight))
    : contentHeight;

  // Keep the highlighted line's rows centred; integer rows only.
  const firstHl = highlightLine ? rows.findIndex((r) => r.line === highlightLine) : -1;
  const hlCount = firstHl >= 0 ? rows.filter((r) => r.line === highlightLine).length : 0;
  const scrollRows =
    rows.length > capRows
      ? Math.min(
          rows.length - capRows,
          Math.max(0, (firstHl >= 0 ? firstHl : 0) - Math.floor((capRows - hlCount) / 2)),
        )
      : 0;

  let remaining = visibleChars ?? Infinity;

  return (
    <div
      style={{
        background: palette.cream,
        border: `${BORDER}px solid ${palette.ink}`,
        boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
        padding: `${PADDING_Y}px ${PADDING_X}px`,
        width,
        height: panelHeight,
        overflow: "hidden",
        boxSizing: "border-box",
        fontFamily: fonts.code,
        fontSize,
        lineHeight: 1.5,
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      <div style={{ height: capRows * rowH, overflow: "hidden" }}>
        <div style={{ translate: `0px ${-scrollRows * rowH}px` }}>
          {rows.map((row, index) => {
            const visibleInRow = Math.max(0, Math.min(row.text.length, remaining));
            remaining = Math.max(
              0,
              remaining - row.text.length - (isLastRowOfLine(rows, index) ? 1 : 0),
            );
            const shown = row.text.slice(0, visibleInRow);
            const isHighlighted = highlightLine === row.line;
            return (
              <div
                key={index}
                style={{
                  display: "flex",
                  background: isHighlighted ? palette.butter : "transparent",
                  height: rowH,
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
                  {row.first ? row.line : ""}
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
    </div>
  );
};

const isLastRowOfLine = (rows: { line: number }[], index: number): boolean =>
  index === rows.length - 1 || rows[index + 1].line !== rows[index].line;
