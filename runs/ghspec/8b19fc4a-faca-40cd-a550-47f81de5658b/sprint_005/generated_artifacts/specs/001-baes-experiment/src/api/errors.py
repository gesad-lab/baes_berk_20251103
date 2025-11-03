# api/errors.py

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# Define error codes for course-related errors.
ERROR_CODE_PREFIX = "E"

class CourseErrors:
    INVALID_NAME = (f"{ERROR_CODE_PREFIX}001", "Course name is required and cannot be empty.")
    INVALID_LEVEL = (f"{ERROR_CODE_PREFIX}002", "Course level is required and cannot be empty.")
    COURSE_NOT_FOUND = (f"{ERROR_CODE_PREFIX}003", "Course not found.")
    INVALID_COURSE_ASSOCIATION = (f"{ERROR_CODE_PREFIX}004", "Invalid course association.")

# Define error codes for teacher-related errors.
class TeacherErrors:
    MISSING_NAME = (f"{ERROR_CODE_PREFIX}005", "Teacher name is required.")
    MISSING_EMAIL = (f"{ERROR_CODE_PREFIX}006", "Teacher email is required.")
    DUPLICATE_EMAIL = (f"{ERROR_CODE_PREFIX}007", "This email is already registered.")

def structured_error_response(code: str, message: str, details: dict = None) -> JSONResponse:
    """Creates a standardized JSON error response."""
    error_response = {
        "error": {
            "code": code,
            "message": message,
            "details": details or {}
        }
    }
    return JSONResponse(status_code=400, content=error_response)

def handle_teacher_creation_errors(name: str, email: str) -> None:
    """Handles input validation for teacher creation."""
    if not name:
        raise HTTPException(status_code=400, detail=structured_error_response(*TeacherErrors.MISSING_NAME))
    
    if not email:
        raise HTTPException(status_code=400, detail=structured_error_response(*TeacherErrors.MISSING_EMAIL))

    # Here we would check if the email already exists; for now, let's mock that check
    # In a real scenario, you'd query the database.
    if email in ["john.doe@example.com"]:  # Replace with actual query
        raise HTTPException(status_code=400, detail=structured_error_response(*TeacherErrors.DUPLICATE_EMAIL))