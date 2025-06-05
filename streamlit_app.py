import streamlit as st
from elevenlabs.client import ElevenLabs
from io import BytesIO

# Initialize ElevenLabs client
elevenlabs = ElevenLabs(api_key="your_api_key_here")

# UI: Text input
text = st.text_input("Enter text to speak", "The first move is what sets everything in motion.")

if st.button("🔊 Generate and Play Audio"):
    # Get generator from ElevenLabs
    audio_gen = elevenlabs.text_to_speech.convert(
        text=text,
        voice_id="JBFqnCBsd6RMkjVDRZzb",
        model_id="eleven_multilingual_v2",
        output_format="mp3_44100_128"
    )

    # Convert generator to bytes
    audio_bytes = b''.join(audio_gen)

    # Wrap in BytesIO and play
    audio_buffer = BytesIO(audio_bytes)
    st.audio(audio_buffer) # format="audio/mp3")

