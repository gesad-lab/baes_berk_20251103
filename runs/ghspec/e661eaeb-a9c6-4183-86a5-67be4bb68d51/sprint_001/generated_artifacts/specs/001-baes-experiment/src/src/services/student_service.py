```python
from sqlalchemy.orm import Session
from models.student import Student
from typing import List, Optional

class StudentService:
    """Service for managing Student entities."""

    def __init__(self, db: Session):
        """Initialize the StudentService with a database session.

        Args:
            db (Session): Database session for interacting with the Student table.
        """
        self.db = db

    def create_student(self, name: str) -> Student:
        """Create a new student.

        Args:
            name (str): The name of the student.

        Returns:
            Student: The created student object.
        """
        new_student = Student(name=name)
        self.db.add(new_student)
        self.db.commit()
        self.db.refresh(new_student)  # Refresh from DB to get generated ID
        return new_student

    def get_student(self, student_id: int) -> Optional[Student]:
        """Retrieve a student by ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Optional[Student]: The student object if found, otherwise None.
        """
        return self.db.query(Student).filter(Student.id == student_id).first()

    def update_student(self, student_id: int, name: str) -> Optional[Student]:
        """Update a student's name.

        Args:
            student_id (int): The ID of the student to update.
            name (str): The new name for the student.

        Returns:
            Optional[Student]: The updated student object if the update was successful, otherwise None.
        """
        student = self.get_student(student_id)
        if student:
            student.name = name
            self.db.commit()
            self.db.refresh(student)  # Refresh to get updated data
            return student
        return None

    def delete_student(self, student_id: int) -> bool:
        """Delete a student by ID.

        Args:
            student_id (int): The ID of the student to delete.

        Returns:
            bool: True if deletion was successful, otherwise False.
        """
        student = self.get_student(student_id)
        if student:
            self.db.delete(student)
            self.db.commit()
            return True
        return False
```