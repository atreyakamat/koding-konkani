/** Design tokens: neo-brutalism, pastel. Black and white are accents only. */
export const palette = {
  tomato: "#FF6F59",
  peach: "#FFD8BE",
  apricot: "#FFB88A",
  butter: "#FFE58A",
  cream: "#FFF4EC",
  pastelBlue: "#BFD7FF",
  mint: "#B8F2D0",
  lilac: "#D9C9FF",
  darkBlue: "#1E2A4A",
  ink: "#111111",
  white: "#FFFFFF",
} as const;

export type ColourName = keyof typeof palette;

/** Shared look: thick borders, hard offset shadows. */
export const brutal = {
  border: 4,
  borderThick: 5,
  shadow: 8,
} as const;
