# Data Model: CLI Todo Application

**Date**: 2026-01-01
**Feature**: [CLI Todo Application](../spec.md)

This document defines the core data entities for the application. As the application stores data in-memory, this model translates directly to the Python data structures that will be used.

## Entity: Task

Represents a single todo item in the application.

### Fields

| Field | Type | Description | Constraints |
| :--- | :--- | :--- | :--- |
| `id` | Integer | A unique identifier for the task. | Required, Unique, System-Generated |
| `title` | String | A short, descriptive title for the task. | Required, Non-empty |
| `description`| String | An optional, more detailed description. | Optional |
| `completed` | Boolean | The completion status of the task. | Required, Defaults to `False` |

### State Transitions

A `Task` object has a simple lifecycle:

1.  **Creation**: A task is created with `completed` set to `False`.
2.  **Completion**: A task's `completed` status can be changed from `False` to `True`. This is a one-way transition.
3.  **Deletion**: A task can be removed from the system at any point.

### Example Object

A Python `dataclass` or a simple class will be used to represent a task.

```python
# Conceptual representation
class Task:
    id: int
    title: str
    description: str | None
    completed: bool = False
```
