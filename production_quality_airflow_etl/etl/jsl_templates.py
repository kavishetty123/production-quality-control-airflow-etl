# etl/jsl_templates.py

def overlay_time_series_jsl(csv_path, sensor_col):
    return f'''
dt = Open("{csv_path}");

dt << Graph Builder(
    Variables(
        X( :date_time ),
        Y( :{sensor_col} ),
        Color( :anomaly_label )
    ),
    Elements( Points( X, Y, Legend( 1 ) ) )
);
'''
