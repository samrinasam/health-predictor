
### File: utils/db.py
from pymongo import MongoClient
import streamlit as st

def get_db_collection():
    client = MongoClient(st.secrets["mongodb"]["uri"])
    db = client["diabetes_prediction"]
    return db["predictions"]

def insert_user_data(user_data):
    collection = get_db_collection()
    collection.insert_one(user_data)

def fetch_all_users():
    collection = get_db_collection()
    return list(collection.find())

def fetch_user_by_name(name):
    collection = get_db_collection()
    return collection.find_one({"Name": name})

def delete_users_by_ids(ids):
    collection = get_db_collection()
    for user_id in ids:
        collection.delete_one({"_id": user_id})