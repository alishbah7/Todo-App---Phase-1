# src/storage.py
import json
from pathlib import Path
from typing import Dict
from src.models import Task

DATA_FILE = Path("tasks.json")

def load_tasks() -> Dict[int, Task]:
    if not DATA_FILE.exists():
        return {}

    raw = json.loads(DATA_FILE.read_text())
    tasks: Dict[int, Task] = {}

    for k, v in raw.items():
        task = Task(
            title=v["title"],
            description=v.get("description"),
            completed=v.get("completed", False),
        )
        task.id = int(k)   # ✅ assign AFTER init
        tasks[task.id] = task

    return tasks


def save_tasks(tasks: Dict[int, Task]) -> None:
    DATA_FILE.write_text(
        json.dumps(
            {
                task_id: {
                    "title": task.title,
                    "description": task.description,
                    "completed": task.completed,
                }
                for task_id, task in tasks.items()
            },
            indent=2,
        )
    )
