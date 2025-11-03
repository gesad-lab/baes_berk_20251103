from marshmallow import Schema, fields, validate

class StudentRegistrationSchema(Schema):
    """Schema for validating student registration data."""

    # Email field with required and email format validation
    email = fields.Email(required=True, validate=validate.Email(error='Invalid email format.'))

    # Additional fields can be added here in future iterations
    # For example:
    # name = fields.Str(required=True, validate=validate.Length(min=1))
    # age = fields.Int(required=True, validate=validate.Range(min=0))

    class Meta:
        # We can specify additional configuration here if necessary
        # such as loading and dumping rules
        ordered = True  # Maintain the order of fields in serialization/deserialization
