import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

INPUT_DIR = "etl"    # read raw CSVs
OUTPUT_DIR = "etl"   # save transformed CSVs
os.makedirs(OUTPUT_DIR, exist_ok=True)

def transform_data():
    # Load raw data
    X = pd.read_csv(f"{INPUT_DIR}/X_raw.csv")

    # Select only feature columns (exclude date_time)
    features = X.drop(columns=["date_time"])

    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    # Convert back to DataFrame, keep column names
    X_scaled_df = pd.DataFrame(X_scaled, columns=features.columns)

    # Optionally add date_time back for reference
    X_scaled_df["date_time"] = X["date_time"]

    # Save transformed data inside repo
    X_scaled_df.to_csv(f"{OUTPUT_DIR}/transformed_data.csv", index=False)

    print(f"Transformation complete. File saved to {OUTPUT_DIR}/transformed_data.csv")

if __name__ == "__main__":
    transform_data()
