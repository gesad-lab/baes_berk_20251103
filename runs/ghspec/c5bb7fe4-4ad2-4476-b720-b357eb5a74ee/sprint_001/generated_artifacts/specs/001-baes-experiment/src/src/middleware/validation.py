```python
from flask import request, jsonify
from werkzeug.exceptions import BadRequest

def validate_student_input(func):
    """
    Middleware to validate input for student-related API requests.

    :param func: The original function to be decorated.
    :return: The wrapped function that performs input validation.
    """
    def wrapper(*args, **kwargs):
        # Retrieve input data from request
        data = request.get_json()

        # Validate the presence of 'name' field
        if not data or 'name' not in data:
            error_response = {
                "error": {
                    "code": "E001",
                    "message": "Invalid input: 'name' is required.",
                    "details": {}
                }
            }
            raise BadRequest(description=jsonify(error_response))

        # Validate that the name is not empty
        name = data['name']
        if not isinstance(name, str) or not name.strip():
            error_response = {
                "error": {
                    "code": "E002",
                    "message": "Invalid input: 'name' must be a non-empty string.",
                    "details": {}
                }
            }
            raise BadRequest(description=jsonify(error_response))

        return func(*args, **kwargs)

    return wrapper
```