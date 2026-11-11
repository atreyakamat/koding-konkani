#!/usr/bin/env python3
"""Generates all narration audio for one episode: one WAV per scene (with
cue timestamps resolved) and one WAV per Short's script. Writes into
audio/voice/epNNN/ (git-ignored) — remotion.config.ts sets "audio" as
Remotion's public dir, so staticFile("voice/epNNN/sceneN.wav") serves these
directly; no separate public/ mirror is needed.

Usage: python scripts/render_episode_audio.py <episode-number> [--lang c|cpp] [--fake-voice]

--lang cpp reads episodes-cpp/ and writes audio/voice/cpp-epNNN/ (the C course keeps ep001 names).
--fake-voice writes silent WAVs with correctly shaped cue, caption and manifest files, so a full
Remotion render can be tried before any real narration is generated. Never use it for a release.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import time
from pathlib import Path

import argparse

ROOT = Path(__file__).resolve().parent.parent
VOICE_DIR = ROOT / "audio" / "voice"
EPISODE_DIRS = {"c": ROOT / "episodes", "cpp": ROOT / "episodes-cpp", "python": ROOT / "episodes-python"}

SCENE_PAUSE_SEC = 0.7
BUG_REVEAL_PAUSE_SEC = 1.0


def folder_name(lang: str, ep: int) -> str:
    """Same rule as epFolder() in src/lib/episode.ts."""
    return f"ep{ep:03d}" if lang == "c" else f"{lang}-ep{ep:03d}"


def fake_scene_audio(narration: str, out_wav: Path, *, leading_silence_sec: float = 0.0, trailing_silence_sec: float = 0.0) -> dict:
    """Silent stand-in for render_scene_audio: ~130 words a minute, evenly spaced word times, same file shapes."""
    import wave

    from narration import align_cues_to_timestamps, build_captions, strip_cues

    clean_text, cues = strip_cues(narration)
    words = clean_text.split(" ") if clean_text else []
    per_word_ms = 60000 / 130 * 1.12
    lead_ms = leading_silence_sec * 1000
    whisper_words = [
        {"text": w, "startMs": round(lead_ms + i * per_word_ms), "endMs": round(lead_ms + (i + 1) * per_word_ms - 60)}
        for i, w in enumerate(words)
    ]
    duration = (lead_ms + len(words) * per_word_ms) / 1000 + trailing_silence_sec
    rate = 24000
    out_wav.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(out_wav), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(b"\x00\x00" * int(duration * rate))
    resolved = align_cues_to_timestamps(clean_text, cues, whisper_words)
    out_wav.with_suffix(".captions.json").write_text(json.dumps(build_captions(clean_text, whisper_words), indent=2), encoding="utf-8")
    out_wav.with_suffix(".cues.json").write_text(json.dumps(resolved, indent=2), encoding="utf-8")
    return {"wav": str(out_wav), "durationSec": duration, "cues": resolved, "wordCount": len(words)}


def render_episode(ep: int, lang: str = "c", fake: bool = False) -> dict:
    episodes_dir = EPISODE_DIRS[lang]
    episode = json.loads((episodes_dir / f"ep{ep:03d}.json").read_text(encoding="utf-8"))
    if fake:
        voice_cfg = None
        render_scene_audio = lambda text, wav, cfg, **kw: fake_scene_audio(text, wav, **kw)  # noqa: E731
    else:
        from narration import load_voice_config, render_scene_audio

        voice_cfg = load_voice_config()

    out_dir = VOICE_DIR / folder_name(lang, ep)
    out_dir.mkdir(parents=True, exist_ok=True)
    # Marker so render_queue can refuse to render a real video over silent dry-run audio.
    fake_marker = out_dir / ".fake"
    if fake:
        fake_marker.write_text("silent dry-run audio; run without --fake-voice before rendering\n", encoding="utf-8")
    else:
        fake_marker.unlink(missing_ok=True)

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
    shutil.copy(episodes_dir / f"ep{ep:03d}.json", out_dir / "episode.json")

    return {"ep": ep, "timings": timings, "scenes": results["scenes"], "shorts": results["shorts"]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("episode", type=int)
    parser.add_argument("--lang", choices=sorted(EPISODE_DIRS), default="c")
    parser.add_argument("--fake-voice", action="store_true", help="silent audio for a dry-run render")
    args = parser.parse_args()
    print(f"Rendering {'FAKE (silent) ' if args.fake_voice else ''}narration audio for {args.lang} EP{args.episode:02d}...")
    out = render_episode(args.episode, args.lang, args.fake_voice)
    total_gen = sum(t["seconds_to_generate"] for t in out["timings"])
    total_audio = sum(t["durationSec"] for t in out["timings"])
    print(f"Done. {len(out['timings'])} clips, {total_audio:.1f}s total audio, {total_gen:.1f}s to generate.")
