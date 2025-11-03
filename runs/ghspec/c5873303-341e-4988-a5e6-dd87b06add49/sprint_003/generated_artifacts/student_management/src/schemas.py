```python
from pydantic import BaseModel, constr
from typing import List, Optional

class CourseCreate(BaseModel):
    """Schema for creating a new course."""
    name: constr(min_length=1, max_length=100)  # Name must be between 1 and 100 characters
    level: constr(min_length=1, max_length=50)  # Level must be between 1 and 50 characters

class CourseResponse(BaseModel):
    """Schema for representing a course response."""
    id: int  # Assuming the API will return an ID for the course
    name: str
    level: str

class CoursesListResponse(BaseModel):
    """Schema for representing a list of courses."""
    courses: List[CourseResponse]

    class Config:
        orm_mode = True  # This allows Pydantic to parse SQLAlchemy models directly
```