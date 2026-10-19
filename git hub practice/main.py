
from gtts import gTTS
import os

# Text to convert into speech
text = input("Enter the text you want to speak: ")

# Select language: English
tts = gTTS(text=text, lang="en")

# Save speech as an MP3 file
tts.save("speech.mp3")

print("Speech generated successfully!")

# Play the generated audio (Windows)
os.startfile("speech.mp3")
