```python
# src/services/input_validation.py

from marshmallow import Schema, fields, ValidationError

class StudentSchema(Schema):
    """Schema for validating student data."""
    name = fields.Str(required=True, error_messages={"required": "E001: Name is required."})

def validate_student_data(data):
    """Validate student creation data.

    Args:
        data (dict): Incoming student data containing the student fields.

    Raises:
        ValidationError: If the data is invalid.

    Returns:
        dict: Validated student data.
    """
    schema = StudentSchema()
    try:
        validated_data = schema.load(data)
    except ValidationError as err:
        # Log error for debugging purposes (could enhance with a proper logging framework)
        print(f"Validation error: {err.messages}")  # This should be replaced with a logging call
        raise
    return validated_data
```