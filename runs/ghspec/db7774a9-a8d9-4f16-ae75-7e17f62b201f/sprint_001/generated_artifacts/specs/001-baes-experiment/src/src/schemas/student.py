```python
from pydantic import BaseModel, Field, validator
from typing import Optional

class StudentBase(BaseModel):
    name: str = Field(..., description="The name of the student")

    @validator('name')
    def validate_name(cls, value):
        """Ensure that the name is not empty or just whitespace."""
        if not value or not value.strip():
            raise ValueError("Name field cannot be empty or just whitespace.")
        return value

class StudentCreate(StudentBase):
    """Schema for creating a new student."""

class Student(StudentBase):
    """Schema representing a student object with an ID."""

    id: int = Field(..., description="The unique identifier of the student")

    class Config:
        orm_mode = True  # Enable ORM mode for SQLAlchemy compatibility
```