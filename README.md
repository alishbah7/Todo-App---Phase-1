# Quickstart: CLI Todo Application

**Date**: 2026-01-01
**Feature**: [CLI Todo Application](../spec.md)

This guide provides instructions to set up the development environment and run the application.

## Prerequisites

-   Python 3.13+
-   `uv` installed (`pip install uv`)

## 2. Environment Setup

First, create and activate a virtual environment using `uv`.

```bash
# Create the virtual environment in a .venv directory
uv venv

# Activate the virtual environment
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
```

## 2. Usage

The application is run from the command line via its main entry point: `python src/main.py`.

Ensure your virtual environment is activated before running any commands:
```bash
# On Windows (PowerShell):
.venv\Scripts\Activate.ps1
# On macOS/Linux:
source .venv/bin/activate
```

Here's how to use the available commands:

### Add a new task

Use the `add` command to create a new task.

```bash
python src/main.py add <TITLE> [--description <DESCRIPTION>]
```

-   `<TITLE>`: The title of the task (required). If it contains spaces, enclose it in quotes.
-   `--description <DESCRIPTION>`: An optional longer description for the task. If it contains spaces, enclose it in quotes.

**Examples:**
```bash
python src/main.py add "Buy groceries"
python src/main.py add "Write report" --description "Draft quarterly financial summary"
```

### View all tasks

Use the `view` command to display all tasks in your list.

```bash
python src/main.py view
```

**Example:**
```bash
python src/main.py view
```
*(Output will show task IDs, titles, descriptions, and completion status.)*

### Mark a task as complete

Use the `complete` command to mark an existing task as finished.

```bash
python src/main.py complete <TASK_ID>
```

-   `<TASK_ID>`: The ID of the task to mark as complete (required). Get this ID from the `view` command.

**Example:**
```bash
python src/main.py complete 1
```

### Update an existing task

Use the `update` command to change the title or description of a task. You must provide at least one of `--title` or `--description`.

```bash
python src/main.py update <TASK_ID> [--title <NEW_TITLE>] [--description <NEW_DESCRIPTION>]
```

-   `<TASK_ID>`: The ID of the task to update (required).
-   `--title <NEW_TITLE>`: An optional new title for the task.
-   `--description <NEW_DESCRIPTION>`: An optional new description for the task.

**Examples:**
```bash
# Update task 1's title
python src/main.py update 1 --title "Finish Project Proposal"

# Update task 2's description
python src/main.py update 2 --description "Review all sections before submission"

# Update both title and description for task 3
python src/main.py update 3 --title "Team Meeting" --description "Discuss sprint progress and blockers"
```

### Delete a task

Use the `delete` command to remove a task from your list.

```bash
python src/main.py delete <TASK_ID>
```

-   `<TASK_ID>`: The ID of the task to delete (required).

**Example:**
```bash
python src/main.py delete 1
```
