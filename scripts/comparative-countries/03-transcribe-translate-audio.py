#!/usr/bin/env python3
import sys
from pathlib import Path
import whisper

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <path>")
    sys.exit(1)

ROOT = Path(sys.argv[1])
MODEL = "medium"
EXTENSIONS = {
    ".mp4", ".mkv", ".avi", ".mov", ".webm",
    ".m4v", ".wmv", ".flv", ".mp3", ".wav",
    ".m4a", ".ogg", ".aac"
}
model = whisper.load_model(MODEL, device="cuda")
for file in ROOT.rglob("*"):
    if file.suffix.lower() not in EXTENSIONS:
        continue
    print(file)
    try:
        audio = whisper.load_audio(str(file))
        mel = whisper.log_mel_spectrogram(
            whisper.pad_or_trim(audio)
        ).to(model.device)
        _, probs = model.detect_language(mel)
        language = max(probs, key=probs.get)
        result = model.transcribe(
            str(file),
            task="transcribe" if language == "en" else "translate",
            fp16=True,
        )
        whisper.utils.get_writer("srt", str(file.parent))(result, file.stem)

    except RuntimeError as e:
        if "Failed to load audio" in str(e):
            print(f"Skipping (no audio): {file}")
            continue
        raise
