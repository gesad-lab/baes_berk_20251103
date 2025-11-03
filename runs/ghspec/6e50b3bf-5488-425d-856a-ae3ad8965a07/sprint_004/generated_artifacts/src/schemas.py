```python
# src/schemas.py

from marshmallow import Schema, fields, validate, ValidationError
from src.models import Student, Course

class EnrollmentSchema(Schema):
    """Validation schema for course enrollment requests."""
    
    student_id = fields.Int(required=True, validate=validate.Range(min=1))
    course_id = fields.Int(required=True, validate=validate.Range(min=1))

    def validate_student(self, student_id):
        """Validate that the student ID exists in the database."""
        if not Student.query.get(student_id):
            raise ValidationError(f"Student with ID {student_id} does not exist.", field_name='student_id')

    def validate_course(self, course_id):
        """Validate that the course ID exists in the database."""
        if not Course.query.get(course_id):
            raise ValidationError(f"Course with ID {course_id} does not exist.", field_name='course_id')

    # Overriding the `load` method to perform custom validation on student and course IDs.
    def load(self, *args, **kwargs):
        """Override load to include custom validators for student and course."""
        data = super().load(*args, **kwargs)
        self.validate_student(data['student_id'])
        self.validate_course(data['course_id'])
        return data
```