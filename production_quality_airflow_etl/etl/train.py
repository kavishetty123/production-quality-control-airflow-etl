import pandas as pd
import joblib
from models.isolation_forest import build_isolation_forest

def train_model(transformed_path, contamination=0.01):
    X = pd.read_csv(transformed_path)

    model = build_isolation_forest(contamination=contamination)
    model.fit(X)

    model_path = "/tmp/isolation_forest.pkl"
    joblib.dump(model, model_path)

    return model_path
