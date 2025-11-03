```python
from marshmallow import Schema, fields, INCLUDE
from src.models import Course, Teacher

class CourseSchema(Schema):
    class Meta:
        # Include unknown fields to allow for dynamic fields
        unknown = INCLUDE

    course_id = fields.Int(required=True)
    name = fields.Str(required=True)
    level = fields.Str(required=True)
    teacher = fields.Nested('TeacherSchema', required=False)

class TeacherSchema(Schema):
    teacher_id = fields.Int(required=True)
    name = fields.Str(required=True)

class AssignTeacherSchema(Schema):
    # Schema for assigning a teacher to a course
    teacher_id = fields.Int(required=True, validate=lambda x: x > 0)  # Ensures positive integer

```