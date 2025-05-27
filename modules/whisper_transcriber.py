import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path, word_timestamps=True)
    words = []
    for segment in result.get("segments", []):
        for word in segment.get("words", []):
            words.append({
                "word": word["word"].strip().lower(),
                "start": round(word["start"], 2),
                "end": round(word["end"], 2)
            })
    return result["text"], words
