```python
# src/services/student_service.py

import re
from src.models import Student
from typing import Optional

# Define a simple regex for validating email format
EMAIL_REGEX = r'^[\w\.-]+@[\w\.-]+\.\w+$'

class StudentService:
    """Service to handle business logic related to Students."""

    @staticmethod
    def validate_email(email: str) -> Optional[str]:
        """
        Validate the provided email format.
        
        Params:
            email (str): The email address to validate.
            
        Returns:
            Optional[str]: None if valid, or an error message if invalid.
        """
        if not email:
            return "E001: Email field is required."
        if not re.match(EMAIL_REGEX, email):
            return "E002: Invalid email format."
        return None

    @staticmethod
    def create_student(name: str, email: str) -> dict:
        """
        Create a new student with the specified name and email.
        
        Params:
            name (str): The name of the student.
            email (str): The email address of the student.
        
        Returns:
            dict: The created student object as a dictionary.
        """
        # Validate the email before creating the student
        email_error = StudentService.validate_email(email)
        if email_error:
            raise ValueError(email_error)
        
        # Create the student instance
        student = Student(name=name, email=email)
        # Logic to save student to the database here
        # Assuming a save method that handles persistence, e.g., session.add(student)
        
        return {"id": student.id, "name": student.name, "email": student.email}

    @staticmethod
    def update_student_email(student_id: int, new_email: str) -> dict:
        """
        Update an existing student's email address.
        
        Params:
            student_id (int): The ID of the student to update.
            new_email (str): The new email address for the student.
        
        Returns:
            dict: The updated student object as a dictionary.
        """
        email_error = StudentService.validate_email(new_email)
        if email_error:
            raise ValueError(email_error)
        
        # Logic to retrieve the student from the database would go here
        # student = session.query(Student).get(student_id)
        
        # student.email = new_email
        # session.commit()

        return {"id": student.id, "name": student.name, "email": student.email}

    @staticmethod
    def get_student_by_id(student_id: int) -> dict:
        """
        Retrieve a student's information by their ID.
        
        Params:
            student_id (int): The ID of the student to retrieve.
        
        Returns:
            dict: The student's information as a dictionary.
        """
        # Logic to retrieve the student from the database
        # student = session.query(Student).get(student_id)
        
        return {"id": student.id, "name": student.name, "email": student.email} 
```