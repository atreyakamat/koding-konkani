#!/usr/bin/env bash
# Back up rendered videos to GitHub Releases, one release per episode (tag ep051, ...).
# Each release holds epNNN-4k.mp4 + epNNN-S1..S5.mp4. Resumable: files already uploaded are skipped.
# This is a BACKUP only. It never uploads to YouTube/Instagram and never pushes commits.
#
#   bash scripts/upload_releases.sh list                 # what would be uploaded, changes nothing
#   bash scripts/upload_releases.sh upload [A B]         # upload EP A..B (default 1..86), asks once first
#   WARN_OK=1 ...     also upload episodes whose QA verdict is WARN (default: PASS only)
#   YES=1 ...         skip the one confirmation prompt
#   REPO=owner/name   override the target repo (default: this checkout's origin)
#
# Needs the GitHub CLI logged in on this machine (`gh auth login`, done by you; this script never reads tokens).
# NOTE: while the repo is public, these videos are public. Make the repo private when the backup is done.
set -euo pipefail
cd "$(dirname "$0")/.."
cmd="${1:-list}"; shift || true
A="${1:-1}"; B="${2:-86}"
epn() { printf "ep%03d" "$1"; }

command -v gh >/dev/null || { echo "gh not installed (https://cli.github.com)"; exit 1; }
command -v python3 >/dev/null || { echo "python3 needed"; exit 1; }
gh auth status >/dev/null 2>&1 || { echo "gh is not logged in: run 'gh auth login' first"; exit 1; }
REPO="${REPO:-$(gh repo view --json nameWithOwner -q .nameWithOwner)}"
TARGET="$(git rev-parse HEAD)"

# Echo "verdict" for an episode from its qa.json (PASS/WARN/FAIL/NONE).
verdict() { python3 -I - "$1" <<'E'
import json,sys,pathlib
p=pathlib.Path(sys.argv[1])/"qa.json"
try: print(json.loads(p.read_text())["verdict"])
except Exception: print("NONE")
E
}

eligible() {                       # prints the files to upload for episode $1, or nothing
  local ep="$1" d v f
  d="out/$(epn "$ep")"; v="$(verdict "$d")"
  case "$v" in PASS) ;; WARN) [ "${WARN_OK:-0}" = 1 ] || { echo "SKIP:$ep verdict WARN (set WARN_OK=1 to include)" >&2; return; } ;;
               *) echo "SKIP:$ep verdict $v" >&2; return ;; esac
  for f in "$d/$(epn "$ep")-4k.mp4" "$d"/"$(epn "$ep")"-S[1-5].mp4; do [ -s "$f" ] && echo "$f"; done
}

if [ "$cmd" = "list" ]; then
  n=0
  for ep in $(seq "$A" "$B"); do
    files="$(eligible "$ep" || true)"
    [ -z "$files" ] && continue
    n=$((n+1)); echo "$(epn "$ep"): $(echo "$files" | wc -l) files, $(echo "$files" | xargs du -ch | tail -1 | cut -f1)"
  done
  echo "$n episode(s) eligible -> $REPO"; exit 0
fi

[ "$cmd" = "upload" ] || { sed -n 2,13p "$0"; exit 1; }
vis="$(gh repo view "$REPO" --json visibility -q .visibility)"
echo "Target: $REPO ($vis). Releases will be ${vis,,}ly readable."
if [ "${YES:-0}" != 1 ]; then read -r -p "Upload EP$A..EP$B as GitHub Releases? [y/N] " a; [ "$a" = y ] || { echo aborted; exit 1; }; fi

done_n=0; fail_n=0
for ep in $(seq "$A" "$B"); do
  name="$(epn "$ep")"; files="$(eligible "$ep" || true)"
  [ -z "$files" ] && continue
  title="$(python3 -I -c "import json;print(json.load(open('episodes/$name.json'))['title'])" 2>/dev/null || echo "$name")"
  gh release view "$name" -R "$REPO" >/dev/null 2>&1 || \
    gh release create "$name" -R "$REPO" --target "$TARGET" --title "EP$ep - $title" \
      --notes "Koding Konkani $name: 4K long video + 5 Shorts. Backup render, $(date +%F)." >/dev/null
  have="$(gh release view "$name" -R "$REPO" --json assets -q '.assets[].name')"
  while IFS= read -r f; do
    b="$(basename "$f")"
    if echo "$have" | grep -qx "$b"; then echo "  skip  $b (already uploaded)"; continue; fi
    if gh release upload "$name" "$f" -R "$REPO"; then echo "  up    $b"; else echo "  FAIL  $b"; fail_n=$((fail_n+1)); fi
  done <<< "$files"
  done_n=$((done_n+1)); echo "done  $name"
done
echo "Finished: $done_n episode(s), $fail_n failed file(s). Re-run the same command to retry failures."
