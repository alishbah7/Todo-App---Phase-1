# src/service.py
from typing import List, Optional
from src.models import Task
from src.storage import load_tasks, save_tasks

class TaskService:
    def __init__(self):
        self._tasks = load_tasks()
        self._next_id = max(self._tasks.keys(), default=0) + 1

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        task = Task(title=title, description=description)
        task.id = self._next_id
        self._tasks[task.id] = task
        self._next_id += 1

        save_tasks(self._tasks)   # ✅ CREATE
        return task

    def get_all_tasks(self) -> List[Task]:
        return list(self._tasks.values())  # ❌ no save here

    def mark_task_complete(self, task_id: int) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task:
            task.completed = True
            save_tasks(self._tasks)  # ✅ UPDATE
        return task

    def update_task(
        self,
        task_id: int,
        title: Optional[str] = None,
        description: Optional[str] = None
    ) -> Optional[Task]:
        task = self._tasks.get(task_id)
        if task:
            if title is not None:
                task.title = title
            if description is not None:
                task.description = description
            save_tasks(self._tasks)  # ✅ UPDATE
        return task

    def delete_task(self, task_id: int) -> bool:
        if task_id in self._tasks:
            del self._tasks[task_id]
            save_tasks(self._tasks)  # ✅ DELETE
            return True
        return False
