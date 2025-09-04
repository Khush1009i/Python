from gtts import gTTS  # Imported module for text-to-speech conversion
import os

# Open the file in read mode and ensure it closes automatically
with open('sample.txt', 'r') as abc:
    text = abc.read()  # Read the content of the file

language = 'en'

# Create a gTTS object for the text-to-speech conversion
obj = gTTS(text=text, lang=language, slow=False)

# Save the audio file
obj.save("sample.mp3")

# Play the audio file
os.system("sample.mp3")  # Use "start" for Windows, "open" for macOS, and "xdg-open" for Linux
