```python
from pydantic import BaseModel
from typing import List, Optional


class StudentCourseCreate(BaseModel):
    """Schema for creating a new student-course association."""
    student_id: int
    course_id: int


class StudentCourseResponse(BaseModel):
    """Schema for the response returned after associating a student with a course."""
    id: int
    student_id: int
    course_id: int

    class Config:
        orm_mode = True


class StudentCourseListResponse(BaseModel):
    """Schema for listing all student-course associations."""
    student_courses: List[StudentCourseResponse]
```