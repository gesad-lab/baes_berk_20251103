```python
from pydantic import BaseModel, EmailStr, Field

class TeacherCreateSchema(BaseModel):
    """Schema for creating a new Teacher."""
    
    name: str = Field(..., title="Name of the Teacher", max_length=100)
    email: EmailStr = Field(..., title="Email of the Teacher")

class TeacherResponseSchema(BaseModel):
    """Schema for the response when retrieving a Teacher."""
    
    id: int
    name: str
    email: EmailStr

    class Config:
        """Pydantic configuration."""
        orm_mode = True  # Allows compatibility with SQLAlchemy models
```