#!/usr/bin/env bash

set -euo pipefail

# run with ./tiktok-dl.sh <ACCOUNT_URL>

# https://www.tiktok.com/@paulinehansononenation
# https://www.tiktok.com/@onenationoz

ACCOUNT_URL="${1:?Usage: $0 <ACCOUNT_URL>}"
USERNAME=$(echo "$ACCOUNT_URL" | grep -oP '(?<=@)[^/?]+')
OUTPUT_DIR="./${USERNAME}"

mkdir -p "$OUTPUT_DIR"

yt-dlp \
  --dateafter  "20250103" \
  --datebefore "20250504" \
  --output "$OUTPUT_DIR/%(upload_date)s_%(id)s_%(title).80s.%(ext)s" \
  --write-info-json \
  --write-description \
  --format "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best" \
  --retries 10 \
  --fragment-retries 10 \
  --retry-sleep 5 \
  --sleep-requests 2 \
  --sleep-interval 3 \
  --max-sleep-interval 8 \
  --ignore-errors \
  --no-abort-on-error \
  --add-header "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36" \
  "$ACCOUNT_URL"

echo ""
echo "Saved to: $OUTPUT_DIR"
