```python
# app/schemas.py

from pydantic import BaseModel, EmailStr, Field


class CreateTeacher(BaseModel):
    """Schema for creating a new Teacher."""
    name: str = Field(..., description="The name of the teacher")
    email: EmailStr = Field(..., description="The email of the teacher, must be a valid email format")


class TeacherResponse(BaseModel):
    """Schema for returning Teacher details."""
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Allow ORM models to be converted to this schema
```