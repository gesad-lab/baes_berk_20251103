```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):
    """Represents a Student entity with CRUD capabilities."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # New email field, must be unique and required

    def __init__(self, name: str, email: str):
        """
        Initializes a new Student instance.

        Parameters:
        - name: The name of the student.
        - email: The email address of the student, must be valid.
        """
        self.name = name
        self.set_email(email)

    def set_email(self, email: str):
        """
        Sets the email for the student, validating the email format.

        Parameters:
        - email: The email address to set for the student.

        Raises:
        - ValueError: If the email format is invalid.
        """
        if not self.is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")
        self.email = email

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates the format of an email address.

        Parameters:
        - email: The email address to validate.

        Returns:
        - A boolean indicating if the email is valid.
        """
        # Basic regex pattern for email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_pattern, email) is not None
```