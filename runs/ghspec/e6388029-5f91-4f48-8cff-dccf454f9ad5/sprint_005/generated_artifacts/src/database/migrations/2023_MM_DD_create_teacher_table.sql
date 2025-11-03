```python
# src/models/teacher.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Teacher(Base):
    """Teacher model for the application, representing a teacher entity."""

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    @validates('name')
    def validate_name(self, key, name):
        """Validate that the provided name is not empty."""
        if not name or not name.strip():
            raise ValueError("Name is required and cannot be empty.")
        return name

    @validates('email')
    def validate_email(self, key, email):
        """Validate that the provided email is in a valid format."""
        if not email or not email.strip():
            raise ValueError("Email is required and cannot be empty.")
        if "@" not in email or "." not in email.split('@')[-1]:
            raise ValueError("Invalid email format.")
        return email

    def __repr__(self):
        """String representation of the Teacher instance."""
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"
```
