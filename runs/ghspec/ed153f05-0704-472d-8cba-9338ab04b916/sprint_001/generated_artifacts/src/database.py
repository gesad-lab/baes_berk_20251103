import os
import sqlite3
from sqlite3 import Error

DATABASE_FILE = 'students.db'  # Database file name

def create_connection():
    """Create a database connection to the SQLite database specified by DATABASE_FILE."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(f"Error '{e}' occurred while connecting to the database.")
        return None

def create_student_table(conn):
    """Create the Student table in the SQLite database.

    Args:
        conn: Connection object to the SQLite database.
    """
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS Student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """
    
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        print("Student table has been created successfully.")
    except Error as e:
        print(f"Error '{e}' occurred while creating the Student table.")

def initialize_database():
    """Initialize the database and create tables if not exists."""
    conn = create_connection()
    if conn is not None:
        create_student_table(conn)
        conn.close()
    else:
        print("Failed to initialize the database.")

if __name__ == "__main__":
    initialize_database()  # This will create the database when the script is run directly.