import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Health Predictor",
        page_icon="🩺",
        layout="centered",
    )
    # Hide sidebar
    st.markdown("""
        <style>
            [data-testid="stSidebar"] { display: none; }
            [data-testid="collapsedControl"] { display: none; }
        </style>
    """, unsafe_allow_html=True)
