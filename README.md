Production Quality ETL Pipeline

This repository contains a sample ETL pipeline built around production quality control data, demonstrating how raw sensor data can be structured into a clear Extract → Transform → Analyze → Visualize workflow. The project is designed to mimic the type of pipelines that can be orchestrated in Apache Airflow, while also integrating anomaly detection and visualization.

Project Overview

The main goal of this project is to refactor script-heavy workflows into a modular, production-ready ETL structure. The pipeline is broken into several stages:

Extract

Pulls in raw CSV files containing sensor data.

Standardizes the input for downstream processing.

Transform

Cleans and normalizes the data.

Prepares features for anomaly detection and visualization.

Analyze / Anomaly Detection

Applies an Isolation Forest model to detect abnormal data points.

Flags anomalies in the dataset and stores results in a structured CSV.

Visualize (JMP Integration)

Exports a JMP-compatible dataset (jmp_ready.csv) and generates JSL scripts.

Allows anomalies to be visualized alongside normal data for easier interpretation.

File Structure
production_quality_airflow_etl/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   ├── detect.py
│   ├── train.py
│   ├── generate_jsl.py
│   ├── ai_jsl_engine.py
│   └── jmp_connector.py
├── output/
│   ├── X_raw.csv
│   ├── transformed_data.csv
│   ├── anomaly_results.csv
│   └── jmp_ready.csv
├── README.md
└── requirements.txt

How to Run

Note: Some scripts assume a Windows environment for JMP integration.

Install dependencies:

pip install -r requirements.txt


Run ETL steps sequentially:

python etl/extract.py
python etl/transform.py
python etl/train.py
python etl/detect.py


Generate JMP scripts from natural language instructions:

python -m etl.generate_jsl


Open JMP and run generated .jsl scripts to visualize the results.

Notes

Large CSV files are tracked using Git LFS to avoid exceeding GitHub size limits.

The project is a proof-of-concept and is intended to demonstrate how existing scripts can be refactored into a pipeline suitable for orchestration in Airflow.

Feedback

Feel free to suggest improvements to the pipeline, ETL structure, or visualization techniques. Any tips are appreciated!
