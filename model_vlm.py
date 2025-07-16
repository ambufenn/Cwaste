import os
from dotenv import load_dotenv
from transformers import pipeline, AutoImageProcessor, AutoModelForImageClassification
from PIL import Image
import requests
from io import BytesIO

# Load token dari .env
load_dotenv()
hf_token = os.getenv("HF_TOKEN")

# Cara 1: Pakai pipeline langsung
def classify_image_from_url(image_url):
    pipe = pipeline("image-classification", model="yangy50/garbage-classification", token=hf_token)
    result = pipe(image_url)
    return result

# Cara 2: (Opsional) Load model langsung untuk custom logic
def classify_image_from_file(image_path):
    processor = AutoImageProcessor.from_pretrained("yangy50/garbage-classification", token=hf_token)
    model = AutoModelForImageClassification.from_pretrained("yangy50/garbage-classification", token=hf_token)

    image = Image.open(image_path).convert("RGB")
    inputs = processor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()
    label = model.config.id2label[predicted_class_idx]
    return label

# Tes dari URL
if __name__ == "__main__":
    image_url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/hub/parrots.png"
    result = classify_image_from_url(image_url)
    print("Hasil klasifikasi (URL):", result)

    # Tes dari file lokal (optional)
    # result_file = classify_image_from_file("contoh.jpg")
    # print("Hasil klasifikasi (file):", result_file)
