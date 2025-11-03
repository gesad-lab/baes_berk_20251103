import sqlite3
from sqlite3 import Error


def create_connection(db_file: str):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn


def create_students_table(conn):
    """Create the students table if it does not already exist."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(f"Error creating table: {e}")


def initialize_database(db_file: str):
    """Initialize the database by creating the required tables."""
    conn = create_connection(db_file)
    if conn is not None:
        create_students_table(conn)
        conn.commit()
        conn.close()
    else:
        raise Exception("Cannot create the database connection.")


if __name__ == "__main__":
    initialize_database("students.db")