```python
import sqlite3
import os

# Define the database file path
DB_FILE = 'students.db'

def initialize_database():
    """Create the Student table in the SQLite database if it does not exist."""
    # Connect to the SQLite database
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    # Create the Student table with required fields
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

# Call the function to initialize the database when the module is loaded
if __name__ == "__main__":
    if not os.path.exists(DB_FILE):
        initialize_database()
```