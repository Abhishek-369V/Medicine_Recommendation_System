# 💊 Medicine Recommendation System

A machine learning-based web application that predicts diseases from user-reported symptoms and provides comprehensive health recommendations including Medicines, Diet_plans, Precautions, Lifestyle_advice and generates a Risk_score based on the severity of the symptoms.

---

## 🚀 Live Demo

> https://medicine-recommendation-system-mav.streamlit.app/

---

## 📌 Features

- 🔍 **Disease Prediction** — Predicts the most likely disease based on input symptoms
- 💊 **Medicine Recommendation** — Suggests relevant medicines for the predicted disease
- 🥗 **Diet Advice** — Recommends suitable diet plans to aid recovery
- ⚠️ **Precautions** — Lists important precautions to follow
- 🏃 **Lifestyle Advice** — Provides actionable lifestyle changes for better health
- 📊 **Risk Score** — Generates a risk score based on the severity of the sympotms

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend / UI | Streamlit |
| ML Model | Random Forest Classifier |
| Language | Python |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |


---

## 🧠 How It Works

1. User enters their symptoms via the web interface
2. The Random Forest model processes the symptoms and predicts the disease
3. Based on the predicted disease, the system fetches:
   - Recommended medicines
   - Diet suggestions
   - Precautions to follow
   - Lifestyle advice
4. A **risk score** is calculated and displayed to the user --> which tells us the condition of the patient!

---

## 📂 Project Structure

```
Medicine-Recommendation-System/
│
├── data/                     # dataset files
├── models/                   # Trained Random Forest model stored
├── src                       # Main Source code 
├── streamlit_app             # Main Streamlit application
├── requirements.txt          # Python dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/medicine-recommendation-system.git
   cd medicine-recommendation-system
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run streamlit_app/app.py
   ```

4. Open your browser and go to `http://localhost:8501`

---

## ⚠️ Limitations

- ❌ No dosage information provided
- ❌ No doctor appointment booking feature
- This tool is for **informational purposes only** and is **not a substitute for professional medical advice**

---

## 👨‍💻 Author

**Madanala Abhishek Varma**
- B.Tech CSE Graduate | AI/ML Enthusiast
- GitHub: [@Abhishek-369V](https://github.com/Abhishek-369V)

---

## 📄 License

This project is licensed under the MIT License.

---

> ⚕️ _Disclaimer: This application is built for educational purposes. Always consult a certified medical professional for health-related decisions._
