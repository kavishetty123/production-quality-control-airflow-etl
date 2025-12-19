import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

OUTPUT_DIR = "/opt/airflow/output"

def scale_and_save():
    df = pd.read_csv("/tmp/features.csv")
    y = df["quality"]
    X = df.drop(columns=["quality", "date_time"])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    output = pd.DataFrame(X_scaled, columns=X.columns)
    output["quality"] = y.values

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output.to_csv(f"{OUTPUT_DIR}/training_data_processed.csv", index=False)
    print(f"Scaling complete: {OUTPUT_DIR}/training_data_processed.csv created.")
