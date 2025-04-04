# 😄 Emotion Prediction Web App

Welcome to the **Emotion Prediction Web App** repository! This project is a fun and interactive tool that uses **Machine Learning** to detect emotions from user-submitted text using a simple **Flask web interface**.

## 📌 Project Overview

This application is designed to:

- 🧠 Predict **emotions** such as Joy, Anger, Sad, etc., based on text input.
- 💬 Provide a simple UI where users can type in their thoughts or feelings.
- 🚀 Serve predictions using a pre-trained **ML model** wrapped in a Flask API.

## 📂 Dataset & Model

- 🔹 **Dataset**: `combined_emotion.csv` - based on Kaggle dataset. Download Dataset[https://www.kaggle.com/datasets/kushagra3204/sentiment-and-emotion-analysis-dataset/data]
- 🔹 **Model**: Trained using Scikit-learn and saved as `emotion_model.pkl`.
- 🔹 **Label Encoder**: Encodes/decodes emotion labels — `label_encoder.pkl`.

## 🛠️ Tech Stack

- **Backend**: Flask 🔥
- **Frontend**: HTML 🌐
- **Machine Learning**: Scikit-learn 🤖
- **Languages**: Python 🐍, HTML 🧾

## 📜 File Contents

1. `app.py` – Flask backend handling routes and predictions.
2. `index.html` – User interface for input and displaying results.
3. `emotion_model.pkl` – Trained emotion classification model.
4. `label_encoder.pkl` – Translates between encoded and readable emotion labels.
5. `combined_emotion.csv` – Dataset used to train the model.
6. `ML_Task2.ipynb` – Training notebook and EDA.

## 🚀 How to Run

1. **Clone this repository**:
   ```bash
   git clone https://github.com/yourusername/emotion-prediction-app.git
   cd emotion-prediction-app
   
2. **Create a virtual environment (optional)**:
   ```bash
   python -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate

3. **Install dependencies**:
   ```bash
   pip install flask scikit-learn pandas

4. **Make sure your folder structure looks like this**:
   ```plaintext
   emotion-prediction-app/
    ├── app.py
    ├── index.html
    ├── emotion_model.pkl
    ├── label_encoder.pkl
    ├── combined_emotion.csv
    └── ML_Task2.ipynb

5. **Run the Flask app**:
   ```bash
   python app.py

7. **Visit in your browser**:
   Navigate to http://127.0.0.1:5000 🌐

## 💡 Example Use
Input: "i know how you feel about being shy"
Output: Predicted Emotion: Fear

## 📸 Screenshots
![Screenshot 2025-04-04 191945](https://github.com/user-attachments/assets/c85a7fe4-9f37-419b-b7f5-e384524cccec)

## 🤝 Contributing
Contributions are welcome! 🛠️
If you'd like to improve the model, UI, or add new features, feel free to fork this repo and submit a pull request!

## 📬 Contact
For any questions or collaborations, feel free to reach out:
📧 Email: drbavaliya13@gmail.com

⭐ If you like this project, please star the repo and share it! ⭐
---

Let me know if you'd like a downloadable version (`README.md`) or if you want a zip package ready to push to GitHub 📦💻.







