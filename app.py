import streamlit as st

st.set_page_config(
    page_title="Scam Voice Detector",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ Scam Voice Detector")
st.write("Upload an audio recording to check whether it may be a scam.")

st.divider()

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3", "m4a", "ogg"]
)

if uploaded_file is not None:
    st.success("Audio file uploaded successfully!")

    st.write("**File name:**", uploaded_file.name)
    st.write("**File size:**", f"{uploaded_file.size / 1024:.2f} KB")

    st.audio(uploaded_file)

    st.divider()

    st.subheader("Analysis Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Voice Score", "Pending")

    with col2:
        st.metric("Risk Level", "Pending")

    st.info("Backend analysis will be connected here.")