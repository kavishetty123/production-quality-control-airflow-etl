import pandas as pd


def extract_data():
    # Load the CSV files
    X = pd.read_csv(f"/workspaces/production-quality-control-airflow-etl/production_quality_airflow_etl/data/data_X.csv")
    Y = pd.read_csv(f"/workspaces/production-quality-control-airflow-etl/production_quality_airflow_etl/data/data_Y.csv")

    # Save raw copies
    X.to_csv("/tmp/X_raw.csv", index=False)
    Y.to_csv("/tmp/Y_raw.csv", index=False)

    # Print basic info for X
    print("X_raw.csv created.")
    print("Shape of X:", X.shape)
    print("Columns in X:", list(X.columns))
    print("First 5 rows of X:")
    print(X.head(), "\n")

    # Print basic info for Y
    print("Y_raw.csv created.")
    print("Shape of Y:", Y.shape)
    print("Columns in Y:", list(Y.columns))
    print("First 5 rows of Y:")
    print(Y.head(), "\n")

    print("Extraction complete.")
# ✅ Call the function
extract_data()
