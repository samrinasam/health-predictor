# pages/View_Records.py
import streamlit as st
from bson.objectid import ObjectId
from utils.page_config import setup_page
from utils.create_navbar import create_navbar
from utils.db import fetch_all_users, delete_user_by_id

setup_page()
create_navbar()

st.title("🧾 User Data Management")
st.caption("Click on a user card to view full details and prediction outcome.")

records = fetch_all_users()
if not records:
    st.warning("No records found.")
    st.stop()

# Prepare data
for rec in records:
    rec["id"] = str(rec["_id"])
    del rec["_id"]

# Search bar
search = st.text_input("🔍 Search by Name or Contact Number")
if search:
    records = [r for r in records if search.lower() in r["Name"].lower() or search in r["Contact"]]
    if not records:
        st.warning("No matching records found.")
        st.stop()

# Display cards
for rec in records:
    with st.container():
        with st.expander(f"👤 {rec['Name']} | 📞 {rec['Contact']}"):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"**🏠 Address:** {rec['Address']}")
                st.markdown(f"**🧪 Prediction:** {rec['Prediction']}")

            with col2:
                if st.button(f"🗑️ Delete {rec['Name']}", key=rec["id"]):
                    delete_user_by_id(ObjectId(rec["id"]))
                    st.success("User deleted successfully.")
                    st.rerun()

            show_inputs = st.checkbox("📋 View Medical Inputs", key=f"med_{rec['id']}")
            if show_inputs:
                st.markdown("**Medical Inputs:**")
                for k, v in rec.items():
                    if k not in ["id", "Name", "Contact", "Address", "Prediction"]:
                        st.markdown(f"- **{k}:** {v}")
