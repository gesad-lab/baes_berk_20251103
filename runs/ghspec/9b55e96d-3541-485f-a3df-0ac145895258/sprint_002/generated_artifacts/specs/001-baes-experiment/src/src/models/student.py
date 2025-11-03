```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)  # New field for email

    @validates('email')
    def validate_email(self, key, email):
        """Validates the email format to ensure it is well-formed."""
        if not isinstance(email, str) or '@' not in email or '.' not in email.split('@')[-1]:
            raise ValueError("Invalid email format.")
        return email

```