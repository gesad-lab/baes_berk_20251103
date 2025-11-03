```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Required name field
    email = Column(String, nullable=False)  # New required email field

    @validates('email')
    def validate_email(self, key, email):
        """
        Validate the email format. Raise a ValueError if invalid.
        
        Args:
            key (str): The name of the field (email).
            email (str): The email value to validate.
        
        Raises:
            ValueError: If the email is missing or not in a valid format.
        
        Returns:
            str: The validated email.
        """
        if not email:
            raise ValueError("E002: Email field is required.")
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("E003: Invalid email format.")
        return email
```