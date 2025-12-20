import pandas as pd
import joblib

def detect_anomalies(transformed_path, model_path):
    X = pd.read_csv(transformed_path)
    model = joblib.load(model_path)

    X["anomaly"] = model.predict(X)

    output_path = "/tmp/anomaly_results.csv"
    X.to_csv(output_path, index=False)

    return output_path
