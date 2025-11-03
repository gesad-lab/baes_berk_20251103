```python
# src/models/student.py

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import validates  # Import validates for email validation

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)  # new field added with unique constraint

    @validates('email')  # Validate email format
    def validate_email(self, key, email):
        if '@' not in email or '.' not in email:  # Basic email format validation
            raise ValueError("Invalid email format")
        return email
```