```python
# services/validation.py

import re
from typing import Optional

class ValidationError(Exception):
    """Custom exception for validation errors."""
    pass

def validate_email(email: str) -> None:
    """
    Validates the given email address against a standard email format.
    
    :param email: The email address to validate.
    :raises ValidationError: If the email format is invalid.
    """
    # Define a regular expression pattern for validating an Email
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_pattern, email):
        # Raise a validation error if the email does not match the pattern
        raise ValidationError("Invalid email format. Please provide a valid email address.")

def validate_student_input(name: str, email: str) -> None:
    """
    Validates student input fields for creating a new student.
    
    :param name: The student's name.
    :param email: The student's email.
    :raises ValidationError: If any input field is invalid.
    """
    if not name:
        raise ValidationError("Name is required.")
    
    if not email:
        raise ValidationError("Email is required.")
    
    # Validate the email format
    validate_email(email)

# Example utility function for validating other fields can be added here
```