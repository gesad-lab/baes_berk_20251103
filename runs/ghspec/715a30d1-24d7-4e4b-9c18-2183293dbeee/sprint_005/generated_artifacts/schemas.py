```python
from pydantic import BaseModel, EmailStr, Field

class TeacherCreateRequest(BaseModel):
    """Schema for creating a new Teacher."""
    name: str = Field(..., title="Name of the teacher", max_length=100)
    email: EmailStr = Field(..., title="Email of the teacher")

class TeacherResponse(BaseModel):
    """Schema for responding with teacher details."""
    id: int
    name: str
    email: EmailStr

    class Config:
        orm_mode = True  # Enable ORM mode to read data as dictionaries
```