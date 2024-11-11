from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

with open("hdp_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        cp = int(request.form['cp'])
        trestbps = int(request.form['trestbps'])
        chol = int(request.form['chol'])
        fbs = int(request.form['fbs'])
        restecg = int(request.form['restecg'])
        thalach = int(request.form['thalach'])
        exang = int(request.form['exang'])
        input_data = np.array([[cp, trestbps, chol, fbs, restecg, thalach, exang]])
        feature_names = ['cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang']
        
        input_data_df = pd.DataFrame(input_data, columns=feature_names)
        
        prediction = model.predict(input_data_df)
        probability_score = model.predict_proba(input_data_df)[:, 1] * 100  
        
        prediction_text = "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease Detected"
        prediction_flag = "Yes" if prediction[0] == 1 else "No"
        
        return render_template(
            'prediction_result.html',
            prediction=prediction_flag,
            prediction_text=prediction_text,
            probability_score=probability_score[0]
        )
    
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=True)
