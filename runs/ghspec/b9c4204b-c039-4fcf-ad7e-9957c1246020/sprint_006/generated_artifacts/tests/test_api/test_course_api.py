```python
# File: src/schemas.py

from pydantic import BaseModel, validator, conint

class TeacherIdValidation(BaseModel):
    """Schema for validating teacher ID"""

    teacher_id: conint(gt=0)  # Ensure teacher_id is a positive integer

    @validator('teacher_id')
    def validate_teacher_id(cls, v):
        """Validate that the teacher_id is a positive integer"""
        if not isinstance(v, int) or v <= 0:
            raise ValueError('teacher_id must be a positive integer greater than 0')
        return v
```