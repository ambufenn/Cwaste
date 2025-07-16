from transformers import pipeline

# Inisialisasi pipeline dengan model dari Hugging Face
pipe = pipeline(
    "text-generation",
    model="satvikag/chatbot",
    max_new_tokens=100,
    do_sample=True,
    temperature=0.7,
)

def get_bot_reply(user_input):
    prompt = user_input
    result = pipe(prompt)
    reply = result[0]["generated_text"].replace(prompt, "").strip()
    return reply
