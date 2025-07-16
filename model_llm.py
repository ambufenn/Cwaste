from transformers import pipeline

# Inisialisasi pipeline LLM dari Hugging Face
pipe = pipeline(
    "text-generation",
    model="HuggingFaceH4/zephyr-7b-beta",
    max_new_tokens=128,
    do_sample=True,
    temperature=0.7,
)

def get_bot_reply(user_input):
    prompt = user_input
    result = pipe(prompt)
    reply = result[0]["generated_text"].replace(prompt, "").strip()
    return reply
