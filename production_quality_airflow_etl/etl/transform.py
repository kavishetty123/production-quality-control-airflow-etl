import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

def transform_data(X_path, Y_path):
    X = pd.read_csv(X_path, parse_dates=["date_time"])
    Y = pd.read_csv(Y_path, parse_dates=["date_time"])

    # Resample X to hourly
    X_hourly = (
        X.set_index("date_time")
         .resample("H")
         .mean()
         .reset_index()
    )

    data = pd.merge(X_hourly, Y, on="date_time", how="inner")

    features = data.drop(columns=["date_time", "quality"])

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    joblib.dump(scaler, "/tmp/scaler.pkl")

    transformed_path = "/tmp/transformed_data.csv"
    pd.DataFrame(
        X_scaled,
        columns=features.columns
    ).to_csv(transformed_path, index=False)

    return transformed_path
