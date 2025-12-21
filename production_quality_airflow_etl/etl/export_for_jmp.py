# etl/export_for_jmp.py
import pandas as pd
import os

INPUT_PATH = "production_quality_airflow_etl/etl/anomaly_results.csv"
OUTPUT_PATH = "production_quality_airflow_etl/etl/jmp_ready.csv"

def export_for_jmp():
    df = pd.read_csv(INPUT_PATH)

    # Human-readable label
    df["anomaly_label"] = df["anomaly"].map({
        1: "Normal",
        -1: "Anomaly"
    })

    df.to_csv(OUTPUT_PATH, index=False)
    print(f"JMP-ready file created at: {OUTPUT_PATH}")

if __name__ == "__main__":
    export_for_jmp()
