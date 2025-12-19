import pandas as pd
import numpy as np

def feature_engineering():
    df = pd.read_csv("/tmp/merged.csv")
    df["date_time"] = pd.to_datetime(df["date_time"])

    df["hour"] = df["date_time"].dt.hour
    df["dayofweek"] = df["date_time"].dt.dayofweek

    df["hour_sin"] = np.sin(2 * np.pi * df["hour"] / 24)
    df["hour_cos"] = np.cos(2 * np.pi * df["hour"] / 24)
    df["dow_sin"] = np.sin(2 * np.pi * df["dayofweek"] / 7)
    df["dow_cos"] = np.cos(2 * np.pi * df["dayofweek"] / 7)

    df = df.drop(columns=["hour", "dayofweek"])
    df.to_csv("/tmp/features.csv", index=False)
    print("Feature engineering complete: features.csv created.")
