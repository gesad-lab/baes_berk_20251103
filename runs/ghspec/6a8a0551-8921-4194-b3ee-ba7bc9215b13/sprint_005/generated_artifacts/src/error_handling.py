```python
# src/error_handling.py

import re
from flask import jsonify

def validate_teacher_creation(data):
    """
    Validates the input data for creating a new teacher.

    Parameters:
    - data (dict): The input data containing 'name' and 'email'.

    Returns:
    - Tuple (bool, dict): A boolean indicating if validation passed, 
                          and a dictionary of error messages if not.
    """
    errors = {}
    is_valid = True

    # Check for missing name
    if 'name' not in data or not data['name'].strip():
        errors['name'] = "E001: Name is required."

    # Check for missing email
    if 'email' not in data or not data['email'].strip():
        errors['email'] = "E002: Email is required."
    else:
        # Validate email format
        if not is_valid_email(data['email']):
            errors['email'] = "E003: Invalid email format."

    if errors:
        is_valid = False
    return is_valid, errors

def is_valid_email(email):
    """
    Validates the email format using a regular expression.

    Parameters:
    - email (str): The email address to validate.

    Returns:
    - bool: True if the email format is valid, False otherwise.
    """
    # Simple regex for basic email format validation
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def handle_validation_errors(errors):
    """
    Prepares a structured response for validation errors.

    Parameters:
    - errors (dict): Validation errors to format.

    Returns:
    - Flask Response: A JSON response containing error details.
    """
    response = {
        "error": {
            "code": "VALIDATION_FAILED",
            "message": "Validation errors occurred.",
            "details": errors
        }
    }
    return jsonify(response), 400
```