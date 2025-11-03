```python
import json
from flask import jsonify

class ErrorFormatter:
    """A utility class to format error messages for user-facing responses."""

    @staticmethod
    def format_validation_error(message: str) -> jsonify:
        """Format validation errors for user responses.
        
        Args:
            message (str): The error message describing the validation issue.
        
        Returns:
            jsonify: A structured JSON response containing the error code and message.
        """
        return jsonify({
            "error": {
                "code": "E400",
                "message": message,
                "details": {}
            }
        }), 400

    @staticmethod
    def format_not_found_error(resource: str, resource_id: str) -> jsonify:
        """Format not found errors for user responses.
        
        Args:
            resource (str): The type of resource (e.g., 'student').
            resource_id (str): The ID of the resource that was not found.
        
        Returns:
            jsonify: A structured JSON response indicating the resource was not found.
        """
        return jsonify({
            "error": {
                "code": "E404",
                "message": f"{resource.capitalize()} with ID '{resource_id}' was not found.",
                "details": {}
            }
        }), 404

    @staticmethod
    def format_internal_server_error(message: str) -> jsonify:
        """Format internal server errors for user responses.
        
        Args:
            message (str): A general message describing the internal error.
        
        Returns:
            jsonify: A structured JSON response for internal server errors.
        """
        return jsonify({
            "error": {
                "code": "E500",
                "message": "An unexpected error occurred. Please try again later.",
                "details": {
                    "internal_message": message
                }
            }
        }), 500
```