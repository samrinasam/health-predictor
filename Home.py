import streamlit as st
from streamlit_lottie import st_lottie
from utils.create_navbar import create_navbar
from utils.page_config import setup_page
from utils.lottie_loader import load_lottie_url
from utils.footer import show_footer

# ------------------- Config & Navbar -------------------
setup_page()
create_navbar()

# ------------------- Content -------------------
lottie_doctor = load_lottie_url("https://lottie.host/348e2357-d823-499e-9f82-962fd4bcadb7/aTZ0qGgaC8.json")

st.title("🏥 Health Predictor")
st.subheader("Early Stage Diabetes Risk Prediction")

st.write("""
Welcome to the **Health Predictor**, an AI-powered tool designed to predict early-stage diabetes using medical inputs.
With this application, hospitals and clinics can quickly assess risk levels and improve patient care.

---
""")

gif_path = "assets/doctor.gif"

try:
    st.image(gif_path, width=200)
except Exception as e:
    st.warning(f"⚠️ Doctor animation could not load: {e}")

st.markdown("---")

# CTA to enter data
st.markdown("### Ready to predict risk?")
if st.button("📝 Enter Patient Data"):
    try:
        st.switch_page("pages/Enter_Data.py")
    except Exception as e:
        st.error("⚠️ Could not navigate to Enter Data page. Make sure 'pages/Enter_Data.py' exists.")

# ------------------- Footer -------------------
show_footer()
