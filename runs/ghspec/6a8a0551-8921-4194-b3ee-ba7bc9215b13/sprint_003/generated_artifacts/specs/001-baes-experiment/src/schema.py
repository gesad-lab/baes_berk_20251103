```python
from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    """Schema for validating course data."""
    
    id = fields.Int(dump_only=True)  # ID is auto-generated, so only for output
    name = fields.Str(required=True, validate=validate.Length(min=1))
    level = fields.Str(required=True, validate=validate.OneOf(["beginner", "intermediate", "advanced"]))
```

