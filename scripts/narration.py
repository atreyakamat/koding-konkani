#!/usr/bin/env python3
"""Per-scene narration pipeline: strip [HL n] / [TRACK a=1] cues from an
episode's narration text (keeping their word positions), synthesize with
Piper using config/voice.json's pacing, insert sentence/scene pauses, and
resolve word-level timestamps (faster-whisper) so cues can fire on the right
frame. See docs/PIPELINE.md and the Phase 5 PR for the full design.

Importable: render_scene_audio() is called once per scene by
scripts/render_episode.py. CLI usage below is for ad-hoc single-scene testing.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np

from loudness import normalize as loudnorm_normalize

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "config" / "voice.json"

_CUE_RE = re.compile(r"\[(HL|TRACK)\s+([^\]]*)\]")
_SENTENCE_SPLIT_RE = re.compile(r"\s+")


@dataclass
class Cue:
    kind: str  # "HL" or "TRACK"
    raw: str  # e.g. "4" for HL, "age=19" for TRACK
    word_index: int  # index into the cue-stripped word list this cue precedes


@dataclass
class SceneAudio:
    audio: np.ndarray
    sample_rate: int
    clean_text: str
    cues: list[Cue]
    words: list[dict] = field(default_factory=list)  # [{text, startMs, endMs}], filled in after whisper


def strip_cues(narration: str) -> tuple[str, list[Cue]]:
    """Removes [HL n] / [TRACK a=1] markers from `narration`, returning the
    clean spoken text and a list of Cues recording which word (by index in
    the clean text's whitespace-split word list) each cue preceded."""
    cues: list[Cue] = []
    pos = 0
    out_words: list[str] = []

    for m in _CUE_RE.finditer(narration):
        before = narration[pos : m.start()]
        out_words.extend(w for w in _SENTENCE_SPLIT_RE.split(before) if w)
        cues.append(Cue(kind=m.group(1), raw=m.group(2), word_index=len(out_words)))
        pos = m.end()

    tail = narration[pos:]
    out_words.extend(w for w in _SENTENCE_SPLIT_RE.split(tail) if w)

    # Collapse any double-spacing left by a removed cue sitting between words.
    clean_text = " ".join(out_words)
    return clean_text, cues


def load_voice_config() -> dict:
    return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))


_PIPER_VOICE_CACHE: dict = {}


def get_piper_voice(model_path: str):
    from piper import PiperVoice

    if model_path not in _PIPER_VOICE_CACHE:
        _PIPER_VOICE_CACHE[model_path] = PiperVoice.load(model_path)
    return _PIPER_VOICE_CACHE[model_path]


def synthesize_with_pauses(
    text: str, voice_cfg: dict, sentence_pause_sec: float
) -> tuple[np.ndarray, int]:
    """Synthesizes `text` with Piper, inserting `sentence_pause_sec` of
    silence between Piper's own per-sentence audio chunks."""
    from piper.config import SynthesisConfig

    voice = get_piper_voice(ROOT / voice_cfg["model"])
    syn_cfg = SynthesisConfig(length_scale=voice_cfg["pacing"]["lengthScale"])

    chunks = list(voice.synthesize(text, syn_cfg))
    if not chunks:
        return np.zeros(0, dtype="float32"), 22050

    sample_rate = chunks[0].sample_rate
    pause = np.zeros(int(sentence_pause_sec * sample_rate), dtype="float32")

    parts: list[np.ndarray] = []
    for i, chunk in enumerate(chunks):
        parts.append(chunk.audio_float_array)
        if i < len(chunks) - 1:
            parts.append(pause)
    return np.concatenate(parts), sample_rate


_WHISPER_MODEL = None


def get_whisper_model():
    global _WHISPER_MODEL
    if _WHISPER_MODEL is None:
        from faster_whisper import WhisperModel

        _WHISPER_MODEL = WhisperModel("small.en", device="cpu", compute_type="int8")
    return _WHISPER_MODEL


def _normalise_word(w: str) -> str:
    return re.sub(r"[^a-z0-9]", "", w.lower())


def transcribe_words(audio_path: Path) -> list[dict]:
    """Runs faster-whisper on `audio_path`, returns [{text, startMs, endMs}]."""
    model = get_whisper_model()
    segments, _info = model.transcribe(str(audio_path), word_timestamps=True)
    words = []
    for seg in segments:
        for w in seg.words or []:
            words.append({"text": w.word, "startMs": round(w.start * 1000), "endMs": round(w.end * 1000)})
    return words


def align_cues_to_timestamps(clean_text: str, cues: list[Cue], whisper_words: list[dict]) -> list[dict]:
    """Maps each Cue's word_index (into clean_text's word list) to a real
    timestamp, by aligning the original words against whisper's transcribed
    words (which may differ slightly — mispronunciations, whisper errors).
    Returns [{type, raw, atMs}]."""
    import difflib

    original_words = [_normalise_word(w) for w in clean_text.split(" ")]
    whisper_norm = [_normalise_word(w["text"]) for w in whisper_words]

    matcher = difflib.SequenceMatcher(None, original_words, whisper_norm, autojunk=False)
    # Build a mapping: original word index -> best-guess whisper word index.
    orig_to_whisper: dict[int, int] = {}
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                orig_to_whisper[i1 + k] = j1 + k
        else:
            # Replace/insert/delete: map proportionally into the whisper range.
            span = max(1, i2 - i1)
            for k in range(i2 - i1):
                j = j1 + round((j2 - j1) * k / span) if j2 > j1 else j1
                orig_to_whisper[i1 + k] = min(j, len(whisper_words) - 1) if whisper_words else 0

    resolved = []
    for cue in cues:
        idx = min(cue.word_index, len(original_words) - 1) if original_words else 0
        w_idx = orig_to_whisper.get(idx, 0)
        at_ms = whisper_words[w_idx]["startMs"] if whisper_words and w_idx < len(whisper_words) else 0
        resolved.append({"type": cue.kind, "raw": cue.raw, "atMs": at_ms})
    return resolved


