#!/usr/bin/env python3
"""Phase 3 voice test: generate the EP 04 scene 5 sample (docs/bible/m00.md,
~30s, [HL] cues stripped) in 4 Kokoro voices + Piper en_US-ryan-high, normalise
each to -16 LUFS / -1 dBTP, and report per-voice generation time.

Run from the repo root with the project venv:
    .venv/Scripts/python.exe scripts/voice_test.py

Outputs go to audio/voice-test/ (git-ignored): <voice>.raw.wav (pre-normalise),
<voice>.wav (normalised), <voice>.captions.json (word timestamps).
"""

from __future__ import annotations

import json
import time
from pathlib import Path

from loudness import normalize
from voice import synth_kokoro, synth_piper

ROOT = Path(__file__).resolve().parent.parent
SAMPLE_TEXT = (ROOT / "scripts" / "fixtures" / "ep04-scene5-sample.txt").read_text(
    encoding="utf-8"
).strip()
OUT_DIR = ROOT / "audio" / "voice-test"
PIPER_MODEL = ROOT / ".cache" / "piper-voices" / "en_US-ryan-high.onnx"

KOKORO_VOICES = ["am_michael", "am_adam", "bm_george", "bm_lewis"]


def write_outputs(voice_name: str, audio, sample_rate: int, captions: list[dict]) -> Path:
    import soundfile as sf

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    raw_path = OUT_DIR / f"{voice_name}.raw.wav"
    sf.write(str(raw_path), audio, sample_rate)

    final_path = OUT_DIR / f"{voice_name}.wav"
    normalize(str(raw_path), str(final_path))

    captions_path = OUT_DIR / f"{voice_name}.captions.json"
    captions_path.write_text(json.dumps(captions, indent=2), encoding="utf-8")

    return final_path


def main() -> None:
    from kokoro import KPipeline

    results = []

    pipelines: dict[str, KPipeline] = {}
    for voice_name in KOKORO_VOICES:
        lang_code = "a" if voice_name.startswith("a") else "b"
        if lang_code not in pipelines:
            pipelines[lang_code] = KPipeline(lang_code=lang_code)

        start = time.time()
        audio, sample_rate, captions = synth_kokoro(
            SAMPLE_TEXT, voice_name, pipeline=pipelines[lang_code]
        )
        elapsed = time.time() - start

        final_path = write_outputs(voice_name, audio, sample_rate, captions)
        results.append(
            {
                "voice": voice_name,
                "engine": "kokoro",
                "seconds_to_generate": round(elapsed, 2),
                "output_duration_s": round(audio.shape[0] / sample_rate, 2),
                "wav": str(final_path.relative_to(ROOT)),
            }
        )

    if PIPER_MODEL.exists():
        from piper import PiperVoice

        piper_voice = PiperVoice.load(str(PIPER_MODEL))
        start = time.time()
        audio, sample_rate, captions = synth_piper(SAMPLE_TEXT, str(PIPER_MODEL), voice=piper_voice)
        elapsed = time.time() - start

        final_path = write_outputs("en_US-ryan-high", audio, sample_rate, captions)
        results.append(
            {
                "voice": "en_US-ryan-high",
                "engine": "piper",
                "seconds_to_generate": round(elapsed, 2),
                "output_duration_s": round(audio.shape[0] / sample_rate, 2),
                "wav": str(final_path.relative_to(ROOT)),
            }
        )
    else:
        print(f"Skipping Piper: model not found at {PIPER_MODEL}")

    summary_path = OUT_DIR / "summary.json"
    summary_path.write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
