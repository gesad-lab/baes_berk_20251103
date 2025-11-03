```python
# src/schemas.py

from marshmallow import Schema, fields, validates, ValidationError
from src.models import Teacher  # Assuming Teacher model is already defined in models.py
from src.database import get_db

class CourseSchema(Schema):
    """Schema for validating Course data."""
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    teacher_id = fields.Int(required=True)

    @validates('teacher_id')
    def validate_teacher_id(self, teacher_id):
        """Validate the teacher_id to ensure it's a valid Teacher."""
        db = get_db()
        teacher = db.session.query(Teacher).filter_by(id=teacher_id).first()
        if teacher is None:
            raise ValidationError(f"E001: Invalid teacher_id {teacher_id}: Teacher does not exist.")

class AssignTeacherSchema(Schema):
    """Schema for validating the request to assign a Teacher to a Course."""
    teacher_id = fields.Int(required=True)

    @validates('teacher_id')
    def validate_teacher_id(self, teacher_id):
        """Validate that the teacher_id exists in the Teacher table."""
        db = get_db()
        teacher = db.session.query(Teacher).filter_by(id=teacher_id).first()
        if teacher is None:
            raise ValidationError(f"E002: Invalid teacher_id {teacher_id}: Teacher does not exist.")

class CourseDetailSchema(Schema):
    """Schema for course detail response including teacher information."""
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    description = fields.Str(required=True)
    teacher = fields.Dict(keys=fields.Str(), values=fields.Str(), required=False)
```