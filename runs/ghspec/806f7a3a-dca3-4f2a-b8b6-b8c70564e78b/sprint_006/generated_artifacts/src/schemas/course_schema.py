```python
from marshmallow import Schema, fields, validate, post_load
from models.course import Course

class CourseSchema(Schema):
    """Schema for Course validation and serialization."""
    
    id = fields.Int(required=True)  # Course ID is required
    name = fields.Str(required=True, validate=validate.Length(min=1))  # Course name is required
    teacher_id = fields.Int(required=False, allow_none=True)  # Teacher ID is optional and can be None

    @post_load
    def make_course(self, data, **kwargs):
        """Create a Course instance from the validated data."""
        return Course(**data)

    @classmethod
    def validate_teacher_id(cls, teacher_id):
        """Validate that the provided teacher_id corresponds to an existing Teacher."""
        # This method should include logic to check if the teacher_id exists in the Teacher model.
        # This is a placeholder for the actual validation.
        return True if teacher_id else False

    @validates('teacher_id')
    def validate_teacher_exists(self, teacher_id):
        """Ensure the teacher_id points to an existing Teacher."""
        if teacher_id is not None and not self.validate_teacher_id(teacher_id):
            raise ValidationError("Invalid teacher_id: Teacher does not exist.")
```