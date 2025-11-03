import sqlite3
from sqlite3 import Connection, Cursor

DATABASE_NAME = "students.db"

def get_db_connection() -> Connection:
    """Create and return a new database connection."""
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row  # Allows access to columns by name
    return connection

def initialize_database() -> None:
    """Create the SQLite database and the students table if it does not exist."""
    connection = get_db_connection()
    cursor = connection.cursor()
    
    try:
        # Create the students table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        connection.commit()  # Commit the changes
    except sqlite3.Error as e:
        # Log the error message with context for debugging
        print(f"Database error: {e}")  # TODO: Replace with proper logging
    finally:
        cursor.close()
        connection.close()  # Ensure the connection is closed

# Initialize the database when this module is imported
initialize_database()