import streamlit as st
import sys
import os

# Tambahkan path ke root supaya bisa import model_llm
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model_llm import get_bot_reply

st.title("📜 Riwayat Transaksi")

st.info("Data transaksi akan muncul di sini.")

st.subheader("🤖 Tanya Riwayat")
prompt = st.chat_input("Tanya riwayat kamu...")
if prompt:
    reply = get_bot_reply(prompt)
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("bot"):
        st.write(reply)
