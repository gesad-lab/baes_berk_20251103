```python
import sqlite3
from contextlib import closing

def create_teacher_table():
    """
    Create the 'teachers' table in the database if it does not already exist.
    
    Table structure:
    - id: INTEGER PRIMARY KEY AUTOINCREMENT
    - name: TEXT NOT NULL
    - email: TEXT NOT NULL UNIQUE
    
    Raises:
        sqlite3.OperationalError: If there is an issue with the database operation.
    """
    try:
        # Connect to the database (assuming the database file is 'school.db')
        with closing(sqlite3.connect('school.db')) as connection:
            with closing(connection.cursor()) as cursor:
                # Create table if it does not exist
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS teachers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL UNIQUE
                    )
                ''')
                # Commit the transaction
                connection.commit()
    except sqlite3.OperationalError as e:
        # Log the error for debugging purposes
        print(f"Error creating teachers table: {str(e)}")
        raise
```