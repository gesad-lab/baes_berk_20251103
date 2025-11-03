```python
# src/api/errors.py

import re

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

def validate_email(email: str) -> None:
    """
    Validate that the email is a non-empty string and follows standard email format.

    Args:
        email (str): The email address to validate.

    Raises:
        ValidationError: If the email is invalid or empty.
    """
    # Check if email is a non-empty string
    if not isinstance(email, str) or not email.strip():
        raise ValidationError("E001: Email must be a non-empty string.")

    # Standard email regex pattern
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Match the email against the regex pattern
    if not re.match(email_pattern, email):
        raise ValidationError("E002: Invalid email format.")
```