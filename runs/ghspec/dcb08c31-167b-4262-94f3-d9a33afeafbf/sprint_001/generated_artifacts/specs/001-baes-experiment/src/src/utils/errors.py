```python
import json
from flask import jsonify

class ErrorResponse:
    """Standardized error response format."""

    @staticmethod
    def create_error_response(code: str, message: str) -> dict:
        """Create a standardized error response.

        Args:
            code (str): Error code for debugging.
            message (str): User-friendly error message.

        Returns:
            dict: Standardized error response structure.
        """
        return {"error": {"code": code, "message": message}}


def handle_validation_error(field: str) -> dict:
    """Generates a standardized error response for validation errors.

    Args:
        field (str): The field that failed validation.

    Returns:
        dict: A standardized error response for validation failure.
    """
    return ErrorResponse.create_error_response(
        code="E001", 
        message=f"{field.capitalize()} cannot be empty"
    )


def handle_internal_error(message: str) -> dict:
    """Generates a standardized error response for internal errors.

    Args:
        message (str): Internal error message.

    Returns:
        dict: A standardized error response for internal errors.
    """
    return ErrorResponse.create_error_response(
        code="E500", 
        message="An internal server error occurred"
    )
```