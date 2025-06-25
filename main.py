import os
import json
import tempfile
from pydub import AudioSegment
from pydub.utils import which
import speech_recognition as sr
from dotenv import load_dotenv
from groq import Groq

# Load .env and Groq API Key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Missing GROQ_API_KEY in .env")

# Configure Groq client
client = Groq(api_key=GROQ_API_KEY)

# Set ffmpeg converter path explicitly
AudioSegment.converter = which(
    "C:\\Users\\visha\\Downloads\\ffmpeg-2025-06-16-git-e6fb8f373e-essentials_build\\ffmpeg-2025-06-16-git-e6fb8f373e-essentials_build\\bin\\ffmpeg.exe"
)

def convert_audio_to_wav(file_path):
    print("Converting audio to 16kHz mono WAV...")
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1).set_frame_rate(16000)
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = tmp.name
        audio.export(wav_path, format="wav")
    return wav_path

def transcribe_audio(file_path):
    wav_path = convert_audio_to_wav(file_path)
    recognizer = sr.Recognizer()
    print("Transcribing audio with Google Speech Recognition...")
    try:
        with sr.AudioFile(wav_path) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
        return text.strip()
    except sr.UnknownValueError:
        raise Exception("Could not understand audio. Try a clearer recording.")
    except sr.RequestError as e:
        raise Exception(f"Google Speech Recognition failed: {e}")
    finally:
        os.remove(wav_path)

def generate_structured_output(user_input):
    system_prompt = """
You are a precise assistant that transforms a stream-of-consciousness journal entry into structured JSON format.

Instructions:
1. Identify individual tasks/activities from the text.
2. For each, return:
   - "title": Short descriptive title.
   - "description": Full sentence explaining what happened.
   - "category": One of "personal", "work", or "social".

If a task doesn't clearly fit any category, skip the category key.

Output valid JSON in this format:
[
  {
    "entry": 1,
    "title": "Short summary",
    "description": "Full explanation.",
    "category": "personal"
  }
]
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_input}
    ]

    print("Sending transcription to LLaMA 3 via Groq...")
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=messages,
        temperature=0.3,
        max_tokens=2048
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    file_path = input("Enter the path to your audio file (.mp3, .wav, or .aac): ").strip().strip('"').strip("'")

    if not os.path.isfile(file_path):
        print("File not found. Please check the path and try again.")
        exit(1)

    try:
        transcription = transcribe_audio(file_path)
        print(f"\nTranscribed Text:\n{transcription}\n")

        structured_output = generate_structured_output(transcription)

        try:
            parsed_output = json.loads(structured_output)
            print("\nStructured JSON Output:\n")
            print(json.dumps(parsed_output, indent=2))

            with open("structured_output.json", "w", encoding="utf-8") as f:
                json.dump(parsed_output, f, indent=2)
            print("Output saved to structured_output.json")

        except json.JSONDecodeError:
            print("Could not parse JSON. Raw output:")
            print(structured_output)

    except Exception as e:
        print(f"\nError during processing:\n{e}")
