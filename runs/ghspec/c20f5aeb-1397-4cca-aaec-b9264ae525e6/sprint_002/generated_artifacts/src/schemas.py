```python
# src/schemas.py

import re
from marshmallow import Schema, fields, ValidationError, validate

class StudentSchema(Schema):
    """Schema for validating Student data."""
    
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Str(required=True, validate=validate.Email(error="Invalid email format."))

    @staticmethod
    def validate_email(email):
        """Validate that the email is a non-empty string conforming to standard email format."""
        if not email or not isinstance(email, str):
            raise ValidationError("Email must be a non-empty string.")
        # Further validation using regex for standard email pattern
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.com$'  # Adjust this regex as necessary
        if not re.match(email_regex, email):
            raise ValidationError("Email is not valid.")

# Include other schemas or classes if necessary...
```