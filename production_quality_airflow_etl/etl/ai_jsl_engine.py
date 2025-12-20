# etl/ai_jsl_engine.py
import os
import re
from openai import OpenAI

client = OpenAI()

def _sanitize_jsl(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    return text.strip()

def prompt_to_jsl(prompt, csv_path, columns):
    csv_path = os.path.abspath(csv_path).replace("\\", "/")

    system_prompt = f"""
You are a JMP JSL expert.
Write ONLY valid JSL.
Dataset path: {csv_path}
Available columns: {', '.join(columns)}
Always include:
dt = Open("{csv_path}");
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return _sanitize_jsl(response.choices[0].message.content)
