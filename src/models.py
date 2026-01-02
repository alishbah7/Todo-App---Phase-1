from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Task:
    """Represents a single task in the todo list."""
    title: str
    description: Optional[str] = None
    completed: bool = False
    id: int = field(default=0, init=False)