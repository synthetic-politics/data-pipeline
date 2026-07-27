#!/usr/bin/env python3
import sys
from pathlib import Path
from paddleocr import PaddleOCR
from langdetect import detect
from deep_translator import GoogleTranslator

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".webp"}

def get_text_from_result(result) -> list[str]:
    lines = []
    for res in result:
        try:
            for text in res["rec_texts"]:
                if text and text.strip():
                    lines.append(text.strip())
        except (KeyError, TypeError):
            pass
    return lines

def translate_to_english(text: str) -> str:
    if not text.strip():
        return ""
    try:
        detected = detect(text)
        if detected == "en":
            return text
        return GoogleTranslator(source="auto", target="en").translate(text) or text
    except Exception as e:
        return f"[translation error: {e}]\n{text}"

def run_ocr_translate(root_dir: str, lang: str = "en"):
    ocr = PaddleOCR(lang=lang)
    root = Path(root_dir)
    images = [p for p in root.rglob("*") if p.suffix.lower() in IMAGE_EXTS]
    if not images:
        print(f"No images found under {root_dir}")
        return

    for img_path in images:
        out_path = img_path.with_suffix(".translated.txt")
        try:
            result = ocr.predict(str(img_path))
            raw_lines = get_text_from_result(result)
            raw_text = "\n".join(raw_lines)
            translated = translate_to_english(raw_text)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write("=== ORIGINAL ===\n")
                f.write(raw_text + "\n\n")
                f.write("=== TRANSLATED (EN) ===\n")
                f.write(translated + "\n")
        except Exception as e:
            print(f"{img_path}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)
    directory = sys.argv[1]
    language = sys.argv[2] if len(sys.argv) > 2 else "en"
    run_ocr_translate(directory, lang=language)
