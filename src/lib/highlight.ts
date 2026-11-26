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

export type CodeLang = "c" | "python" | "java" | "yaml" | "shell" | "dockerfile";

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

const JAVA_KEYWORDS = new Set([
  "abstract",
  "assert",
  "boolean",
  "break",
  "byte",
  "case",
  "catch",
  "char",
  "class",
  "const",
  "continue",
  "default",
  "do",
  "double",
  "else",
  "enum",
  "extends",
  "final",
  "finally",
  "float",
  "for",
  "goto",
  "if",
  "implements",
  "import",
  "instanceof",
  "int",
  "interface",
  "long",
  "native",
  "new",
  "package",
  "private",
  "protected",
  "public",
  "return",
  "short",
  "static",
  "strictfp",
  "super",
  "switch",
  "synchronized",
  "this",
  "throw",
  "throws",
  "transient",
  "try",
  "void",
  "volatile",
  "while",
  "var",
  "record",
  "yield",
  "sealed",
  "permits",
  "true",
  "false",
  "null",
]);

/** comment | text block or string | annotation | number | word | other. */
const JAVA_PATTERN =
  /(\/\/.*$)|("""|"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')|(@\w+)|(\b\d[\d_]*\.?\d*[LlFfDd]?\b)|(\b[A-Za-z_]\w*\b)|(.)/g;

const tokenizeJava = (line: string): Token[] => {
  const tokens: Token[] = [];
  for (const match of line.matchAll(JAVA_PATTERN)) {
    const [, comment, str, annotation, number, word, other] = match;
    if (comment !== undefined) tokens.push({ text: comment, color: "rgba(17, 17, 17, 0.45)" });
    else if (str !== undefined) tokens.push({ text: str, color: "#1f7a4c" });
    else if (annotation !== undefined) tokens.push({ text: annotation, color: palette.tomato });
    else if (number !== undefined) tokens.push({ text: number, color: palette.darkBlue });
    else if (word !== undefined) {
      const isKeyword = JAVA_KEYWORDS.has(word);
      tokens.push({
        text: word,
        color: isKeyword ? palette.darkBlue : palette.ink,
        bold: isKeyword,
      });
    } else if (other !== undefined) tokens.push({ text: other, color: palette.ink });
  }
  return tokens;
};

const YAML_PATTERN =
  /(#.*$)|("(?:[^"\\]|\\.)*"|'[^']*')|((?<=^\s*-?\s*)[\w.\-/]+(?=\s*:))|(\b(?:true|false|null|yes|no|on|off)\b)|(\b\d[\d.]*\b)|(.)/g;

const tokenizeYaml = (line: string): Token[] => {
  const tokens: Token[] = [];
  for (const match of line.matchAll(YAML_PATTERN)) {
    const [, comment, str, key, literal, number, other] = match;
    if (comment !== undefined) tokens.push({ text: comment, color: "rgba(17, 17, 17, 0.45)" });
    else if (str !== undefined) tokens.push({ text: str, color: "#1f7a4c" });
    else if (key !== undefined) tokens.push({ text: key, color: palette.darkBlue, bold: true });
    else if (literal !== undefined) tokens.push({ text: literal, color: palette.tomato });
    else if (number !== undefined) tokens.push({ text: number, color: palette.darkBlue });
    else if (other !== undefined) tokens.push({ text: other, color: palette.ink });
  }
  return tokens;
};

const SHELL_KEYWORDS = new Set([
  "if",
  "then",
  "else",
  "elif",
  "fi",
  "for",
  "in",
  "do",
  "done",
  "while",
  "until",
  "case",
  "esac",
  "function",
  "return",
  "exit",
  "export",
  "local",
  "set",
  "unset",
  "readonly",
  "cd",
  "echo",
  "sudo",
]);

const SHELL_PATTERN =
  /(#.*$)|("(?:[^"\\]|\\.)*"|'[^']*')|(\$\{?\w+\}?)|(--?[\w-]+)|(\b[A-Za-z_][\w-]*\b)|(.)/g;

const tokenizeShell = (line: string): Token[] => {
  const tokens: Token[] = [];
  for (const match of line.matchAll(SHELL_PATTERN)) {
    const [, comment, str, variable, flag, word, other] = match;
    if (comment !== undefined) tokens.push({ text: comment, color: "rgba(17, 17, 17, 0.45)" });
    else if (str !== undefined) tokens.push({ text: str, color: "#1f7a4c" });
    else if (variable !== undefined) tokens.push({ text: variable, color: palette.tomato });
    else if (flag !== undefined) tokens.push({ text: flag, color: palette.darkBlue });
    else if (word !== undefined) {
      const isKeyword = SHELL_KEYWORDS.has(word);
      tokens.push({
        text: word,
        color: isKeyword ? palette.darkBlue : palette.ink,
        bold: isKeyword,
      });
    } else if (other !== undefined) tokens.push({ text: other, color: palette.ink });
  }
  return tokens;
};

const DOCKERFILE_INSTRUCTIONS = new Set([
  "ARG",
  "CMD",
  "COPY",
  "ENTRYPOINT",
  "ENV",
  "EXPOSE",
  "FROM",
  "HEALTHCHECK",
  "LABEL",
  "ONBUILD",
  "RUN",
  "SHELL",
  "STOPSIGNAL",
  "USER",
  "VOLUME",
  "WORKDIR",
  "ADD",
  "AS",
]);

const DOCKERFILE_PATTERN =
  /(#.*$)|("(?:[^"\\]|\\.)*"|'[^']*')|(--?[\w-]+(?:=[^\s]*)?)|(\b[A-Za-z0-9_][\w.-]*\b)|(.)/g;

const tokenizeDockerfile = (line: string): Token[] => {
  const tokens: Token[] = [];
  let firstWord = true;
  for (const match of line.matchAll(DOCKERFILE_PATTERN)) {
    const [, comment, str, flag, word, other] = match;
    if (comment !== undefined) tokens.push({ text: comment, color: "rgba(17, 17, 17, 0.45)" });
    else if (str !== undefined) tokens.push({ text: str, color: "#1f7a4c" });
    else if (flag !== undefined) tokens.push({ text: flag, color: palette.darkBlue });
    else if (word !== undefined) {
      const isInstruction = firstWord && DOCKERFILE_INSTRUCTIONS.has(word.toUpperCase());
      tokens.push({
        text: word,
        color: isInstruction ? palette.tomato : palette.ink,
        bold: isInstruction,
      });
      if (firstWord) firstWord = false;
    } else if (other !== undefined) {
      if (other.trim() !== "") firstWord = false;
      tokens.push({ text: other, color: palette.ink });
    }
  }
  return tokens;
};

/** Minimal tokenizer: comments, strings, numbers, keywords (C by default; Python, Java, YAML, shell and Dockerfile by lang). */
export const tokenizeLine = (line: string, lang: CodeLang = "c"): Token[] => {
  if (lang === "python") return tokenizePython(line);
  if (lang === "java") return tokenizeJava(line);
  if (lang === "yaml") return tokenizeYaml(line);
  if (lang === "shell") return tokenizeShell(line);
  if (lang === "dockerfile") return tokenizeDockerfile(line);
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
