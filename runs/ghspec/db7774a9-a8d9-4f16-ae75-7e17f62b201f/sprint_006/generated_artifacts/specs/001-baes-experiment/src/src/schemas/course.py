```python
# src/schemas/course.py

from pydantic import BaseModel, conint, constr
from typing import List, Optional

class CourseBase(BaseModel):
    name: constr(min_length=1)  # Course name cannot be empty

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    teacher_id: conint(strict=True)  # Ensure teacher_id is an integer and required

class CourseResponse(CourseBase):
    id: int  # Course ID for response
    teacher_id: Optional[int]  # Associated teacher ID
    teacher_name: Optional[str]  # Associated teacher's name

    class Config:
        orm_mode = True  # Enable compatibility with ORM models

class CourseListResponse(BaseModel):
    courses: List[CourseResponse]  # List of course responses
```