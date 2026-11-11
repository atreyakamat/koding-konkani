# Fonts: sources and licences

Self-hosted copies of the three Google Fonts the design system uses, so a render never
depends on fonts.gstatic.com being reachable (a DNS blip there failed renders on 1 Nov 2026).
They are the exact latin-subset woff2 files `@remotion/google-fonts` 4.0.539 would fetch;
Space Grotesk and JetBrains Mono are variable fonts, one file each covers weights 500 and 700.

- Licence for all three: **SIL Open Font License 1.1** (OFL). Free for commercial use, embedding
  and video. No attribution required on screen; the licence text lives with each family on
  Google Fonts. Safe for YouTube and Instagram.
- Downloaded 2026-11-01 with `curl` from the URLs below.

| File | Family / weights | Source | Licence | Attribution |
|---|---|---|---|---|
| ArchivoBlack-Regular.woff2 | Archivo Black 400 | https://fonts.gstatic.com/s/archivoblack/v23/HTxqL289NzCGg4MzN6KJ7eW6CYyF_g.woff2 (https://fonts.google.com/specimen/Archivo+Black) | OFL 1.1 | none |
| SpaceGrotesk-Variable.woff2 | Space Grotesk 300–700 (used: 500, 700) | https://fonts.gstatic.com/s/spacegrotesk/v22/V8mDoQDjQSkFtoMM3T6r8E7mPbF4Cw.woff2 (https://fonts.google.com/specimen/Space+Grotesk) | OFL 1.1 | none |
| JetBrainsMono-Variable.woff2 | JetBrains Mono 100–800 (used: 500, 700) | https://fonts.gstatic.com/s/jetbrainsmono/v24/tDbV2o-flEEny0FZhsfKu5WU4xD7OwE.woff2 (https://fonts.google.com/specimen/JetBrains+Mono) | OFL 1.1 | none |
