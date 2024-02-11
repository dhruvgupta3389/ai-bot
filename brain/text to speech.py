from gtts import gTTS
import os

# Specify the path to your text file
txt_file_path = r"D:\ai\brain\DataBase\095408.txt"


# Read text from the file
with open(txt_file_path, "r") as file:
    text_to_convert = file.read()

# Create a gTTS object
tts = gTTS(text=text_to_convert, lang='en')

# Specify the path for the output speech file (optional)
output_file_path = "output.mp3"

# Save the speech to a file
tts.save(output_file_path)

# Play the speech using a media player (optional)
os.system(f"start {output_file_path}")  # On Windows

