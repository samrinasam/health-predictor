import streamlit as st
from datetime import datetime

def show_footer():
    current_year = datetime.now().year
    st.markdown("---")

    st.markdown(f"""
        <div style="text-align: center; font-size: 0.9rem; color: #6c757d; padding: 1rem 0; font-family: 'Inter', sans-serif;">
            <p><strong>🩺 Health Predictor</strong> – Empowering early-stage diabetes detection with AI.</p>
            <p><strong>👤 CEO & Founder:</strong> <em>Samrina Nadeem</em></p>
            <p>📧 Contact: <a href="mailto:support@healthpredictor.ai" style="color: #6c757d;">support@healthpredictor.ai</a></p>
            <p>© {current_year} Health Predictor. All rights reserved.</p>
        </div>
    """, unsafe_allow_html=True)
