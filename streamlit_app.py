import streamlit as st
from elevenlabs.client import ElevenLabs
from io import BytesIO

# Initialize ElevenLabs client
elevenlabs = ElevenLabs(api_key="sk_70c410217f76f261a50a293d37e29b51c17157a7317b9ff1")

# UI: Text input
text = st.text_input("Enter text to speak", "The first move is what sets everything in motion.")

if st.button("🔊 Generate and Play Audio"):
    # Call ElevenLabs API
    audio_bytes = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )

    # In-memory audio stream
    audio_buffer = BytesIO(audio_bytes)

    # Streamlit audio player
    st.audio(audio_buffer, format="audio/mp3")
