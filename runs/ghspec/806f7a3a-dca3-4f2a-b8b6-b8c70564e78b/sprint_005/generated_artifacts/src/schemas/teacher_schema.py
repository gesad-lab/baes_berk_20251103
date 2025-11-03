```python
from marshmallow import Schema, fields, ValidationError, validates
import re

class TeacherSchema(Schema):
    name = fields.String(required=True, error_messages={"required": "Name is required."})
    email = fields.String(required=True, error_messages={"required": "Email is required."})

    @validates('email')
    def validate_email(self, email):
        """Validate the email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        if not re.match(email_regex, email):
            raise ValidationError("Invalid email format.")

    class Meta:
        # This helps with the error messages that are returned in a structured format.
        strict = True
```