```python
# src/services/teacher_service.py

from typing import List, Optional
from models.teacher import Teacher  # Import the Teacher model
from schemas.teacher_schema import TeacherSchema  # Import the Teacher schema
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()  # Assuming db is initialized elsewhere in your app

class TeacherService:
    """Service class to handle business logic related to Teachers."""

    @staticmethod
    def create_teacher(name: str, email: str) -> Teacher:
        """
        Create a new Teacher record in the database.

        Parameters:
        - name (str): The name of the teacher.
        - email (str): The email of the teacher.

        Returns:
        - Teacher: The created Teacher object.

        Raises:
        - ValueError: If the validation of name or email fails.
        """
        # Validate input
        if not name or not email:
            raise ValueError("Name and email must be provided.")

        # Validate email format
        if not TeacherService.is_valid_email(email):
            raise ValueError("Invalid email format.")

        # Create a new Teacher instance
        new_teacher = Teacher(name=name, email=email)

        # Add to the session and commit
        db.session.add(new_teacher)
        db.session.commit()
        
        return new_teacher

    @staticmethod
    def get_teacher_by_id(teacher_id: int) -> Optional[Teacher]:
        """
        Retrieve a Teacher record by its ID.

        Parameters:
        - teacher_id (int): The ID of the teacher.

        Returns:
        - Teacher: The Teacher object if found, else None.
        """
        return Teacher.query.get(teacher_id)

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validate the email format.

        Parameters:
        - email (str): The email to validate.

        Returns:
        - bool: True if the email format is valid, else False.
        """
        import re
        # Simple regex for basic email validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
```