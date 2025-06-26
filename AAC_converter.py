from pydub import AudioSegment
import os
import mimetypes

def convert_to_aac(input_path, output_path=None):
    if not os.path.isfile(input_path):
        print(f"File not found: {input_path}")
        return

    # Try to detect the audio format
    mime_type, _ = mimetypes.guess_type(input_path)
    file_format = None
    if mime_type and mime_type.startswith("audio/"):
        file_format = mime_type.split("/")[1]

    try:
        audio = AudioSegment.from_file(input_path, format=file_format)
    except Exception as e:
        print(f"Could not load audio: {e}")
        return

    if output_path is None:
        base = os.path.splitext(input_path)[0]
        output_path = base + ".m4a"

    try:
        audio.export(output_path, format="mp4")
        print(f"Conversion successful. Saved as: {output_path}")
    except Exception as e:
        print(f"Export failed: {e}")

if __name__ == "__main__":
    input_audio = input("Enter path to your audio file: ").strip()
    convert_to_aac(input_audio)
