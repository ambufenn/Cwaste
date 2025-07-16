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

#we try use html

import streamlit as st
from PIL import Image
import tempfile

from model_vlm import classify_image_from_file
from model_llm import get_bot_reply

hf_token = st.secrets["HF_TOKEN"]  # dari secrets

st.set_page_config(page_title="Sampah Bercuan", layout="centered")
menu = st.selectbox("Menu", ["Main", "Coin", "History"])

# === MAIN PAGE ===
if menu == "Main":
    st.header("Upload Trash Image")
    uploaded_file = st.file_uploader("Upload image of trash", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        # Simpan sementara dan klasifikasikan
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
            img.save(temp.name)
            label = classify_image_from_file(temp.name, token=hf_token)
            st.success(f"Detected: {label}")

    # Chatbot
    st.subheader("Ask About the Trash")
    prompt = st.chat_input("Tanya ke chatbot")
    if prompt:
        reply = get_bot_reply(prompt)
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("bot"):
            st.write(reply)

# === COIN PAGE ===
elif menu == "Coin":
    st.header("Your eWallet Balance")
    st.markdown("_Coming soon..._ 💸")

    st.subheader("Available Investments")
    st.warning("Fitur investasi akan segera hadir...")

# === HISTORY PAGE ===
elif menu == "History":
    st.header("Transaction History")
    st.info("Transaksi akan ditampilkan setelah fitur aktif.")

    st.subheader("Ask About History")
    prompt = st.chat_input("Tanya tentang riwayatmu")
    if prompt:
        reply = get_bot_reply(prompt)
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("bot"):
            st.write(reply)
