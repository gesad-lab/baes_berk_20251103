```python
import sqlite3
from sqlite3 import Error

def create_connection(db_file: str) -> sqlite3.Connection:
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def initialize_database(conn: sqlite3.Connection) -> None:
    """Initialize the database and create tables if they do not exist."""
    try:
        cursor = conn.cursor()
        # Create the students table
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''')
        conn.commit()
        print("Database initialized and tables created successfully.")
    except Error as e:
        print(f"Error initializing database: {e}")
    finally:
        if conn:
            conn.close()

# Example usage
if __name__ == "__main__":
    database_file = "students.db"  # Specify your desired database file
    connection = create_connection(database_file)
    if connection:
        initialize_database(connection)
```