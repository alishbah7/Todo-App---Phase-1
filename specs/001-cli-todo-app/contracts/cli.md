# CLI Contracts: Todo Application

**Date**: 2026-01-01
**Feature**: [CLI Todo Application](../spec.md)

This document defines the public command-line interface for the application, based on the functional requirements in the specification.

The application will be invoked via a main entry point, assumed here to be `todo`.

## Commands

### `add`

Adds a new task to the list.

-   **Usage**: `todo add <TITLE> [--description <TEXT>]`
-   **Arguments**:
    -   `TITLE` (String, Required): The title of the task.
-   **Options**:
    -   `--description <TEXT>` (String, Optional): A longer description for the task.
-   **Success Output**: "✅ Task '[TITLE]' added."
-   **Error Output**:
    -   If title is missing: "Error: Missing argument 'TITLE'."

---

### `view`

Displays all tasks in the list.

-   **Usage**: `todo view`
-   **Output Format**: A formatted table or list showing the ID, Title, Description, and Status of each task. A visual indicator (e.g., emoji) will be used for the status.
    -   Pending: 📝
    -   Complete: ✅
-   **Example**:
    ```
    📝 1: Buy milk
    ✅ 2: Walk the dog - Remember the new leash!
    ```
-   **Empty List Output**: "Your todo list is empty."

---

### `complete`

Marks an existing task as complete.

-   **Usage**: `todo complete <TASK_ID>`
-   **Arguments**:
    -   `TASK_ID` (Integer, Required): The ID of the task to mark as complete.
-   **Success Output**: "✅ Task [TASK_ID] marked as complete."
-   **Error Output**:
    -   If `TASK_ID` does not exist: "Error: Task with ID [TASK_ID] not found."

---

### `update`

Updates the title and/or description of an existing task.

-   **Usage**: `todo update <TASK_ID> [--title <TEXT>] [--description <TEXT>]`
-   **Arguments**:
    -   `TASK_ID` (Integer, Required): The ID of the task to update.
-   **Options**:
    -   `--title <TEXT>` (String, Optional): The new title for the task.
    -   `--description <TEXT>` (String, Optional): The new description for the task.
-   **Success Output**: "✅ Task [TASK_ID] updated."
-   **Error Output**:
    -   If `TASK_ID` does not exist: "Error: Task with ID [TASK_ID] not found."
    -   If neither `--title` nor `--description` is provided: "Error: At least one field (--title or --description) must be provided to update."

---

### `delete`

Deletes a task from the list.

-   **Usage**: `todo delete <TASK_ID>`
-   **Arguments**:
    -   `TASK_ID` (Integer, Required): The ID of the task to delete.
-   **Success Output**: "✅ Task [TASK_ID] deleted."
-   **Error Output**:
    -   If `TASK_ID` does not exist: "Error: Task with ID [TASK_ID] not found."
