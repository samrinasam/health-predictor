# Home.py
import re
import joblib
import numpy as np
import streamlit as st
from utils.page_config import setup_page
from utils.create_navbar import create_navbar
from utils.db import insert_user_data

setup_page()
create_navbar()

st.title("🩺 Diabetes Risk Prediction")
st.caption("Fill out the form below to check early-stage diabetes risk.")

model = joblib.load("best_diabetes_model.pkl")
feature_names = [
    'Age', 'Gender', 'Polyuria', 'Polydipsia', 'Sudden Weight Loss',
    'Weakness', 'Polyphagia', 'Genital Thrush', 'Visual Blurring',
    'Itching', 'Irritability', 'Delayed Healing', 'Partial Paresis',
    'Muscle Stiffness', 'Alopecia', 'Obesity'
]

def is_valid_contact(contact):
    return re.fullmatch(r"^\d{10,15}$", contact)

with st.form("prediction_form"):
    name = st.text_input("👤 Name")
    contact = st.text_input("📞 Contact Number")
    address = st.text_input("🏠 Address")
    age = st.slider("🎂 Age", 1, 120, 25)
    gender = st.radio("🚻 Gender", ["Male", "Female"])

    yes_no_fields = feature_names[2:]  # Exclude Age & Gender
    yes_no_values = [st.selectbox(f"{field}?", ["Yes", "No"]) for field in yes_no_fields]

    submit = st.form_submit_button("🔍 Predict")

    if submit:
        if not name or not contact or not address:
            st.error("❗ Please fill in all fields.")
        elif not is_valid_contact(contact):
            st.error("❗ Invalid contact number format.")
        else:
            input_data = [age, 1 if gender == "Male" else 0] + [1 if val == "Yes" else 0 for val in yes_no_values]
            prediction = model.predict(np.array(input_data).reshape(1, -1))[0]
            prediction_msg = (
                f"{name} has been diagnosed with early-stage diabetes."
                if prediction == 1 else
                f"{name} is assessed as low-risk for diabetes."
            )

            readable_data = [age, gender] + yes_no_values
            user_record = {
                "Name": name,
                "Contact": contact,
                "Address": address,
                "Prediction": prediction_msg
            }
            for i, feat in enumerate(feature_names):
                user_record[feat] = readable_data[i]

            insert_user_data(user_record)
            st.success(prediction_msg)
