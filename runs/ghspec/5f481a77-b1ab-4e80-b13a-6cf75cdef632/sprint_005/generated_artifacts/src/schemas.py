```python
from marshmallow import Schema, fields

class TeacherSchema(Schema):
    """Schema for serializing and validating Teacher entities."""
    
    id = fields.Int(dump_only=True)  # Auto-generated ID for the Teacher
    name = fields.String(required=True)  # Name of the Teacher
    email = fields.Email(required=True)   # Email of the Teacher, must be valid email format
```