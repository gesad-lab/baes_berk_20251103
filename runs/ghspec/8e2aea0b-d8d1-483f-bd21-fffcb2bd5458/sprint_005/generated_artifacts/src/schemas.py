```python
# src/schemas.py

from marshmallow import Schema, fields, validate

class StudentSchema(Schema):
    student_id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Str(required=True, validate=validate.Email())
    # Add other student fields as necessary

class CourseSchema(Schema):
    course_id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1))
    # Add other course fields as necessary

class TeacherSchema(Schema):
    """Schema for validating teacher creation and retrieval."""

    teacher_id = fields.Int(dump_only=True)  # Auto-generated ID by the database
    name = fields.Str(required=True, validate=validate.Length(min=1))  # Required field for teacher's name
    email = fields.Str(required=True, validate=validate.Email())  # Required field for teacher's email
```