```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
from .database import Base

class Teacher(Base):
    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __repr__(self):
        return f"<Teacher(id={self.id}, name={self.name}, email={self.email})>"

    @validates('name')
    def validate_name(self, key, value):
        """Validate the name field to ensure it is not empty."""
        if not value:
            raise ValueError("Name must not be empty.")
        return value

    @validates('email')
    def validate_email(self, key, value):
        """Validate the email field to ensure it is not empty and follows basic email format."""
        if not value:
            raise ValueError("Email must not be empty.")
        # Basic email validation (should be improved or replaced with a regex if necessary)
        if "@" not in value or len(value) < 5:
            raise ValueError("Email must be a valid email address.")
        return value
```