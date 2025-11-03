```python
import sqlite3
from sqlite3 import Error
from contextlib import closing

DATABASE_FILE = "students.db"

def create_connection():
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(f"Error '{e}' occurred while connecting to the database")
        return None

def create_table(conn):
    """Create the students table in the SQLite database."""
    create_students_table_sql = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """
    try:
        with closing(conn.cursor()) as cursor:
            cursor.execute(create_students_table_sql)
            print("Students table created successfully")
    except Error as e:
        print(f"Error '{e}' occurred during table creation")

def initialize_database():
    """Initialize the database and create tables if they do not exist."""
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

# Call to initialize the database on startup
if __name__ == '__main__':
    initialize_database()
```