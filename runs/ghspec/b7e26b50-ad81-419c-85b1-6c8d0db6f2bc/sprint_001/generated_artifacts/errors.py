```python
import json
from flask import jsonify

class ErrorResponse:
    """Class to standardize error responses in the application."""

    @staticmethod
    def bad_request(message: str):
        """Return a 400 Bad Request error with a specified message.

        Args:
            message (str): The error message to include in the response.

        Returns:
            tuple: A tuple containing the response object and HTTP status code.
        """
        response = {
            "error": {
                "code": "E400",
                "message": message,
            }
        }
        return jsonify(response), 400

    @staticmethod
    def not_found(message: str):
        """Return a 404 Not Found error with a specified message.

        Args:
            message (str): The error message to include in the response.

        Returns:
            tuple: A tuple containing the response object and HTTP status code.
        """
        response = {
            "error": {
                "code": "E404",
                "message": message,
            }
        }
        return jsonify(response), 404

    @staticmethod
    def internal_server_error(message: str):
        """Return a 500 Internal Server Error with a specified message.

        Args:
            message (str): The error message to include in the response.

        Returns:
            tuple: A tuple containing the response object and HTTP status code.
        """
        response = {
            "error": {
                "code": "E500",
                "message": message,
            }
        }
        return jsonify(response), 500
```