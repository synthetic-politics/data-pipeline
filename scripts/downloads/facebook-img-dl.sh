#!/usr/bin/env bash
set -euo pipefail
# run with ./facebook-img-dl.sh <ACCOUNT_URL>
# https://www.facebook.com/OneNationParty
# https://www.facebook.com/PaulineHansonAu

ACCOUNT_URL="${1:?Usage: $0 <ACCOUNT_URL>}"
USERNAME=$(echo "$ACCOUNT_URL" | grep -oP '(?<=facebook\.com/)[^/?]+')
OUTPUT_DIR="./data/one-nation/facebook/${USERNAME}"
mkdir -p "$OUTPUT_DIR"

gallery-dl \
  --write-metadata \
  --cookies-from-browser chrome \
  --date-after  "2025-01-03" \
  --date-before "2025-05-04" \
  --dest "$OUTPUT_DIR" \
  --retries 10 \
  --sleep "3-8" \
  --sleep-request 2 \
  --sleep-retries 5 \
  --user-agent "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36" \
  "$ACCOUNT_URL"
