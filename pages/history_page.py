import streamlit as st
from model_llm import get_bot_reply

def run():
    st.header("📜 Riwayat Transaksi")
    st.info("Data transaksi akan tampil setelah fitur aktif.")

    st.subheader("🤖 Tanya Tentang Riwayatmu")
    prompt = st.chat_input("Tanya tentang transaksi kamu...")
    if prompt:
        reply = get_bot_reply(prompt)
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("bot"):
            st.write(reply)
