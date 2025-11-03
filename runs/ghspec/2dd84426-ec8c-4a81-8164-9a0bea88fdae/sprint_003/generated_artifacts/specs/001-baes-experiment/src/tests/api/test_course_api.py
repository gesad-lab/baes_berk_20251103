```python
# src/validation/course_validation.py

from pydantic import BaseModel, Field, ValidationError

class CourseCreateSchema(BaseModel):
    """
    Schema for validating course creation input.
    """
    name: str = Field(..., title="Course Name", description="The name of the course. It must not be empty.")
    level: str = Field(..., title="Course Level", description="The level of the course, which is a required field.")

def validate_course_creation(data: dict) -> CourseCreateSchema:
    """
    Validate the input data for course creation.

    Args:
        data (dict): The input data to validate.

    Returns:
        CourseCreateSchema: The validated course creation data.

    Raises:
        ValidationError: If the validation fails, an exception will be raised with details.
    """
    try:
        return CourseCreateSchema(**data)  # Validate input and create an instance if valid
    except ValidationError as e:
        # Log the validation error here if necessary (not implementing logging in this task)
        raise ValueError(f"Input validation error: {e.errors()}")  # Raise a ValueError with details on failure
```