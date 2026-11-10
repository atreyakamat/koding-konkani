#!/usr/bin/env python3
"""Generates all narration audio for one episode: one WAV per scene (with
cue timestamps resolved) and one WAV per Short's script. Writes into
audio/voice/epNNN/ (git-ignored) — remotion.config.ts sets "audio" as
Remotion's public dir, so staticFile("voice/epNNN/sceneN.wav") serves these
directly; no separate public/ mirror is needed.

Usage: python scripts/render_episode_audio.py <episode-number>
"""

from __future__ import annotations

import json
import shutil
import sys
import time
from pathlib import Path

from narration import load_voice_config, render_scene_audio

ROOT = Path(__file__).resolve().parent.parent
EPISODES_DIR = ROOT / "episodes"
VOICE_DIR = ROOT / "audio" / "voice"

SCENE_PAUSE_SEC = 0.7
BUG_REVEAL_PAUSE_SEC = 1.0


def render_episode(ep: int) -> dict:
    episode = json.loads((EPISODES_DIR / f"ep{ep:03d}.json").read_text(encoding="utf-8"))
    voice_cfg = load_voice_config()

    out_dir = VOICE_DIR / f"ep{ep:03d}"
    out_dir.mkdir(parents=True, exist_ok=True)

    results = {"scenes": [], "shorts": []}
    timings = []

    for scene in episode["scenes"]:
        is_bug = scene["template"] == "bug-of-the-day"
        t0 = time.time()
        summary = render_scene_audio(
            scene["narration"],
            out_dir / f"scene{scene['id']}.wav",
            voice_cfg,
            leading_silence_sec=BUG_REVEAL_PAUSE_SEC if is_bug else 0.0,
            trailing_silence_sec=0.0 if is_bug else SCENE_PAUSE_SEC,
        )
        elapsed = time.time() - t0
        timings.append({"scene": scene["id"], "template": scene["template"], "seconds_to_generate": round(elapsed, 2), "durationSec": round(summary["durationSec"], 2)})
        results["scenes"].append(summary)
        print(f"  scene {scene['id']:>2} ({scene['template']:<16}) {summary['durationSec']:.2f}s audio, {elapsed:.1f}s to generate, {len(summary['cues'])} cues")

    for short in episode["shorts"]:
        t0 = time.time()
        summary = render_scene_audio(short["script"], out_dir / f"{short['id']}.wav", voice_cfg)
        elapsed = time.time() - t0
        timings.append({"short": short["id"], "seconds_to_generate": round(elapsed, 2), "durationSec": round(summary["durationSec"], 2)})
        results["shorts"].append(summary)
        print(f"  short {short['id']} {summary['durationSec']:.2f}s audio, {elapsed:.1f}s to generate")

    # Remove the raw (pre-normalise) intermediates; only the final files are served.
    for raw in out_dir.glob("*.raw.wav"):
        raw.unlink()

    manifest_path = out_dir / "manifest.json"
    manifest_path.write_text(json.dumps({"ep": ep, "timings": timings}, indent=2), encoding="utf-8")
    shutil.copy(EPISODES_DIR / f"ep{ep:03d}.json", out_dir / "episode.json")

    return {"ep": ep, "timings": timings, "scenes": results["scenes"], "shorts": results["shorts"]}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python scripts/render_episode_audio.py <episode-number>")
    ep_num = int(sys.argv[1])
    print(f"Rendering narration audio for EP{ep_num:02d}...")
    out = render_episode(ep_num)
    total_gen = sum(t["seconds_to_generate"] for t in out["timings"])
    total_audio = sum(t["durationSec"] for t in out["timings"])
    print(f"Done. {len(out['timings'])} clips, {total_audio:.1f}s total audio, {total_gen:.1f}s to generate.")
