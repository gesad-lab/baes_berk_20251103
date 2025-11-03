from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    """Schema for validating student data."""
    
    id = fields.Int(required=False)  # id is not required during creation
    name = fields.Str(required=True, validate=validate.Length(min=1, error="Name cannot be empty."))

# Optional: Define a schema for student creation response
class StudentResponseSchema(Schema):
    """Schema for student creation response."""
    
    id = fields.Int(required=True)
    name = fields.Str(required=True)