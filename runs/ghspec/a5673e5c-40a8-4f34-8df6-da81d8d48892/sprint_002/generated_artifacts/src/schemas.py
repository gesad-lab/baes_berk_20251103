```python
from pydantic import BaseModel, EmailStr, Field

class StudentBase(BaseModel):
    """Base model for Student entity."""
    name: str = Field(..., description="The name of the student")
    age: int = Field(..., ge=0, description="The age of the student")
    email: EmailStr = Field(..., description="The email address of the student")

class StudentCreate(StudentBase):
    """Model for creating a new student."""
    pass

class StudentUpdate(BaseModel):
    """Model for updating an existing student's fields."""
    name: str = Field(None, description="The name of the student")
    age: int = Field(None, ge=0, description="The age of the student")
    email: EmailStr = Field(None, description="The email address of the student")

class StudentResponse(StudentBase):
    """Model for the response when retrieving a student."""
    id: int = Field(..., description="The unique identifier of the student")

    class Config:
        orm_mode = True
```