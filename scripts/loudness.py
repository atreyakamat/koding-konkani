#!/usr/bin/env python3
"""Normalise a WAV file to -16 LUFS integrated, peaks below -1 dBTP, using
ffmpeg's two-pass loudnorm filter (per CLAUDE.md's audio rules).

Usage:
    python scripts/loudness.py --in audio/voice/raw.wav --out audio/voice/raw.norm.wav
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys

TARGET_I = -16.0
TARGET_TP = -1.0
TARGET_LRA = 11.0


def measure(in_path: str, target_i: float = TARGET_I, target_tp: float = TARGET_TP, target_lra: float = TARGET_LRA) -> dict:
    cmd = [
        "ffmpeg",
        "-i",
        in_path,
        "-af",
        f"loudnorm=I={target_i}:TP={target_tp}:LRA={target_lra}:print_format=json",
        "-f",
        "null",
        "-",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    # loudnorm prints its JSON report to stderr, as the last `{...}` block.
    stderr = result.stderr
    start = stderr.rfind("{")
    end = stderr.rfind("}") + 1
    return json.loads(stderr[start:end])


def _sample_rate(in_path: str) -> str:
    cmd = [
        "ffprobe",
        "-v",
        "error",
        "-select_streams",
        "a:0",
        "-show_entries",
        "stream=sample_rate",
        "-of",
        "csv=p=0",
        in_path,
    ]
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout.strip()


def normalize(in_path: str, out_path: str) -> dict:
    return normalize_file(in_path, out_path)


def normalize_file(
    in_path: str,
    out_path: str,
    *,
    target_i: float = TARGET_I,
    target_tp: float = TARGET_TP,
    target_lra: float = TARGET_LRA,
    copy_video: bool = False,
) -> dict:
    """Two-pass loudnorm: measure, then apply a linear gain (falling back to
    dynamic normalisation only if the measured values are too far off target).
    `copy_video=True` keeps the video stream untouched (`-c:v copy`) for
    mastering a rendered MP4's audio without re-encoding its picture."""
    measured = measure(in_path, target_i, target_tp, target_lra)
    # loudnorm's true-peak detection oversamples internally (to 192kHz); without
    # an explicit -ar the encoded output inherits that rate, so pin it back.
    sample_rate = _sample_rate(in_path)
    cmd = [
        "ffmpeg",
        "-y",
        "-i",
        in_path,
        "-af",
        (
            f"loudnorm=I={target_i}:TP={target_tp}:LRA={target_lra}:"
            f"measured_I={measured['input_i']}:measured_TP={measured['input_tp']}:"
            f"measured_LRA={measured['input_lra']}:measured_thresh={measured['input_thresh']}:"
            f"offset={measured['target_offset']}:linear=true:print_format=json"
        ),
        "-ar",
        sample_rate,
    ]
    if copy_video:
        cmd += ["-c:v", "copy"]
    cmd += [out_path]
    subprocess.run(cmd, capture_output=True, text=True, check=True)
    return measured


def master_video(in_path: str, out_path: str, target_tp: float = -1.5) -> dict:
    """Final mastering pass for a rendered MP4: two-pass loudnorm on the mixed
    audio (narration + music + SFX together can peak hotter than any single
    normalised clip), -c:v copy so the picture is untouched. Returns the
    pre-mastering measurement for the review log."""
    return normalize_file(in_path, out_path, target_tp=target_tp, copy_video=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--in", dest="in_path", required=True)
    parser.add_argument("--out", dest="out_path", required=True)
    args = parser.parse_args()

    try:
        measured = normalize(args.in_path, args.out_path)
    except subprocess.CalledProcessError as exc:
        sys.exit(f"ffmpeg loudnorm failed: {exc.stderr}")

    print(
        json.dumps(
            {
                "in": args.in_path,
                "out": args.out_path,
                "measured_input_i_lufs": measured["input_i"],
                "measured_input_tp_dbtp": measured["input_tp"],
                "target_i_lufs": TARGET_I,
                "target_tp_dbtp": TARGET_TP,
            }
        )
    )


if __name__ == "__main__":
    main()