def build_captions(clean_text: str, whisper_words: list[dict]) -> list[dict]:
    """Produces caption words using the exact text sent to Piper — we know
    precisely what was synthesized — with timestamps borrowed from whisper's
    transcription via the same alignment used for cue resolution. This avoids
    burning whisper's own transcription errors into the rendered video (e.g.
    faster-whisper has mis-heard a clip-opening "Hello?" as "I love-" in
    testing); whisper words with no corresponding original word (insertions /
    hallucinations) are simply dropped, and original words whisper dropped
    entirely are timed by interpolating between their resolved neighbours."""
    import difflib

    original_words = clean_text.split(" ") if clean_text else []
    original_norm = [_normalise_word(w) for w in original_words]
    whisper_norm = [_normalise_word(w["text"]) for w in whisper_words]

    matcher = difflib.SequenceMatcher(None, original_norm, whisper_norm, autojunk=False)

    resolved: dict[int, dict] = {}
    for tag, i1, i2, j1, j2 in matcher.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                w = whisper_words[j1 + k]
                resolved[i1 + k] = {"startMs": w["startMs"], "endMs": w["endMs"]}
        elif tag == "replace" and j2 > j1:
            span = max(1, i2 - i1)
            for k in range(i2 - i1):
                j = min(j1 + round((j2 - j1) * k / span), j2 - 1)
                w = whisper_words[j]
                resolved[i1 + k] = {"startMs": w["startMs"], "endMs": w["endMs"]}
        # "delete", or "replace" with no whisper words on this side: left
        # unresolved here, filled in by interpolation below.

    n = len(original_words)
    for i in range(n):
        if i in resolved:
            continue
        prev_end = resolved[i - 1]["endMs"] if (i - 1) in resolved else 0
        j = i + 1
        while j < n and j not in resolved:
            j += 1
        next_start = resolved[j]["startMs"] if j in resolved else prev_end + 200
        resolved[i] = {"startMs": prev_end, "endMs": max(prev_end + 1, min(next_start, prev_end + 400))}

    return [
        {
            "text": original_words[i],
            "startMs": resolved[i]["startMs"],
            "endMs": resolved[i]["endMs"],
            "timestampMs": None,
            "confidence": None,
        }
        for i in range(n)
    ]


def render_scene_audio(
    narration: str,
    out_wav: Path,
    voice_cfg: dict,
    *,
    leading_silence_sec: float = 0.0,
    trailing_silence_sec: float = 0.0,
) -> dict:
    """Full per-scene pipeline: strip cues, synthesize, add pauses, loudness-
    normalise, transcribe, resolve cue timestamps. Writes `out_wav` (final,
    normalised) and `out_wav` with `.cues.json`/`.captions.json` suffixes.
    Returns a summary dict (also used by the caller to size the Remotion scene)."""
    import soundfile as sf

    clean_text, cues = strip_cues(narration)
    audio, sample_rate = synthesize_with_pauses(clean_text, voice_cfg, voice_cfg["pacing"]["sentencePauseSec"])

    lead = np.zeros(int(leading_silence_sec * sample_rate), dtype="float32")
    trail = np.zeros(int(trailing_silence_sec * sample_rate), dtype="float32")
    audio = np.concatenate([lead, audio, trail])

    out_wav.parent.mkdir(parents=True, exist_ok=True)
    raw_wav = out_wav.with_suffix(".raw.wav")
    sf.write(str(raw_wav), audio, sample_rate)
    loudnorm_normalize(str(raw_wav), str(out_wav))
    raw_wav.unlink(missing_ok=True)

    whisper_words = transcribe_words(out_wav)
    # Whisper timestamps are relative to the final (lead-silence-included) audio,
    # which is what the Remotion side needs — no offset adjustment required.
    resolved_cues = align_cues_to_timestamps(clean_text, cues, whisper_words)

    captions = build_captions(clean_text, whisper_words)
    out_wav.with_suffix(".captions.json").write_text(json.dumps(captions, indent=2), encoding="utf-8")
    out_wav.with_suffix(".cues.json").write_text(json.dumps(resolved_cues, indent=2), encoding="utf-8")

    import soundfile as sf_info

    info = sf_info.info(str(out_wav))
    return {
        "wav": str(out_wav),
        "durationSec": info.frames / info.samplerate,
        "cues": resolved_cues,
        "wordCount": len(whisper_words),
    }


if __name__ == "__main__":
    import sys

    sample = (
        'Here is a tiny taste. [HL 4] printf, open bracket, "Hi" in double quotes, '
        "close bracket, semicolon. [TRACK x=1] printf is a function."
    )
    clean, cues = strip_cues(sample)
    print("clean:", clean)
    for c in cues:
        words = clean.split(" ")
        nearby = " ".join(words[max(0, c.word_index - 1) : c.word_index + 2])
        print(f"  {c.kind} {c.raw!r} before word #{c.word_index} ({nearby!r})")
    sys.exit(0)
