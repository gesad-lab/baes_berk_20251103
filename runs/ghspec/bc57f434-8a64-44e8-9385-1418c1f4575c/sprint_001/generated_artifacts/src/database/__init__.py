import os
import sqlite3

def initialize_database(db_name: str = "students.db") -> None:
    """Initialize SQLite database and create the student table if it does not exist."""
    try:
        # Connect to the SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(db_name)
        
        with conn:
            # Create a cursor object to execute SQL commands
            cursor = conn.cursor()
            
            # Create a student table if it does not already exist
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
            """)
        
        print(f"Database '{db_name}' initialized and 'students' table created.")
    except sqlite3.Error as e:
        print(f"An error occurred while initializing the database: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    # Initialize the database on application startup
    initialize_database(os.getenv("DATABASE_NAME", "students.db"))