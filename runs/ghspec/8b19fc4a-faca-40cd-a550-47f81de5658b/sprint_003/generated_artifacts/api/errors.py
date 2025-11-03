```python
# api/errors.py

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# Define error codes for course-related errors.
ERROR_CODE_PREFIX = "E"

class CourseErrors:
    INVALID_NAME = (f"{ERROR_CODE_PREFIX}001", "Course name is required and cannot be empty.")
    INVALID_LEVEL = (f"{ERROR_CODE_PREFIX}002", "Course level is required and cannot be empty.")
    COURSE_NOT_FOUND = (f"{ERROR_CODE_PREFIX}003", "Course not found.")

def raise_course_error(error_type: str):
    """Raise a structured HTTP error based on the error type."""
    if error_type == "INVALID_NAME":
        error_code, message = CourseErrors.INVALID_NAME
        raise HTTPException(status_code=400, detail={"error": {"code": error_code, "message": message}})
    elif error_type == "INVALID_LEVEL":
        error_code, message = CourseErrors.INVALID_LEVEL
        raise HTTPException(status_code=400, detail={"error": {"code": error_code, "message": message}})
    elif error_type == "COURSE_NOT_FOUND":
        error_code, message = CourseErrors.COURSE_NOT_FOUND
        raise HTTPException(status_code=404, detail={"error": {"code": error_code, "message": message}})
    else:
        # Fallback for unknown error types
        raise HTTPException(status_code=500, detail={"error": {"code": "E999", "message": "An unexpected error occurred."}})

def handle_course_creation_errors(name: str, level: str):
    """Validate course inputs and raise appropriate errors if invalid."""
    if not name:
        raise_course_error("INVALID_NAME")
    if not level:
        raise_course_error("INVALID_LEVEL")
```