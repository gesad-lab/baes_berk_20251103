```python
# src/utils/email_validators.py

import re

def is_valid_email(email: str) -> bool:
    """Validate the format of an email address.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """
    # Basic email format validation using regular expression
    # The regex checks for:
    # - At least one character before @
    # - A domain name with at least one dot
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(email_regex, email))

# Example usage:
# if not is_valid_email(student_email):
#     raise ValueError("Invalid email format.")
```