```python
# src/services/student_service.py

import re
from src.models.student import Student
from flask import abort

# Email validation regex pattern
EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

def is_valid_email(email: str) -> bool:
    """
    Check if the provided email is valid according to the regex pattern.
    
    Parameters:
    - email: The email address to validate.
    
    Returns:
    - bool: True if the email is valid, False otherwise.
    """
    return re.match(EMAIL_REGEX, email) is not None

def create_student(data: dict) -> Student:
    """
    Create a new student record after validating the input data.
    
    Parameters:
    - data: A dictionary containing student information, including email.
    
    Returns:
    - Student: The created Student object.

    Raises:
    - ValueError: If required fields are missing or email is invalid.
    """
    email = data.get('email')
    
    # Validate the email field
    if not email:
        abort(400, description="E001: Email field is required")
    
    if not is_valid_email(email):
        abort(400, description="E002: Invalid email format")
    
    # Assuming other validation checks are done for required fields
    
    # Create and return the new Student record
    student = Student(**data)
    # Logic to save the student to the database omitted for brevity
    return student
```