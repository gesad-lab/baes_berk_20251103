```python
# src/repositories/student_repository.py

from src.models.student import Student
from typing import Optional, List, Dict
import re

class StudentRepository:
    """Repository for managing student data in the database."""

    def create(self, name: str, email: str) -> Student:
        """Create a new student with the given name and email.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            Student: The created Student object.
        """
        self.validate_email(email)  # Validate the provided email
        student = Student(name=name, email=email)
        # Insert student into the database
        # (Assumed to be handled by an ORM or database connection)
        # db.session.add(student)
        # db.session.commit()
        return student

    def get_by_id(self, student_id: int) -> Optional[Dict]:
        """Retrieve a student by their ID.

        Args:
            student_id (int): The ID of the student to retrieve.

        Returns:
            Optional[Dict]: A dictionary containing the student's ID, name, and email, or None if not found.
        """
        # Fetch the student from the database using the student_id
        # (Assumed to be handled by an ORM or database connection)
        # student = db.session.query(Student).filter_by(id=student_id).first()
        # return student.to_dict() if student else None
        
        # Mocked return for demonstration
        student = Student(id=student_id, name="Jane Doe", email="jane.doe@example.com")  # Replace with actual database query
        if student:  # If student is found
            return {
                'id': student.id,
                'name': student.name,
                'email': student.email
            }
        return None

    @staticmethod
    def validate_email(email: str) -> None:
        """Validate the given email address.

        Args:
            email (str): The email address to validate.

        Raises:
            ValueError: If the email is invalid.
        """
        if not email:
            raise ValueError("E001: Email cannot be empty")
        # Basic email regex pattern for validation
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("E002: Invalid email format")
```
