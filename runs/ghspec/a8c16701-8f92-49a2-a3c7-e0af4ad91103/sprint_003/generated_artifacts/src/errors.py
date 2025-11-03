```python
# src/errors.py

from fastapi import HTTPException
from starlette.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND

class CourseError(Exception):
    """Custom exception for course-related errors."""
    pass

def raise_if_missing_fields(name: str, level: str):
    """
    Raise an HTTPException if either the name or level is missing.
    
    Parameters:
        name (str): The name of the course.
        level (str): The level of the course.
    
    Raises:
        HTTPException: If name or level is missing.
    """
    if not name:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E001", "message": "Course name is required."}}
        )
    
    if not level:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST,
            detail={"error": {"code": "E002", "message": "Course level is required."}}
        )

def raise_if_course_not_found(course_id: int):
    """
    Raise an HTTPException if a course is not found by its ID.
    
    Parameters:
        course_id (int): The unique identifier of the course.
    
    Raises:
        HTTPException: If the course is not found.
    """
    # Here we assume a function `get_course` is defined elsewhere that tries to fetch the course
    # If it returns None, it means the course does not exist
    if get_course(course_id) is None:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND,
            detail={"error": {"code": "E003", "message": "Course not found."}}
        )
```
