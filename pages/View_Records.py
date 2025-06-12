import streamlit as st
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.page_config import setup_page
from utils.create_navbar import create_navbar

setup_page()

create_navbar()
st.title("🧾 User Data Management")
st.title("🧾 Stored Diabetes Predictions")
st.caption("Click on a user card to view full details and prediction outcome.")

# ----------------- MongoDB Connection -------------------
client = MongoClient(st.secrets["mongodb"]["uri"])
db = client["diabetes_prediction"]
collection = db["predictions"]

# ----------------- Fetch Records -------------------
records = list(collection.find())
if not records:
    st.warning("No records found.")
    st.stop()

# Convert `_id` to string for UI operations
for rec in records:
    rec["id"] = str(rec["_id"])
    del rec["_id"]

# ----------------- Search -------------------
search = st.text_input("🔍 Search by Name or Contact Number")
if search:
    records = [
        rec for rec in records
        if search.lower() in rec["Name"].lower()
        or search in rec["Contact"]
    ]

if not records:
    st.warning("No matching records found.")
    st.stop()

# ----------------- Display Cards -------------------
for rec in records:
    with st.container():
        with st.expander(f"👤 {rec['Name']} | 📞 {rec['Contact']}"):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"**🏠 Address:** {rec['Address']}")
                st.markdown(f"**🧪 Prediction:** {rec['Prediction']}")

            with col2:
                if st.button(f"🗑️ Delete {rec['Name']}", key=rec["id"]):
                    collection.delete_one({"_id": ObjectId(rec["id"])})
                    st.success("User deleted successfully.")
                    st.rerun()

            # Show medical inputs as a collapsible section alternative (use checkbox)
            show_inputs = st.checkbox("🔍 View Medical Inputs", key=f"med_{rec['id']}")
            if show_inputs:
                st.markdown("**Medical Inputs:**")
                medical_data = {
                    k: v for k, v in rec.items()
                    if k not in ["id", "Name", "Contact", "Address", "Prediction"]
                }
                for key, val in medical_data.items():
                    st.markdown(f"- **{key}:** {val}")
