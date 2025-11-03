from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import logging
import re

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

class ErrorDetail:
    """Class representing structured error details."""
    
    def __init__(self, code: str, message: str, details: dict = None):
        self.code = code
        self.message = message
        self.details = details if details else {}

def create_error_response(error_detail: ErrorDetail) -> JSONResponse:
    """Creates a JSON response for errors."""
    logger.error(f"Error occurred: {error_detail.message} (Code: {error_detail.code})")
    return JSONResponse(
        status_code=400,
        content={
            "error": {
                "code": error_detail.code,
                "message": error_detail.message,
                "details": error_detail.details
            }
        }
    )

def validate_email(email: str) -> None:
    """Validates that the email is not empty and follows the correct format.
    
    Args:
        email (str): The email address to validate.
        
    Raises:
        ValueError: If the email is empty or does not match the valid format.
    """
    if not email:
        raise ValueError("Email field cannot be empty.")
    
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, email):
        raise ValueError("Invalid email format.")

@app.exception_handler(ValueError)
async def validation_exception_handler(request, exc: ValueError):
    """Handles validation errors by creating a structured JSON response."""
    error_detail = ErrorDetail(code="E001", message=str(exc))
    return create_error_response(error_detail)