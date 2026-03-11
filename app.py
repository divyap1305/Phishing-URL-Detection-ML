import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("phishing_model.pkl")

st.title("Phishing URL Detection")

st.write("Enter website features to check if URL is phishing")

# Example input fields
url_length = st.number_input("URL Length")
having_ip = st.number_input("Having IP Address (1 or -1)")
prefix_suffix = st.number_input("Prefix/Suffix (-1 or 1)")
having_subdomain = st.number_input("Having Subdomain (-1 or 1)")

if st.button("Predict"):
    
    features = np.array([[url_length, having_ip, prefix_suffix, having_subdomain]])
    
    prediction = model.predict(features)
    
    if prediction == -1:
        st.error("⚠ Phishing Website")
    else:
        st.success("✅ Legitimate Website")