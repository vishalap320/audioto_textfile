import sounddevice as sd
import numpy as np
import wave
from pydub import AudioSegment
import os
import threading

sample_rate = 44100
channels = 2
temp_wav = "temp_audio.wav"
recording = []
is_recording = True

def record_audio():
    global recording
    print("Recording... Press Enter to stop.")
    audio = []

    def callback(indata, frames, time, status):
        if is_recording:
            audio.append(indata.copy())

    with sd.InputStream(samplerate=sample_rate, channels=channels, dtype='int16', callback=callback):
        while is_recording:
            sd.sleep(100)

    full_recording = np.concatenate(audio, axis=0)
    recording = full_recording

def wait_for_enter():
    global is_recording
    input()
    is_recording = False

def save_to_m4a(output_filename):
    with wave.open(temp_wav, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())

    try:
        audio = AudioSegment.from_wav(temp_wav)
        audio.export(output_filename, format="mp4")
        print(f"Saved as {output_filename}")
    except Exception as e:
        print("Export failed:", e)
    finally:
        if os.path.exists(temp_wav):
            os.remove(temp_wav)

if __name__ == "__main__":
    output_file = "recorded.m4a"
    threading.Thread(target=wait_for_enter).start()
    record_audio()
    save_to_m4a(output_file)
