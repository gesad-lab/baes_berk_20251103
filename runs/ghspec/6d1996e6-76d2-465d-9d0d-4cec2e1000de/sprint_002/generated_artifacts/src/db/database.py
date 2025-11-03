```python
# src/models/student.py

class Student:
    """Represents a student with a name and email."""
    
    def __init__(self, name: str, email: str):
        """
        Initializes a new Student instance.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.

        Raises:
            ValueError: If the email is not valid.
        """
        self.name = name
        self.email = email  # New attribute to store the student's email

        # Validate the email format
        if not self._is_valid_email(self.email):
            raise ValueError(f"Invalid email format: {self.email}")

    def _is_valid_email(self, email: str) -> bool:
        """
        Validates the email format.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, otherwise False.
        """
        # Simple regex for email validation
        import re
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None
```