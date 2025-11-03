```python
from marshmallow import Schema, fields, post_load
from src.models import StudentCourse

class StudentCourseSchema(Schema):
    """Schema for serializing and validating StudentCourse relationships."""
    student_id = fields.Int(required=True)
    course_id = fields.Int(required=True)

    @post_load
    def create_student_course(self, data, **kwargs):
        """Creates a StudentCourse instance from validated data."""
        return StudentCourse(**data)
```