```python
from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    """Schema for validating Course data."""
    
    id = fields.Int(dump_only=True)  # Automatically generated ID
    name = fields.Str(required=True, validate=validate.Length(min=1), error_messages={
        "required": {"code": "E001", "message": "name is required."},
        "null": {"code": "E002", "message": "name cannot be null."}
    })
    level = fields.Str(required=True, validate=validate.Length(min=1), error_messages={
        "required": {"code": "E003", "message": "level is required."},
        "null": {"code": "E004", "message": "level cannot be null."}
    })
```