```python
import sqlite3
from sqlite3 import Error

# Define the SQLite database file
DATABASE = 'students.db'

class StudentRepository:
    """
    Repository for managing student data in the SQLite database.
    """

    def __init__(self, db_file: str = DATABASE):
        """Initialize the repository with the database file."""
        self.connection = self.create_connection(db_file)
        self.create_table()  # Ensure table exists on initialization

    def create_connection(self, db_file: str) -> sqlite3.Connection:
        """Create a database connection to the SQLite database specified by db_file."""
        conn = None
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def create_table(self):
        """Create the students table if it doesn't already exist."""
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        );
        """
        try:
            if self.connection:
                cursor = self.connection.cursor()
                cursor.execute(create_table_sql)
                self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")

    def add_student(self, name: str) -> int:
        """
        Add a new student to the database.

        :param name: The name of the student.
        :return: The ID of the created student.
        :raises ValueError: If the name is empty.
        """
        if not name:
            raise ValueError("Student name cannot be empty.")
        
        insert_student_sql = "INSERT INTO students (name) VALUES (?);"
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_student_sql, (name,))
            self.connection.commit()
            return cursor.lastrowid  # Return the ID of the newly created student
        except Error as e:
            print(f"Error adding student: {e}")
            return -1  # Optionally handle this case differently in production

    def get_student(self, student_id: int) -> dict:
        """
        Retrieve a student's detail by ID.

        :param student_id: The ID of the student to retrieve.
        :return: A dictionary with the student's details or None if not found.
        """
        query_student_sql = "SELECT id, name FROM students WHERE id = ?;"
        cursor = self.connection.cursor()
        cursor.execute(query_student_sql, (student_id,))
        row = cursor.fetchone()

        if row:
            return {"id": row[0], "name": row[1]}
        else:
            return None  # Student not found
```
