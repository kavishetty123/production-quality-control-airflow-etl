import pandas as pd
import os

# Paths
DATA_DIR = "data"          # folder with original CSVs
OUTPUT_DIR = "etl"         # save processed CSVs here

os.makedirs(OUTPUT_DIR, exist_ok=True)

def extract_data():
    # Load CSVs
    X = pd.read_csv(f"{DATA_DIR}/data_X.csv")
    Y = pd.read_csv(f"{DATA_DIR}/data_Y.csv")

    # Save raw copies inside repo
    X.to_csv(f"{OUTPUT_DIR}/X_raw.csv", index=False)
    Y.to_csv(f"{OUTPUT_DIR}/Y_raw.csv", index=False)

    print(f"Extraction complete. Files saved to {OUTPUT_DIR}/")

if __name__ == "__main__":
    extract_data()
