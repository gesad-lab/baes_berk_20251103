```python
from marshmallow import Schema, fields

class CourseSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    teacher = fields.Nested('TeacherSchema', only=('id', 'name', 'email'))  # Added teacher relationship

class TeacherSchema(Schema):
    id = fields.Int()
    name = fields.String(required=True)
    email = fields.Email(required=True)
```