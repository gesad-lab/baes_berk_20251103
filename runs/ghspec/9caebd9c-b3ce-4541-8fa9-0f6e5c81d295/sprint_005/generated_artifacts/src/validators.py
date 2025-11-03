```python
# src/validators.py

from flask import jsonify
import re

def validate_teacher_creation(data):
    """
    Validate the input data for creating a new Teacher.

    Parameters:
    - data (dict): The input data containing 'name' and 'email'.

    Returns:
    - tuple: A tuple containing a boolean indicating validity, and an error message if invalid.
    """
    if 'name' not in data or not data['name'].strip():
        return False, jsonify({"error": {"code": "E001", "message": "Missing or empty 'name' field."}})
    
    if 'email' not in data or not validate_email(data['email']):
        return False, jsonify({"error": {"code": "E002", "message": "Invalid or missing 'email' field."}})

    return True, None  # Valid input

def validate_email(email):
    """
    Validate the email format using a regular expression.

    Parameters:
    - email (str): The email address to validate.

    Returns:
    - bool: True if the email format is valid, False otherwise.
    """
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email) is not None
```