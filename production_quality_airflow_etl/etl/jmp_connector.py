# etl/jmp_connector.py
import subprocess
import os

JMP_PATH = r"C:\Program Files\JMP\JMPSTUDENT\19\jmp.exe"

def run_jsl_script(jsl_path: str):
    if not os.path.exists(JMP_PATH):
        raise FileNotFoundError(f"JMP not found at {JMP_PATH}")

    if not os.path.exists(jsl_path):
        raise FileNotFoundError(f"JSL file not found: {jsl_path}")

    subprocess.Popen([JMP_PATH, jsl_path])  
    print("JSL script sent to JMP")
