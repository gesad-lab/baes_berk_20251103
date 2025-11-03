```python
from pydantic import BaseModel, EmailStr, ValidationError, Field

class StudentCreateSchema(BaseModel):
    """Schema for creating a new Student."""
    
    name: str = Field(..., description="Name of the student, required.")
    email: EmailStr = Field(..., description="Email of the student, must be a valid email format.")

class StudentResponseSchema(BaseModel):
    """Schema for the response of the student data."""
    
    id: int = Field(..., description="Unique identifier of the student.")
    name: str = Field(..., description="Name of the student.")
    email: EmailStr = Field(..., description="Email of the student.")
```