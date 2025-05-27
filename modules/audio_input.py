import sounddevice as sd
import wave
import tempfile

def record_audio(duration=5, samplerate=16000):
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    with wave.open(temp.name, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(samplerate)
        wf.writeframes(audio.tobytes())
    return temp.name

def save_uploaded_file(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
        temp_file.write(uploaded_file.read())
        return temp_file.name
