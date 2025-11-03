```python
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Teacher(Base):
    """Represents a Teacher entity in the system."""
    
    __tablename__ = 'teachers'  # Table name for the Teacher entity

    id = Column(Integer, primary_key=True)  # Primary key
    name = Column(String, nullable=False)  # Teacher's name, required field
    email = Column(String, unique=True, nullable=False)  # Teacher's email, required and must be unique

    @validates('name')
    def validate_name(self, key, value):
        """Validate that the name field is not empty."""
        if not value:
            raise ValueError("Name must not be empty.")
        return value

    @validates('email')
    def validate_email(self, key, value):
        """Validate that the email field is not empty."""
        if not value:
            raise ValueError("Email must not be empty.")
        return value
```