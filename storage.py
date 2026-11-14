from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path(__file__).resolve().parent / "output"
OUTPUT_FILE = OUTPUT_DIR / "payloads.txt"
DIVIDER = "=" * 60


def ensure_output_dir():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    return OUTPUT_DIR


def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def save_payloads(base, encoded):
    ensure_output_dir()

    lines = [
        DIVIDER,
        f"Timestamp: {_timestamp()}",
        f"Base payload: {base}",
    ]
    for label, value in encoded.items():
        lines.append(f"  [{label}] {value}")
    lines.append("")
    entry = "\n".join(lines) + "\n"

    try:
        with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
            f.write(entry)
        return OUTPUT_FILE
    except OSError:
        return None


def get_output_path():
    return OUTPUT_FILE
