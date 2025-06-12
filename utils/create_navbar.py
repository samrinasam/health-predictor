import streamlit as st

def create_navbar():
    st.markdown("""
        <style>
            .navbar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                flex-wrap: wrap;
                padding: 1rem 0;
                font-family: 'Inter', sans-serif;
            }

            .navbar-links {
                display: flex;
                gap: 1.5rem;
            }

            .navbar-left {
                font-size: 1.2rem;
                font-weight: bold;
            }

            .nav-button button {
                background: none !important;
                border: none !important;
                color: inherit !important;
                font-weight: 600 !important;
                font-size: 1rem !important;
                cursor: pointer;
                padding: 0.5rem 1rem !important;
                text-align: left;
            }

            .nav-button button:hover {
                text-decoration: underline;
            }

            @media screen and (max-width: 768px) {
                .navbar {
                    flex-direction: column;
                    align-items: flex-start;
                }

                .navbar-links {
                    flex-direction: column;
                    width: 100%;
                    margin-top: 1rem;
                }

                .nav-button button {
                    width: 100%;
                    padding: 1rem 0 !important;
                }
            }
        </style>
    """, unsafe_allow_html=True)

    # Navbar content
    st.markdown('<div class="navbar">', unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])

    with col1:
        st.markdown('<div class="navbar-left">🩺 Health Predictor</div>', unsafe_allow_html=True)

    with col2:
        with st.container():
            if st.button("Home", key="nav_home"):
                st.switch_page("Home.py")

    with col3:
        with st.container():
            if st.button("Predict", key="nav_predict"):
                st.switch_page("pages/Enter_Data.py")

    with col4:
        with st.container():
            if st.button("Records", key="nav_records"):
                st.switch_page("pages/View_Records.py")

    st.markdown('</div>', unsafe_allow_html=True)  # Close .navbar
