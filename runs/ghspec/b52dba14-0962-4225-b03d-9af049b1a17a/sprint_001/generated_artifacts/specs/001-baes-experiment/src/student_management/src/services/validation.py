```python
# student_management/src/services/validation.py

from flask import jsonify

def validate_student_name(name: str) -> None:
    """
    Validates the student's name.

    Parameters:
        name (str): The name of the student to validate.

    Raises:
        ValueError: If the name is empty or not a string.
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Invalid name: Name should be a non-empty string.")

def handle_validation_errors(func):
    """
    Decorator to handle validation errors in API endpoints.

    Parameters:
        func (Callable): The API endpoint function to decorate.

    Returns:
        Callable: The decorated function with error handling.
    """
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            # Return a 400 Bad Request response with the error message
            return jsonify({
                "error": {
                    "code": "E001",
                    "message": str(e)
                }
            }), 400
    return wrapper
```