#!/usr/bin/env bash
# Regenerates the placeholder music bed + SFX used by the Phase 3 voice test
# (audio/music/*.wav, audio/sfx/*.wav are git-ignored — synthesized, disposable
# fixtures, not real assets). Real royalty-free music/SFX still need sourcing;
# see LICENSES.md in each folder.
set -euo pipefail
cd "$(dirname "$0")/.."

mkdir -p audio/music audio/sfx

ffmpeg -y \
  -f lavfi -i "sine=frequency=220:duration=32,volume=0.08" \
  -f lavfi -i "sine=frequency=277.18:duration=32,volume=0.06" \
  -f lavfi -i "sine=frequency=329.63:duration=32,volume=0.05" \
  -filter_complex "[0][1][2]amix=inputs=3:duration=longest,afade=t=in:st=0:d=2,afade=t=out:st=29:d=3" \
  -ar 44100 -ac 2 audio/music/placeholder-pad.wav

ffmpeg -y -f lavfi -i "sine=frequency=880:duration=0.18,volume=0.5,afade=t=out:st=0.08:d=0.1" \
  -ar 44100 -ac 2 audio/sfx/placeholder-tick.wav

ffmpeg -y -f lavfi -i "sine=frequency=1200:duration=0.12,volume=0.45,afade=t=out:st=0.05:d=0.07" \
  -ar 44100 -ac 2 audio/sfx/placeholder-chime.wav

ffmpeg -y -f lavfi -i "sine=frequency=500:duration=0.3,volume=0.4,afade=t=out:st=0.1:d=0.2" \
  -ar 44100 -ac 2 audio/sfx/placeholder-whoosh.wav

echo "Wrote audio/music/placeholder-pad.wav and 3 audio/sfx/placeholder-*.wav files."
