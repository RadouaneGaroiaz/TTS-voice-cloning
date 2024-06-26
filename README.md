
# TTS App with Emotion Selection

This is a Streamlit web application that utilizes a Text-to-Speech (TTS) voice cloning API with emotion selection capabilities. Users can input a prompt and select an emotion from a predefined list, and the application generates synthesized audio based on the input.

## Features

- **Prompt Input:** Users can input a prompt for the TTS synthesis.
- **Emotion Selection:** Users can select an emotion (e.g., Happy, Sad, Angry, etc.) to infuse into the synthesized audio.
- **Real-time Generation:** Upon submitting the input prompt and selected emotion, the application sends a request to the TTS API, generates the audio, and displays it to the user in real-time.
- **Easy Integration:** Built using Streamlit, making it easy to deploy and integrate into various environments.

## Schema
![Schema](./Capture%20d'écran%202024-03-22%20153544.png)

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python 3.x
- Streamlit
- requests

## Setup

1. Clone this repository to your local machine:

   ```bash
   https://github.com/RadouaneGaroiaz/TTS-voice-cloning
   ```

2. Navigate to the project directory:

   ```bash
   cd your_repository
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py

## Docker Setup (Optional)

Alternatively, you can run the application using Docker. Follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t tts-app .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 8501:8501 tts-app
   ```

   Replace `8501` with the desired port number if you want to use a different port.

3. Access the application in your web browser at `http://localhost:8501`.
   ```

## Usage

1. Launch the application by following the setup instructions.
2. Enter your desired prompt in the provided text input field.
3. Select an emotion from the radio button options.
4. Click the "Send" button to initiate the TTS synthesis process.
5. Wait for the audio synthesis to complete, and the generated audio will be displayed on the screen.

## Credits

This application utilizes the following libraries:

- [Streamlit](https://streamlit.io/): For building interactive web applications with Python.
- [requests](https://docs.python-requests.org/en/latest/): For making HTTP requests to the TTS API.
- [tortoise-tts](https://github.com/neonbjb/tortoise-tts):











