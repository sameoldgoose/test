import streamlit as st
import sounddevice as sd
import soundfile as sf
import requests
import json
import speech_recognition as sr
import os

r = sr.Recognizer()
def stot():
    filename = 'audio.wav'
    record_audio(filename, 6)
    # Show success message and download link
    # st.success("Recording saved successfully!")
    # st.audio(filename, format='audio/wav', start_time=0)
def query(data):
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
def record_audio(filename, duration):
    # Sample rate and number of channels
    sample_rate = 16000
    channels = 2

    # Start recording audio using sounddevice
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels)
    sd.wait()
    # Save the audio file using soundfile
    sf.write(filename, recording, sample_rate)

st.title("Audio Recorder")

# Get the desired filename and duration from the user
filename = st.text_input("Enter Filename", "audio.wav")
duration = st.slider("Recording Duration (seconds)", 1, 10, 5)
stop = st.button('Stop')
start = st.button('Start')
# Record button
if start:
    st.info("Recording started. Speak into the microphone.")

    # Record audio
    while start:
        print('recording')
        stot()
        audio = sr.AudioFile('audio.wav')
        with audio as source:
            audio1 = r.record(source)
            st.write(r.recognize_google(audio1))
        os.remove('audio.wav')
        if stop:
            break

# Display instructions
st.write("Click the 'Record' button to start recording audio.")
st.write("The recorded audio will be saved as a WAV file.")
