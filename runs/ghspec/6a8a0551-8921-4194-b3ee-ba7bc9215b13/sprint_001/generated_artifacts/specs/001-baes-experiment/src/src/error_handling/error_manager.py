```python
# src/error_handling/error_manager.py

from flask import jsonify

class ErrorResponse:
    """Class to generate standard error responses."""

    @staticmethod
    def validation_error(message: str) -> tuple:
        """Generate a validation error response.
        
        Args:
            message (str): The validation error message to be included in the response.

        Returns:
            tuple: A tuple containing the error response and an HTTP status code.
        """
        error_payload = {
            "error": {
                "code": "E001",  # Error Code for validation errors
                "message": message,
                "details": {}
            }
        }
        return jsonify(error_payload), 400  # HTTP status code for Bad Request

    @staticmethod
    def not_found_error(resource: str) -> tuple:
        """Generate a not found error response.
        
        Args:
            resource (str): The name of the resource that was not found (e.g., student).

        Returns:
            tuple: A tuple containing the error response and an HTTP status code.
        """
        error_payload = {
            "error": {
                "code": "E404",  # Error Code for not found errors
                "message": f"{resource.capitalize()} not found.",
                "details": {}
            }
        }
        return jsonify(error_payload), 404  # HTTP status code for Not Found

    @staticmethod
    def internal_server_error(message: str) -> tuple:
        """Generate an internal server error response.
        
        Args:
            message (str): A message describing the internal error that occurred.

        Returns:
            tuple: A tuple containing the error response and an HTTP status code.
        """
        error_payload = {
            "error": {
                "code": "E500",  # Error Code for internal server errors
                "message": "An unexpected error occurred.",
                "details": {
                    "internal_message": message
                }
            }
        }
        return jsonify(error_payload), 500  # HTTP status code for Internal Server Error
```
