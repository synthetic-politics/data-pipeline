#!/bin/bash

SRC="$HOME/Desktop/data-pipeline/data/comparative-countries"
DST="$HOME/Desktop/output"

for type_dir in "$SRC"/*/; do
  type_name=$(basename "$type_dir")

  for account_dir in "$type_dir"*/; do
    account_name=$(basename "$account_dir")
    dest_account="$DST/$type_name/$account_name"
    mkdir -p "$dest_account"

    for date_dir in "$account_dir"*/; do
      [[ -d "$date_dir" ]] || continue
      date_raw=$(basename "$date_dir")
      date_tag="${date_raw/ (/_\(}"
      date_tag="${date_tag// /_}"

      for filepath in "$date_dir"*; do
        [[ -f "$filepath" ]] || continue
        filename=$(basename "$filepath")
        new_name="${date_tag}_${filename}"
        cp "$filepath" "$dest_account/$new_name"
        echo "  copied  $date_raw/$filename  →  $new_name"
      done
    done
  done
done
