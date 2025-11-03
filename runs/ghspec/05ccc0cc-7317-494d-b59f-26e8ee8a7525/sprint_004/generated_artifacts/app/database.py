```python
from pydantic import BaseModel, conint
from typing import List, Optional

class CourseBase(BaseModel):
    id: conint(ge=1)  # Course ID should be a positive integer

class EnrollStudentRequest(BaseModel):
    course_id: conint(ge=1)  # Required course ID, must be a positive integer

class StudentResponse(BaseModel):
    id: conint(ge=1)  # Student ID should be a positive integer
    name: str  # Student's name
    courses: List[CourseBase]  # List of courses the student is enrolled in

class ErrorResponse(BaseModel):
    error: str  # Error message
    code: str  # Error code for debugging
```