```python
import sqlite3
from sqlite3 import Error

DATABASE_PATH = "students.db"

def create_connection(db_file):
    """Create a database connection to the SQLite database specified by db_file."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error creating connection: {e}")
    return conn

def create_student_table():
    """Create the Student table in the database if it doesn't exist."""
    conn = create_connection(DATABASE_PATH)
    if conn is not None:
        try:
            cursor = conn.cursor()
            # Create table SQL command
            table_creation_query = """
            CREATE TABLE IF NOT EXISTS Student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
            """
            cursor.execute(table_creation_query)
            conn.commit()
        except Error as e:
            print(f"Error creating table: {e}")
        finally:
            conn.close()
    else:
        print("Error! Cannot create the database connection.")

def get_student_by_id(student_id):
    """Retrieve a student by ID from the database.
    
    Args:
        student_id (int): The ID of the student to retrieve.

    Returns:
        dict: The student details (id, name) or None if not found.
    """
    conn = create_connection(DATABASE_PATH)
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name FROM Student WHERE id = ?", (student_id,))
            row = cursor.fetchone()
            if row is not None:
                return {"id": row[0], "name": row[1]}  # Return student info as dictionary
        except Error as e:
            print(f"Error retrieving student: {e}")
        finally:
            conn.close()
    return None

# On application startup, create the Student table
if __name__ == "__main__":
    create_student_table()
```