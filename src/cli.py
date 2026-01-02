import typer
from typing import Annotated
from typing import Optional

from src.app_core import app, console
from src.service import TaskService

# Function to get a single TaskService instance
_task_service_instance: Optional[TaskService] = None

def get_task_service_instance() -> TaskService:
    global _task_service_instance
    if _task_service_instance is None:
        _task_service_instance = TaskService()
    return _task_service_instance

task_service = get_task_service_instance()

@app.command()
def add(
    title: Annotated[str, typer.Argument(help="The title of the task.")],
    description: Annotated[
        Optional[str],
        typer.Option(help="A longer description for the task."),
    ] = None,
):
    """
    Adds a new task to the list.
    """
    task = task_service.add_task(title, description)
    console.print(f"✅ Task '{task.title}' added.")

@app.command()
def view():
    """
    Displays all tasks in the list.
    """
    tasks = task_service.get_all_tasks()
    
    if not tasks:
        console.print("Your todo list is empty.")
        return

    for task in tasks:
        status_emoji = "✅" if task.completed else "📝"
        desc_str = f" - {task.description}" if task.description else ""
        console.print(f"{status_emoji} {task.id}: {task.title}{desc_str}")

@app.command()
def complete(
    task_id: Annotated[int, typer.Argument(help="The ID of the task to mark as complete.")],
):
    """
    Marks an existing task as complete.
    """
    task = task_service.mark_task_complete(task_id)
    if task:
        console.print(f"✅ Task {task.id} marked as complete.")
    else:
        console.print(f"❌ Error: Task with ID {task_id} not found.", style="bold red")
        raise typer.Exit(code=1) # Exit with error code 1 for not found

@app.command()
def update(
    task_id: Annotated[int, typer.Argument(help="The ID of the task to update.")],
    title: Annotated[
        Optional[str],
        typer.Option(help="New title for the task."),
    ] = None,
    description: Annotated[
        Optional[str],
        typer.Option(help="New description for the task."),
    ] = None,
):
    """
    Updates an existing task's title or description.
    """
    if title is None and description is None:
        console.print("❌ Error: At least one of --title or --description must be provided for update.", style="bold red")
        raise typer.Exit(code=1)

    task = task_service.update_task(task_id, title, description)
    if task:
        console.print(f"✅ Task {task.id} updated.")
    else:
        console.print(f"❌ Error: Task with ID {task_id} not found.", style="bold red")
        raise typer.Exit(code=1)

@app.command()
def delete(
    task_id: Annotated[int, typer.Argument(help="The ID of the task to delete.")],
):
    """
    Deletes an existing task.
    """
    if task_service.delete_task(task_id):
        console.print(f"✅ Task {task_id} deleted.")
    else:
        console.print(f"❌ Error: Task with ID {task_id} not found.", style="bold red")
        raise typer.Exit(code=1)