```python
# src/db/database.py

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to a SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_courses_table(conn):
    """Create the courses table in the database.

    :param conn: Connection object for the SQLite database
    :return: None
    """
    try:
        sql_create_courses_table = """
        CREATE TABLE IF NOT EXISTS courses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            level TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_courses_table)
    except Error as e:
        print(f"Error creating courses table: {e}")

def migrate(db_file):
    """Run migrations to update the database schema.

    :param db_file: Path to the SQLite database file
    :return: None
    """
    conn = create_connection(db_file)
    if conn is not None:
        create_courses_table(conn)
        conn.commit()  # Commit changes
        conn.close()   # Close connection
    else:
        raise Exception("Cannot establish a database connection")

# Below part can be called to perform migrations, this would typically be run
# when setting up the application or when changes to the database schema are needed.
# migrate('path_to_your_database_file.db')
```