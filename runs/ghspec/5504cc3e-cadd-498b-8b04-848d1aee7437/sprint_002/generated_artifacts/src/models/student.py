```python
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    """ORM model for the Student entity with contact information."""
    
    __tablename__ = 'students'

    id = Column(String, primary_key=True)  # Assuming 'id' is the primary key
    name = Column(String, nullable=False)  # Existing field
    email = Column(String, nullable=False)  # New field, added for email

    def __init__(self, name: str, email: str):
        """Initialize the Student instance with name and email."""
        if not self.validate_email(email):
            raise ValueError("Invalid email format")
        self.name = name
        self.email = email

    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate the email format."""
        import re
        # Simple regex for email validation
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, email) is not None

    def __repr__(self):
        """Return a string representation of the Student instance."""
        return f"<Student id={self.id}, name={self.name}, email={self.email}>"
```