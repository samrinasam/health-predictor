# utils/db.py
import streamlit as st
from pymongo import MongoClient, errors
from bson.objectid import ObjectId

def get_db_collection():
    try:
        client = MongoClient(st.secrets["mongodb"]["uri"], serverSelectionTimeoutMS=5000)
        client.server_info()  # Force a connection check
        db = client["diabetes_prediction"]
        return db["predictions"]
    except errors.ServerSelectionTimeoutError:
        st.error("❌ Unable to connect to MongoDB. Please check your internet connection or database URI.")
        st.stop()
    except errors.ConnectionFailure:
        st.error("❌ No internet connection. Please try again later.")
        st.stop()
    except Exception:
        st.error("❌ Unexpected error while connecting to MongoDB. Please check your internet connection.")
        st.stop()

def insert_user_data(user_data):
    try:
        with st.spinner("🔄 Saving data..."):
            collection = get_db_collection()
            collection.insert_one(user_data)
    except Exception:
        st.error("❌ Error saving data. Please check your internet or database connection.")

def fetch_all_users():
    try:
        with st.spinner("🔄 Fetching user records..."):
            collection = get_db_collection()
            return list(collection.find())
    except Exception:
        st.error("❌ Error fetching data. Please check your internet or database connection.")
        return []

def delete_user_by_id(object_id):
    try:
        with st.spinner("🔄 Deleting user..."):
            collection = get_db_collection()
            collection.delete_one({"_id": ObjectId(object_id)})
    except Exception:
        st.error("❌ Error deleting user. Please check your internet or database connection.")
