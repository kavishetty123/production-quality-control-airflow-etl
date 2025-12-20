import pandas as pd
import joblib
import os

INPUT_DIR = "etl"
MODEL_DIR = "models"
OUTPUT_DIR = "etl"

# Load data and model
X = pd.read_csv(f"{INPUT_DIR}/transformed_data.csv")
features = X.drop(columns=["date_time"])
model = joblib.load(f"{MODEL_DIR}/isolation_forest.pkl")

# Predict anomalies
X["anomaly"] = model.predict(features)

# Save results
X.to_csv(f"{OUTPUT_DIR}/anomaly_results.csv", index=False)
print("Anomaly detection complete. Results saved to etl/anomaly_results.csv")
