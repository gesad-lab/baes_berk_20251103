```python
# File: src/services.py

from sqlalchemy.exc import IntegrityError
from flask import jsonify
from src.models import db, Teacher  # Import the Teacher model
import re

def validate_teacher_inputs(name: str, email: str) -> list:
    """Validate the inputs for creating a Teacher entity.

    Parameters:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Returns:
        list: A list of error messages (empty if valid).
    """
    errors = []
    
    # Validate name
    if not name:
        errors.append("E001: Name is required")
    
    # Validate email format and uniqueness
    if not email:
        errors.append("E002: Email is required")
    elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Simple email format check
        errors.append("E003: Invalid email format")
    
    # Check for uniqueness of the email in the database
    if email and Teacher.query.filter_by(email=email).first():
        errors.append("E004: Email must be unique")

    return errors

def create_teacher(name: str, email: str) -> dict:
    """Create a new Teacher entity in the database.

    Parameters:
        name (str): The name of the teacher.
        email (str): The email of the teacher.

    Returns:
        dict: Success message and created teacher information or error messages.
    """
    # Validate inputs
    errors = validate_teacher_inputs(name, email)
    if errors:
        return {"success": False, "errors": errors}

    # Create a new Teacher instance
    new_teacher = Teacher(name=name, email=email)
    
    try:
        db.session.add(new_teacher)  # Add the teacher to the session
        db.session.commit()  # Commit the transaction
        return {
            "success": True,
            "teacher": {
                "name": new_teacher.name,
                "email": new_teacher.email
            }
        }
    except IntegrityError:
        db.session.rollback()  # Rollback in case of integrity error
        return {"success": False, "errors": ["E005: Failed to create teacher due to an internal error."]}

def retrieve_teachers() -> dict:
    """Retrieve a list of all teachers from the database.

    Returns:
        dict: A dictionary containing a list of teachers.
    """
    teachers = Teacher.query.all()
    return {
        "success": True,
        "teachers": [{"name": teacher.name, "email": teacher.email} for teacher in teachers]
    }
```