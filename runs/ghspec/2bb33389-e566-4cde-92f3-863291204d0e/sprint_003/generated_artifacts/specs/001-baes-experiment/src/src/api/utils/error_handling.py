```python
# src/api/utils/error_handling.py

from fastapi import HTTPException
from pydantic import BaseModel, validator

class CourseCreateRequest(BaseModel):
    name: str
    level: str

    @validator('name')
    def validate_name(cls, v):
        if not v:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "E001", "message": "The name field is required."}}
            )
        return v

    @validator('level')
    def validate_level(cls, v):
        if not v:
            raise HTTPException(
                status_code=400,
                detail={"error": {"code": "E002", "message": "The level field is required."}}
            )
        return v


def handle_course_creation(request_body: dict):
    """
    Handles the course creation request by validating the input and
    throwing appropriate HTTP exceptions for missing fields.

    Parameters:
    - request_body (dict): The JSON body from the request containing 'name' and 'level'.

    Raises:
    HTTPException: If 'name' or 'level' is missing from the request_body.
    """

    try:
        # Validate the incoming request body
        course_request = CourseCreateRequest(**request_body)
        # Further processing to create the course can be added here
        return course_request
    except ValidationError as e:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E003", "message": str(e)}}
        )
```
