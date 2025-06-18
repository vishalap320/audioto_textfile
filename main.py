import os
import json
import tempfile
from pydub import AudioSegment
from pydub.utils import which
import speech_recognition as sr
from groq import Groq
from dotenv import load_dotenv

# ✅ Set exact path to ffmpeg.exe (avoids RuntimeWarning)
AudioSegment.converter = which(
    "C:\\Users\\visha\\Downloads\\ffmpeg-2025-06-16-git-e6fb8f373e-essentials_build\\ffmpeg-2025-06-16-git-e6fb8f373e-essentials_build\\bin\\ffmpeg.exe"
)

# ✅ Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY! Set it in .env or system environment.")

# ✅ Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def convert_audio_to_wav(file_path):
    print("🔊 Converting audio to WAV...")
    audio = AudioSegment.from_file(file_path)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = tmp.name
        audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio(file_path):
    wav_path = convert_audio_to_wav(file_path)
    recognizer = sr.Recognizer()
    print("🧠 Transcribing audio with SpeechRecognition...")
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    os.remove(wav_path)  # Cleanup temp file
    return text.strip()

def generate_structured_output(user_input):
    system_prompt = """
You are a precise assistant that transforms a stream-of-consciousness journal entry into a structured JSON format.

Instructions:
- Break the journal entry into individual events or concerns.
- For each, provide:
  - "title": a short, specific summary (include time if present, e.g., "Swimming class at 12 PM").
  - "description": a detailed sentence (not a list) summarizing everything related to the title.
- Ensure every entry has both a "title" and a "description" key.
- Output only valid, complete JSON in this format:

[
  {
    "entries": [
      {
        "entry": 1,
        "title": "Short, specific title",
        "description": "Clear and complete description."
      }
    ]
  }
]

Notes:
- Do not include empty or partial entries.
- Do not include categories or commentary.
- Output only valid JSON, nothing else.
"""
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    print("📡 Sending transcription to Groq...")
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.3,
        max_tokens=2048
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    file_path = input("Enter the path to your audio file (.mp3 or .wav): ").strip()

    if not os.path.isfile(file_path):
        print("❌ File does not exist. Please check the path.")
        exit(1)

    try:
        transcription = transcribe_audio(file_path)
        print(f"\n📝 Transcribed Text:\n{transcription}\n")

        structured_output = generate_structured_output(transcription)

        try:
            parsed_output = json.loads(structured_output)
            print("\n📦 Structured JSON Output:\n")
            print(json.dumps(parsed_output, indent=2))
        except json.JSONDecodeError:
            print("⚠️ Could not parse the response as JSON. Raw output:")
            print(structured_output)

    except Exception as e:
        print("❌ Error during processing:", e)
