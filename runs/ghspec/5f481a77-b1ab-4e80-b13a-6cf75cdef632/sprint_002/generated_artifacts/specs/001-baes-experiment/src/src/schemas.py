from marshmallow import Schema, fields

class StudentSchema(Schema):
    """Schema for serializing and validating Student data."""
    
    id = fields.Int(dump_only=True)  # Automatically generated identifier
    name = fields.Str(required=True)   # Student name, required field
    email = fields.Email(required=True) # Student email, required field with validation for email format

