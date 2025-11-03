```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, EmailStr, Field

Base = declarative_base()

class Student(Base):
    """Database model for a Student."""
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)  # New email field

class StudentCreate(BaseModel):
    """Pydantic model for creating a new Student."""
    name: str = Field(..., max_length=255)
    email: EmailStr  # Validated email format

class StudentUpdate(BaseModel):
    """Pydantic model for updating an existing Student."""
    name: str = Field(..., max_length=255)
    email: EmailStr  # Validated email format
```