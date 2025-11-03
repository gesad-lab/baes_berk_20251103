```python
from pydantic import BaseModel, conint, validator
from typing import List, Optional

class CourseSchema(BaseModel):
    course_id: int
    course_name: str
    level: str

class CourseAssociationRequestSchema(BaseModel):
    course_id: conint(gt=0)  # Ensure the course ID is a positive integer

    @validator('course_id')
    def validate_course_id(cls, course_id):
        # Placeholder for custom validation logic 
        # (e.g., check if course_id exists in the database)
        if not course_id:
            raise ValueError("Course ID is required")
        return course_id

class CourseAssociationResponseSchema(BaseModel):
    message: str
    course: CourseSchema

class StudentCoursesResponseSchema(BaseModel):
    courses: List[CourseSchema]
```