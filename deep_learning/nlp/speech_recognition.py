"""
3. Browser‑based Audio Recording (Web + AI Integration)
The JavaScript code records audio inside Google Colab.

This is AI system integration, not a core AI field, but essential for building real applications.
"""

# Install required packages
from IPython.display import Javascript, display
from google.colab import output
from base64 import b64decode
import speech_recognition as sr
import librosa
import librosa.display
import matplotlib.pyplot as plt
import os

# ---------------------------------------
# JavaScript Code to Record Audio (5 sec)
# ---------------------------------------
RECORD_JS = """
async function record() {
    const stream = await navigator.mediaDevices.getUserMedia({audio:true});
    const recorder = new MediaRecorder(stream);
    const chunks = [];

    recorder.ondataavailable = e => chunks.push(e.data);
    recorder.start();

    // Record for 5 seconds
    await new Promise(resolve => setTimeout(resolve, 5000));

    recorder.stop();
    await new Promise(resolve => recorder.onstop = resolve);

    const blob = new Blob(chunks);
    const reader = new FileReader();

    return await new Promise(resolve => {
        reader.onloadend = () => resolve(reader.result.split(',')[1]);
        reader.readAsDataURL(blob);
    });
}
"""

display(Javascript(RECORD_JS))

# Execute JS and save audio
audio_data = output.eval_js("record()")

with open("speech.webm", "wb") as f:
    f.write(b64decode(audio_data))

# ---------------------------------------
# Convert WEBM → WAV using FFmpeg
# ---------------------------------------
os.system("ffmpeg -loglevel panic -i speech.webm speech.wav -y")

# ---------------------------------------
# Speech Recognition
# ---------------------------------------
recognizer = sr.Recognizer()

with sr.AudioFile("speech.wav") as source:
    audio = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio)
    print("Recognized Text:")
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
