```python
# src/schemas/teacher_schema.py
from pydantic import BaseModel, EmailStr, Field, constr

class TeacherCreate(BaseModel):
    """Schema for creating a new Teacher."""
    
    name: constr(min_length=1) = Field(..., description="The name of the teacher, must not be empty.")
    email: EmailStr = Field(..., description="The email of the teacher, must be a valid email format.")

    class Config:
        """Pydantic configuration."""
        schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john.doe@example.com"
            }
        }
```