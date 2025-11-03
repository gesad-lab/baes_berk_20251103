```python
# src/utils/validators.py

import re
from typing import Optional

def is_valid_email(email: str) -> bool:
    """
    Validate the format of an email address using a regular expression.

    Parameters:
    - email: The email address to validate.

    Returns:
    - bool: True if the email format is valid, False otherwise.
    """
    # Regular expression for validating an Email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    
    # Perform the regex match and return the result
    return re.match(email_regex, email) is not None

def validate_student_email(email: str) -> Optional[str]:
    """
    Validate the email address for a student.
    
    Parameters:
    - email: The student email address to validate.

    Returns:
    - Optional[str]: Returns an error message if validation fails, otherwise None.
    """
    if not email:
        return "E001: Email field is required."
    
    if not is_valid_email(email):
        return "E002: Invalid email format."
    
    return None  # No errors, email is valid
```