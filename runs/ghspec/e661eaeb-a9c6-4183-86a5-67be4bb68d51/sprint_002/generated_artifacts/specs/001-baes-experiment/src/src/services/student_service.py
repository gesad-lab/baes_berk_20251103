```python
# src/services/student_service.py

from typing import Any
import re

class StudentService:
    """Service for managing student entities, including email validation."""

    EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    def validate_email(self, email: str) -> bool:
        """Validate the provided email against standard formatting rules.

        Args:
            email (str): The email address to validate.

        Returns:
            bool: True if the email format is valid, False otherwise.
        """
        if isinstance(email, str):
            is_valid = re.match(self.EMAIL_REGEX, email) is not None
            return is_valid
        return False

    def create_student(self, name: str, email: str) -> Any:
        """Create a new student after validating the email.

        Args:
            name (str): The name of the student.
            email (str): The email address of the student.

        Raises:
            ValueError: If the email is not valid.

        Returns:
            Any: The created student entity if successful.
        """
        if not self.validate_email(email):
            raise ValueError("Invalid email format: {}".format(email))

        # Proceed with the actual student creation logic (not shown)
        # e.g., student = Student(name=name, email=email)
        # return student.save() or similar logic

        # Placeholder return statement for demonstration
        return {"name": name, "email": email}

    # Other methods for managing students can be added here
```