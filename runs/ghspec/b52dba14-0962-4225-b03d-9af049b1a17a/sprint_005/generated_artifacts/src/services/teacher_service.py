```python
# src/services/teacher_service.py

from flask import jsonify
import re

# Error codes
MISSING_FIELDS_ERROR = {
    "error": {
        "code": "E001",
        "message": "Name and email are required."
    }
}
INVALID_EMAIL_ERROR = {
    "error": {
        "code": "E002",
        "message": "Invalid email format."
    }
}

def validate_teacher_data(name: str, email: str) -> tuple:
    """
    Validates the teacher's name and email.

    Parameters:
    - name (str): The name of the teacher.
    - email (str): The email of the teacher.

    Returns:
    - tuple: A tuple containing a boolean indicating validation success,
             and an error message or None.
    """
    if not name or not email:
        return False, MISSING_FIELDS_ERROR

    # Simple regex for validating an email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_regex, email):
        return False, INVALID_EMAIL_ERROR

    return True, None

def create_teacher(name: str, email: str):
    """
    Creates a new teacher entry.

    Parameters:
    - name (str): The name of the teacher.
    - email (str): The email of the teacher.

    Returns:
    - response: JSON response containing either the created teacher info
                or an error message.
    """
    # Validate the teacher's data
    is_valid, error_response = validate_teacher_data(name, email)
    if not is_valid:
        return jsonify(error_response), 400

    # Assuming the rest of the teacher creation logic goes here...
    # This would involve saving the teacher to the database

    response = {
        "message": "Teacher created successfully",
        # "teacher": created_teacher_data 
    }
    
    return jsonify(response), 201
```