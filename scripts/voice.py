#!/usr/bin/env python3
"""Synthesize narration audio with Kokoro (CPU) or Piper TTS, with word-level
caption timestamps in the @remotion/captions `Caption` shape.

CLI usage (single clip):
    python scripts/voice.py --text-file notes.txt --engine kokoro --voice am_michael \
        --out audio/voice/ep01-scene1.wav

    python scripts/voice.py --text-file notes.txt --engine piper --voice en_US-ryan-high \
        --model .cache/piper-voices/en_US-ryan-high.onnx --out audio/voice/ep01-scene1.wav

The synth_kokoro / synth_piper functions are also importable for batch jobs that
want to reuse a loaded pipeline across many lines instead of paying model-load
cost per call (see voice_test.py).
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np


def synth_kokoro(text: str, voice: str, pipeline=None):
    """Returns (audio: np.ndarray float32, sample_rate: int, captions: list[dict]).

    `pipeline`, if given, is a pre-built `kokoro.KPipeline` (must match the
    voice's language: lang_code "a" for am_*/af_* voices, "b" for bm_*/bf_*).
    Reuse one across calls to avoid repeated model loads.
    """
    from kokoro import KPipeline

    owns_pipeline = pipeline is None
    if owns_pipeline:
        lang_code = "a" if voice.startswith("a") else "b"
        pipeline = KPipeline(lang_code=lang_code)

    captions: list[dict] = []
    audio_chunks: list[np.ndarray] = []
    offset_s = 0.0
    sample_rate = 24000

    for result in pipeline(text, voice=voice):
        chunk = result.audio.numpy() if result.audio is not None else None
        if chunk is not None:
            audio_chunks.append(chunk)
        for tok in result.tokens or []:
            if tok.start_ts is None or tok.end_ts is None:
                continue
            captions.append(
                {
                    "text": tok.text + (tok.whitespace or ""),
                    "startMs": round((tok.start_ts + offset_s) * 1000),
                    "endMs": round((tok.end_ts + offset_s) * 1000),
                    "timestampMs": None,
                    "confidence": None,
                }
            )
        if chunk is not None:
            offset_s += chunk.shape[0] / sample_rate

    audio = np.concatenate(audio_chunks) if audio_chunks else np.zeros(0, dtype="float32")
    return audio, sample_rate, captions


def synth_piper(text: str, model_path: str, voice=None):
    """Returns (audio, sample_rate, captions). Word timestamps are an estimate
    (proportional to word length over total duration): Piper exposes
    phoneme-level alignments, not word boundaries, so this is approximate.
    """
    from piper import PiperVoice

    owns_voice = voice is None
    if owns_voice:
        voice = PiperVoice.load(model_path)

    chunks = list(voice.synthesize(text))
    sample_rate = chunks[0].sample_rate if chunks else 22050
    audio = (
        np.concatenate([c.audio_float_array for c in chunks])
        if chunks
        else np.zeros(0, dtype="float32")
    )

    words = text.split()
    total_s = audio.shape[0] / sample_rate
    total_chars = sum(len(w) for w in words) or 1
    captions = []
    t = 0.0
    for w in words:
        dur = total_s * (len(w) / total_chars)
        captions.append(
            {
                "text": w + " ",
                "startMs": round(t * 1000),
                "endMs": round((t + dur) * 1000),
                "timestampMs": None,
                "confidence": None,
            }
        )
        t += dur

    return audio, sample_rate, captions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text-file", required=True)
    parser.add_argument("--engine", choices=["kokoro", "piper"], required=True)
    parser.add_argument("--voice", required=True)
    parser.add_argument("--model", help="Piper .onnx model path (required for --engine piper)")
    parser.add_argument("--out", required=True, help="Output WAV path")
    args = parser.parse_args()

    text = Path(args.text_file).read_text(encoding="utf-8").strip()
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    start = time.time()
    if args.engine == "kokoro":
        audio, sample_rate, captions = synth_kokoro(text, args.voice)
    else:
        if not args.model:
            sys.exit("--model is required for --engine piper")
        audio, sample_rate, captions = synth_piper(text, args.model)
    elapsed = time.time() - start

    import soundfile as sf

    sf.write(str(out_path), audio, sample_rate)

    captions_path = out_path.with_suffix(".captions.json")
    captions_path.write_text(json.dumps(captions, indent=2), encoding="utf-8")

    print(
        json.dumps(
            {
                "voice": args.voice,
                "engine": args.engine,
                "seconds_to_generate": round(elapsed, 2),
                "output_duration_s": round(audio.shape[0] / sample_rate, 2),
                "wav": str(out_path),
                "captions": str(captions_path),
            }
        )
    )


if __name__ == "__main__":
    main()
