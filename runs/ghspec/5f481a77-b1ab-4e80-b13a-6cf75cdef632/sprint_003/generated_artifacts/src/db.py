```python
import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def create_course_table(conn):
    """Create the Course table in the database if it doesn't already exist."""
    try:
        sql_create_courses_table = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(100) NOT NULL,
            level VARCHAR(50) NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_courses_table)
    except Error as e:
        print(f"Error creating Course table: {e}")

def initialize_db(db_file):
    """Initialize the database and create required tables."""
    conn = create_connection(db_file)
    if conn:
        create_course_table(conn)
        conn.commit()
        conn.close()

# Add a call to initialize_db to ensure the database is set up correctly
if __name__ == '__main__':
    initialize_db("student_management.db")
```