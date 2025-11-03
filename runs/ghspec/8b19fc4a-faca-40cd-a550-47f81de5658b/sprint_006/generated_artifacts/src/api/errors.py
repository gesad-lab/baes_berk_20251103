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
    INVALID_COURSE_ASSOCIATION = (f"{ERROR_CODE_PREFIX}004", "Teacher cannot be assigned to a non-existing Course.")
    TEACHER_ALREADY_ASSIGNED = (f"{ERROR_CODE_PREFIX}005", "A Teacher is already assigned to this Course.")
    TEACHER_NOT_FOUND = (f"{ERROR_CODE_PREFIX}006", "Teacher not found.")
    
def raise_error(code: str, message: str):
    """Utility function to raise HTTPException with error details."""
    raise HTTPException(status_code=400, detail={"error": {"code": code, "message": message}})
```