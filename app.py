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

hf_token = st.secrets["HF_TOKEN"]

st.set_page_config(page_title="Sampah Bercuan", layout="centered")

# CSS style for HTML
st.markdown("""
    <style>
        .section { margin-top: 30px; }
        .chat-message { margin-top: 10px; padding: 10px; border-radius: 5px; }
        .user { background-color: #d9fdd3; }
        .bot { background-color: #f0f0f0; }
    </style>
""", unsafe_allow_html=True)

menu = st.selectbox("Menu", ["Main", "Coin", "History"])

# === MAIN ===
if menu == "Main":
    st.markdown("## 🖼️ Upload Trash Image")

    uploaded_file = st.file_uploader("Upload image of trash", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img, caption="Uploaded Image", use_column_width=True)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
            img.save(temp.name)
            label = classify_image_from_file(temp.name, token=hf_token)
        st.success(f"🧠 Detected: **{label}**")

    # === CHAT ===
    st.markdown('<div class="section"><h3>🤖 Ask About the Trash</h3></div>', unsafe_allow_html=True)
    prompt = st.chat_input("Tanya ke chatbot")
    if prompt:
        response = get_bot_reply(prompt)
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-message user">🧍 {prompt}</div>', unsafe_allow_html=True)
        with st.chat_message("bot"):
            st.markdown(f'<div class="chat-message bot">🤖 {response}</div>', unsafe_allow_html=True)

# === COIN ===
elif menu == "Coin":
    st.markdown("## 💰 Your eWallet Balance")
    st.info("Fitur ini sedang dikembangkan.")

# === HISTORY ===
elif menu == "History":
    st.markdown("## 🕘 Transaction History")
    st.info("Transaksi akan ditampilkan setelah fitur aktif.")

    st.markdown('<div class="section"><h3>🧾 Ask About History</h3></div>', unsafe_allow_html=True)
    prompt = st.chat_input("Tanya tentang riwayatmu")
    if prompt:
        response = get_bot_reply(prompt)
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-message user">🧍 {prompt}</div>', unsafe_allow_html=True)
        with st.chat_message("bot"):
            st.markdown(f'<div class="chat-message bot">🤖 {response}</div>', unsafe_allow_html=True)
