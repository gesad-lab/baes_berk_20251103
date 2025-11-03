```python
from pydantic import BaseModel, EmailStr
from typing import Optional

class TeacherBase(BaseModel):
    name: str  # Name of the teacher
    email: EmailStr  # Unique email of the teacher

class TeacherCreate(TeacherBase):
    pass  # Extra validation rules for creating a teacher can be added here later

class Teacher(TeacherBase):
    id: Optional[int] = None  # Database ID for the teacher, optional on creation

    class Config:
        orm_mode = True  # Enables compatibility with ORM models
```