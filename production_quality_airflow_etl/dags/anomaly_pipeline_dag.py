from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract_data
from etl.transform import transform_data
from etl.train import train_model
from etl.detect import detect_anomalies

with DAG(
    dag_id="production_quality_anomaly_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_data,
        op_args=["/tmp/X_raw.csv", "/tmp/Y_raw.csv"]
    )

    train = PythonOperator(
        task_id="train",
        python_callable=train_model,
        op_args=["/tmp/transformed_data.csv"]
    )

    detect = PythonOperator(
        task_id="detect",
        python_callable=detect_anomalies,
        op_args=["/tmp/transformed_data.csv", "/tmp/isolation_forest.pkl"]
    )

    extract >> transform >> train >> detect
