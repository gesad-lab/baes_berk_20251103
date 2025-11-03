```python
from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    """Validation schema for Course data."""
    
    id = fields.Int(required=True, validate=validate.Range(min=1))
    name = fields.Str(required=True)


class EnrollStudentSchema(Schema):
    """Validation schema for student course enrollment."""
    
    course_ids = fields.List(fields.Int(required=True), required=True)


class StudentDetailSchema(Schema):
    """Validation schema for retrieving student details."""
    
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    courses = fields.List(fields.Nested(CourseSchema))


class StudentCoursesSchema(Schema):
    """Validation schema for the relationship between students and courses."""
    
    student_id = fields.Int(required=True, validate=validate.Range(min=1))
    course_id = fields.Int(required=True, validate=validate.Range(min=1))
```