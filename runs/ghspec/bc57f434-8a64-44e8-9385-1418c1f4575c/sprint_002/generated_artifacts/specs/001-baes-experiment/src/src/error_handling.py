```python
# src/error_handling.py

from fastapi import HTTPException, status
import re

# Custom exception for handling client errors with a specific message format
class ClientError(HTTPException):
    def __init__(self, detail: str):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

def validate_email(email: str) -> None:
    """
    Validates the provided email format.
    
    :param email: The email address to validate.
    :raises ClientError: If the email format is invalid.
    """
    # Regex pattern for validating an email format
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    if not re.match(email_regex, email):
        raise ClientError("E002: Invalid email format. Please provide a valid email.")

def validate_student_data(name: str, email: str) -> None:
    """
    Validate student creation data.
    
    :param name: The name of the student.
    :param email: The email address of the student.
    :raises ClientError: If validation fails.
    """
    if not name:
        raise ClientError("E001: Name is required.")
    
    if not email:
        raise ClientError("E002: Email is required.")

    validate_email(email)

def handle_error(e: Exception) -> dict:
    """
    Handles exceptions and formats error responses.
    
    :param e: The exception raised.
    :return: A dictionary with error information.
    """
    if isinstance(e, ClientError):
        return {"error": {"code": e.detail.split(":")[0], "message": e.detail}}
    
    # For other exceptions, log and return a generic error message
    return {"error": {"code": "E999", "message": "An unexpected error occurred."}}
```