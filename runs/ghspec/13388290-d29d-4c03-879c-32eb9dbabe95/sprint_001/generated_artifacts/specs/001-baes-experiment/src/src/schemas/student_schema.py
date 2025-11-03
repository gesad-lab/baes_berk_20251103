```python
from marshmallow import Schema, fields, validate, ValidationError


class StudentSchema(Schema):
    """Schema for validating student data."""

    id = fields.Int(dump_only=True)  # Automatically populated by the database
    name = fields.Str(required=True, validate=validate.Length(min=1))  # Name is required

    class Meta:
        # Define the JSON serialization formats and error message formats
        ordered = True  # Maintain order of fields


def get_student_response(student):
    """Return a JSON response for retrieving a student."""
    if student:
        return {
            "id": student.id,
            "name": student.name
        }, 200  # HTTP 200 OK
    else:
        return {
            "error": {
                "code": "E002",
                "message": "Student not found"
            }
        }, 404  # HTTP 404 Not Found


def create_student_response(student):
    """Return a JSON response for creating a student."""
    return {
        "id": student.id,
        "name": student.name
    }, 201  # HTTP 201 Created


def error_response(error_code: str, message: str):
    """Return a standardized error response."""
    return {
        "error": {
            "code": error_code,
            "message": message
        }
    }, 400  # HTTP 400 Bad Request


def validate_student_input(data):
    """Validate the student input data and return errors if invalid.

    Args:
        data (dict): Input data containing student information.

    Returns:
        tuple: A tuple containing response object (dict) and HTTP status code (int).
    """
    try:
        StudentSchema().load(data)  # Validate input
    except ValidationError as err:
        return error_response("E001", "Name is required")  # Handle validation error

    return None  # No errors


# Add additional functions for retrieving a student and other logic as needed
```