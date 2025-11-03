```python
from pydantic import BaseModel, conlist
from typing import List, Optional

class CourseEnrollmentRequest(BaseModel):
    """Schema for enrolling a student in one or more courses."""
    course_ids: conlist(int, min_items=1)  # List of course IDs, must have at least one

class CourseResponse(BaseModel):
    """Schema for returning course details associated with a student."""
    id: int
    name: str
    level: str

class StudentDetailResponse(BaseModel):
    """Schema for returning detailed information about a student."""
    id: int
    name: str
    enrolled_courses: List[CourseResponse]  # List of courses associated with the student

class EnrollmentConfirmationResponse(BaseModel):
    """Schema for confirming successful enrollment of a student."""
    message: str  # Confirmation message indicating successful enrollment
```