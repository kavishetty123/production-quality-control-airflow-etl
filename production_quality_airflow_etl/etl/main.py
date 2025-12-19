from etl.extract import extract_data
from etl.transform import transform_data
from etl.feature_engineering import feature_engineering
from etl.scale_and_save import scale_and_save

def run_etl():
    extract_data()
    transform_data()
    feature_engineering()
    scale_and_save()
    print("ETL pipeline finished successfully.")

if __name__ == "__main__":
    run_etl()
