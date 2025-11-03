```python
from marshmallow import Schema, fields

class TeacherSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

class CourseSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True, allow_none=True)
    teacher_id = fields.Int(load_only=True)  # Added for assignment
    teacher = fields.Nested(TeacherSchema, dump_only=True)  # Include Teacher details in serialization

    class Meta:
        fields = ('id', 'title', 'description', 'teacher_id', 'teacher')
        # Ensure fields are sorted in the output JSON, if necessary
        ordered = True
```