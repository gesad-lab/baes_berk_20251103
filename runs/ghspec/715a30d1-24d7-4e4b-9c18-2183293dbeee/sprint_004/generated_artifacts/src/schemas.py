```python
from pydantic import BaseModel, conlist, validator
from typing import List, Optional
from models import Course  # Import existing Course model

class StudentEnrollmentSchema(BaseModel):
    student_id: int
    course_ids: conlist(int, min_items=1)  # Validates that at least one course ID is provided

    @validator('course_ids', each_item=True)
    def validate_course_id(cls, course_id):
        # Here you can include a check against the database or a list of valid course IDs
        # For demonstration, let's assume we have a function 'is_course_valid' to check this
        if not is_course_valid(course_id):  # A placeholder for actual validation logic
            raise ValueError(f'Course with ID {course_id} does not exist.')
        return course_id

class StudentDetailSchema(BaseModel):
    student_id: int
    name: str
    enrolled_courses: List[Course]  # Assuming Course model can be utilized directly

    class Config:
        orm_mode = True  # Allows Pydantic to read ORM models like SQLAlchemy
```
