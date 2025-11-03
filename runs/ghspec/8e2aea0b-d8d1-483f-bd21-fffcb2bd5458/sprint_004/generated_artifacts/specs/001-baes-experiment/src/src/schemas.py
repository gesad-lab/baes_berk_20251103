```python
from marshmallow import Schema, fields, validate

class CourseSchema(Schema):
    """Schema for validating Course data."""
    course_id = fields.Int(required=True, description="The unique identifier for the course.")
    name = fields.Str(required=True, description="The name of the course.")
    level = fields.Str(required=True, validate=validate.OneOf(["beginner", "intermediate", "advanced"]),
                       description="The difficulty level of the course.")

class StudentSchema(Schema):
    """Schema for validating Student data including courses."""
    student_id = fields.Int(required=True, description="The unique identifier for the student.")
    name = fields.Str(required=True, description="The name of the student.")
    courses = fields.List(fields.Int(), description="List of course identifiers the student is enrolled in.")

    class Meta:
        # Additional Meta options can be set here if needed
        ordered = True
```