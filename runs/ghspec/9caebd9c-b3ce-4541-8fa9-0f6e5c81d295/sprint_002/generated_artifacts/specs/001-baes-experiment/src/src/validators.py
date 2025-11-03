```python
# src/validators.py

import re

def validate_student_name(name: str) -> None:
    """Validate the student's name.

    Args:
        name (str): The name of the student.

    Raises:
        ValueError: If name is empty.
    """
    if not name or not name.strip():
        raise ValueError("E001: Student name cannot be empty.")

def validate_student_email(email: str) -> None:
    """Validate the student's email.

    Args:
        email (str): The email of the student.

    Raises:
        ValueError: If email is empty or has an invalid format.
    """
    if not email or not email.strip():
        raise ValueError("E002: Student email cannot be empty.")
    
    # Regex for basic email validation
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        raise ValueError("E003: Invalid email format.")

# You may add further validation functions as needed for other entities.
```