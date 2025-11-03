import sqlite3

DATABASE_NAME = 'students.db'

def initialize_database():
    """Initialize the database and create the schema as needed."""
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()

        # Create the Student table if it does not exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        
        # Commit changes and close the connection
        conn.commit()

    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    initialize_database()