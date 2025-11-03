```python
import sqlite3
from sqlite3 import Error

# Create a connection to the SQLite database
def create_connection(db_file):
    """Create a SQLite database connection"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
    return conn

# Create a table for students
def create_table(conn):
    """Create the students table in the database"""
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

# Create a new student
def create_student(conn, name):
    """Insert a new student into the students table"""
    sql = '''INSERT INTO students(name) VALUES(?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name,))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"Error creating student: {e}")
        return None

# Retrieve a student by ID
def get_student(conn, student_id):
    """Fetch a student by their ID"""
    sql = '''SELECT * FROM students WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        student = cursor.fetchone()
        return student  # Returns a tuple (id, name) or None if not found
    except Error as e:
        print(f"Error retrieving student: {e}")
        return None

# Update a student's name by ID
def update_student(conn, student_id, new_name):
    """Update a student's name by ID"""
    sql = '''UPDATE students SET name = ? WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (new_name, student_id))
        conn.commit()
        return cursor.rowcount  # Returns the number of rows affected
    except Error as e:
        print(f"Error updating student: {e}")
        return None

# Delete a student by ID
def delete_student(conn, student_id):
    """Delete a student by their ID"""
    sql = '''DELETE FROM students WHERE id = ?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        conn.commit()
        return cursor.rowcount  # Returns the number of rows affected
    except Error as e:
        print(f"Error deleting student: {e}")
        return None

# Main execution to create database and table
if __name__ == '__main__':
    database = "students.db"
    # Create a database connection
    conn = create_connection(database)

    # Create tables
    if conn is not None:
        create_table(conn)
    else:
        print("Error! Cannot create the database connection.")
```