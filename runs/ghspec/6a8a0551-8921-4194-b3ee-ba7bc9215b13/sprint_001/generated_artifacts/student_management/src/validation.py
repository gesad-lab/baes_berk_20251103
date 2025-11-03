```python
# student_management/src/validation.py

from flask import request, jsonify
from werkzeug.exceptions import BadRequest
from your_database_module import get_student_by_id  # Adjust import based on your DB module


def validate_student_id(student_id):
    """Validate the provided student ID.

    Args:
        student_id (str): The student ID to validate.

    Raises:
        BadRequest: If the student ID is invalid or not found.
    """
    # Check if the provided student ID is a valid integer
    try:
        student_id = int(student_id)
    except ValueError:
        raise BadRequest("Invalid student ID. It must be an integer.")

    # Check if student exists in the database
    student = get_student_by_id(student_id)
    if student is None:
        error_response = {
            "error": {
                "code": "E002",
                "message": "Student not found"
            }
        }
        raise BadRequest(jsonify(error_response))

    return student_id
```