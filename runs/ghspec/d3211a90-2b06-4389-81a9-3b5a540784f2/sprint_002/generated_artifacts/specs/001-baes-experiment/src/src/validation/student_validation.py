```python
# File: src/validation/student_validation.py

from sqlalchemy.exc import IntegrityError
from src.models.student import Student
from flask import jsonify

def validate_student_data(data):
    """
    Validate student data for creating or updating a student.
    
    Args:
        data (dict): Data containing student attributes like name and email.
    
    Raises:
        ValueError: If the name or email is missing or invalid.
    """
    if 'name' not in data or not data['name'].strip():
        raise ValueError("Name field is required.")
    
    if 'email' not in data or not data['email'].strip():
        raise ValueError("Email field is required.")
    
    if not is_valid_email(data['email']):
        raise ValueError("Invalid email format.")

def is_valid_email(email):
    """
    Check if the given email is in a valid format.
    
    Args:
        email (str): Email to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    # Simple regex for validating an Email
    import re
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

def get_student_by_id(student_id):
    """
    Retrieve a student by ID and return their details including email.
    
    Args:
        student_id (int): The ID of the student to retrieve.
    
    Returns:
        dict: A dictionary containing student name and email.
    """
    try:
        student = Student.query.get(student_id)
        if student is None:
            return jsonify({"error": {"code": "E002", "message": "Student not found."}}), 404

        return {
            "name": student.name,
            "email": student.email
        }, 200

    except IntegrityError:
        return jsonify({"error": {"code": "E003", "message": "Database integrity error."}}), 500
```