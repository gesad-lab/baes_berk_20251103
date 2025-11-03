```python
import sqlite3
from sqlite3 import Error

def initialize_database():
    """Initialize the SQLite database and create the students table."""
    try:
        # Connect to the SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()

        # Create the students table if it does not already exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        
        # Commit changes and close the connection
        conn.commit()
        cursor.close()
        conn.close()

        print("Database initialized and students table created.")
    except Error as e:
        # Log the error to help with debugging
        print(f"Error initializing database: {e}")
```
