import pandas as pd
import joblib

def detect_anomalies(transformed_path, model_path):
    X = pd.read_csv(transformed_path)
    model = joblib.load(model_path)

    X["anomaly"] = model.predict(X)

    output_path = "/tmp/anomaly_results.csv"
    X.to_csv(output_path, index=False)

    print("Anomalies detected:", (X["anomaly"] == -1).sum())
    return output_path
