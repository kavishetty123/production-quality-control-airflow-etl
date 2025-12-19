from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.main import run_etl

with DAG(
    dag_id="production_quality_etl",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={"retries": 2},
) as dag:

    etl_task = PythonOperator(
        task_id="run_full_etl",
        python_callable=run_etl
    )
.