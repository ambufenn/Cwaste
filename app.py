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
import os
from huggingface_hub import InferenceClient

hf_token = os.getenv("HF_TOKEN")
client = InferenceClient(provider="fireworks-ai", api_key=hf_token)

def get_bot_reply(user_input, chat_history=None):
    messages = []

    # History (jika mau disimpan, bisa pakai st.session_state nanti)
    if chat_history:
        messages.extend(chat_history)

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=messages,
    )

    reply = completion.choices[0].message.content
    return reply, messages + [{"role": "assistant", "content": reply}]


