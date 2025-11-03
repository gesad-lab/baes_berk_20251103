import os
import sqlite3
from sqlite3 import Error
from src.models import Student  # Assuming Student model is defined in models.py

DATABASE = 'students.db'

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

def migrate_database(conn):
    """Migrate the database schema to include the email field in the Student table."""
    try:
        cursor = conn.cursor()

        # Check if the email column already exists
        cursor.execute("PRAGMA table_info(Student);")
        columns = [column[1] for column in cursor.fetchall()]
        if 'email' not in columns:
            # Add email column if it does not exist
            cursor.execute("ALTER TABLE Student ADD COLUMN email TEXT;")
            print("Email column added to Student table.")

        # Commit the changes
        conn.commit()

    except Error as e:
        print(f"Error during migration: {e}")

def initialize_db():
    """Initialize the database and apply migrations."""
    conn = create_connection(DATABASE)
    if conn:
        migrate_database(conn)
        conn.close()

if __name__ == '__main__':
    # Ensure the database is initialized on application startup
    initialize_db()