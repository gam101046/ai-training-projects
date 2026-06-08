from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image

# path ของโมเดลที่คุณ save หลัง fine-tune
model_path = "/Users/gam/Desktop/fine_tune_convNeXT/fine_tune_convnext"

# โหลด feature extractor และโมเดล
feature_extractor = AutoImageProcessor.from_pretrained(model_path)
model = AutoModelForImageClassification.from_pretrained(model_path)

# ส่งโมเดลไป GPU ถ้ามี
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# ตัวอย่างโหลดรูปเดียว
img_path = "/Users/gam/Desktop/fine_tune_convNeXT/ไม่ดีเท่าไหร่_frame_00246_aug1.jpg"
image = Image.open(img_path).convert("RGB")

# preprocess
inputs = feature_extractor(image, return_tensors="pt").to(device)


with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_idx = logits.argmax(-1).item()  # index ของ class
    predicted_label = model.config.id2label[predicted_class_idx]

print("Predicted class:", predicted_label)
