```python
# File: src/errors.py

from fastapi import HTTPException
from fastapi.responses import JSONResponse

# Custom error codes
ERROR_CODES = {
    "E001": "Email field is required.",
}

def handle_missing_email() -> HTTPException:
    """
    Create an HTTP exception for missing email field

    Returns:
        HTTPException: An exception to be raised when the email is missing
    """
    return HTTPException(
        status_code=400,
        detail={
            "error": {
                "code": "E001",
                "message": ERROR_CODES["E001"],
                "details": {}
            }
        }
    )

def handle_invalid_request(message: str) -> HTTPException:
    """
    Create an HTTP exception for generic invalid requests

    Args:
        message (str): Custom message describing the error

    Returns:
        HTTPException: An exception to be raised for invalid requests
    """
    return HTTPException(
        status_code=400,
        detail={
            "error": {
                "code": "E002",
                "message": message,
                "details": {}
            }
        }
    )

def handle_internal_error(message: str) -> HTTPException:
    """
    Create an HTTP exception for internal server errors

    Args:
        message (str): Custom message describing the internal error

    Returns:
        HTTPException: An exception to be raised for internal server errors
    """
    return HTTPException(
        status_code=500,
        detail={
            "error": {
                "code": "E003",
                "message": message,
                "details": {}
            }
        }
    )

# Additional error handling functions can be added as needed
```