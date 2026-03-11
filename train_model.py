import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv("phishing.csv")

# Select 4 useful features from dataset
X = data[[
    "URLURL_Length",
    "having_IPhaving_IP_Address",
    "Prefix_Suffix",
    "having_Sub_Domain"
]]

# Target column
y = data["Result"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# Save model
joblib.dump(model, "phishing_model.pkl")

print("✅ Model trained and saved successfully")