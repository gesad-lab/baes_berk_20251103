```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.exc import IntegrityError

Base = declarative_base()

class Student(Base):
    """Model representing a student in the database."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)

    def __repr__(self):
        """Return a string representation of the student."""
        return f"<Student(name={self.name}, email={self.email})>"

    @staticmethod
    def validate_email(email: str) -> str:
        """Validate the email format.
        
        Parameters:
            email (str): The email to validate.
        
        Returns:
            str: An error message if the email format is invalid, otherwise returns an empty string.
        """
        import re
        if not email or not isinstance(email, str) or not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return "Invalid email format."
        return ""
```

