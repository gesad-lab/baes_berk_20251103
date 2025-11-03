```python
# src/validations/course_validators.py

from fastapi import HTTPException, status
from pydantic import BaseModel, Field, validator

class CourseCreateRequest(BaseModel):
    """Model for creating a new course request."""
    name: str = Field(..., min_length=1, description="The name of the course.")
    level: str = Field(..., min_length=1, description="The level of the course.")
    
    @validator('name', 'level')
    def check_non_empty(cls, value):
        """Check that the fields name and level are non-empty."""
        if not value.strip():
            raise ValueError("Field must not be empty.")
        return value

def validate_course_creation(request: CourseCreateRequest):
    """
    Validates the course creation request.

    Args:
        request (CourseCreateRequest): Course creation request data.

    Raises:
        HTTPException: If validation fails.
    """
    try:
        request_dict = request.dict()  # Validate and convert to dictionary
    except ValueError as e:
        # Raise HTTP Exception for invalid input
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E001", "message": str(e)}}
        )
    
    return request_dict
```