```python
from marshmallow import Schema, fields, validate, ValidationError

class CourseSchema(Schema):
    """Schema for course creation and validation."""
    
    name = fields.String(required=True, validate=validate.Length(min=1))
    level = fields.String(required=True, validate=validate.Length(min=1))

    @classmethod
    def validate_input(cls, data):
        """Validate input data for course creation.
        
        Args:
            data (dict): The input data to validate.

        Raises:
            ValidationError: If validation fails for missing fields.
        
        Returns:
            dict: Validated data.
        """
        try:
            return cls().load(data)
        except ValidationError as err:
            # Raise an error with details for the API response
            raise ValidationError({
                "error": {
                    "code": "E001",
                    "message": "Invalid input data",
                    "details": err.messages
                }
            })

# Example usage
# course_data = {'name': 'Mathematics', 'level': 'Intermediate'}
# validated_data = CourseSchema.validate_input(course_data)
```