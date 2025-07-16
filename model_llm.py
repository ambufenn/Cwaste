from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model & tokenizer sekali
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Simpan riwayat percakapan (jika perlu buat konteks)
chat_history_ids = None

def get_bot_reply(user_input, past_chat_ids=None):
    # Encode input dan tambahkan end-of-string token
    new_user_input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')

    # Gabungkan dengan riwayat percakapan sebelumnya (kalau ada)
    bot_input_ids = torch.cat([past_chat_ids, new_user_input_ids], dim=-1) if past_chat_ids is not None else new_user_input_ids

    # Generate response
    chat_history_ids = model.generate(
        bot_input_ids,
        max_length=bot_input_ids.shape[-1] + 50,
        pad_token_id=tokenizer.eos_token_id
    )

    # Decode respons terakhir bot
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response, chat_history_ids

