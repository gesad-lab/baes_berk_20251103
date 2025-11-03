```python
# models.py

from pydantic import BaseModel, EmailStr, Field
from typing import List

class TeacherCreate(BaseModel):
    """Model for creating a new teacher."""
    
    name: str = Field(..., description="The name of the teacher.")
    email: EmailStr = Field(..., description="The email address of the teacher.")

class Teacher(TeacherCreate):
    """Model representing a teacher including database ID."""
    
    id: int

class TeacherList(BaseModel):
    """Model for listing teachers."""
    
    teachers: List[Teacher]
```