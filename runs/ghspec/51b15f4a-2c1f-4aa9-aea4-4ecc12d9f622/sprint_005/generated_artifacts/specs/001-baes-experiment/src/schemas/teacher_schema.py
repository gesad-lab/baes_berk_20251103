```python
# schemas/teacher_schema.py

from pydantic import BaseModel, EmailStr, validator
from typing import Optional


class TeacherCreateSchema(BaseModel):
    """
    Schema for creating a new teacher.

    Attributes:
        name (str): The name of the teacher. Must be a non-empty string.
        email (EmailStr): The email of the teacher. Must be a valid email format.
    """
    
    name: str
    email: EmailStr

    @validator('name')
    def validate_name(cls, value):
        """
        Validates that the name is not empty.
        """
        if not value.strip():
            raise ValueError("Name must not be empty.")
        return value


class TeacherResponseSchema(BaseModel):
    """
    Schema for responding with teacher details.

    Attributes:
        id (int): The unique identifier for the teacher.
        name (str): The name of the teacher.
        email (EmailStr): The email of the teacher.
    """
    
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enables ORM mode to read data from the database models
```