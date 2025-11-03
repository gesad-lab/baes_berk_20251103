from marshmallow import Schema, fields, validate, ValidationError

class StudentSchema(Schema):
    """Schema for Student registration and validation."""
    id = fields.Integer(dump_only=True)  # ID is auto-generated, only for output
    name = fields.String(required=True, validate=validate.Length(min=1, error="Name is required."))

    @staticmethod
    def validate(data):
        """Static method for validating input data.
        
        Args:
            data (dict): The data to validate.
        
        Raises:
            ValidationError: If data is invalid.
        """
        errors = {}
        if not data.get('name'):
            errors['name'] = "Name is required."
        
        if errors:
            raise ValidationError({"error": {"code": "E001", "message": errors['name']}})

    class Meta:
        """Meta class for schema configuration."""
        ordered = True  # Maintain order of fields in serialized output