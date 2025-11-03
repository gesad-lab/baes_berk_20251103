```python
from pydantic import BaseModel, EmailStr, conint, constr
from typing import Optional

class TeacherSchema(BaseModel):
    """Schema for teacher validation."""
    name: constr(min_length=1, max_length=100)  # Name must be between 1 and 100 characters
    email: EmailStr  # Validate email format

class CourseAssignmentSchema(BaseModel):
    """Schema for validating course assignment requests."""
    teacher_id: Optional[conint(ge=1)]  # Teacher ID must be a positive integer, optional but used for assignment

class CourseDetailSchema(BaseModel):
    """Schema for fetching course details including teacher information."""
    course_id: int  # ID of the course
    teacher: Optional[TeacherSchema]  # Nested schema for teacher details (if assigned)
```
