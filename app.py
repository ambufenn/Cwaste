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

import streamlit as st
from model_vlm import classify_image_from_file
from model_llm import get_bot_reply
import tempfile
from PIL import Image

hf_token = st.secrets["HF_TOKEN"]

# UI: Buat tab untuk pisahkan fitur
tab1, tab2 = st.tabs(["🖼️ Klasifikasi Gambar", "💬 Chatbot Sampah"])

# =====================
# 🖼️ TAB 1: KLASIFIKASI
# =====================
with tab1:
    st.header("Klasifikasi Sampah dari Gambar")
    uploaded_file = st.file_uploader("Upload gambar sampah")
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Gambar yang diunggah", use_column_width=True)
        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp:
            image.save(temp.name)
            result = classify_image_from_file(temp.name, token=hf_token)
        st.success(f"Hasil klasifikasi: **{result}**")

# =====================
# 💬 TAB 2: CHATBOT
# =====================
with tab2:
    st.header("Tanya Bot tentang Sampah ♻️")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    user_input = st.text_input("Tanyakan sesuatu ke bot (contoh: Apa itu sampah organik?)")

    if user_input:
        bot_reply, updated_history = get_bot_reply(user_input, st.session_state.chat_history)
        st.session_state.chat_history = updated_history
        st.markdown(f"**🤖 Bot:** {bot_reply}")
