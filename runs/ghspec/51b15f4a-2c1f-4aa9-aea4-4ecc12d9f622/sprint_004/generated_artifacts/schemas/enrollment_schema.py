```python
# schemas/enrollment_schema.py

from marshmallow import Schema, fields, validates, ValidationError

class EnrollmentSchema(Schema):
    """
    Schema for validating enrollment requests.
    
    This schema checks that incoming requests to enroll a student in courses
    include both a student ID and an array of course IDs, ensuring they are
    of the correct type and format.
    """
    student_id = fields.Int(required=True, description="The ID of the student to enroll.")
    course_ids = fields.List(fields.Int(), required=True, description="Array of course IDs to enroll the student in.")

    @validates('student_id')
    def validate_student_id(self, value):
        """Validate that the student ID is a positive integer."""
        if value <= 0:
            raise ValidationError("Invalid student_id: Must be a positive integer.")

    @validates('course_ids')
    def validate_course_ids(self, value):
        """Validate that the course IDs are positive integers."""
        if not value or not all(isinstance(course_id, int) and course_id > 0 for course_id in value):
            raise ValidationError("Invalid course_ids: Must be a non-empty list of positive integers.")
```