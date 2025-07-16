from transformers import pipeline

# Buat pipeline-nya
pipe = pipeline(
from transformers import pipeline

# Inisialisasi pipeline sekali
pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-beta",
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
)

def get_bot_reply(user_input, history=None):
    # History belum dipakai di sini, tapi bisa dikembangkan nanti
    prompt = user_input
    response = pipe(prompt)
    reply_text = response[0]['generated_text'].replace(prompt, '').strip()
    return reply_text, history


