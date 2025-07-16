'''
import streamlit as st
from PIL import Image
import tempfile
from model_vlm import classify_image_from_file
from model_llm import get_bot_reply

def run():
    hf_token = st.secrets["HF_TOKEN"]

    st.header("📸 Upload Gambar Sampah")
    uploaded_file = st.file_uploader("Upload gambar (jpg/png)", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Gambar yang Diupload", use_column_width=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
            img.save(temp.name)
            label = classify_image_from_file(temp.name, token=hf_token)
        st.success(f"♻️ Jenis Sampah Terdeteksi: **{label}**")

    st.subheader("🤖 Tanya Soal Sampah")
    prompt = st.chat_input("Tulis pertanyaanmu...")
    if prompt:
        reply = get_bot_reply(prompt)
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("bot"):
            st.write(reply)
            '''

import streamlit as st
from PIL import Image
import tempfile
import sys
import os

# Tambah path ke root folder supaya bisa import modul dari luar folder 'pages'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_vlm import classify_image_from_file
from model_llm import get_bot_reply

# Load token dari secret
hf_token = st.secrets["HF_TOKEN"]

st.title("📸 Upload & Tanya Sampah")

# Upload gambar
uploaded_file = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Gambar Terupload", use_column_width=True)
    
    # Simpan sementara dan klasifikasikan
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
        img.save(temp.name)
        label = classify_image_from_file(temp.name, token=hf_token)
    st.success(f"♻️ Jenis sampah: **{label}**")

# Chatbot
st.subheader("🤖 Chatbot tentang Sampah")
prompt = st.chat_input("Tanya di sini...")
if prompt:
    reply = get_bot_reply(prompt)
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("bot"):
        st.write(reply)


