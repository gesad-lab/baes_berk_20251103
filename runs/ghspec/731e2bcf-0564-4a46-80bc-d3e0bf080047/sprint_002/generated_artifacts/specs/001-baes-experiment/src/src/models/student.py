```python
from src import db
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.exc import IntegrityError
import re

class Student(db.Model):
    """Represents a student in the system."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), nullable=False, unique=True)  # New email field

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, name: str, email: str):
        """Initialize a new Student instance.

        Args:
            name (str): Name of the student.
            email (str): Email address of the student (must be valid format).
        """
        self.name = name
        self.set_email(email)

    def set_email(self, email: str):
        """Set the email attribute with validation.

        Args:
            email (str): Email address to set.

        Raises:
            ValueError: If email format is invalid.
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format")  # Raise exception for invalid email
        self.email = email

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Validate the email format.

        Args:
            email (str): Email address to validate.

        Returns:
            bool: True if valid email format, False otherwise.
        """
        # Simple regex for validating an email
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
```