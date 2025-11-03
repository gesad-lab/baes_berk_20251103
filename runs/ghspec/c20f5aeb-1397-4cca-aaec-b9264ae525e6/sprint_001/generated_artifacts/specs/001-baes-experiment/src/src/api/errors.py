```python
# src/api/errors.py

from flask import jsonify

class ApiError(Exception):
    """Custom exception class for API errors."""

    def __init__(self, message: str, code: str, status_code: int):
        """
        Initialize an ApiError instance.

        Args:
            message (str): A user-friendly error message.
            code (str): A unique error code for identification.
            status_code (int): The HTTP status code related to the error.
        """
        super().__init__(message)
        self.message = message
        self.code = code
        self.status_code = status_code

def create_error_response(error: ApiError):
    """
    Create a standardized error response format.

    Args:
        error (ApiError): The ApiError instance containing error details.

    Returns:
        tuple: A tuple containing the response data and the HTTP status code.
    """
    response = {
        "error": {
            "code": error.code,
            "message": error.message,
            "details": {}
        }
    }
    return jsonify(response), error.status_code

# Example usage for handling validation errors
def handle_validation_error(message: str):
    """Create a validation error response."""
    error = ApiError(message=message, code="E400", status_code=400)
    return create_error_response(error)

# Example usage for handling creation errors
def handle_creation_error(message: str):
    """Create a creation error response."""
    error = ApiError(message=message, code="E400", status_code=400)
    return create_error_response(error)

# You can extend the handlers to include other response types depending on business logic
```