```python
import os
import sqlite3
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from contextlib import closing

# Initialize FastAPI application
app = FastAPI()

# Database file path
DATABASE_FILE = "student_management.db"

def create_database():
    """Create SQLite database and required tables if they don't exist."""
    try:
        with closing(sqlite3.connect(DATABASE_FILE)) as connection:
            with closing(connection.cursor()) as cursor:
                # Create students table if it doesn't exist
                cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
                """)
                connection.commit()  # Commit the changes to the database
    except sqlite3.Error as e:
        # Raise an HTTP exception if there is a database error
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(e)}"
        )

# Call the create_database function on startup to ensure the database is ready
@app.on_event("startup")
def startup():
    create_database()
```