```python
from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import List

# Create a new router for teacher-related endpoints
router = APIRouter()

class TeacherResponse(BaseModel):
    """Schema for Teacher response validation."""
    id: int
    name: str
    email: EmailStr
    
    class Config:
        # This allows the use of ORM models directly as a response 
        orm_mode = True

# Example of how routes might look for teacher creation
@router.post("/teachers", response_model=TeacherResponse)
async def create_teacher(teacher: TeacherResponse):
    """
    Create a new Teacher.

    Args:
        teacher (TeacherResponse): The teacher's details.

    Returns:
        TeacherResponse: The created teacher's details.
    """
    # Logic to create a teacher will be implemented here
    pass

# Other route definitions can go here...
```