```python
# File: src/services/teacher_service.py

from flask import jsonify
from src.models import Teacher
from src.database import db
import re

class TeacherService:
    """Service class for managing Teacher operations."""
    
    @staticmethod
    def create_teacher(name: str, email: str):
        """
        Create a new Teacher.

        Parameters:
        - name (str): The name of the teacher.
        - email (str): The email of the teacher.

        Returns:
        - dict: Created teacher details.
        - None: If an error occurs during creation.
        """
        # Input validation
        if not name or not email:
            return {"error": {"code": "E001", "message": "Name and email are required."}}, 400
        
        if not TeacherService.is_valid_email(email):
            return {"error": {"code": "E002", "message": "Invalid email format."}}, 400
        
        # Create teacher instance and save to database
        new_teacher = Teacher(name=name, email=email)
        db.session.add(new_teacher)
        db.session.commit()
        
        return {"id": new_teacher.id, "name": new_teacher.name, "email": new_teacher.email}, 201

    @staticmethod
    def get_teacher_by_id(teacher_id: int):
        """
        Retrieve a Teacher by ID.

        Parameters:
        - teacher_id (int): The ID of the teacher.

        Returns:
        - dict: Teacher details if found.
        - None: If the teacher is not found.
        """
        teacher = Teacher.query.get(teacher_id)
        if not teacher:
            return {"error": {"code": "E003", "message": "Teacher not found."}}, 404
        
        return {"id": teacher.id, "name": teacher.name, "email": teacher.email}, 200

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Check if the provided email is valid.

        Parameters:
        - email (str): Email to validate.

        Returns:
        - bool: True if valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
```