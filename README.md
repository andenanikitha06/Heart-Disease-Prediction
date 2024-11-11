# Heart Disease Prediction Web App

This repository contains the code for a web application built using Flask that predicts whether a person is at risk for heart disease based on user-provided health data. The app uses a pre-trained machine learning model to make predictions and displays the results to the user.

## Project Structure

1. **`index.html`** - The main landing page where users can log in to access the app.
2. **`homepage.html`** - The home page shown to users after logging in, featuring a navigation menu and links to other sections.
3. **`predict.html`** - The user input page where users can enter their health data (age, cholesterol levels, blood pressure, etc.) for prediction.
4. **`prediction_result.html`** - The results page displaying the heart disease prediction based on the user’s inputs.
5. **`homepage.css`** - Styles for the homepage layout.
6. **`predict.css`** - Styles for the user input page (prediction form).
7. **`script.js`** - JavaScript for handling the form submission and making AJAX requests.
8. **`app.py`** - Main Flask application file to handle routing and machine learning model prediction.
9. **`model.py`** - Python script for loading and using the pre-trained machine learning model (`hdp_model.pkl`).
10. **`hdp_model.pkl`** - The trained machine learning model file used for heart disease prediction.
11. **`README.md`** - Project documentation.

## Features

- **User Authentication:** Users can log in and access the prediction page. The app uses a simple login mechanism (though this can be expanded in the future).
- **Heart Disease Prediction:** Users input their health data, and the app uses a trained machine learning model to predict whether they are at risk for heart disease.
- **Results Display:** The prediction result is displayed on a separate page with the recommendation of either being at risk or not at risk for heart disease.
- **Responsive Design:** The website is designed to be responsive, ensuring accessibility on various devices.

## How to Run

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/Heart_disease_flask.git
    cd Heart_disease_flask
    ```

2. **Set up a virtual environment (optional but recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the necessary dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask application:**
    ```bash
    python app.py
    ```

5. Open a web browser and visit `http://127.0.0.1:5000/` to use the app.

## Usage

### Home Page (`index.html`)

- **Login Page:** This is the main landing page where users can log in to access the application. Once logged in, users are redirected to the homepage.

### Homepage (`homepage.html`)

- **Navigation:** The homepage contains links to the prediction page where users can input their health data.
- **Prediction Link:** Clicking on the link will take users to the input form (`predict.html`).

### User Input Page (`predict.html`)

- **Health Data Input:** Users enter details such as age, cholesterol levels, blood pressure, and other health parameters to predict the likelihood of heart disease.
- **Submit:** Upon submitting the form, the app will process the input data and predict the likelihood of heart disease.

### Prediction Result Page (`prediction_result.html`)

- **Prediction Result:** After the user submits the form, the results page will display whether the user is at risk for heart disease or not based on the machine learning model’s prediction.

---

## How It Works

1. **User Input:** Users input their health data on the `predict.html` page. This page includes a form where users can enter their personal health details, such as cholesterol level, blood pressure, etc.

2. **Model Loading and Prediction:** When the user submits the form, the app loads the pre-trained machine learning model (`hdp_model.pkl`) using the `model.py` script. The model processes the data and performs a prediction.

3. **Displaying Results:** After the model makes a prediction, the result is shown on the `prediction_result.html` page, indicating whether the user is at risk for heart disease (1) or not (0) and some suggestions.

---



