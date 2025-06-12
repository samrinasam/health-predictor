import numpy as np
import joblib
import re
import streamlit as st
from pymongo import MongoClient

# Load model once
model = joblib.load("best_diabetes_model.pkl")

feature_names = [
    'Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden Weight Loss',
    'Weakness', 'Polyphagia', 'Genital Thrush', 'Visual Blurring',
    'Itching', 'Irritability', 'Delayed Healing', 'Partial Paresis',
    'Muscle Stiffness', 'Alopecia', 'Obesity'
]

def predict_diabetes(input_data, name):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)[0]

    return (
        f"{name} Patient Diagnosed with early-stage diabetes"
        if prediction == 1 else
        "Individual assessed as low-risk for diabetes"
    )

def save_user_data(name, contact, address, input_data, prediction_message):
    client = MongoClient(st.secrets["mongodb"]["uri"])
    db = client["diabetes_prediction"]
    collection = db["predictions"]

    readable_data = []
    for i, val in enumerate(input_data):
        if feature_names[i] == 'Age':
            readable_data.append(val)
        elif feature_names[i] == 'Gender':
            readable_data.append("Male" if val == 1 else "Female")
        else:
            readable_data.append("Yes" if val == 1 else "No")

    user_record = {
        "Name": name,
        "Contact": contact,
        "Address": address,
        "Prediction": prediction_message
    }

    for i, feature in enumerate(feature_names):
        user_record[feature] = readable_data[i]

    collection.insert_one(user_record)

def is_valid_contact(contact):
    return re.fullmatch(r"^\d{10,15}$", contact) is not None
