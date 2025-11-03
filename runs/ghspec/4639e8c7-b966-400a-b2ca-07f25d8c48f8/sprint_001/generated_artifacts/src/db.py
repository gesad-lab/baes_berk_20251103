import os
import sqlite3
from sqlite3 import Error

DATABASE_FILE = 'students.db'

def create_connection():
    """Create a database connection to the SQLite database specified by the DATABASE_FILE."""
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        return conn
    except Error as e:
        print(f"Error creating database connection: {e}")
    return conn

def create_table(conn):
    """Create the students table if it does not already exist."""
    try:
        sql_create_students_table = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """
        cursor = conn.cursor()
        cursor.execute(sql_create_students_table)
    except Error as e:
        print(f"Error creating table: {e}")

def insert_student(conn, name):
    """Insert a new student into the students table."""
    sql = ''' INSERT INTO students(name)
              VALUES(?) '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error inserting student: {e}")
        return None

def get_all_students(conn):
    """Retrieve all students from the students table."""
    sql = 'SELECT * FROM students'
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        return cursor.fetchall()
    except Error as e:
        print(f"Error retrieving students: {e}")
        return []

def initialize_database():
    """Initialize the database by creating the required tables."""
    conn = create_connection()
    if conn is not None:
        create_table(conn)
        conn.close()
    else:
        print("Error! cannot create the database connection.")

# Example usage (this can be removed or modified as needed)
if __name__ == "__main__":
    initialize_database()  # Call this to create the database and table on startup