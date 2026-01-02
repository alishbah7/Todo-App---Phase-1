# Quickstart: CLI Todo Application

**Date**: 2026-01-01
**Feature**: [CLI Todo Application](../spec.md)

This guide provides instructions to set up the development environment and run the application.

## Prerequisites

-   Python 3.13+
-   `uv` installed (`pip install uv`)

## 1. Environment Setup

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

## 2. Install Dependencies

Install the required Python packages using the `requirements.txt` file (which will be created during implementation).

```bash
uv pip install -r requirements.txt
```

## 3. Run the Application

The application is run from the command line via its main entry point. All commands follow the patterns defined in the `contracts/cli.md` document.

```bash
# Example: Add a new task
python src/main.py add "Buy groceries" --description "Milk, eggs, and bread"

# Example: View all tasks
python src/main.py view

# Example: Mark a task as complete
python src/main.py complete 1
```

## 4. Run Tests

To ensure the application is working correctly, run the test suite using `pytest`.

```bash
pytest
```
