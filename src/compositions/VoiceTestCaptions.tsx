import { useMemo } from "react";
import { AbsoluteFill, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import type { Caption, TikTokPage } from "@remotion/captions";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";

/** Max time a page stays on screen. Kokoro/Piper timestamps are contiguous
 * (no pauses), so gap-based grouping (createTikTokStyleCaptions) would merge
 * the whole clip into one page; chunk by elapsed time instead. */
const MAX_PAGE_MS = 1800;

const chunkIntoPages = (captions: Caption[]): TikTokPage[] => {
  const pages: TikTokPage[] = [];
  let current: Caption[] = [];

  const flush = () => {
    if (current.length === 0) {
      return;
    }
    const startMs = current[0].startMs;
    const endMs = current[current.length - 1].endMs;
    pages.push({
      text: current.map((c) => c.text).join(""),
      startMs,
      tokens: current.map((c) => ({ text: c.text, fromMs: c.startMs, toMs: c.endMs })),
      durationMs: endMs - startMs,
    });
    current = [];
  };

  for (const caption of captions) {
    const pageStart = current[0]?.startMs ?? caption.startMs;
    if (current.length > 0 && caption.endMs - pageStart > MAX_PAGE_MS) {
      flush();
    }
    current.push(caption);
  }
  flush();

  return pages;
};

const CaptionPage: React.FC<{ page: TikTokPage }> = ({ page }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const absoluteTimeMs = page.startMs + (frame / fps) * 1000;

  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 140 }}>
      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: 56,
          whiteSpace: "pre",
          textAlign: "center",
          maxWidth: "85%",
          background: palette.ink,
          padding: "20px 32px",
        }}
      >
        {page.tokens.map((token, tokenIndex) => {
          const isActive = token.fromMs <= absoluteTimeMs && token.toMs > absoluteTimeMs;
          return (
            <span
              key={`${token.fromMs}-${tokenIndex}`}
              style={{ color: isActive ? palette.butter : palette.white }}
            >
              {token.text}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/** Simple word-highlighted captions, TikTok-style pages, for the voice test. */
export const VoiceTestCaptions: React.FC<{ captions: Caption[] }> = ({ captions }) => {
  const { fps } = useVideoConfig();
  const pages = useMemo(() => chunkIntoPages(captions), [captions]);

  return (
    <AbsoluteFill>
      {pages.map((page, index) => {
        const startFrame = Math.round((page.startMs / 1000) * fps);
        const endFrame = Math.round(((page.startMs + page.durationMs) / 1000) * fps);
        const durationInFrames = endFrame - startFrame;
        if (durationInFrames <= 0) {
          return null;
        }
        return (
          <Sequence key={index} from={startFrame} durationInFrames={durationInFrames}>
            <CaptionPage page={page} />
          </Sequence>
        );
      })}
    </AbsoluteFill>
  );
};
