import type { TransitionPresentation, TransitionPresentationComponentProps } from "@remotion/transitions";
import { AbsoluteFill } from "remotion";
import { palette } from "../theme/palette";

/** Shared max length per docs/STYLE.md: "Max length 12 frames (0.4s)". */
export const TRANSITION_FRAMES = 12;

type Props = Record<string, unknown>;

const presentation = (
  Component: (p: TransitionPresentationComponentProps<Props>) => React.ReactNode,
): TransitionPresentation<Props> => ({ component: Component, props: {} });

/** Hard cut: hold 2 frames of flat white, then reveal the next scene. No blur. */
export const hardCutImpact = () =>
  presentation(({ presentationProgress, children, presentationDirection }) => {
    const flashFrames = 2 / TRANSITION_FRAMES;
    const showFlash = presentationProgress < flashFrames;
    if (presentationDirection === "exiting") {
      return showFlash ? null : children;
    }
    return (
      <AbsoluteFill>
        {children}
        {showFlash ? <AbsoluteFill style={{ background: palette.white }} /> : null}
      </AbsoluteFill>
    );
  });

/** Push-in: incoming scene scales from 1.06 to 1.0 while a vertical wipe reveals it. */
export const pushIn = () =>
  presentation(({ presentationProgress, children, presentationDirection }) => {
    if (presentationDirection === "exiting") {
      return <AbsoluteFill style={{ opacity: 1 - presentationProgress }}>{children}</AbsoluteFill>;
    }
    const scale = 1.06 - 0.06 * presentationProgress;
    return (
      <AbsoluteFill
        style={{
          clipPath: `inset(0 0 ${(1 - presentationProgress) * 100}% 0)`,
          scale: `${scale} ${scale}`,
        }}
      >
        {children}
      </AbsoluteFill>
    );
  });

/** Window pop: the incoming scene springs up from a small centred rectangle. */
export const windowPop = () =>
  presentation(({ presentationProgress, children, presentationDirection }) => {
    if (presentationDirection === "exiting") {
      return presentationProgress > 0.5 ? null : children;
    }
    const t = Math.min(1, presentationProgress / 0.7);
    const eased = 1 - (1 - t) * (1 - t);
    const scaleY = 0.05 + 0.95 * eased;
    return (
      <AbsoluteFill style={{ background: palette.ink, display: "flex", alignItems: "center" }}>
        <AbsoluteFill style={{ scale: `1 ${scaleY}`, transformOrigin: "center" }}>{children}</AbsoluteFill>
      </AbsoluteFill>
    );
  });

/** Whip: fast horizontal slide with a 3-frame shake on landing. */
export const whip = () =>
  presentation(({ presentationProgress, children, presentationDirection }) => {
    const sign = presentationDirection === "exiting" ? -1 : 1;
    const base = presentationDirection === "exiting" ? presentationProgress : 1 - presentationProgress;
    const translateX = sign * base * 100;
    const settleWindow = 3 / TRANSITION_FRAMES;
    const isSettling = presentationDirection === "entering" && presentationProgress > 1 - settleWindow;
    const shake = isSettling ? Math.sin(presentationProgress * 60) * 6 * (1 - presentationProgress) * 10 : 0;
    return (
      <AbsoluteFill style={{ translate: `${translateX}% 0px`, filter: undefined }}>
        <AbsoluteFill style={{ translate: `${shake}px 0px` }}>{children}</AbsoluteFill>
      </AbsoluteFill>
    );
  });

/** Split: the entering panel slides over the exiting one from the right (wrong -> fixed code). */
export const split = () =>
  presentation(({ presentationProgress, children, presentationDirection }) => {
    if (presentationDirection === "exiting") {
      return children;
    }
    const x = (1 - presentationProgress) * 100;
    return (
      <AbsoluteFill
        style={{
          translate: `${x}% 0px`,
          borderLeft: x > 0.1 ? `6px solid ${palette.ink}` : undefined,
        }}
      >
        {children}
      </AbsoluteFill>
    );
  });
