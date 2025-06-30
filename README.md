# 1. Audio to Structured JSON Converter (with Groq LLaMA 3)

This project takes unstructured, stream-of-consciousness **audio journal entries** and converts them into clean, structured **JSON format** using **Google Speech Recognition** and **Groq's LLaMA 3** language model.

---

##  What This Code Does

 Accepts an `.mp3` or `.wav` audio file.
 Converts the audio to a consistent format (`16kHz` mono WAV).
 Transcribes the audio to text using **Google's Speech Recognition** API.
 Sends the transcription to Groq's **LLaMA 3** model.
 Outputs a clean JSON structure for journaling, task logs, or daily reviews.

---

##  Example Input & Output

###  Example Audio Transcription with gramer mistak

today start my day at 5:30 and I like it was to lazy and I finished my personal work by 6:00 and started to go to gym and I reached there by 6:15 and I started my shoulder workout as per the schedule and after the gym I acceleration by 7:30 and after the gym I went to my home and like played with my dogs for all time and return to my living space in any sorry at 8:15 and I started my daily morning meeting I know the way told me to volunteer for Bhishma hunt which is for the students were it tells to improve their knowledge by asking simple maths question and it took very long time and I was late to my college and I got scold and after that I have I had my internship meeting which in which I was late to that also because of the meeting and I actually clarified some doubt with Vikram sir about my task after the meeting finished by 10 15 and since like I was hungry I went and bits for my breakfast and after the event back to my work where I have to convert audio file into text file with JSON output and I was writing code for that after that I had my lunch time which is 2:30 so yeah happy after finishing my after hearing that my friend got internship company will be appointed as full time worker 133 finish your lunch and then started my work again after that my sister call me and remember that on 27th her engagement was there since his brother so I have to be there on time and how to make some I have to put some permission on the day especially like putting putting permission in the base camp walking to the messenger and I went to sleep at 10:00 a.m.


```python
###  Generated JSON Output

{
  "personal": [
    {
      "title": "Morning routine",
      "description": "Started the day at 5:30 and finished personal work by 6:00"
    },
    {
      "title": "Gym",
      "description": "Went to the gym and completed a shoulder workout from 6:15 to 7:30"
    },
    {
      "title": "Play with dogs",
      "description": "Played with dogs at home from 7:30 to 8:15"
    },
    {
      "title": "Sister's engagement",
      "description": "Made plans to attend sister's engagement on 27th and requested permission for the day"
    }
  ],
  "work": [
    {
      "title": "Daily morning meeting",
      "description": "Attended daily morning meeting and volunteered for Bhishma hunt"
    },
    {
      "title": "Internship meeting",
      "description": "Attended internship meeting and clarified doubts with Vikram sir"
    },
    {
      "title": "Convert audio file to text",
      "description": "Wrote code to convert audio file to text file with JSON output"
    }
  ],
  "social": [
    {
      "title": "Breakfast",
      "description": "Took a break to have breakfast"
    },
    {
      "title": "Lunch",
      "description": "Took a break to have lunch and heard about friend's internship news"
    },
    {
      "title": "Call with sister",
      "description": "Received a call from sister to discuss her engagement plans"
    }
  ]
}

```
## Setting Up the Environment (macOS & Windows)
Install dependencies
Make sure Python 3.10+ is installed. You can check by running:

```bash
python --version
```
If it's not installed, download and install it from:
https://www.python.org/downloads/

Clone the Repository
```bash
git clone https://github.com/vishal320/audioto_textfile.git
cd audioto_textfile
```
Install Required Packages
Import necessary Python libraries:

Groq API key

ffmpeg installed and its path known (for pydub)

Install Dependencies
```python
pip install -r requirements.txt
```
Or manually:
```python
pip install pydub speechrecognition python-dotenv groq
```
Configure API Keys
Create a file named .env in your project directory:

```python
GROQ_API_KEY=your_actual_groq_api_key_here
```
don't share your .env file or post your API key publicly.

# Running the Script
```python
python main.py
```
You'll be prompted to enter the full path to your audio file:

```python
Enter the path to your audio file (.mp3 or .wav): C:\Users\you\Downloads\voice_note.mp3
```
The program will:

Convert and transcribe the audio

Generate structured JSON

Save the output to structured_output.json

# Use Cases
Personal journaling automation

Daily productivity summaries

Voice notes to structured insights

Mental health or self-awareness tools

# Notes
Make sure the ffmpeg.exe path is valid in the code.

JSON parsing may fail if Groq returns unstructured output. Debugging info will be shown in that case.

The model used: llama3-70b-8192 via Groq.


# Audio to AAC Converter (with Pydub and FFmpeg)

This  converts **any audio file format** (like `.mp3`, `.wav`, `.flac`, `.ogg`, `.opus`, `.webm`, etc.) into **AAC audio** saved as a `.m4a` file. It uses the Python `pydub` library along with `ffmpeg`.

---

## What This Code Does

- Accepts an audio file in any format supported by FFmpeg.
- Automatically detects the file type and decodes it.
- Converts and saves it as `.m4a` (AAC inside MP4 container).
- Works on `.mp3`, `.wav`, `.flac`, `.opus`, `.webm`, `.m4a`, even `.dat` files containing audio.

---

## Clone the Repository
```python
git clone https://github.com/vishal320/audioto_textfile.git
cd audioto_textfile
```
How to Run the Script
Run the converter with:

```python
python convert_to_aac.py
```
Then provide the full path to your audio file:
text
```
Enter path to your audio file: C:\Users\you\Downloads\voice_note.ogg
```
The script will convert it and save a file like:
text
```
C:\Users\you\Downloads\voice_note.m4a
```
Use Cases
Normalize audio format before transcription

Convert WhatsApp, Telegram, or other voice notes to .m4a

Prepare audio for mobile or browser playback

## Notes
This script does not transcribe audio.

For transcription + structured JSON using LLaMA 3 and Groq, see the related project: Audio to Structured JSON

Make sure ffmpeg is correctly installed and accessible from your command line.

