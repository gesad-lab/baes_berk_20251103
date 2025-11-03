```python
import sqlite3

class StudentService:
    """
    Handles business logic for managing student records, including
    creating, retrieving, updating, and deleting student entries.

    Attributes:
        db_path (str): The file path to the SQLite database.
    """

    def __init__(self, db_path: str):
        self.db_path = db_path

    def validate_student_name(self, name: str) -> bool:
        """
        Validates the student name input to ensure it meets specified criteria.
        
        Args:
            name (str): The name of the student to validate.

        Returns:
            bool: True if the name is valid, False otherwise.
        """
        if not name or not isinstance(name, str) or len(name) > 100:
            return False
        return True

    def create_student(self, name: str) -> dict:
        """
        Adds a new student record to the database after validating the name.
        
        Args:
            name (str): The name of the student to be added.

        Returns:
            dict: The created student record.

        Raises:
            ValueError: If the student name is invalid.
        """
        if not self.validate_student_name(name):
            raise ValueError("Invalid student name. Must be a non-empty string with a maximum length of 100 characters.")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO students (name) VALUES (?)", (name,))
        conn.commit()
        
        student_id = cursor.lastrowid
        conn.close()

        return {"id": student_id, "name": name}

    def get_students(self) -> list:
        """
        Retrieves all student records from the database.
        
        Returns:
            list: A list of dictionaries representing student records.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT id, name FROM students")
        students = cursor.fetchall()
        
        conn.close()
        return [{"id": student[0], "name": student[1]} for student in students]

    def update_student(self, student_id: int, name: str) -> dict:
        """
        Updates an existing student record's name after validating the name.
        
        Args:
            student_id (int): The ID of the student to update.
            name (str): The new name for the student.

        Returns:
            dict: The updated student record.

        Raises:
            ValueError: If the student name is invalid or student ID does not exist.
        """
        if not self.validate_student_name(name):
            raise ValueError("Invalid student name. Must be a non-empty string with a maximum length of 100 characters.")

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("UPDATE students SET name = ? WHERE id = ?", (name, student_id))
        if cursor.rowcount == 0:
            conn.close()
            raise ValueError("Student ID does not exist.")

        conn.commit()
        conn.close()
        
        return {"id": student_id, "name": name}

    def delete_student(self, student_id: int) -> bool:
        """
        Deletes a student record by ID from the database.
        
        Args:
            student_id (int): The ID of the student to delete.

        Returns:
            bool: True if successfully deleted, False otherwise.
        """
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        deleted = cursor.rowcount > 0

        conn.commit()
        conn.close()
        
        return deleted
```