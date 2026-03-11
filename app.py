import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("phishing_model.pkl")

st.set_page_config(page_title="Phishing URL Detector", page_icon="🔐", layout="wide")

# Title
st.title("🔐 AI Phishing URL Detection System")
st.write("This tool uses **Machine Learning** to detect whether a website may be **phishing or legitimate**.")

st.divider()

# URL input
url = st.text_input("🌐 Enter Website URL")

# Feature extraction function
def extract_features(url):

    url_length = len(url)

    if any(char.isdigit() for char in url):
        having_ip = -1
    else:
        having_ip = 1

    if "-" in url:
        prefix_suffix = -1
    else:
        prefix_suffix = 1

    if url.count(".") > 2:
        having_subdomain = -1
    else:
        having_subdomain = 1

    return [url_length, having_ip, prefix_suffix, having_subdomain]


if st.button("🔍 Analyze URL"):

    if url == "":
        st.warning("⚠ Please enter a URL to analyze.")

    else:

        features = extract_features(url)
        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)
        probability = model.predict_proba(features)

        phishing_risk = probability[0][0] * 100
        safe_risk = probability[0][1] * 100

        st.divider()

        col1, col2 = st.columns(2)

        # Prediction result
        with col1:

            st.subheader("Prediction Result")

            if prediction == -1:
                st.error("⚠ This website is likely a PHISHING site.")
            else:
                st.success("✅ This website appears LEGITIMATE.")

        # Risk analysis
        with col2:

            st.subheader("Risk Analysis")

            st.progress(int(phishing_risk))

            st.write(f"Phishing Risk: **{phishing_risk:.2f}%**")
            st.write(f"Legitimate Probability: **{safe_risk:.2f}%**")

        st.divider()

        # Risk level indicator
        st.subheader("Risk Level")

        if phishing_risk < 30:
            st.success("🟢 Low Risk Website")

        elif phishing_risk < 70:
            st.warning("🟡 Medium Risk Website")

        else:
            st.error("🔴 High Risk Website")

        st.divider()

        # Safety tips
        st.subheader("🔐 Cybersecurity Tips")

        st.write("""
        - Always verify the **domain name** before entering credentials.
        - Avoid clicking suspicious links from emails or messages.
        - Check if the website uses **HTTPS**.
        - Never share personal or banking information on unknown websites.
        """)

st.divider()

# Footer
st.caption("Machine Learning Project | Phishing Website Detection using Random Forest")