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
  // C++ (the C++ course); none of these is an identifier in the C course's programs.
  "class",
  "template",
  "typename",
  "namespace",
  "using",
  "public",
  "private",
  "protected",
  "virtual",
  "override",
  "final",
  "nullptr",
  "new",
  "delete",
  "auto",
  "constexpr",
  "explicit",
  "noexcept",
  "try",
  "catch",
  "throw",
  "operator",
  "this",
  "decltype",
]);

const TOKEN_PATTERN =
  /(\/\/.*$)|(#\w+.*$)|("(?:[^"\\]|\\.)*")|('(?:[^'\\]|\\.)*')|(\b\d+\.?\d*\b)|(\b[A-Za-z_]\w*\b)|(.)/gm;

export type CodeLang = "c" | "python";

const PY_KEYWORDS = new Set([
  "and",
  "as",
  "assert",
  "async",
  "await",
  "break",
  "case",
  "class",
  "continue",
  "def",
  "del",
  "elif",
  "else",
  "except",
  "finally",
  "for",
  "from",
  "global",
  "if",
  "import",
  "in",
  "is",
  "lambda",
  "match",
  "nonlocal",
  "not",
  "or",
  "pass",
  "raise",
  "return",
  "try",
  "while",
  "with",
  "yield",
  "True",
  "False",
  "None",
]);

/** comment | string (optional f/r/b prefix; triple or single quotes) | decorator | number | word | other. */
const PY_PATTERN =
  /(#.*$)|([fFrRbB]{0,2}(?:"""[^]*?(?:"""|$)|'''[^]*?(?:'''|$)|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'))|(@\w+)|(\b\d[\d_]*\.?\d*(?:[eE][-+]?\d+)?\b)|(\b[A-Za-z_]\w*\b)|(.)/gm;

const tokenizePython = (line: string): Token[] => {
  const tokens: Token[] = [];
  for (const match of line.matchAll(PY_PATTERN)) {
    const [, comment, str, decorator, number, word, other] = match;
    if (comment !== undefined) tokens.push({ text: comment, color: "rgba(17, 17, 17, 0.45)" });
    else if (str !== undefined) tokens.push({ text: str, color: "#1f7a4c" });
    else if (decorator !== undefined) tokens.push({ text: decorator, color: palette.tomato });
    else if (number !== undefined) tokens.push({ text: number, color: palette.darkBlue });
    else if (word !== undefined) {
      const isKeyword = PY_KEYWORDS.has(word);
      tokens.push({
        text: word,
        color: isKeyword ? palette.darkBlue : palette.ink,
        bold: isKeyword,
      });
    } else if (other !== undefined) tokens.push({ text: other, color: palette.ink });
  }
  return tokens;
};

/** Minimal tokenizer: comments, strings, numbers, keywords (C by default; Python with lang="python"). */
export const tokenizeLine = (line: string, lang: CodeLang = "c"): Token[] => {
  if (lang === "python") return tokenizePython(line);
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
