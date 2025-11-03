```python
from marshmallow import Schema, fields, validates, ValidationError

class StudentSchema(Schema):
    """Schema for Student model to validate and serialize data."""
    
    id = fields.Int(dump_only=True)  # Auto-generated ID field for output
    name = fields.Str(required=True)  # Required name field
    email = fields.Str(required=True)  # Required email field

    @validates('email')
    def validate_email(self, email):
        """Validate that the email is a valid format."""
        if not isinstance(email, str) or '@' not in email:
            raise ValidationError('Invalid email format.', code='E002')
    
    @validates('name')
    def validate_name(self, name):
        """Validate that the name is a non-empty string."""
        if not name.strip():
            raise ValidationError('Name field cannot be empty.', code='E001')
```