import { useCurrentFrame, useVideoConfig, interpolate, Easing } from "remotion";
import { palette } from "../theme/palette";
import { impactShakeX } from "../lib/motion";

export type XecxecPose = "idle" | "scuttle" | "clawsUp" | "shellShake" | "snap" | "wave" | "dance";

export type XecxecProps = {
  pose: XecxecPose;
  size?: number;
  flip?: boolean;
  /** Overrides useCurrentFrame(), for stills and tests. */
  frame?: number;
};

const BLINK_EVERY_SECONDS = 3;
const BLINK_FRAMES = 4;

/**
 * Xecxec: a tomato-shelled crab, thick ink outline, eyes on stalks, two big claws.
 * Pure SVG so it stays sharp at any render scale. Never speaks; reacts with animation only.
 */
export const Xecxec: React.FC<XecxecProps> = ({
  pose,
  size = 220,
  flip = false,
  frame: frameProp,
}) => {
  const { fps } = useVideoConfig();
  const currentFrame = useCurrentFrame();
  const frame = frameProp ?? currentFrame;

  const blinkCycle = frame % (BLINK_EVERY_SECONDS * fps);
  const eyeOpen = blinkCycle < BLINK_FRAMES ? 0.08 : 1;

  // Idle bob: every pose gets a gentle breathing motion underneath its own animation.
  const bob = Math.sin((frame / fps) * Math.PI) * 3;

  let bodyTranslateX = 0;
  let bodyTranslateY = 0;
  let bodyRotate = 0;
  let leftClawRotate = -18;
  let rightClawRotate = 18;
  let legPhase = 0;

  if (pose === "scuttle") {
    bodyTranslateX = interpolate(frame, [0, 14], [-140, 0], {
      easing: Easing.out(Easing.cubic),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    legPhase = frame;
  } else if (pose === "clawsUp") {
    const lift = interpolate(frame, [0, 10], [0, 1], {
      easing: Easing.spring({ damping: 12 }),
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    leftClawRotate = -18 - lift * 70;
    rightClawRotate = 18 + lift * 70;
  } else if (pose === "shellShake") {
    bodyTranslateX = impactShakeX(frame, 0, 10);
    bodyRotate = impactShakeX(frame, 0, 4);
  } else if (pose === "snap") {
    const snapProgress = interpolate(frame, [0, 3, 6], [0, 1, 0.4], {
      extrapolateLeft: "clamp",
      extrapolateRight: "clamp",
    });
    rightClawRotate = 18 + snapProgress * 40;
  } else if (pose === "dance") {
    // Two bounces per second, body sways, claws pump alternately, legs stomp.
    const beat = (frame / fps) * Math.PI * 2 * 1.5;
    bodyTranslateY = -Math.abs(Math.sin(beat)) * 22;
    bodyRotate = Math.sin(beat) * 7;
    leftClawRotate = -18 - (Math.sin(beat) * 0.5 + 0.5) * 75;
    rightClawRotate = 18 + (Math.cos(beat) * 0.5 + 0.5) * 75;
    legPhase = frame * 2;
  } else if (pose === "wave") {
    rightClawRotate = 18 + Math.sin((frame / fps) * Math.PI * 2) * 30;
  }

  const legWiggle = Math.sin(legPhase / 2) * 10;
  // Face: smile by default, worried frown while the shell shakes.
  const mouthPath =
    pose === "shellShake" ? "M102 152 Q120 136 138 152" : "M102 140 Q120 160 138 140";

  return (
    <svg
      viewBox="0 0 240 200"
      width={size}
      height={(size * 200) / 240}
      overflow="visible"
      style={{
        scale: flip ? "-1 1" : "1 1",
        translate: `${bodyTranslateX}px ${bob + bodyTranslateY}px`,
        rotate: `${bodyRotate}deg`,
      }}
    >
      {/* legs */}
      {[-70, -35, 35, 70].map((x, i) => (
        <line
          key={x}
          x1={120 + x}
          y1={150}
          x2={120 + x * 1.3}
          y2={178 + (i % 2 === 0 ? legWiggle : -legWiggle)}
          stroke={palette.ink}
          strokeWidth={7}
          strokeLinecap="round"
        />
      ))}

      {/* left claw */}
      <g transform={`rotate(${leftClawRotate} 48 110)`}>
        <line
          x1={70}
          y1={120}
          x2={30}
          y2={100}
          stroke={palette.ink}
          strokeWidth={10}
          strokeLinecap="round"
        />
        <ellipse
          cx={30}
          cy={95}
          rx={26}
          ry={18}
          fill={palette.tomato}
          stroke={palette.ink}
          strokeWidth={6}
        />
      </g>

      {/* right claw */}
      <g transform={`rotate(${rightClawRotate} 192 110)`}>
        <line
          x1={170}
          y1={120}
          x2={210}
          y2={100}
          stroke={palette.ink}
          strokeWidth={10}
          strokeLinecap="round"
        />
        <ellipse
          cx={210}
          cy={95}
          rx={26}
          ry={18}
          fill={palette.tomato}
          stroke={palette.ink}
          strokeWidth={6}
        />
      </g>

      {/* body shell */}
      <ellipse
        cx={120}
        cy={130}
        rx={72}
        ry={52}
        fill={palette.tomato}
        stroke={palette.ink}
        strokeWidth={7}
      />

      {/* cheeks and mouth */}
      <ellipse cx={80} cy={138} rx={11} ry={7} fill={palette.apricot} opacity={0.9} />
      <ellipse cx={160} cy={138} rx={11} ry={7} fill={palette.apricot} opacity={0.9} />
      <path d={mouthPath} fill="none" stroke={palette.ink} strokeWidth={6} strokeLinecap="round" />

      {/* eye stalks */}
      <line
        x1={95}
        y1={90}
        x2={88}
        y2={55}
        stroke={palette.ink}
        strokeWidth={6}
        strokeLinecap="round"
      />
      <line
        x1={145}
        y1={90}
        x2={152}
        y2={55}
        stroke={palette.ink}
        strokeWidth={6}
        strokeLinecap="round"
      />

      {/* eyes (blink: scale vertically) */}
      <g transform={`translate(88 50) scale(1 ${eyeOpen})`}>
        <circle r={14} fill={palette.white} stroke={palette.ink} strokeWidth={5} />
        <circle r={5} fill={palette.ink} />
      </g>
      <g transform={`translate(152 50) scale(1 ${eyeOpen})`}>
        <circle r={14} fill={palette.white} stroke={palette.ink} strokeWidth={5} />
        <circle r={5} fill={palette.ink} />
      </g>
    </svg>
  );
};
