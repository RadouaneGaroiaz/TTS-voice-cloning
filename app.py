import streamlit as st
import pyttsx3

# Initialize TTS engine globally to avoid multiple initializations
engine_initialized = False

def initialize_engine():
    global engine_initialized
    if not engine_initialized:
        pyttsx3.init()
        engine_initialized = True

def generate_tts_with_emotion(text, emotion):
    initialize_engine()

    engine = pyttsx3.init()
    emotion_properties = {
        "Happy": {"rate": 150, "volume": 1.0},
        "Sad": {"rate": 100, "volume": 0.8},
        "Angry": {"rate": 200, "volume": 1.0},
        "Neutral": {"rate": 125, "volume": 1.0},
    }
    properties = emotion_properties.get(emotion, emotion_properties["Neutral"])

    engine.setProperty('rate', properties['rate'])
    engine.setProperty('volume', properties['volume'])
    engine.say(text)
    engine.runAndWait()

def voice_clone(text, speaker_wav, language):
    # Placeholder for voice cloning functionality
    # This would involve loading a model, processing the audio, and generating a voice clone.
    output_file_path = "path_to_generated_voice_clone.wav"
    return output_file_path

# Streamlit UI
st.title("Unified Text-to-Speech Interface with Emotion and Voice Cloning")

# Unified text input
text_input = st.text_area("Enter your text:")

# Choice between TTS with emotion and voice cloning
task = st.selectbox("Choose Task:", ["Text-to-Speech with Emotion", "Voice Cloning"])

# Conditional UI elements based on the task
if task == "Text-to-Speech with Emotion":
    emotion = st.selectbox("Select Emotion:", ("Happy", "Sad", "Angry", "Neutral"))
elif task == "Voice Cloning":
    speaker_wav = st.file_uploader("Upload Speaker WAV File", type=["wav"])
    language = st.selectbox("Language", ["en", "ko"])

# Process input
if st.button("Process"):
    if task == "Text-to-Speech with Emotion":
        if text_input:
            generate_tts_with_emotion(text_input, emotion)
            st.success("TTS with emotion generated.")
        else:
            st.error("Please enter some text.")
    elif task == "Voice Cloning":
        if text_input and speaker_wav:
            # Placeholder functionality; replace with actual voice cloning implementation.
            st.success("Voice clone generated. (Placeholder functionality)")
        else:
            st.error("Please provide both text and a speaker WAV file.")
