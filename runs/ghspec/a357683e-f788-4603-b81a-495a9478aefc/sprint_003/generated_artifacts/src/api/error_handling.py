```python
# src/api/error_handling.py

from flask import jsonify, make_response

class APIError(Exception):
    """Custom Exception class for API errors."""
    
    def __init__(self, message: str, status_code: int):
        super().__init__(message)
        self.message = message
        self.status_code = status_code

def handle_api_error(error: APIError):
    """Global error handler for the API."""
    response = {
        "error": {
            "code": f"E{error.status_code}",
            "message": error.message,
            "details": {}
        }
    }
    return make_response(jsonify(response), error.status_code)

def validate_course_fields(name: str, level: str):
    """Validates the course fields for creation or update.
    
    Args:
        name: The name of the course.
        level: The level of the course.

    Raises:
        APIError: If validation fails, an APIError is raised with the appropriate message.
    """
    if not name or not name.strip():
        raise APIError("Course name is required.", status_code=400)
    
    if not level or not level.strip():
        raise APIError("Course level is required.", status_code=400)

# Register the API error handler with Flask
def init_error_handling(app):
    """Initialize error handling for the Flask app."""
    app.register_error_handler(APIError, handle_api_error)
```