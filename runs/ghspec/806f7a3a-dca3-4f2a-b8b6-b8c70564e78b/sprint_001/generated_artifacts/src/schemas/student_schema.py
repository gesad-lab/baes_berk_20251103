```python
from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    """
    Schema for validating Student data.
    """
    id = fields.Int(dump_only=True)  # Student ID, only for output
    name = fields.Str(required=True, validate=validate.Length(min=1), 
                       error_messages={"required": "Name is required."})

    class Meta:
        # Fields to be included in the output representation
        fields = ("id", "name")

# Additional code, such as validation functions or helper methods, can be added here.
```