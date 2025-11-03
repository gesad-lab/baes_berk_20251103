```python
# src/services/student_service.py

from flask import jsonify, request
from app import db
from app.models import Student
from sqlalchemy.exc import IntegrityError
import re

class StudentService:
    """Service layer to manage student operations."""

    @staticmethod
    def create_student(name: str, email: str):
        """Create a new student record.

        Args:
            name (str): The name of the student.
            email (str): The email of the student.

        Returns:
            Tuple[dict, int]: A success message and the student ID.
        """
        # Validate email format
        if not StudentService.is_valid_email(email):
            return {"error": {"code": "E001", "message": "Invalid email format."}}, 400
        
        new_student = Student(name=name, email=email)
        
        # Attempt to add the student to the database
        try:
            db.session.add(new_student)
            db.session.commit()
            return {"message": "Student created successfully.", "student_id": new_student.id}, 201
        except IntegrityError:
            db.session.rollback()
            return {"error": {"code": "E002", "message": "Student already exists."}}, 400

    @staticmethod
    def retrieve_student(identifier: str):
        """Retrieve a student record by ID or name.

        Args:
            identifier (str): The student's ID or name.

        Returns:
            dict: The student record in JSON format including email.
        """
        # Check if identifier is an integer (ID) or string (name)
        student = None
        if identifier.isdigit():
            student = Student.query.get(identifier)
        else:
            student = Student.query.filter_by(name=identifier).first()

        if student:
            return jsonify({"id": student.id, "name": student.name, "email": student.email}), 200
        else:
            return {"error": {"code": "E003", "message": "Student not found."}}, 404

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate email format using a regex pattern.

        Args:
            email (str): The email to validate.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None
```