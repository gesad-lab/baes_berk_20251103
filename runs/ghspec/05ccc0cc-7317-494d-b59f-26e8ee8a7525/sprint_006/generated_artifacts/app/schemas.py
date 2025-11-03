```python
# app/schemas.py

from pydantic import BaseModel, Field
from typing import Optional

class TeacherBase(BaseModel):
    """Base model for Teacher data."""
    name: str = Field(..., description="The teacher's name")

class TeacherCreate(TeacherBase):
    """Model for creating a new Teacher."""
    pass

class TeacherResponse(TeacherBase):
    """Model for returning Teacher information."""
    id: int = Field(..., description="The unique identifier for the teacher")

class CourseBase(BaseModel):
    """Base model for Course data."""
    title: str = Field(..., description="The title of the course")
    description: Optional[str] = Field(None, description="A brief description of the course")

class CourseCreate(CourseBase):
    """Model for creating a new Course."""
    teacher_id: Optional[int] = Field(None, description="The ID of the teacher assigned to the course")

class CourseResponse(CourseBase):
    """Model for returning Course information along with associated Teacher."""
    id: int = Field(..., description="The unique identifier for the course")
    teacher: Optional[TeacherResponse] = Field(None, description="Details of the assigned teacher")

class CourseAssignTeacher(BaseModel):
    """Model for assigning a teacher to a course."""
    teacher_id: int = Field(..., description="The ID of the teacher to assign to the course")

class ErrorResponse(BaseModel):
    """Model for error responses."""
    error: str = Field(..., description="Error message")
    code: str = Field(..., description="Error code")
```