# Phishing URL Detection using Machine Learning

## Overview

Phishing attacks are a common cybersecurity threat where malicious websites imitate legitimate ones to steal sensitive information such as passwords, banking credentials, and personal data.

This project uses **Machine Learning** to detect whether a website URL is **legitimate or phishing** by analyzing various URL features. The model is trained using a dataset obtained from Kaggle and predicts the nature of a website based on learned patterns.

The project also includes a **Streamlit web application** that allows users to interact with the model and test predictions in real time.

---

## Features

* Machine Learning based phishing website detection
* Random Forest classification model
* Real-time prediction through a web interface
* Easy-to-use Streamlit application
* Dataset sourced from Kaggle

---

## Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**
* **Joblib**

---

## Project Structure

```
Phishing-URL-Detection-ML
│
├── phishing.csv              # Dataset from Kaggle
├── train_model.py            # Script to train the ML model
├── app.py                    # Streamlit web application
├── phishing_model.pkl        # Saved trained model
├── requirements.txt          # Required Python libraries
└── README.md                 # Project documentation
```

---

## Dataset

The dataset used for this project is the **Phishing Website Dataset** obtained from Kaggle.

It contains multiple features extracted from URLs such as:

* URL length
* Presence of IP address
* Prefix/Suffix usage
* Subdomain information
* SSL certificate status
* Domain age

These features help the model learn patterns that differentiate **phishing websites from legitimate ones**.

---

## Machine Learning Model

The project uses a **Random Forest Classifier**, which is an ensemble learning method that combines multiple decision trees to improve prediction accuracy.

Steps involved in the ML pipeline:

1. Load the dataset
2. Preprocess and separate features and labels
3. Split the dataset into training and testing sets
4. Train the Random Forest model
5. Save the trained model for future predictions

---

## Installation

Clone the repository:

```bash
git clone https://github.com/divyap1305/Phishing-URL-Detection-ML.git
```

Navigate to the project folder:

```bash
cd Phishing-URL-Detection-ML
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Train the Model

Run the training script:

```bash
python train_model.py
```

This will generate the trained model file:

phishing_model.pkl

---

### Step 2: Run the Web Application

Start the Streamlit app:

streamlit run app.py

Open the provided **local URL** in your browser to access the phishing detection interface.

---

## Example Output

The application predicts whether a website is:

* **Legitimate Website**
* **Phishing Website**

based on the features provided by the user.

---

## Applications

* Cybersecurity threat detection
* Website safety analysis
* Educational demonstration of machine learning in security

---

## Future Improvements

* Automatic URL feature extraction from user input
* Integration with browser extensions
* Deep learning based phishing detection
* Larger and updated datasets

---

## Author

Developed by Divya Palanisamy.
