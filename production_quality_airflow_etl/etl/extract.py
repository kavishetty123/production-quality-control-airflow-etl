import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
TMP_DIR = "/tmp"

def extract_data():
    X = pd.read_csv(os.path.join(DATA_DIR, "data_X.csv"))
    Y = pd.read_csv(os.path.join(DATA_DIR, "data_Y.csv"))

    

    X_path = os.path.join(TMP_DIR, "X_raw.csv")
    Y_path = os.path.join(TMP_DIR, "Y_raw.csv")

    X.to_csv(X_path, index=False)
    Y.to_csv(Y_path, index=False)

    return X_path, Y_path


if __name__ == "__main__":
    extract_data()
