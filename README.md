#  Audio to Structured JSON Converter (with Groq LLaMA 3)

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

###  Example Audio Transcription

I started my day at 5:25 AM and went to the gym around 6:00 AM.
I did a workout and returned home by 7:15 AM.
After my morning routine, I attended a meeting at 7:47 AM about acids and bases.
I'm volunteering at a workshop called Beshma Hunt.

```python
###  Generated JSON Output

```json
[
  {
    "entry": 1,
    "title": "Woke up at 5:25 AM",
    "description": "Started the day by waking up at 5:25 AM."
  },
  {
    "entry": 2,
    "title": "Gym at 6:00 AM",
    "description": "Went to the gym at 6:00 AM and completed a workout, returning home by 7:15 AM."
  },
  {
    "entry": 3,
    "title": "Morning meeting at 7:47 AM",
    "description": "Attended a morning meeting about acids and bases, including experiments and classifications."
  },
  {
    "entry": 4,
    "title": "Volunteering at Beshma Hunt",
    "description": "Volunteering at a children's workshop called Beshma Hunt, focused on brain development through activities."
  }
]

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
The program will:
```
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