#!/usr/bin/env python3
import sys
from pathlib import Path
from deep_translator import GoogleTranslator
from langdetect import detect

def translate_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8").strip()
    if not text or detect(text) == "en":
        return
    src_lang = detect(text)
    translator = GoogleTranslator(source=src_lang, target="en")
    if len(text) > 4500:
        chunks = [text[i:i + 4500] for i in range(0, len(text), 4500)]
        translated = " ".join(translator.translate(chunk) for chunk in chunks)
    else:
        translated = translator.translate(text)
    with path.open("a", encoding="utf-8") as f:
        f.write("\n\n--- English Translation ---\n")
        f.write(translated)

def main():
    directory = Path(sys.argv[1])
    for path in sorted(directory.glob("*.txt")):
        translate_file(path)

if __name__ == "__main__":
    main()
