```python
import os
import sqlite3
from fastapi import FastAPI, HTTPException

# Define constant for environment variable names
DATABASE_URL = "DATABASE_URL"

# Check necessary environment variables at startup
def check_environment_variables():
    if DATABASE_URL not in os.environ:
        raise ValueError(f"Missing required environment variable: {DATABASE_URL}")

# Call the check function when the module/module is imported
check_environment_variables()

app = FastAPI()

# Database setup
def get_database_connection():
    """Creates and returns a new SQLite connection."""
    try:
        conn = sqlite3.connect(os.environ[DATABASE_URL])  # Retrieve the database URL from environment variables
        return conn
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection failed: {str(e)}")

# Below would be the rest of your CRUD operations and FastAPI route definitions
# ...
```