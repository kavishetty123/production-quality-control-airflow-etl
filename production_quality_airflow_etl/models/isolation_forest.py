from sklearn.ensemble import IsolationForest

def build_isolation_forest(contamination=0.01, random_state=42):
    return IsolationForest(
        n_estimators=100,
        contamination=contamination,
        max_samples="auto",
        random_state=random_state
    )
