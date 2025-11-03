```python
import os
import sqlite3

DATABASE_FILE = 'students.db'

def init_db():
    """
    Initialize the SQLite database and create the required schema.
    
    This function establishes a connection to the SQLite database,
    and creates a Students table if it does not already exist.
    """
    # Ensure the database file exists
    if not os.path.exists(DATABASE_FILE):
        # Connect to SQLite database (it will be created if it doesn't exist)
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        
        # Create the Students table with an auto-incrementing ID
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        ''')
        
        # Commit changes and close the connection
        conn.commit()
        conn.close()
    else:
        print("Database already initialized.")

if __name__ == "__main__":
    init_db()
```