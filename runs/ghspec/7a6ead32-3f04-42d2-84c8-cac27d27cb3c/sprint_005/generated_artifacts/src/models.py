```python
# src/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Teacher(Base):
    """Represents a Teacher entity in the database."""
    
    __tablename__ = 'teachers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    @validates('email')
    def validate_email(self, key, email):
        """Validate that the email is properly formatted and unique."""
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")
        return email

    @staticmethod
    def is_valid_email(email):
        """Simple regex for validating email format (to be improved)."""
        import re
        email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        return re.match(email_regex, email) is not None
```