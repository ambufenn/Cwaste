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

import streamlit as st
from model_llm import get_bot_reply

st.title("🤖 Chatbot Sampah (LLaMA 3.1)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Tanya ke bot:")

if user_input:
    with st.spinner("Bot sedang menulis..."):
        reply, updated_history = get_bot_reply(user_input, st.session_state.chat_history)
        st.session_state.chat_history = updated_history
        st.markdown(f"**Bot:** {reply}")



