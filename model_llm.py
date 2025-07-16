from transformers import pipeline

# Buat pipeline-nya
pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-beta",
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
)

def get_bot_reply(user_input, history=None):
    # Gabungkan history kalau ada (belum pakai memory permanen ya)
    prompt = user_input
    response = pipe(prompt)
    reply_text = response[0]['generated_text'].replace(prompt, '').strip()
    return reply_text, history

