```python
from pydantic import BaseModel, Field
from typing import Optional

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None

class CourseCreate(CourseBase):
    """
    Schema for creating a new Course. Inherits from CourseBase
    and includes required fields for course creation.
    """
    teacher_id: Optional[int] = Field(None, description="ID of the teacher associated with the course.")

class CourseUpdate(CourseBase):
    """
    Schema for updating an existing Course. Allows for the
    updating of course attributes including teacher association.
    """
    teacher_id: Optional[int] = Field(None, description="ID of the teacher associated with the course.")

class CourseResponse(CourseBase):
    id: int
    teacher_id: Optional[int] = Field(None, description="ID of the teacher associated with the course.")
    
    class Config:
        orm_mode = True
```
