```python
# validators/course_validator.py

from pydantic import BaseModel, validator, ValidationError

class CourseValidator(BaseModel):
    name: str
    level: str

    @validator('name')
    def name_must_not_be_empty(cls, value):
        """Ensure the name is a non-empty string."""
        if not value:
            raise ValueError("E001: Course name is required and cannot be empty.")
        return value

    @validator('level')
    def level_must_be_valid(cls, value):
        """Validate that the level is one of the allowed values."""
        valid_levels = {"Beginner", "Intermediate", "Advanced"}
        if value not in valid_levels:
            raise ValueError(f"E002: Level must be one of {valid_levels}.")
        return value
```