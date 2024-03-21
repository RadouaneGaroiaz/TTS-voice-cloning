import streamlit as st
import requests

def make_api_request(prompt, emotion):
    response = requests.post("http://127.0.0.1:7860/run/generate", json={
        "data": [
            prompt,
            "hello world",
            emotion,
            "hello world",
            "random",
            {"name":"audio.wav","data":"data:audio/wav;base64,UklGRiQAAABXQVZFZm10IBAAAAABAAEARKwAAIhYAQACABAAZGF0YQAAAAA="},
            0,
            1,
            0,
            16,
            30,
            0.2,
            "P",
            8,
            0,
            0.8,
            1,
            1,
            2,
            2,
            ["Half Precision"],
            False,
            False,
        ]
    }).json()
    return response["data"]

st.title("TTS App with Emotion Selection")

prompt = st.text_input("Enter your prompt:")
emotion = st.radio("Select emotion:", ("Happy", "Sad", "Angry", "Disgusted", "Arrogant", "None"))

if st.button("Send"):
    with st.spinner("Loading..."):
        data = make_api_request(prompt, emotion)
        st.success("Data received!")
        st.write(data)
