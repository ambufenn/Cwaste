import streamlit as st
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
