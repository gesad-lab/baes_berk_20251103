```python
from pydantic import BaseModel, EmailStr, constr
from typing import List, Optional

class TeacherBase(BaseModel):
    """Base model for Teacher, containing common fields."""
    name: constr(min_length=1, max_length=100)  # Name must be between 1 and 100 characters
    email: EmailStr  # Email must be a valid email format

class TeacherCreate(TeacherBase):
    """Schema for creating a new Teacher."""
    pass

class TeacherResponse(TeacherBase):
    """Schema for returning a Teacher response with ID."""
    id: int  # The unique identifier for the Teacher record

    class Config:
        orm_mode = True  # Enable ORM mode to work with SQLAlchemy models

class TeacherListResponse(BaseModel):
    """Schema for returning a list of Teachers."""
    teachers: List[TeacherResponse]  # A list of TeacherResponse instances
```