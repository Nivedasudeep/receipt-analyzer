import streamlit as st
import requests

st.title("📥 Receipt Uploader & Visualizer")

uploaded_file = st.file_uploader("Upload Receipt (.jpg, .pdf, .png, .txt)", type=["jpg", "png", "pdf", "txt"])
if uploaded_file:
    with open("temp_upload", "wb") as f:
        f.write(uploaded_file.read())
    files = {"file": open("temp_upload", "rb")}
    response = requests.post("http://localhost:8000/upload/", files=files)
    if response.status_code == 200:
        st.success("Uploaded & Parsed!")
        st.json(response.json()["data"])
    else:
        st.error("Failed to process.")
