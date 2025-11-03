from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import logging

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

def create_error_response(error_detail: ErrorDetail):
    """Create a structured JSON error response.
    
    Args:
        error_detail (ErrorDetail): The details of the error.

    Returns:
        JSONResponse: A FastAPI JSON response object containing error details.
    """
    logger.error(f"Error occurred: {error_detail.message} (Code: {error_detail.code}, Details: {error_detail.details})")
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

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc: HTTPException):
    """Handle HTTP exceptions and return structured error responses.

    Args:
        request: The incoming request object.
        exc (HTTPException): The exception to handle.

    Returns:
        JSONResponse: A JSON response with the error details.
    """
    error_detail = ErrorDetail(code="E001", message=exc.detail)
    return create_error_response(error_detail)

@app.middleware("http")
async def add_exception_handling_middleware(request, call_next):
    """Middleware to handle unexpected exceptions globally.

    Args:
        request: The incoming request object.
        call_next: The next middleware or endpoint function.

    Returns:
        JSONResponse: A JSON response or forwarded request response.
    """
    try:
        response = await call_next(request)
    except Exception as e:
        logger.exception("Unhandled exception occurred")
        error_detail = ErrorDetail(code="E002", message="An unexpected error occurred.", details={"exception": str(e)})
        return create_error_response(error_detail)
    
    return response

# Define additional endpoints and logic as needed in future tasks
