```python
from pydantic import BaseModel, EmailStr, constr
from typing import Optional

class TeacherCreateSchema(BaseModel):
    """Schema for validating the creation of a Teacher."""
    
    name: constr(min_length=1)  # Name must be a non-empty string
    email: EmailStr  # Email must be a valid email format


class TeacherSchema(TeacherCreateSchema):
    """Schema for representing a Teacher including the ID."""
    
    id: int  # The unique identifier for the teacher

    class Config:
        orm_mode = True  # Enable ORM mode for compatibility with SQLAlchemy models

```