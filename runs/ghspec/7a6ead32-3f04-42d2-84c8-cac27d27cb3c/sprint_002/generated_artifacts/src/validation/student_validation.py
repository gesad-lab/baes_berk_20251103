```python
# src/validation/student_validation.py

import re
from fastapi import HTTPException, status

class StudentValidation:
    """Validation class for Student entity to ensure data integrity."""

    @staticmethod
    def validate_email(email: str) -> None:
        """Validate the email format.

        Args:
            email (str): The email address to validate.

        Raises:
            HTTPException: If the email format is invalid.
        """
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if not re.match(email_regex, email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"error": {"code": "E001", "message": "Invalid email format"}},
            )

# Usage:
# This validation method can be used in API endpoints to validate 
# the email field when creating or updating Student records.
```