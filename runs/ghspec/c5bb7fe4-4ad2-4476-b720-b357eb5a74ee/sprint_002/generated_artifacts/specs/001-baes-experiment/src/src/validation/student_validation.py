```python
# src/validation/student_validation.py

import re
from typing import Optional

class StudentValidationError(Exception):
    """Custom exception for student validation errors."""
    def __init__(self, message: str):
        super().__init__(message)

def validate_student_email(email: str) -> Optional[str]:
    """
    Validate the student's email address.

    Parameters:
        email (str): The email address to validate.

    Returns:
        Optional[str]: Returns the email if valid, otherwise raises a StudentValidationError.
    
    Raises:
        StudentValidationError: If the email format is invalid.
    """
    # Basic regex pattern for matching email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Validate email using regex
    if not re.match(email_regex, email):
        raise StudentValidationError("E001: Invalid email format.")
    
    return email
```