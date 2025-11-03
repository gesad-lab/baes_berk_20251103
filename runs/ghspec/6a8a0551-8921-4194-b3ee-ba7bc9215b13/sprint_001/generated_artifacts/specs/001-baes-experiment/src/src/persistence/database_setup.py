import os
import sqlite3
from flask import current_app

def create_database():
    """
    Creates the SQLite database and the required schema for storing students.
    This function should be called upon application startup to ensure that the
    database is set up correctly.

    Raises:
        Exception: If there is an error while trying to create the database or schema.
    """
    # Path to the SQLite database file
    db_file_path = current_app.config['DATABASE_PATH']
    
    # Check if the database file already exists
    db_exists = os.path.exists(db_file_path)
    
    try:
        # Connecting to the SQLite database
        with sqlite3.connect(db_file_path) as conn:
            cursor = conn.cursor()
            
            # Create the students table if it doesn't already exist
            if not db_exists:
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )
                ''')
                print("Database created and table 'students' initialized.")
            else:
                print("Database already exists. No need to create schema.")
    
    except sqlite3.Error as e:
        # Log error and raise Exception for handling in the application
        print(f"Database error: {e}")
        raise Exception("Failed to create database schema") from e
    except Exception as e:
        # Handle any other exceptions
        print(f"Unexpected error: {e}")
        raise Exception("An unexpected error occurred while setting up the database") from e

# This function would be called during the application startup,
# e.g., in an app factory or initialization routine.
