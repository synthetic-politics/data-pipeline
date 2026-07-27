## 01 - Download
./gallery-dl  --dater-after YYYY-MM-DD --date-before YYYY-MM-DD <INSTAGRAM_URL>

Where --date-after is 120 days prior to the election date & --date before is election day +1 day (as date before is not inclusive)


## 04 - Transcribe & Translate Audio
python 3.14 whisper-script.py

## Translate Captions
python3.11 txt.py <path/to/folder>

## OCR Text & Translate
python3.11 ocr.py <path/to/folder> <lang>

Where lang is 2-letter ISO 639-1 language codes, e.g. de, en, nl
