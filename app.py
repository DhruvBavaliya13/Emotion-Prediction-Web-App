from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load the saved model and label encoder
with open("D:\Desktop\Work\IPYNB\Projects\emotion_model.pkl", 'rb') as f:
    model = pickle.load(f)

with open("D:\Desktop\Work\IPYNB\Projects\label_encoder.pkl", 'rb') as f:
    label_encoder = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']
    prediction = model.predict([text])  # Predict emotion
    emotion = label_encoder.inverse_transform(prediction)[0]  # Convert number to label

    return render_template("index.html", prediction=emotion, text=text)

if __name__ == '__main__':
    app.run(debug=True)
