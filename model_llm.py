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
