# api/errors.py

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# Define error codes for course-related errors.
ERROR_CODE_PREFIX = "E"

class CourseErrors:
    INVALID_NAME = (f"{ERROR_CODE_PREFIX}001", "Course name is required and cannot be empty.")
    INVALID_LEVEL = (f"{ERROR_CODE_PREFIX}002", "Course level is required and cannot be empty.")
    COURSE_NOT_FOUND = (f"{ERROR_CODE_PREFIX}003", "Course not found.")
    INVALID_COURSE_ASSOCIATION = (f"{ERROR_CODE_PREFIX}004", "Attempted to enroll in invalid courses.")

def raise_course_error(error_type: str):
    """Raises an HTTPException based on the error type provided."""
    if error_type == 'course_not_found':
        code, message = CourseErrors.COURSE_NOT_FOUND
    elif error_type == 'invalid_course_association':
        code, message = CourseErrors.INVALID_COURSE_ASSOCIATION
    else:
        code, message = CourseErrors.INVALID_NAME  # Default to INVALID_NAME for fallback

    # Log error for debugging and raise HTTP exception
    # Logging can be added here if needed
    raise HTTPException(status_code=400, detail={"error": {"code": code, "message": message}})