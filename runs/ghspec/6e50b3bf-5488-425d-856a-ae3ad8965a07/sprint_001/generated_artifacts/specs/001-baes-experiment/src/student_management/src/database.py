import sqlite3
from sqlite3 import Error

def create_connection(db_file: str):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connection established to {db_file}")
    except Error as e:
        print(f"Error connecting to database {db_file}: {e}")
    return conn

def create_table(conn):
    """Create the student table in the database."""
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );"""
    
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Student table created successfully.")
    except Error as e:
        print(f"Error creating table: {e}")

def setup_database(db_file: str):
    """Setup the SQLite database, creating necessary tables."""
    conn = create_connection(db_file)
    if conn:
        create_table(conn)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    setup_database("students.db")  # Change this to your desired database file location (e.g., in the project directory)