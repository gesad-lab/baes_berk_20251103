```python
# src/validation/email_validator.py

import re

class EmailValidationError(Exception):
    """Custom exception class for email validation errors."""
    pass

def is_valid_email(email: str) -> bool:
    """
    Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Raises:
        EmailValidationError: If the email format is invalid.

    Returns:
        bool: True if the email format is valid, otherwise raises an error.
    """
    # Define a regex pattern for validating email format
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    
    # Check if the email matches the regex pattern
    if not re.match(email_pattern, email):
        raise EmailValidationError("Invalid email format. Please provide a valid email address.")
    
    return True
```