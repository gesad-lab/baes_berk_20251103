```python
# File: src/services/student_service.py

from typing import Optional
import re
from models import Student  # Assuming the Student model is defined in models.py
from database import db  # Assuming there's a database module for DB interactions

class StudentService:
    """Service layer for managing students, including validation for name and email."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate the email format using a regular expression.
        
        Args:
            email: The email address to validate.
        
        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(email_regex, email) is not None

    def create_student(self, name: str, email: str) -> Student:
        """
        Create a new student with a name and email.
        
        Args:
            name: The name of the student.
            email: The email of the student.
        
        Returns:
            Student: The created Student object.
        
        Raises:
            ValueError: If the name or email is invalid.
        """
        if not name:
            raise ValueError("Name is required.")
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")

        new_student = Student(name=name, email=email)
        db.session.add(new_student)
        db.session.commit()
        return new_student

    def update_student(self, student_id: int, name: Optional[str] = None, email: Optional[str] = None) -> Student:
        """
        Update an existing student's name and/or email.
        
        Args:
            student_id: The ID of the student to update.
            name: The new name of the student.
            email: The new email of the student.
        
        Returns:
            Student: The updated Student object.
        
        Raises:
            ValueError: If the name or email is invalid or if the student is not found.
        """
        student = db.session.query(Student).filter(Student.id == student_id).one_or_none()
        if not student:
            raise ValueError("Student not found.")

        if name is not None:
            student.name = name
        if email is not None:
            if not self.validate_email(email):
                raise ValueError("Invalid email format.")
            student.email = email

        db.session.commit()
        return student

    def get_student(self, student_id: int) -> Student:
        """
        Retrieve a student by their ID.
        
        Args:
            student_id: The ID of the student to retrieve.
        
        Returns:
            Student: The Student object if found.
        
        Raises:
            ValueError: If the student is not found.
        """
        student = db.session.query(Student).filter(Student.id == student_id).one_or_none()
        if not student:
            raise ValueError("Student not found.")
        return student
```