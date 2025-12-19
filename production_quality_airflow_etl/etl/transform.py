import pandas as pd
import numpy as np

def cap_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[column] = np.clip(df[column], lower, upper)
    return df

def transform_data():
    X = pd.read_csv("/tmp/X_raw.csv")
    Y = pd.read_csv("/tmp/Y_raw.csv")

    X["date_time"] = pd.to_datetime(X["date_time"])
    Y["date_time"] = pd.to_datetime(Y["date_time"])

    numeric_cols = X.select_dtypes(include=["int64", "float64"]).columns
    X = X.dropna()
    for col in numeric_cols:
        if X[col].nunique() > 10:
            X = cap_outliers(X, col)

    X["hour"] = X["date_time"].dt.floor("H")
    X_hourly = X.groupby("hour")[numeric_cols].mean().reset_index()
    X_hourly = X_hourly.rename(columns={"hour": "date_time"})

    Y["hour"] = Y["date_time"].dt.floor("H")
    Y_hourly = Y.drop_duplicates("hour")
    Y_hourly["date_time"] = Y_hourly["hour"]
    Y_hourly = Y_hourly[["date_time", "quality"]]

    merged = pd.merge(X_hourly, Y_hourly, on="date_time", how="inner")
    merged.to_csv("/tmp/merged.csv", index=False)
    print("Transformation complete: merged.csv created.")
