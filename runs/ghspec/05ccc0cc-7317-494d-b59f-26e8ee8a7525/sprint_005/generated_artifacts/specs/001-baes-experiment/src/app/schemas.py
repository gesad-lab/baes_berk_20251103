```python
# app/schemas.py

from pydantic import BaseModel, EmailStr, Field


class TeacherBase(BaseModel):
    name: str = Field(..., description="The name of the teacher")
    email: EmailStr = Field(..., description="The email address of the teacher")


class TeacherCreate(TeacherBase):
    """Schema for creating a new teacher."""
    pass


class TeacherResponse(TeacherBase):
    id: int = Field(..., description="The unique identifier of the teacher")

    class Config:
        orm_mode = True  # This allows compatibility with the SQLAlchemy model
```
