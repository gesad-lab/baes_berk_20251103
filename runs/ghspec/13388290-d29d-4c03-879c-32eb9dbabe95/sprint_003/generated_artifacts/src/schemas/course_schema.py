```python
from marshmallow import Schema, fields, validate, ValidationError

class CourseSchema(Schema):
    """Schema for Course validation."""
    
    name = fields.String(required=True, validate=validate.Length(min=1), error_messages={
        "required": {"code": "E001", "message": "Name is a required field"},
        "invalid": {"code": "E002", "message": "Name must be a non-empty string"}
    })
    
    level = fields.String(required=True, validate=validate.Length(min=1), error_messages={
        "required": {"code": "E003", "message": "Level is a required field"},
        "invalid": {"code": "E004", "message": "Level must be a non-empty string"}
    })

    @staticmethod
    def validate(data):
        """Validate the incoming data for Course."""
        schema = CourseSchema()
        try:
            schema.load(data)  # Validate and deserialize input data
        except ValidationError as err:
            # Raise a structured error if validation fails
            return {"error": err.messages}, 400
        return None  # No errors

```