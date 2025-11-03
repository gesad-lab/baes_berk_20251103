```python
from flask import jsonify

def create_error_response(code: str, message: str) -> dict:
    """
    Create a structured error response.

    Args:
        code (str): The error code.
        message (str): A descriptive error message.

    Returns:
        dict: A JSON serializable error response.
    """
    return jsonify({
        "error": {
            "code": code,
            "message": message
        }
    }), 400  # HTTP status code for Bad Request


def create_success_response(data: dict, message: str) -> dict:
    """
    Create a structured success response.

    Args:
        data (dict): The data to include in the response.
        message (str): A descriptive success message.

    Returns:
        dict: A JSON serializable success response.
    """
    return jsonify({
        "data": data,
        "message": message
    }), 201  # HTTP status code for Created


def create_not_found_response(message: str) -> dict:
    """
    Create a structured not found response.

    Args:
        message (str): A descriptive message indicating the resource was not found.

    Returns:
        dict: A JSON serializable not found response.
    """
    return jsonify({
        "error": {
            "code": "E002",
            "message": message
        }
    }), 404  # HTTP status code for Not Found
```