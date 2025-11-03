```python
from pydantic import BaseModel, constr, conint, validator
from typing import Optional


class TeacherAssignmentSchema(BaseModel):
    teacher_id: conint(gt=0)  # Ensure teacher_id is a positive integer
    course_id: conint(gt=0)    # Ensure course_id is a positive integer

    @validator('teacher_id')
    def validate_teacher_id(cls, value):
        if not is_valid_teacher_id(value):
            raise ValueError(f"E001: Teacher ID {value} does not exist")
        return value

    @validator('course_id')
    def validate_course_id(cls, value):
        if not is_valid_course_id(value):
            raise ValueError(f"E002: Course ID {value} does not exist")
        return value

def is_valid_teacher_id(teacher_id: int) -> bool:
    # Placeholder for actual validation logic
    return True

def is_valid_course_id(course_id: int) -> bool:
    # Placeholder for actual validation logic
    return True
```