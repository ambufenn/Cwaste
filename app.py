#only for vlm show
'''
import streamlit as st
from model_vlm import classify_image_from_file
import tempfile
from PIL import Image

hf_token = st.secrets["HF_TOKEN"]

uploaded_file = st.file_uploader("Upload gambar")
if uploaded_file:
    image = Image.open(uploaded_file)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
        image.save(temp.name)
        result = classify_image_from_file(temp.name, token=hf_token)
    st.write(f"Hasil klasifikasi: {result}")

'''

#only for llm
'''
import streamlit as st
from model_llm import get_bot_reply

st.set_page_config(page_title="Chatbot Satvika", page_icon="💬")
st.title("🤖 Chatbot Satvika (Streamlit Edition)")

# Inisialisasi riwayat obrolan
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input dari user
user_input = st.text_input("Tanya ke chatbot:")

# Proses jawaban jika ada input
if user_input:
    with st.spinner("Bot sedang menjawab..."):
        reply = get_bot_reply(user_input)
        st.session_state.chat_history.append(("🧑 Kamu", user_input))
        st.session_state.chat_history.append(("🤖 Bot", reply))

# Tampilkan riwayat obrolan
for speaker, text in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {text}")
'''

#we try use html gabung 3 halaman

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Sampah Bercuan", layout="centered")

st.title("👋 Selamat Datang di Sampah Bercuan!")

st.markdown("""
Aplikasi ini membantu kamu mengenali jenis sampah, berkonsultasi lewat chatbot, dan memantau coin serta histori transaksi.
""")

st.markdown("### 🔍 Pilih fitur yang ingin kamu akses:")

# Buat 3 tombol sebagai gateway ke 3 halaman
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🖼️ Deteksi Sampah + Chat"):
        st.switch_page("pages/main_page.py")

with col2:
    if st.button("💰 Coin & Investasi"):
        st.switch_page("pages/coin_page.py")

with col3:
    if st.button("📜 Riwayat Transaksi"):
        st.switch_page("pages/history_page.py")



