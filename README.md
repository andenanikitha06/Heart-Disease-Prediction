# Heart Disease Prediction Web App

This is a web-based application developed using Flask to predict heart disease based on user inputs. The model is a machine learning classifier trained to predict whether a person is likely to have heart disease or not. The application allows users to input health-related data, and it provides a prediction result indicating the likelihood of heart disease.

## Project Structure

The project consists of several folders and files:

### Heart_disease_flask/
│
├── static/                        # Static files (CSS, JS, images)
│   ├── Heart.jpg                  # Image for the webpage
│   ├── homepage.css              # Styles for the homepage
│   ├── homepage.js               # JavaScript for the homepage
│   ├── predict.css               # Styles for the predict page , predcition_results page 
│   └── script.js                 # JavaScript for the prediction page
│
├── templates/                     # HTML templates for rendering pages
│   ├── homepage.html             # Homepage layout
│   ├── index.html                # Main landing page
│   ├── predict.html              # Form to input data for prediction
│   └── prediction_result.html    # Page to display prediction results
│
├── app.py                         # Main Flask application
├── hdp_model.pkl                  # Trained machine learning model
├── model.py                       # Python script to load and use the trained model


## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/Heart_disease_flask.git
cd Heart_disease_flask

**### Step 2 : Setup Virtual Environment**

**### Install the necessary libraries using pip:**
pip install -r requirements.txt

**### Start the Flask server:**

python app.py

**Visit http://127.0.0.1:5000/ in your web browser to access the app.**

**USAGE**
Login Page (index.html): This is the main landing page where users can log in to access the app. It serves as the entry point to the application.
Home Page (homepage.html): After logging in, users are directed to the home page, where they can navigate to the prediction form or view other details about the app.
User Input Page (predict.html): Users fill out their health data, such as cholesterol levels, blood pressure, etc., to be used for heart disease prediction.
Prediction Result Page (prediction_result.html): After submitting the form, users are shown the prediction result indicating whether they are at risk of heart disease or not and with Some Suggestions .

**How It Works**
User Input: Users input their health data on the predict.html page. This page includes a form where users can enter their personal health details like age, cholesterol level, blood pressure, etc.

Model Loading and Prediction: When the user submits the form, the app loads the pre-trained machine learning model (hdp_model.pkl) using the model.py script. The model performs a prediction based on the user-provided data.

Displaying Results: After the model makes a prediction, the result is displayed on the prediction_result.html page. The page shows whether the user is at risk for heart disease or not, based on the model's output.


