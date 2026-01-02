import sys
import os

# Add the parent directory to sys.path to allow imports from src
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.app_core import app, console

# Import CLI commands to register them
# This is a bit of a workaround to avoid circular imports in a simple setup.
# In a larger application, you might use a different structure.
from src import cli # type: ignore 

if __name__ == "__main__":
    app()