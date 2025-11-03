```python
from marshmallow import Schema, fields

class CourseSchema(Schema):
    """Schema for serializing and validating course data."""
    
    id = fields.Int(dump_only=True)  # Automatically include ID when dumping to JSON
    name = fields.Str(required=True)   # Course name is a required field
    level = fields.Str(required=True)  # Course level is a required field
```