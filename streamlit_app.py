import streamlit as st
from pydantic import BaseModel
from speech_processing import convert_voice_to_text, convert_text_to_voice
from text_processing import process_text

# Function to handle voice input
def handle_voice_input(voice_data):
    text = convert_voice_to_text(voice_data)
    response_text = process_text(text)
    response_voice = convert_text_to_voice(response_text)
    return response_voice

# Function to handle text input
def handle_text_input(text_input):
    response_text = process_text(text_input)
    return response_text

# Streamlit app layout
st.title("Voice and Text Processing App")

st.header("Voice Input")
voice_file = st.file_uploader("Upload a voice file", type=["wav", "mp3"])
if voice_file is not None:
    voice_data = voice_file.read()
    response_voice = handle_voice_input(voice_data)
    st.audio(response_voice, format="audio/wav")

st.header("Text Input")
text_input = st.text_input("Enter text:")
if st.button("Process Text"):
    if text_input:
        response_text = handle_text_input(text_input)
        st.write(response_text)
    else:
        st.write("Please enter some text.")
