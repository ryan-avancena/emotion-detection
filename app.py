from flask import Flask, request, jsonify, render_template
from tensorflow import keras
import numpy as np
import joblib
import keras
from tensorflow.keras.preprocessing.sequence import pad_sequences
from helper import preprocess_input, preprocess

app = Flask(__name__)

nb_model = joblib.load('./emotion_detection_nb.joblib')
tf_idf = joblib.load('./tfidf.joblib')
rnn_model = keras.models.load_model('./emotion_classifier_model.keras')
tokenizer = joblib.load('./tokenizer.joblib')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.form.get('sentence')

    if not sentence:
        return render_template('predict.html')

    nb_features = tf_idf.transform([sentence])
    nb_prediction = nb_model.predict_proba(nb_features)[0]

    tokens = preprocess_input(sentence)  
    sequence = tokenizer.texts_to_sequences([tokens])  
    padded_sequence = pad_sequences(sequence, padding='post', maxlen=100)  
    rnn_prediction = rnn_model.predict(padded_sequence)[0]

    emotions = ['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']

    nb_results = {emotions[i]: round(float(nb_prediction[i]), 4) for i in range(len(emotions))}
    rnn_results = {emotions[i]: round(float(rnn_prediction[i]), 4) for i in range(len(emotions))}

    nb_label = max(nb_results, key=nb_results.get)
    rnn_label = max(rnn_results, key=rnn_results.get)

    return render_template('predict.html', 
                           sentence=sentence, 
                           nb_label=nb_label, 
                           rnn_label=rnn_label, 
                           emotions=emotions,
                           nb_values=list(nb_results.values()), 
                           rnn_values=list(rnn_results.values()))

if __name__ == '__main__':
    app.run(debug=True)
    