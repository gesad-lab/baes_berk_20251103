```python
from marshmallow import Schema, fields, validate

class AssignTeacherSchema(Schema):
    """Schema for validating the request to assign a teacher to a course."""
    teacher_id = fields.Int(required=True, 
                             validate=validate.Range(min=1, error="E001: Teacher ID must be a positive integer."))

class CourseDetailsSchema(Schema):
    """Schema for validating course details response."""
    course_id = fields.Int(required=True, 
                            validate=validate.Range(min=1, error="E002: Course ID must be a positive integer."))
    course_name = fields.Str(required=True, 
                              validate=validate.Length(min=1, error="E003: Course name cannot be empty."))
    assigned_teacher = fields.Dict(required=True, 
                                    keys=fields.String(), 
                                    values=fields.Any(
                                        fields.Int(required=True, 
                                                    validate=validate.Range(min=1, error="E004: Teacher ID must be a positive integer.")),
                                        fields.Str(required=True, 
                                                    validate=validate.Email(error="E005: Invalid email format.")),
                                        fields.Str(required=True, 
                                                    validate=validate.Length(min=1, error="E006: Name cannot be empty."))
                                    ))

```