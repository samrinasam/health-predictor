import requests
import streamlit as st

def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except Exception as e:
        st.warning(f"⚠️ Failed to load animation: {e}")
        return None
