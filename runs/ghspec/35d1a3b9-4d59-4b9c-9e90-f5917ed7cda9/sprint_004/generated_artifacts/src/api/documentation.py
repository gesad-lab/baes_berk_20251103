```python
# src/api/documentation.py

"""
Documentation for the API endpoints related to student course enrollment.
This module will detail the operations provided by the API.
"""

# Required packages for the application
DEPENDENCIES = [
    "fastapi",    # Framework for building the API
    "uvicorn",    # ASGI server for running the FastAPI application
    "sqlalchemy",  # ORM for easier database interaction
    "alembic",     # Migration tool for managing DB schema changes
    "pytest"       # Testing framework for unit and integration testing
]

def print_dependencies():
    """
    Print the required dependencies for the application.
    This function lists out the packages that need to be present in the requirements.txt.
    """
    print("Required dependencies for the project:")
    for dependency in DEPENDENCIES:
        print(f"- {dependency}")

if __name__ == "__main__":
    print_dependencies()
```