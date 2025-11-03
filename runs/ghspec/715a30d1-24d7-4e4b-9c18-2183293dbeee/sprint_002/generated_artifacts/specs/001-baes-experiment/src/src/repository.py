```python
# src/repository.py

from sqlalchemy.orm import Session
from models import Student  # Assuming Student model includes an email field now

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, name: str, email: str) -> Student:
        """
        Save a new student to the database.

        Parameters:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            Student: The created student object.
        """
        # Validate input fields
        if not name or not email:
            raise ValueError("Both name and email are required.")

        # Create new student instance
        student = Student(name=name, email=email)
        self.db.add(student)
        self.db.commit()
        self.db.refresh(student)  # Fetch the created student with its ID
        return student

    def get_by_id(self, student_id: int) -> Student:
        """
        Retrieve a student by their ID.

        Parameters:
            student_id (int): The ID of the student.

        Returns:
            Student: The requested student object.

        Raises:
            ValueError: if the student with the given ID is not found.
        """
        student = self.db.query(Student).filter(Student.id == student_id).first()
        if student is None:
            raise ValueError("Student not found.")
        return student
```