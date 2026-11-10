#!/usr/bin/env bash
# One-command, resumable full re-render (long 4K + Shorts S1-S5) on the Linux laptop.
#
#   bash scripts/render_all.sh check            # preflight only, changes nothing
#   bash scripts/render_all.sh start [A B]      # preflight, then render EP A..B (default 1..86) in tmux
#   bash scripts/render_all.sh status           # progress + ETA
#   bash scripts/render_all.sh report           # write out/render-all-report.md
#   bash scripts/render_all.sh attach           # watch the live log
#
# Safe to re-run: `start` again resumes where it stopped. Nothing is deleted:
# old renders are MOVED to out/old-full-<date>/epNNN. Never pushes, never uploads.
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(pwd)"
SESSION="renderall"
STATE="out/.render-all"                 # holds run id + range
LOG="out/render-all.log"
MIN_FREE_GB=25
MIN_FREE_RAM_GB=6
MAX_RETRIES=5
FIX_COMMIT="45b81d1"                    # window-pop black-flash fix must be in this checkout

cmd="${1:-check}"; shift || true
A="${1:-1}"; B="${2:-86}"
epn() { printf "ep%03d" "$1"; }

fail=0
ok()   { echo "  OK    $*"; }
warn() { echo "  WARN  $*"; }
bad()  { echo "  FAIL  $*"; fail=1; }

preflight() {
  echo "== Preflight (EP$A..EP$B) =="
  local br; br="$(git rev-parse --abbrev-ref HEAD)"
  case "$br" in main|master) bad "on $br - switch to feat/render-all-laptop (never render from main)";; *) ok "branch $br";; esac
  git merge-base --is-ancestor "$FIX_COMMIT" HEAD 2>/dev/null && ok "window-pop fix $FIX_COMMIT present" \
    || bad "window-pop fix $FIX_COMMIT missing: git pull origin $br"
  [ -z "$(git status --porcelain -- src scripts episodes config)" ] && ok "working tree clean (src/scripts/episodes/config)" \
    || warn "uncommitted changes in src/scripts/episodes/config (renders would not match the branch)"

  for t in node ffmpeg ffprobe gcc tmux python3; do command -v "$t" >/dev/null && ok "$t" || bad "$t not installed"; done
  command -v systemd-inhibit >/dev/null && ok systemd-inhibit || warn "systemd-inhibit missing: laptop may sleep mid-render"
  [ -d node_modules ] && ok node_modules || bad "node_modules missing: run npm ci"

  # The pipeline hard-codes .venv/Scripts/python.exe (Windows layout). Make Linux work without editing it.
  if [ ! -e .venv/Scripts/python.exe ]; then
    if [ -x .venv/bin/python ]; then
      mkdir -p .venv/Scripts && ln -sf "$ROOT/.venv/bin/python" .venv/Scripts/python.exe && ok ".venv/Scripts/python.exe -> .venv/bin/python (symlink created)"
    else bad ".venv missing: python3 -m venv .venv && .venv/bin/pip install -r requirements.txt"; fi
  else ok ".venv/Scripts/python.exe"; fi
  [ -x .venv/Scripts/python.exe ] && .venv/Scripts/python.exe -c "import kokoro" 2>/dev/null && ok "kokoro importable" \
    || warn "kokoro not importable in .venv: only fine if all narration already exists"

  local free_gb; free_gb=$(df -Pk "$ROOT" | awk 'NR==2{printf "%d",$4/1048576}')
  [ "$free_gb" -ge "$MIN_FREE_GB" ] && ok "disk free ${free_gb} GB" || bad "disk free ${free_gb} GB (< $MIN_FREE_GB). Move out/old-* elsewhere first"
  local ram_gb; ram_gb=$(awk '/MemAvailable/{printf "%d",$2/1048576}' /proc/meminfo)
  [ "$ram_gb" -ge "$MIN_FREE_RAM_GB" ] && ok "RAM available ${ram_gb} GB" || warn "RAM available ${ram_gb} GB: close browsers/apps"

  echo "  ...validators"
  for v in check_scenes check_boxes validate_episodes; do
    if [ -f "scripts/$v.mts" ]; then
      node --experimental-strip-types --no-warnings "scripts/$v.mts" >/tmp/render_all_$v.txt 2>&1 \
        && ok "$v" || { bad "$v failed (see /tmp/render_all_$v.txt)"; tail -5 "/tmp/render_all_$v.txt"; }
    fi
  done

  # Narration: pipeline skips it when audio/voice/epNNN/manifest.json exists, else generates it.
  local missing=() i
  for i in $(seq "$A" "$B"); do [ -f "audio/voice/$(epn "$i")/manifest.json" ] || missing+=("$i"); done
  if [ "${#missing[@]}" -eq 0 ]; then ok "narration present for every episode"
  else
    warn "narration missing for ${#missing[@]} episode(s): ${missing[*]}"
    echo "        Best: copy audio/voice/ from the PC (keeps the voice identical to what is already uploaded)."
    echo "        Otherwise they are generated here on CPU (slow, +~1-2 h) with config/voice.json: re-run with ALLOW_NEW_VOICE=1."
    if [ "${ALLOW_NEW_VOICE:-0}" != "1" ] && [ "$cmd" = "start" ]; then bad "refusing to generate new narration without ALLOW_NEW_VOICE=1"; fi
  fi
  [ "$fail" -eq 0 ]
}

