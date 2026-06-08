# 🧠 AI Training Projects

> *คลังรวมของโค้ดสำหรับฝึกสอนและทดสอบโมเดลปัญญาประดิษฐ์ในหลากหลายโดเมน*

---

## ✨ Overview

โปรเจคนี้รวบรวมงานวิจัยและการทดลองด้าน Machine Learning ที่ครอบคลุมหลายโดเมน ตั้งแต่ **Computer Vision**, **Natural Language Processing** ไปจนถึง **Time-Series Forecasting** โดยแต่ละโฟลเดอร์ออกแบบมาให้เป็นอิสระและเข้าใจได้ง่าย พร้อมสำหรับการต่อยอดและปรับแต่งได้ทันที

---

## 📁 Project Structure

```
ai-training-projects/
│
├── 🔥 boiler-loss-prediction-lstm/
├── 🖼️  conv-next/
├── 🍽️  efficientnetb0-food-classification/
└── 📄 xlm-roberta-document-classification/
```

---

## 🚀 Projects

### 🔥 Boiler Loss Prediction — LSTM
> **Domain:** Time-Series Forecasting | **Model:** LSTM

พยากรณ์การสูญเสียพลังงานใน **Boiler** ด้วยโมเดล LSTM ที่รับ sequential sensor data แล้วทำนายค่า heat loss ล่วงหน้า ช่วยให้วิศวกรวางแผนการบำรุงรักษาเชิงป้องกันได้แม่นยำยิ่งขึ้น

| ไฟล์ | คำอธิบาย |
|------|----------|
| `LSTM.ipynb` | Notebook หลักสำหรับฝึกสอน วิเคราะห์ และประเมินโมเดล |

**Highlights:**
- ใช้ LSTM สำหรับ multi-step time-series forecasting
- มี preprocessing pipeline ด้วย StandardScaler + PCA


---



### 🖼️ ConvNeXt — Computer Vision
> **Domain:** Computer Vision | **Model:** ConvNeXt

นำ **ConvNeXt** มาใช้สำหรับงาน image classification และ feature extraction พร้อม fine-tuning pipeline ที่ปรับแต่งได้ผ่านไฟล์ config

| ไฟล์/โฟลเดอร์ | คำอธิบาย |
|----------------|----------|
| `main.py` | Entry point สำหรับรันการฝึกสอน |
| `fine_tune_convnext/` | โฟลเดอร์สำหรับ fine-tuning scripts |
| Config files | ตั้งค่า hyperparameter และ preprocessing |

**Highlights:**
- รองรับ transfer learning จาก pretrained ConvNeXt weights
- มีระบบ config แยกระหว่าง training และ preprocessing
- โครงสร้างเหมาะสำหรับ production deployment

---

### 🍽️ EfficientNetB0 — Food Classification
> **Domain:** Image Classification | **Model:** EfficientNetB0

จัดหมวดหมู่ **ภาพอาหาร** ด้วย EfficientNetB0 ซึ่งเป็นโมเดล lightweight ที่ให้ความแม่นยำสูงในขนาดที่เหมาะสำหรับ edge deployment

| ไฟล์ | คำอธิบาย |
|------|----------|
| `efficientnetb0.ipynb` | Notebook สาธิตการฝึกสอน, data augmentation, และประเมินผล |

**Highlights:**
- ใช้ EfficientNetB0 pretrained บน ImageNet
- มี data augmentation pipeline เพื่อเพิ่ม generalization
- Evaluation ด้วย confusion matrix และ classification report

---

### 📄 XLM-RoBERTa — Document Classification
> **Domain:** Natural Language Processing | **Model:** XLM-RoBERTa

จัดหมวดหมู่ **เอกสารหลายภาษา** ด้วย XLM-RoBERTa เหมาะสำหรับ corpus ที่มีทั้งภาษาไทยและภาษาอังกฤษ

| ไฟล์ | คำอธิบาย |
|------|----------|
| `y040-game-nam-four-3.ipynb` | Notebook สำหรับทดลองและประเมินโมเดล |

**Highlights:**
- Multilingual support ด้วย XLM-RoBERTa
- Fine-tuning บน custom document dataset
- วัดประสิทธิภาพด้วย F1-score, precision, recall

---

## 🛠️ Getting Started

### 1. Clone Repository
```bash
git clone https://github.com/your-username/ai-training-projects.git
cd ai-training-projects
```

### 2. เลือกโปรเจคที่สนใจ
```bash
cd boiler-loss-prediction-lstm   # หรือโฟลเดอร์อื่น
```

### 3. ติดตั้ง Dependencies
```bash
pip install -r requirements.txt
```

### 4. รัน Notebook หรือ Script
```bash
jupyter notebook LSTM.ipynb
# หรือ
python main.py
```

---

## 📦 Tech Stack

| Category | Libraries |
|----------|-----------|
| Deep Learning | TensorFlow / Keras, PyTorch |
| NLP | Hugging Face Transformers, XLM-RoBERTa |
| Computer Vision | EfficientNet, ConvNeXt, OpenCV |
| Data Processing | NumPy, Pandas, Scikit-learn |
| Visualization | Matplotlib, Seaborn |
| Serialization | Joblib, Pickle |

---

## 📌 Notes

> โครงสร้างนี้ออกแบบให้แต่ละโปรเจคเป็นอิสระจากกัน (self-contained) เพื่อให้ง่ายต่อการนำไปใช้ต่อในงานจริง
> หากต้องการรันการทดลองใหม่ ให้ตรวจสอบ environment และ dependency ในแต่ละโฟลเดอร์ก่อนเสมอ

---

<div align="center">
  <sub>Built with ❤️ for organized ML experimentation</sub>
</div>