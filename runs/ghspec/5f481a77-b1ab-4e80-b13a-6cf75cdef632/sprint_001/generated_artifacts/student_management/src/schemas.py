```python
from marshmallow import Schema, fields

class Student:
    """Represents a student with an id and name."""

    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name


class StudentSchema(Schema):
    """Marshmallow schema for serializing/deserializing Student data."""
    
    id = fields.Int(required=True)  # Student ID
    name = fields.Str(required=True)  # Student name
```