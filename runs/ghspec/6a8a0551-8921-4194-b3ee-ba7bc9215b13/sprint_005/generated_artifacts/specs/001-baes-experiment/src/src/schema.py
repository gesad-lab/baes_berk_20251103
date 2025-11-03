```python
from marshmallow import Schema, fields, validate

class TeacherSchema(Schema):
    """Schema for validating Teacher data."""
    
    # Define the fields with their types and validation
    name = fields.String(required=True, validate=validate.Length(min=1), 
                         error_messages={"required": "Name is required."})
    email = fields.Email(required=True, 
                         error_messages={"required": "Email is required.", 
                                         "invalid": "Invalid email format."})

    class Meta:
        # Additional settings can be added here
        # e.g., strict=True to ensure no unknown fields are accepted
        strict = True
```