#Member 4 task with creating a folder and saving the payloads to a text file.

from pathlib import Path
from datetime import datetime

#Guide the file to the output folder and create a text file to save the payloads.
OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_FILE = OUTPUT_DIR / "payloads.txt" #The text output name is payloads, but you can change it if you want
DIVIDER = "=" * 60

#Create a folder
def ensure_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR

#Timestamp on output file
def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#Core functions where it save.
def save_payloads(base, encoded):
    ensure_output_dir()

    lines = [
        DIVIDER,
        f"Timestamp: {_timestamp()}",
        f"Base payload: {base}", ]
    
    for label, value in encoded.items():
        lines.append(f"  [{label}] {value}")
    lines.append("")
    entry = "\n".join(lines) + "\n"

    try:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        return OUTPUT_FILE


def get_output_path():
    return OUTPUT_FILE
