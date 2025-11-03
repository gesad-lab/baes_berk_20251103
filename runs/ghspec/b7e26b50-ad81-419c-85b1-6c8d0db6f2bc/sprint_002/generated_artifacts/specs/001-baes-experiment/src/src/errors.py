```python
# src/errors.py

from flask import jsonify
from typing import Any

def bad_request_error(message: str) -> Any:
    """Generate a standardized 400 Bad Request error response.

    Args:
        message (str): The error message to return.

    Returns:
        Any: A Flask response object with a 400 status code and JSON error message.
    """
    response = {
        "error": {
            "code": "E400",
            "message": message,
            "details": {}
        }
    }
    return jsonify(response), 400

def student_email_required() -> Any:
    """Return a 400 error response when the email is required but not provided.

    Returns:
        Any: A Flask response object with a 400 status code.
    """
    return bad_request_error("Email is required.")
```