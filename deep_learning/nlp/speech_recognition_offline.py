"""
Automatic Speech Recognition (ASR)

Audio Signal Processing (DSP)
"""

import speech_recognition as sr
import librosa
import librosa.display
import matplotlib.pyplot as plt

# ---------------------------------------
# Record Audio using Microphone (VS Code)
# ---------------------------------------
recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak now... (recording for 5 seconds)")
    recognizer.adjust_for_ambient_noise(source)
    audio = recognizer.record(source, duration=5)

# Save audio to WAV file
with open("speech.wav", "wb") as f:
    f.write(audio.get_wav_data())

# ---------------------------------------
# Speech Recognition
# ---------------------------------------
try:
    text = recognizer.recognize_google(audio)
    print("\nRecognized Text:")
    print(text)
except Exception as e:
    print("Recognition Error:", e)

# ---------------------------------------
# Audio Signal Processing (Waveform Plot)
# ---------------------------------------
signal, sr_rate = librosa.load("speech.wav", sr=None)

plt.figure(figsize=(12, 4))
librosa.display.waveshow(signal, sr=sr_rate)
plt.title("Speech Signal Waveform")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()
