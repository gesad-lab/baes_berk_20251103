```python
# src/validation.py

import re
from typing import Optional

class ValidationError(Exception):
    """Custom exception to handle validation errors"""
    pass

def validate_email(email: str) -> None:
    """Validates the provided email address.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email is invalid or missing.
    """
    if not email:
        raise ValidationError("E001: Email is required.")
    
    # Simple regex for basic email validation
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        raise ValidationError("E002: Invalid email format.")

def validate_student_creation(name: str, email: Optional[str]) -> None:
    """Validates the input for creating a new student.

    Args:
        name (str): The name of the student.
        email (Optional[str]): The email of the student (required).

    Raises:
        ValidationError: If the name or email is invalid.
    """
    if not name:
        raise ValidationError("E003: Name is required.")
    
    # Validate the email address provided
    validate_email(email)
```
