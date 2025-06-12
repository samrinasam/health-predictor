import streamlit as st
from utils.page_config import setup_page
from utils.create_navbar import create_navbar
from utils.predict_utils import predict_diabetes, save_user_data, is_valid_contact

# ------------------- Setup -------------------
setup_page()
create_navbar()

st.title("🧪 Early-Stage Diabetes Prediction")
st.write("Enter your details to assess diabetes risk.")

# ------------------- User Inputs -------------------
name = st.text_input("Name")
contact = st.text_input("Contact Number")
address = st.text_input("Address")
age = st.number_input("Age", min_value=1, max_value=120, value=30)
gender = st.radio("Gender", ["Male", "Female"])
polyuria = st.radio("Polyuria (Frequent Urination)", ["Yes", "No"])
polydipsia = st.radio("Polydipsia (Excessive Thirst)", ["Yes", "No"])
sudden_weight_loss = st.radio("Sudden Weight Loss", ["Yes", "No"])
weakness = st.radio("Weakness", ["Yes", "No"])
polyphagia = st.radio("Polyphagia (Excessive Hunger)", ["Yes", "No"])
genital_thrush = st.radio("Genital Thrush", ["Yes", "No"])
visual_blurring = st.radio("Visual Blurring", ["Yes", "No"])
itching = st.radio("Itching", ["Yes", "No"])
irritability = st.radio("Irritability", ["Yes", "No"])
delayed_healing = st.radio("Delayed Healing", ["Yes", "No"])
partial_paresis = st.radio("Partial Paresis", ["Yes", "No"])
muscle_stiffness = st.radio("Muscle Stiffness", ["Yes", "No"])
alopecia = st.radio("Alopecia (Hair Loss)", ["Yes", "No"])
obesity = st.radio("Obesity", ["Yes", "No"])

# ------------------- Encode Input -------------------
input_data = [
    age,
    1 if gender == "Male" else 0,
    1 if polyuria == "Yes" else 0,
    1 if polydipsia == "Yes" else 0,
    1 if sudden_weight_loss == "Yes" else 0,
    1 if weakness == "Yes" else 0,
    1 if polyphagia == "Yes" else 0,
    1 if genital_thrush == "Yes" else 0,
    1 if visual_blurring == "Yes" else 0,
    1 if itching == "Yes" else 0,
    1 if irritability == "Yes" else 0,
    1 if delayed_healing == "Yes" else 0,
    1 if partial_paresis == "Yes" else 0,
    1 if muscle_stiffness == "Yes" else 0,
    1 if alopecia == "Yes" else 0,
    1 if obesity == "Yes" else 0,
]

# ------------------- Predict Button -------------------
if st.button("🔍 Predict Diabetes"):
    if not name.strip() or not contact.strip() or not address.strip():
        st.error("⚠️ Please fill in all required fields.")
    elif not is_valid_contact(contact):
        st.error("⚠️ Invalid contact number. Must be 10–15 digits.")
    else:
        prediction = predict_diabetes(input_data, name)
        st.subheader("Prediction:")
        st.success(prediction)

        save_user_data(name, contact, address, input_data, prediction)
        st.info("✅ Data saved to MongoDB successfully.")
