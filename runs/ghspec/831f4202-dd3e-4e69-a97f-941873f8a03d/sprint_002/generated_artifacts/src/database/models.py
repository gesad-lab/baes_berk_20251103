```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import re

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)  # New email field
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.set_email(email)

    def set_email(self, email: str):
        """Sets the email after validating its format."""
        if not self.validate_email(email):
            raise ValueError("Invalid email format.")
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validates the email format using a regex pattern."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None
```