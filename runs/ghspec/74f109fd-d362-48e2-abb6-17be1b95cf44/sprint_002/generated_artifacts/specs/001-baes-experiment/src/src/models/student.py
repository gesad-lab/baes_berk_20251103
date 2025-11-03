```python
# src/models/student.py

import re

class Student:
    """Class representing a student entity."""

    def __init__(self, name: str, email: str = None, age: int = None):
        self.name = name
        self.email = email
        self.age = age

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the format of an email address.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        if email is None:
            return True  # Consider None as valid for optional emails
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        is_valid = re.match(email_regex, email) is not None
        return is_valid
```