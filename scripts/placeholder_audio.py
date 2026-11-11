#!/usr/bin/env python3
"""DEV ONLY: writes silent placeholder narration for an episode, so a full Remotion render can be tested
without the TTS voice. Same files and shape as render_episode_audio.py makes (scene WAVs, word captions,
resolved [HL]/[TRACK] cues, manifest.json, episode.json). Never use the output for a real video.

Usage: KK_COURSE=python python3 scripts/placeholder_audio.py <from> [<to>]
Writes audio/voice/python-epNNN/ (git-ignored) for Python, audio/voice/cpp-epNNN/ for C++, audio/voice/epNNN/ for C.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import sys
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG = os.environ.get("KK_COURSE", "c")   # c, cpp or python
EP_DIR = ROOT / {"c": "episodes", "cpp": "episodes-cpp", "python": "episodes-python"}[LANG]
VOICE_DIR = ROOT / "audio" / "voice"   # same folder rule as epFolder() in src/lib/episode.ts
FOLDER_PREFIX = "" if LANG == "c" else f"{LANG}-"

WORDS_PER_SEC = 2.1      # about 126 wpm, the pace of the real narrator (Piper length_scale 1.12)
SCENE_PAUSE = 0.7
BUG_LEAD = 1.0
RATE = 8000   # low rate and 8-bit keep the silent files small (about 8 KB per second)
CUE = re.compile(r"\[(HL|TRACK)\s+([^\]]*)\]")


def silent_wav(path: Path, seconds: float) -> None:
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(1)
        w.setframerate(RATE)
        w.writeframes(b"\x80" * int(RATE * seconds))  # 8-bit WAV: 0x80 is silence


def make_clip(text: str, wav: Path, lead: float = 0.0, tail: float = 0.0) -> float:
    words: list[str] = []
    cues: list[tuple[str, str, int]] = []
    pos = 0
    for m in CUE.finditer(text):
        words += text[pos:m.start()].split()
        cues.append((m.group(1), m.group(2).strip(), len(words)))
        pos = m.end()
    words += text[pos:].split()
    speech = max(1.0, len(words) / WORDS_PER_SEC)
    total = lead + speech + tail
    silent_wav(wav, total)
    per = speech / max(1, len(words))
    caps = [{"text": w + " ", "startMs": round((lead + i * per) * 1000), "endMs": round((lead + (i + 1) * per) * 1000),
             "timestampMs": None, "confidence": None} for i, w in enumerate(words)]
    wav.with_suffix(".captions.json").write_text(json.dumps(caps, indent=2), encoding="utf-8")
    resolved = [{"type": k, "raw": raw, "atMs": round((lead + idx * per) * 1000)} for k, raw, idx in cues]
    wav.with_suffix(".cues.json").write_text(json.dumps(resolved, indent=2), encoding="utf-8")
    return total


def render(ep: int) -> None:
    episode = json.loads((EP_DIR / f"ep{ep:03d}.json").read_text(encoding="utf-8"))
    out = VOICE_DIR / f"{FOLDER_PREFIX}ep{ep:03d}"
    out.mkdir(parents=True, exist_ok=True)
    # Same marker as render_episode_audio.py --fake-voice, so render_queue refuses to render real videos over this audio.
    (out / ".fake").write_text("silent dry-run audio; run render_episode_audio.py without --fake-voice before rendering\n", encoding="utf-8")
    timings = []
    for s in episode["scenes"]:
        bug = s["template"] == "bug-of-the-day"
        d = make_clip(s["narration"], out / f"scene{s['id']}.wav", BUG_LEAD if bug else 0.0, 0.0 if bug else SCENE_PAUSE)
        timings.append({"scene": s["id"], "template": s["template"], "durationSec": round(d, 2)})
    for sh in episode["shorts"]:
        d = make_clip(sh["script"], out / f"{sh['id']}.wav")
        timings.append({"short": sh["id"], "durationSec": round(d, 2)})
    (out / "manifest.json").write_text(json.dumps({"ep": ep, "timings": timings, "placeholder": True}, indent=2), encoding="utf-8")
    shutil.copy(EP_DIR / f"ep{ep:03d}.json", out / "episode.json")
    total = sum(t["durationSec"] for t in timings if "scene" in t)
    print(f"EP{ep:02d}: placeholder audio, long video about {total / 60:.1f} min")


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2]) if len(sys.argv) > 2 else a
    for n in range(a, b + 1):
        render(n)
