```python
from marshmallow import Schema, fields, validate

class TeacherSchema(Schema):
    """Schema for validating Teacher data."""
    
    name = fields.String(required=True, validate=validate.Length(min=1), 
                         error_messages={"required": "Name is required."})
    email = fields.String(required=True, validate=validate.Email(), 
                          error_messages={"required": "Email is required."})

    class Meta:
        ordered = True  # Ensures order of fields in output
```