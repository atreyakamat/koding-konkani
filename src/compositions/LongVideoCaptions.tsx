import { useCallback, useEffect, useMemo, useState } from "react";
import { AbsoluteFill, Sequence, staticFile, useCurrentFrame, useDelayRender } from "remotion";
import { palette } from "../theme/palette";
import { fonts } from "../theme/fonts";
import type { SceneTiming } from "./LongVideo";

const FPS = 30;
const msToFrame = (ms: number): number => Math.round((ms / 1000) * FPS);

/** Max time a caption page stays on screen — see the same note in VoiceTestCaptions.tsx:
 * Piper/whisper timestamps are contiguous (no pauses), so gap-based grouping would merge
 * a whole scene into one page; chunk by elapsed time instead. */
const MAX_PAGE_MS = 1800;

type Word = { text: string; startFrame: number; endFrame: number };
type Page = { startFrame: number; endFrame: number; words: Word[] };

const chunkIntoPages = (words: Word[]): Page[] => {
  const pages: Page[] = [];
  let current: Word[] = [];
  const flush = () => {
    if (current.length === 0) return;
    pages.push({ startFrame: current[0].startFrame, endFrame: current.at(-1)!.endFrame, words: current });
    current = [];
  };
  for (const word of words) {
    const pageStartFrame = current[0]?.startFrame ?? word.startFrame;
    if (current.length > 0 && word.endFrame - pageStartFrame > msToFrame(MAX_PAGE_MS)) {
      flush();
    }
    current.push(word);
  }
  flush();
  return pages;
};

const CaptionPage: React.FC<{ page: Page }> = ({ page }) => {
  const frame = useCurrentFrame() + page.startFrame; // absolute frame, since this is mounted in a Sequence
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 90 }}>
      <div
        style={{
          fontFamily: fonts.body,
          fontWeight: 700,
          fontSize: 42,
          whiteSpace: "pre-wrap",
          textAlign: "center",
          maxWidth: "80%",
          background: "rgba(17, 17, 17, 0.82)",
          padding: "14px 24px",
        }}
      >
        {page.words.map((word, i) => {
          const isActive = word.startFrame <= frame && frame < word.endFrame;
          return (
            <span key={`${word.startFrame}-${i}`} style={{ color: isActive ? palette.butter : palette.white }}>
              {word.text}
              {i < page.words.length - 1 ? " " : ""}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

/** Burnt-in word-highlight captions for the whole episode, lower third. Loads every
 * scene's .captions.json (word timestamps) and converts them to absolute frames. */
export const LongVideoCaptions: React.FC<{ epId: string; sceneTimings: SceneTiming[] }> = ({
  epId,
  sceneTimings,
}) => {
  const [allWords, setAllWords] = useState<Word[] | null>(null);
  const { delayRender, continueRender, cancelRender } = useDelayRender();
  const [handle] = useState(() => delayRender());

  const load = useCallback(async () => {
    try {
      const perScene = await Promise.all(
        sceneTimings.map(async (timing) => {
          const raw: { text: string; startMs: number; endMs: number }[] = await fetch(
            staticFile(`voice/${epId}/scene${timing.scene.id}.captions.json`),
          )
            .then((r) => r.json())
            .catch(() => []);
          return raw.map(
            (w): Word => ({
              text: w.text,
              startFrame: timing.startFrame + msToFrame(w.startMs),
              endFrame: timing.startFrame + msToFrame(w.endMs),
            }),
          );
        }),
      );
      setAllWords(perScene.flat());
      continueRender(handle);
    } catch (e) {
      cancelRender(e);
    }
  }, [epId, sceneTimings, continueRender, cancelRender, handle]);

  useEffect(() => {
    load();
  }, [load]);

  const pages = useMemo(() => (allWords ? chunkIntoPages(allWords) : []), [allWords]);

  if (!allWords) {
    return null;
  }

  return (
    <AbsoluteFill>
      {pages.map((page, i) => (
        <Sequence key={i} from={page.startFrame} durationInFrames={page.endFrame - page.startFrame}>
          <CaptionPage page={page} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
