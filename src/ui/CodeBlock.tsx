import { palette, brutal } from "../theme/palette";
import { fonts } from "../theme/fonts";
import { tokenizeLine } from "../lib/highlight";
import {
  BORDER,
  BOTTOM_EXTRA,
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
  /** Show the line-number gutter (default). A one-line snippet has nothing to number. */
  lineNumbers?: boolean;
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
  lineNumbers = true,
}) => {
  const rows = layoutRows(source, width, fontSize, lineNumbers);
  const rowH = rowHeightPx(fontSize);
  const chrome = chromePx();

  const byHeight = maxHeight ? Math.max(1, Math.floor((maxHeight - chrome) / rowH)) : Infinity;
  const capRows = Math.min(rows.length, maxVisibleLines ?? Infinity, byHeight);
  const contentHeight = capRows * rowH + chrome;
  const panelHeight = fillHeight
    ? Math.max(contentHeight, Math.min(fillHeight, maxHeight ?? fillHeight))
    : contentHeight;

  // Per-row typing state: a row may be highlighted or scrolled to only once it has finished
  // typing; blank rows never are. `lastTyped` is the last row that has started typing.
  const typed = visibleChars ?? Infinity;
  const rowEnd: number[] = [];
  let consumed = 0;
  rows.forEach((row, i) => {
    consumed += row.text.length - row.hang;
    rowEnd.push(consumed);
    if (isLastRowOfLine(rows, i)) consumed += 1;
  });
  const rowStart = rowEnd.map((end, i) => end - (rows[i].text.length - rows[i].hang));
  const lastTyped = rows.reduce((acc, _row, i) => (typed > rowStart[i] ? i : acc), 0);
  const rowDone = (i: number): boolean => typed >= rowEnd[i] && rows[i].text.trim().length > 0;
  const lineDone = (line: number): boolean =>
    rows.every((r, i) => r.line !== line || rowDone(i) || r.text.trim().length === 0) &&
    rows.some((r, i) => r.line === line && rowDone(i));
  const hlActive =
    highlightLine !== undefined && lineDone(highlightLine) ? highlightLine : undefined;

  // Keep the highlighted line's rows centred (else follow the typing); whole rows only,
  // and never past the last row that has been typed.
  const firstHl = hlActive ? rows.findIndex((r) => r.line === hlActive) : -1;
  const hlCount = firstHl >= 0 ? rows.filter((r) => r.line === hlActive).length : 0;
  const anchor = firstHl >= 0 ? firstHl : lastTyped;
  const centredScroll =
    rows.length > capRows
      ? Math.min(
          rows.length - capRows,
          Math.max(0, anchor - Math.floor((capRows - Math.max(1, hlCount)) / 2)),
          Math.max(0, lastTyped - capRows + 1 + (firstHl >= 0 ? hlCount : 0)),
        )
      : 0;
  // Whole LINES, not just whole rows: snap the window to the start of a source line, and hide
  // a trailing line whose wrapped rows would be cut off (a partial line is never drawn).
  let scrollRows = centredScroll;
  while (scrollRows > 0 && !rows[scrollRows].first) scrollRows--;
  let lastRow = Math.min(rows.length - 1, scrollRows + capRows - 1);
  while (lastRow > scrollRows && !isLastRowOfLine(rows, lastRow)) lastRow--;
  if (!isLastRowOfLine(rows, lastRow))
    lastRow = Math.min(rows.length - 1, scrollRows + capRows - 1);

  let remaining = visibleChars ?? Infinity;

  return (
    <div
      style={{
        background: palette.cream,
        border: `${BORDER}px solid ${palette.ink}`,
        boxShadow: `${brutal.shadow}px ${brutal.shadow}px 0 0 ${palette.ink}`,
        padding: `${PADDING_Y}px ${PADDING_X}px ${PADDING_Y + BOTTOM_EXTRA}px`,
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
            const srcLen = row.text.length - row.hang;
            const typedHere = Math.max(0, Math.min(srcLen, remaining));
            remaining = Math.max(0, remaining - srcLen - (isLastRowOfLine(rows, index) ? 1 : 0));
            const shown = typedHere > 0 ? row.text.slice(0, row.hang + typedHere) : "";
            const isHighlighted = hlActive === row.line && row.text.trim().length > 0;
            return (
              <div
                key={index}
                style={{
                  visibility: index > lastRow ? "hidden" : "visible",
                  display: "flex",
                  background: isHighlighted ? palette.butter : "transparent",
                  height: rowH,
                }}
              >
                {lineNumbers ? (
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
                ) : null}
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