archive_range() {
  local run_id="$1" i d old
  old="out/old-full-$(date +%F)"
  for i in $(seq "$A" "$B"); do
    d="out/$(epn "$i")"
    if [ -f "$d/.render-all-$run_id" ]; then continue; fi          # resume: already ours
    if [ -d "$d" ]; then
      [ -e "$old/$(epn "$i")" ] && { echo "refusing: $old/$(epn "$i") exists"; exit 1; }
      mkdir -p "$old"; mv "$d" "$old/$(epn "$i")"
      echo "moved $d -> $old/$(epn "$i")"
    fi
    mkdir -p "$d"
    date -u +%FT%TZ > "$d/.rerender-4k-2026-11-03"                 # makes the pipeline's own archive step a no-op
    echo "$run_id" > "$d/.render-all-$run_id"
  done
}

run_loop() {                          # runs INSIDE tmux
  export LC_ALL=C RENDER_CONCURRENCY="${RENDER_CONCURRENCY:-2}"
  local tries=0 rc
  while :; do
    echo "[$(date -u +%FT%TZ)] pipeline EP$A..EP$B (attempt $((tries+1)), concurrency $RENDER_CONCURRENCY)"
    set +e
    node --experimental-strip-types --no-warnings scripts/episode_pipeline.mts "$A" "$B" --no-timebox
    rc=$?
    set -e
    git checkout -- docs/c-check-summary.md 2>/dev/null || true   # check_c rewrites it every episode
    [ "$rc" -eq 0 ] && break
    if [ "$rc" -eq 2 ]; then echo "[$(date -u +%FT%TZ)] STOP: two episodes failed in a row (exit 2). See out/episode-skips.log"; break; fi
    tries=$((tries+1))
    [ "$tries" -ge "$MAX_RETRIES" ] && { echo "STOP: $MAX_RETRIES crashes"; break; }
    echo "[$(date -u +%FT%TZ)] crashed (exit $rc); resuming in 30 s"; sleep 30
  done
  python3 scripts/render_all_report.py "$A" "$B" || true
  echo "[$(date -u +%FT%TZ)] DONE. Report: out/render-all-report.md"
}

case "$cmd" in
  check) preflight && echo "Preflight passed." || { echo "Preflight FAILED."; exit 1; } ;;
  start)
    preflight || { echo "Preflight FAILED, nothing changed."; exit 1; }
    tmux has-session -t "$SESSION" 2>/dev/null && { echo "Already running: bash scripts/render_all.sh status"; exit 1; }
    mkdir -p out
    run_id="$(cat "$STATE" 2>/dev/null | head -1 || true)"
    [ -z "$run_id" ] && run_id="$(date +%Y%m%d-%H%M)" && echo "$run_id" > "$STATE"
    archive_range "$run_id"
    inhibit=""; command -v systemd-inhibit >/dev/null && inhibit="systemd-inhibit --what=sleep:idle:handle-lid-switch --who=koding-konkani --why=rendering"
    tmux new-session -d -s "$SESSION" "cd '$ROOT' && $inhibit bash scripts/render_all.sh _run $A $B 2>&1 | tee -a $LOG; echo finished; sleep 86400"
    echo "Started in tmux '$SESSION' (run $run_id). Watch: bash scripts/render_all.sh attach   Status: bash scripts/render_all.sh status"
    echo "If it ever dies (tmux crash, reboot): run the same start command again. It resumes." ;;
  _run) run_loop ;;
  status) python3 scripts/render_all_report.py "$A" "$B" --status
          tmux has-session -t "$SESSION" 2>/dev/null && echo "tmux: running" || echo "tmux: not running"
          tail -3 "$LOG" 2>/dev/null || true ;;
  report) python3 scripts/render_all_report.py "$A" "$B" ;;
  attach) tmux attach -t "$SESSION" ;;
  *) sed -n 2,12p "$0"; exit 1 ;;
esac
