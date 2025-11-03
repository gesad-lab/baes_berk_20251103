```python
from sqlalchemy import Column, Integer, String
from db.database import Base

class Student(Base):
    """Student entity with ORM functionality including email."""
    
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field
    
    def __init__(self, name: str, email: str):
        if not name:
            logger.error('Failed to create student: name is required', extra={'context': 'Student'})
            raise ValueError("Name is required.")
        if not email or "@" not in email:
            logger.error('Failed to create student: invalid email', extra={'context': 'Student'})
            raise ValueError("Email is required and must be valid.")
        
        self.name = name
        self.email = email
```