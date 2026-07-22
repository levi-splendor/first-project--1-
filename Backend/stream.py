import streamlit as st
import requests

if st.button("Predict"):
    response = requests.get("http://127.0.0.1:8000/predict")
    st.write(response.json())