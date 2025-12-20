import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

def train_model(transformed_path):
    X = pd.read_csv(transformed_path)

    model = IsolationForest(
        n_estimators=100,
        contamination=0.01,
        random_state=42
    )

    model.fit(X)

    model_path = "/tmp/isolation_forest.pkl"
    joblib.dump(model, model_path)

    return model_path
