import pandas as pd

DATA_DIR = "/opt/airflow/data"

def extract_data():
    X = pd.read_csv(f"{DATA_DIR}/data_X_sample.csv")
    Y = pd.read_csv(f"{DATA_DIR}/data_Y_sample.csv")

    X.to_csv("/tmp/X_raw.csv", index=False)
    Y.to_csv("/tmp/Y_raw.csv", index=False)
    print("Extraction complete: X_raw.csv and Y_raw.csv created.")
