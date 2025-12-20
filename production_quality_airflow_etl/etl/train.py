import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

INPUT_DIR = "etl"
MODEL_DIR = "models"
os.makedirs(MODEL_DIR, exist_ok=True)

# Load transformed data
X = pd.read_csv(f"{INPUT_DIR}/transformed_data.csv")
features = X.drop(columns=["date_time"])

# Train Isolation Forest
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(features)

# Save the model
joblib.dump(model, f"{MODEL_DIR}/isolation_forest.pkl")
print("Isolation Forest trained and saved to models/isolation_forest.pkl")
