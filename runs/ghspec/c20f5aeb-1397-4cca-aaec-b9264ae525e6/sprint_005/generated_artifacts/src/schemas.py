```python
from marshmallow import Schema, fields, validate, ValidationError

class TeacherSchema(Schema):
    """Schema for validating Teacher data."""
    
    name = fields.String(required=True, validate=validate.Length(min=1), error_messages={
        "required": "E001: Name is required.",
        "null": "E002: Name cannot be null.",
        "validator_failed": "E003: Name cannot be empty.",
    })
    
    email = fields.Email(required=True, error_messages={
        "required": "E004: Email is required.",
        "invalid": "E005: Invalid email format."
    })

def validate_teacher_data(data):
    """Validate the input data for creating a Teacher."""
    schema = TeacherSchema()
    try:
        # Validate and deserialize input data
        return schema.load(data)
    except ValidationError as err:
        raise err  # Reraise validation error to be handled at a higher level
```