#!/usr/bin/env python3
"""Generate the placeholder sound-effect set and a music bed from scratch (numpy only).

Everything here is synthesised from maths, so there is nothing to license: the files are original
and released under CC0 by this project. Replace any of them later with a recorded sound of the
same file name (record the source in audio/sfx/LICENSES.md). Run: python scripts/make_sfx.py
"""
import wave
from pathlib import Path

import numpy as np

SR = 44100
ROOT = Path(__file__).resolve().parent.parent
rng = np.random.default_rng(7)


def t(d):
    return np.arange(int(SR * d)) / SR


def env(n, a=0.002, r=0.05):
    e = np.ones(n)
    na, nr = max(1, int(SR * a)), max(1, int(SR * r))
    e[:na] = np.linspace(0, 1, na)
    e[-nr:] = np.linspace(1, 0, nr)
    return e


def decay(x, k):
    return np.exp(-k * x)


def noise(d):
    return rng.standard_normal(int(SR * d))


def lowpass(x, cutoff):
    a = np.exp(-2 * np.pi * cutoff / SR)
    y = np.zeros_like(x)
    prev = 0.0
    for i, v in enumerate(x):
        prev = (1 - a) * v + a * prev
        y[i] = prev
    return y


def highpass(x, cutoff):
    return x - lowpass(x, cutoff)


def tone(f, d, k=8, harm=(1.0,)):
    x = t(d)
    return sum(h * np.sin(2 * np.pi * f * (i + 1) * x) for i, h in enumerate(harm)) * decay(x, k)


def norm(x, peak=0.8):
    return x / (np.max(np.abs(x)) + 1e-9) * peak


def save(path, x):
    path.parent.mkdir(parents=True, exist_ok=True)
    pcm = (np.clip(x, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


def click(d=0.06):
    n = highpass(noise(d), 1500) * decay(t(d), 90)
    return n + tone(2200, d, 70) * 0.5


sfx = {}
# claw-click: two sharp ticks (the "xec-xec")
gap = np.zeros(int(SR * 0.07))
sfx["claw-click"] = norm(np.concatenate([click(), gap, click(), np.zeros(int(SR * 0.04))]))
# thud: low sine drop
x = t(0.35)
sfx["thud"] = norm(np.sin(2 * np.pi * (110 * decay(x, 6) + 45) * x) * decay(x, 9) + lowpass(noise(0.35), 300) * decay(x, 25) * 0.4)
# whoosh: filtered noise, rising then falling
n = noise(0.5)
sweep = np.sin(np.linspace(0, np.pi, len(n)))
sfx["whoosh"] = norm(highpass(lowpass(n, 5000), 400) * sweep)
# key-tick: soft mechanical key
sfx["key-tick"] = norm(click(0.04) * 0.8 + tone(900, 0.04, 100) * 0.2, 0.5)
# marker-swipe: short filtered noise glide
n = noise(0.22)
sfx["marker-swipe"] = norm(highpass(lowpass(n, 6000), 1200) * env(len(n), 0.02, 0.09), 0.5)
# ding: bright bell, success
x = t(0.9)
sfx["ding"] = norm(tone(1318.5, 0.9, 5, (1.0, 0.4, 0.15)) + 0.4 * tone(1976, 0.9, 7))
# buzzer: low square-ish, error
x = t(0.45)
sfx["buzzer"] = norm(np.sign(np.sin(2 * np.pi * 120 * x)) * 0.5 * env(len(x), 0.005, 0.08) + np.sign(np.sin(2 * np.pi * 126 * x)) * 0.4 * env(len(x), 0.005, 0.08), 0.6)
# pop: quick pitch drop
x = t(0.12)
sfx["pop"] = norm(np.sin(2 * np.pi * (900 * decay(x, 30) + 200) * x) * decay(x, 35))
# stamp: thud + click
sfx["stamp"] = norm(sfx["thud"][: int(SR * 0.25)] * 0.9 + np.pad(click(0.05), (0, int(SR * 0.25) - int(SR * 0.05))) * 0.5)
# chime: three rising notes (course map tiles)
sfx["chime"] = norm(np.concatenate([tone(f, 0.28, 6, (1.0, 0.3)) for f in (784, 988, 1175)]))
# rimshot: snare + cymbal ting
snare = highpass(noise(0.18), 800) * decay(t(0.18), 22) + tone(190, 0.18, 25) * 0.6
snare2 = np.concatenate([snare, np.zeros(int(SR * 0.05)), snare])
ting = highpass(noise(0.5), 5000) * decay(t(0.5), 8) * 0.4
sfx["rimshot"] = norm(np.concatenate([snare2, ting]))
# sting: 3-second channel sting, a rising four-note arpeggio resolving to a held chord
notes = [(523.25, 0.0), (659.25, 0.18), (783.99, 0.36), (1046.5, 0.54)]
sting = np.zeros(int(SR * 3.0))
for f, start in notes:
    seg = tone(f, 1.4, 3.5, (1.0, 0.35, 0.12)) * env(int(SR * 1.4), 0.004, 0.2)
    i = int(SR * start)
    sting[i : i + len(seg)] += seg * 0.5
for f in (523.25, 659.25, 783.99):
    seg = tone(f, 2.2, 1.8, (1.0, 0.25)) * env(int(SR * 2.2), 0.01, 0.6)
    i = int(SR * 0.7)
    sting[i : i + len(seg)] += seg * 0.35
sfx["sting"] = norm(sting)

for name, data in sfx.items():
    save(ROOT / "audio" / "sfx" / f"{name}.wav", data)

# Music bed: 8 bars of a soft lo-fi loop, 80 BPM, Am - F - C - G, seamless loop point.
bpm, bars = 80, 8
beat = 60 / bpm
total = int(SR * beat * 4 * bars)
bed = np.zeros(total)
chords = [(220.0, 261.63, 329.63), (174.61, 220.0, 261.63), (261.63, 329.63, 392.0), (196.0, 246.94, 293.66)]
roots = [55.0, 43.65, 65.41, 49.0]
for bar in range(bars):
    ch, root = chords[bar % 4], roots[bar % 4]
    start = int(SR * beat * 4 * bar)
    length = int(SR * beat * 4)
    pad = sum(np.sin(2 * np.pi * f * np.arange(length) / SR) + 0.3 * np.sin(2 * np.pi * 2 * f * np.arange(length) / SR) for f in ch)
    bed[start : start + length] += pad * env(length, 0.25, 0.4) * 0.12
    for b in range(4):  # bass on beats 1 and 3, soft hat on every beat
        i = start + int(SR * beat * b)
        if b % 2 == 0:
            seg = tone(root, beat, 5) * 0.5
            bed[i : i + len(seg)] += seg[: total - i]
        hat = highpass(noise(0.05), 6000) * decay(t(0.05), 60) * 0.08
        bed[i : i + len(hat)] += hat[: total - i]
bed = norm(lowpass(bed, 3500), 0.5)
save(ROOT / "audio" / "music" / "bed-01.wav", bed)
print("wrote", len(sfx), "sfx + 1 music bed")
