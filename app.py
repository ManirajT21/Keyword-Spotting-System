import streamlit as st
import numpy as np
import tempfile
import json
import os
from pydub import AudioSegment
from st_audiorec import st_audiorec

from modules.whisper_transcriber import transcribe_audio
from modules.keyword_analyzer import analyze_keywords  # returns paragraph
from modules.audio_input import save_uploaded_file

# --- Page Setup ---
st.set_page_config(page_title="Audio Keyword Detector", page_icon="🎧", layout="wide")
st.markdown("<h1 style='font-size: 36px;'>🎧 Audio Keyword Detection App</h1>", unsafe_allow_html=True)
st.caption("Upload or record audio, and detect keyword occurrences with precise timestamps.")

# --- Ensure output directory exists ---
os.makedirs("outputs", exist_ok=True)

# --- Keyword Input ---
with st.sidebar:
    st.header("🔑 Keywords to Detect")
    keywords = st.text_input("Enter keywords (comma-separated):", "fire, help, emergency, evacuate")
    keyword_list = [kw.strip().lower() for kw in keywords.split(",")]

# --- Input Method ---
st.markdown("### 🎤 Choose Input Method")
audio_path = None
input_method = st.radio("", ["🎙️ Record from Mic", "📁 Upload Audio File"], horizontal=True)

if input_method == "🎙️ Record from Mic":
    st.info("Click below to start recording.")
    wav_audio_data = st_audiorec()

    if wav_audio_data is not None:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(wav_audio_data)
            audio_path = f.name
            st.audio(f.name)
            st.success("🎙️ Recording complete!")

elif input_method == "📁 Upload Audio File":
    uploaded_file = st.file_uploader("Upload audio (.wav, .mp3)", type=["wav", "mp3"])
    if uploaded_file:
        audio_path = save_uploaded_file(uploaded_file)
        st.audio(audio_path)
        st.success("📁 File uploaded successfully!")

# --- Analysis and Output ---
if audio_path:
    try:
        with st.spinner("Transcribing audio..."):
            transcript, words = transcribe_audio(audio_path)

        st.subheader("🧾 Keyword Detection Summary")
        paragraph_summary = analyze_keywords(words, keyword_list, transcript)
        st.markdown(paragraph_summary, unsafe_allow_html=True)

        with st.expander("📜 Full Transcript"):
            st.markdown(f"<i>{transcript}</i>", unsafe_allow_html=True)

        # Export Section
        st.markdown("### 💾 Export Result")
        if st.button("Export to JSON"):
            result_data = {
                "summary": paragraph_summary,
                "transcript": transcript,
                "keywords": keyword_list
            }
            with open("outputs/keyword_results.json", "w") as f:
                json.dump(result_data, f, indent=2)
            st.success("✅ Results saved to `outputs/keyword_results.json`")

    except Exception as e:
        st.error(f"❌ Error: {e}")
