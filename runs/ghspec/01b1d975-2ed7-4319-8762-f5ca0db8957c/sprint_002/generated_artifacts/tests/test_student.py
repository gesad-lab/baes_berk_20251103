```python
# src/validation.py

import re
from flask import jsonify

def validate_student_data(name: str, email: str) -> dict:
    """Validate student name and email.

    Args:
        name (str): The name of the student.
        email (str): The email address of the student.

    Returns:
        dict: Validation results, containing 'is_valid' status and 'errors' list.
    """
    errors = []
    
    # Validate name (assuming name must be non-empty)
    if not name or not isinstance(name, str):
        errors.append("E001: Name is required and must be a string.")

    # Validate email format
    if not validate_email_format(email):
        errors.append("E002: Invalid email format.")
    
    # Validation summary
    is_valid = len(errors) == 0
    return {"is_valid": is_valid, "errors": errors}

def validate_email_format(email: str) -> bool:
    """Check if the email address is valid using a regex.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, otherwise False.
    """
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None
```