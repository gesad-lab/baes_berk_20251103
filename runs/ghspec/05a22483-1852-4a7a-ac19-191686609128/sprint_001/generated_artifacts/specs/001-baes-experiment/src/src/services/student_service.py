```python
from typing import Optional
from src.models import Student  # Assuming there's a Student model defined in models
from src.database import get_db_connection  # Assuming there's a method to get a DB connection
import sqlite3

def create_student(name: str) -> Student:
    """
    Creates a new student in the database.

    Args:
        name (str): The name of the student to be created.

    Returns:
        Student: The created student object with its ID populated.

    Raises:
        ValueError: If the name is not provided or is empty.
        Exception: If an error occurs while creating the student in the database.
    """
    if not name:
        raise ValueError("Name must be provided and cannot be empty")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        student_id = cursor.lastrowid  # Get the ID of the newly created student
        conn.commit()

        return Student(id=student_id, name=name)  # Update as per your Student model constructor

    except sqlite3.Error as e:
        conn.rollback()  # Roll back any changes if an error occurs
        raise Exception(f"Database error occurred while creating student: {e}")
    finally:
        conn.close()  # Ensure the database connection is closed


def get_student_by_id(student_id: int) -> Optional[Student]:
    """
    Retrieves a student from the database by ID.

    Args:
        student_id (int): The unique identifier of the student to retrieve.

    Returns:
        Optional[Student]: The student object if found, None otherwise.

    Raises:
        ValueError: If the student_id is less than or equal to zero.
        Exception: If an error occurs while retrieving the student from the database.
    """
    if student_id <= 0:
        raise ValueError("Student ID must be a positive integer")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name FROM students WHERE id = ?", (student_id,))
        row = cursor.fetchone()

        if row is None:
            return None  # No student found

        # Assuming the Student model has a constructor that accepts id and name
        return Student(id=row[0], name=row[1])  

    except sqlite3.Error as e:
        raise Exception(f"Database error occurred while retrieving student: {e}")
    finally:
        conn.close()  # Ensure the database connection is closed
```