```python
# src/validation/student_validation.py

import re
from typing import Any

def validate_name(name: str) -> None:
    """Validates the name of a student.
    
    Args:
        name (str): The name of the student.
    
    Raises:
        ValueError: If the name is empty or has invalid characters.
    """
    if not name or not all(char.isalpha() or char.isspace() for char in name):
        raise ValueError("E001: Invalid name format. Name must contain only alphabetic characters and spaces.")


def validate_email(email: str) -> None:
    """Validates the email address format for a student.
    
    Args:
        email (str): The email address of the student.
    
    Raises:
        ValueError: If the email format is invalid.
    """
    # Simple email regex pattern for basic validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        raise ValueError("E002: Invalid email format. Please provide a valid email address.")

def validate_student_data(name: str, email: str) -> None:
    """Validates student data including name and email.
    
    Args:
        name (str): The name of the student.
        email (str): The email address of the student.
    
    Raises:
        ValueError: If name or email validations fail.
    """
    validate_name(name)
    validate_email(email)
```