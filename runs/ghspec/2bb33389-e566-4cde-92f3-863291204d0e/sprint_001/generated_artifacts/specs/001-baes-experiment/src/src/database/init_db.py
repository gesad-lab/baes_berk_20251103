import os
import sqlite3

def initialize_database(db_path: str) -> None:
    """
    Initialize the SQLite database schema.
    
    :param db_path: Path to the SQLite database file.
    """
    if not os.path.exists(db_path):
        try:
            # Connect to the SQLite database (it will be created if it doesn't exist)
            with sqlite3.connect(db_path) as conn:
                cursor = conn.cursor()
                
                # Create student table with required fields
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )
                ''')
                
                # Commit the transaction
                conn.commit()
                
        except sqlite3.Error as e:
            # Log detailed error context
            print(f"Database initialization error: {e}")
            raise RuntimeError("Failed to initialize the database.") from e

if __name__ == "__main__":
    # Define the database path
    DATABASE_PATH = "students.db"
    
    # Initialize the database
    initialize_database(DATABASE_PATH)
    print("Database initialized successfully.")