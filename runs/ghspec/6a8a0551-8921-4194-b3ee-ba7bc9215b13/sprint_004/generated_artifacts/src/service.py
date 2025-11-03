```python
# src/service.py

from marshmallow import Schema, fields, ValidationError, post_load
from api.models import Course  # Assuming the Course model is defined in models.py
from api import db  # Assuming this is where the db instance is defined

class CourseAssignmentSchema(Schema):
    """Schema for validating course assignments to students."""

    course_ids = fields.List(fields.Int(required=True), required=True)

    @post_load
    def validate_course_ids(self, data, **kwargs):
        """Validate the course IDs provided in the request."""
        course_ids = data['course_ids']
        
        # Check if each course ID exists in the database
        existing_courses = Course.query.filter(Course.id.in_(course_ids)).all()
        if len(existing_courses) != len(course_ids):
            # Create a set of existing and provided IDs for comparison
            existing_ids = {course.id for course in existing_courses}
            invalid_ids = [course_id for course_id in course_ids if course_id not in existing_ids]
            raise ValidationError({
                "error": {
                    "code": "E002",
                    "message": "One or more course IDs are invalid.",
                    "details": {"invalid_ids": invalid_ids}
                }
            })
        
        return data

# Usage example:
# from src.service import CourseAssignmentSchema
# schema = CourseAssignmentSchema()
# result = schema.load({"course_ids": [1, 2, 3]})  # Validate input
```