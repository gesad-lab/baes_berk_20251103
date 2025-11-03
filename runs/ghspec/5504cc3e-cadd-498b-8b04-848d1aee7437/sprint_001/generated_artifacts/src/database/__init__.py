import os
import sqlite3

DATABASE_NAME = 'students.db'

def init_db():
    """Initialize the SQLite database and create tables if they do not exist."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create a table for storing student information
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    ''')
    
    # Commit changes and close the connection
    conn.commit()
    cursor.close()
    conn.close()

# Call the init_db function to ensure the database is initialized upon module import
if __name__ == "__main__":
    init_db()