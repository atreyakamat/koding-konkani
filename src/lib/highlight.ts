import { palette } from "../theme/palette";

/** A coloured run of source text, for CodeBlock to render token by token. */
export type Token = { text: string; color: string; bold?: boolean };

const KEYWORDS = new Set([
  "int",
  "char",
  "float",
  "double",
  "void",
  "if",
  "else",
  "for",
  "while",
  "do",
  "return",
  "struct",
  "typedef",
  "const",
  "unsigned",
  "signed",
  "short",
  "long",
  "break",
  "continue",
  "switch",
  "case",
  "default",
  "sizeof",
  "bool",
  "true",
  "false",
  "static",
  "enum",
  "union",
  "goto",
  "extern",
  "volatile",
  "inline",
]);

const TOKEN_PATTERN =
  /(\/\/.*$)|(#\w+.*$)|("(?:[^"\\]|\\.)*")|('(?:[^'\\]|\\.)*')|(\b\d+\.?\d*\b)|(\b[A-Za-z_]\w*\b)|(.)/gm;

/** Minimal C tokenizer: comments, preprocessor lines, strings, numbers, keywords. */
export const tokenizeLine = (line: string): Token[] => {
  const tokens: Token[] = [];
  for (const match of line.matchAll(TOKEN_PATTERN)) {
    const [, comment, preprocessor, dquote, squote, number, word, other] = match;
    if (comment !== undefined) {
      tokens.push({ text: comment, color: "rgba(17, 17, 17, 0.45)" });
    } else if (preprocessor !== undefined) {
      tokens.push({ text: preprocessor, color: palette.tomato });
    } else if (dquote !== undefined || squote !== undefined) {
      tokens.push({ text: dquote ?? squote ?? "", color: "#1f7a4c" });
    } else if (number !== undefined) {
      tokens.push({ text: number, color: palette.darkBlue });
    } else if (word !== undefined) {
      const isKeyword = KEYWORDS.has(word);
      tokens.push({
        text: word,
        color: isKeyword ? palette.darkBlue : palette.ink,
        bold: isKeyword,
      });
    } else if (other !== undefined) {
      tokens.push({ text: other, color: palette.ink });
    }
  }
  return tokens;
};
