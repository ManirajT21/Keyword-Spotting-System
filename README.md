🎧 Audio Keyword Detection with Whisper & Streamlit
An interactive web application for detecting user-defined keywords in speech using OpenAI’s Whisper model, enhanced with NLP concepts and delivered through a clean Streamlit interface.
This project showcases how to properly apply pre-trained models in real-world workflows, especially in educational and voice-driven applications.



📌 Table of Contents
1. Features

2. NLP Concepts Applied

3. Tech Stack

4. Project Structure

5. Setup Instructions

6. Usage

7. Sample Output

8. Future Enhancements

9. License
    
    

✅ Features
🎤 Mic Recording: Record live speech via browser

📁 File Upload: Upload .wav or .mp3 audio

🔍 Keyword Detection: Match user-defined keywords with timestamp tracking

🧾 Paragraph Summary: NLP-style explanation of detected words

📜 Full Transcript Viewer: Expandable section for complete speech output

💾 Export Options: Save results as JSON and transcript as .txt



🧠 NLP Concepts Applied
Text normalization & lowercasing

Token filtering and word mapping

Timestamp alignment

Keyword-based paragraph summarization

(Optional extensions):

Filler word detection

Speaking pace estimation

Semantic keyword similarity (e.g., using sentence-transformers)



⚙️ Tech Stack
| Component | Tool/Library                                |
| --------- | ------------------------------------------- |
| UI        | Streamlit                                   |
| Model     | OpenAI Whisper / Faster-Whisper             |
| Audio I/O | Pydub, st-audiorec                          |
| NLP Logic | Pure Python / Optional: spaCy, Transformers |
| Export    | JSON, plain text                            |
| Language  | Python 3.8+                                 |



🗂 Project Structure
audio-keyword-detector/
│
├── app.py                        # Main Streamlit app
├── requirements.txt
├── README.md
├── outputs/                      # JSON / TXT output
└── modules/
    ├── audio_input.py           # Mic/file save handling
    ├── whisper_transcriber.py   # Whisper-based transcription
    └── keyword_analyzer.py      # Keyword matching and summary generation



🚀 Future Enhancements
 Word-by-word pronunciation feedback

 Real-time transcription preview

 Filler word detection ("um", "uh")

 Speech pacing analysis

 Support for multilingual transcription

 Integration with educational platforms (LMS, Google Classroom)



 📜 License
This project is licensed under the MIT License.
© 2025 [Maniraj T]

