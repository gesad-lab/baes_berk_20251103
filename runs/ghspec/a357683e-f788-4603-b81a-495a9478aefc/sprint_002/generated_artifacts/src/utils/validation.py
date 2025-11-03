```python
# src/utils/validation.py

from email_validator import validate_email, EmailNotValidError

def is_valid_email(email: str) -> bool:
    """Validate the format of an email address.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email format is valid, False otherwise.
    
    Raises:
        EmailNotValidError: If the email format is invalid.
    """
    try:
        # Validate the email format using the email-validator library
        valid = validate_email(email)
        return True  # If validation passes, return True
    except EmailNotValidError:
        return False  # Return False if validation fails
```