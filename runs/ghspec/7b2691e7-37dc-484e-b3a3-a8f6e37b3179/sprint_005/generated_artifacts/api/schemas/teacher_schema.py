```python
from marshmallow import Schema, fields, validates, ValidationError
from models.teacher import Teacher  # Assuming the Teacher model is defined in models.teacher

class TeacherSchema(Schema):
    """Schema to validate Teacher data, ensuring that the teacher's name and email are properly formatted."""
    
    id = fields.Int(dump_only=True)  # Unique identifier for the teacher; only included in output
    name = fields.Str(required=True)  # Name of the teacher; cannot be empty
    email = fields.Str(required=True)  # Email of the teacher; cannot be empty
    
    @validates('email')
    def validate_email(self, email):
        """Validate that the email is in a proper format."""
        if '@' not in email or '.' not in email.split('@')[-1]:
            raise ValidationError("Invalid email format.")  # Raise an error for invalid email

    @validates('name')
    def validate_name(self, name):
        """Validate that the teacher's name is not empty or too long."""
        if len(name) == 0:
            raise ValidationError("Name cannot be empty.")  # Raise an error for empty name
        if len(name) > 100:
            raise ValidationError("Name cannot exceed 100 characters.")  # Raise an error for long names
```