import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")

def load_tasks():
    if not DATA_FILE.exists():
        return []

    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_tasks(task):
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(task, f, indent=2)
