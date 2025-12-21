import os
import sys
import platform
import pandas as pd

from etl.ai_jsl_engine import prompt_to_jsl
from etl.jmp_connector import run_jsl_script



DATA_PATH = os.path.join("data", "anomaly_results.csv")
OUTPUT_JSL_PATH = os.path.join("etl", "plot.jsl")



def load_column_names(csv_path: str) -> list[str]:
    """Load column names from anomaly_results.csv"""
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Required file not found: {csv_path}")

    df = pd.read_csv(csv_path, nrows=1)
    return list(df.columns)



def main():
    print("\n=== Anomaly Visualization (JMP) ===\n")

    # 1 Load column names
    try:
        columns = load_column_names(DATA_PATH)
    except Exception as e:
        print(f"Error loading data: {e}")
        sys.exit(1)

    # 2️ Ask user what they want to visualize
    user_prompt = input(
        "What would you like to visualize?\n"
        "(example: Plot T_data_1_1 over time and highlight anomalies)\n\n> "
    ).strip()

    if not user_prompt:
        print("No input provided. Exiting.")
        sys.exit(0)

    # 3️ Generate JSL using OpenAI
    print("\nGenerating JSL using OpenAI...\n")

    jsl_code = prompt_to_jsl(
        prompt=user_prompt,
        data_path=DATA_PATH,
        column_names=columns,
    )

    if not jsl_code or jsl_code.strip() == "":
        print("OpenAI returned empty JSL. Aborting.")
        sys.exit(1)

    # 4️ Write JSL to file
    os.makedirs(os.path.dirname(OUTPUT_JSL_PATH), exist_ok=True)

    with open(OUTPUT_JSL_PATH, "w", encoding="utf-8") as f:
        f.write(jsl_code)

    print(f"JSL script generated at: {OUTPUT_JSL_PATH}\n")

    # 5️ Attempt to run JMP (Windows only)
    if platform.system() == "Windows":
        print("Launching JMP...\n")
        run_jsl_script(os.path.abspath(OUTPUT_JSL_PATH))
    else:
        print(
            "Not running on Windows.\n"
            "Please open the following file manually in JMP:\n"
            f"  {os.path.abspath(OUTPUT_JSL_PATH)}\n"
        )



if __name__ == "__main__":
    main()
