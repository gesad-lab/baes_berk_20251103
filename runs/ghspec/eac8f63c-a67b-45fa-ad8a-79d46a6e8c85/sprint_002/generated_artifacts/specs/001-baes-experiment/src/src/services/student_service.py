```python
# src/services/student_service.py

from sqlalchemy.exc import IntegrityError
from src.models.student import Student
from src.repositories.student_repository import add_student  # Assuming this function exists
import re  # Regular expression module for email validation

class StudentService:
    """Handles business logic related to student operations."""

    def create_student(self, name: str, age: int, email: str) -> Student:
        """
        Create a new student with the given name, age, and email.

        Parameters:
        - name (str): The name of the student.
        - age (int): The age of the student.
        - email (str): The email of the student.

        Returns:
        - Student: The created student object.

        Raises:
        - ValueError: If the email is invalid.
        - IntegrityError: If a student with the same email already exists.
        """
        # Validate the email format
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")

        try:
            new_student = Student(name=name, age=age, email=email)
            add_student(new_student)  # Save student to the database
            return new_student
        except IntegrityError as e:
            raise IntegrityError("A student with this email already exists.") from e

    def is_valid_email(self, email: str) -> bool:
        """
        Validate the format of an email address.

        Parameters:
        - email (str): The email to validate.

        Returns:
        - bool: True if the email is valid, False otherwise.
        """
        # Standard email format validation using regex
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None
```