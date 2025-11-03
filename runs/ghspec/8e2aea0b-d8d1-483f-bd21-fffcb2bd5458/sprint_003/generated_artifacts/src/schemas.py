from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    """Schema for Course entity validation."""
    
    name = fields.String(required=True, validate=validate.Length(min=1), error_messages={
        "required": "E001: Course name is required.",
        "null": "E002: Course name cannot be null."
    })
    
    level = fields.String(required=True, validate=validate.Length(min=1), error_messages={
        "required": "E003: Course level is required.",
        "null": "E004: Course level cannot be null."
    })