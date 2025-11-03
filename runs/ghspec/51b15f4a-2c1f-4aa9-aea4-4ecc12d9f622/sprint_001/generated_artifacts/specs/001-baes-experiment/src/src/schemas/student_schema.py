from flask import Schema, fields, ValidationError

class StudentSchema(Schema):
    """
    Schema for validating Student input data and formatting responses.
    """

    id = fields.Int(dump_only=True)  # Auto-incremented ID
    name = fields.String(required=True, validate=lambda s: len(s) > 0, error_messages={"required": "Name is required."})
    age = fields.Int(required=True, error_messages={"required": "Age is required."})
    email = fields.Email(required=True, error_messages={"required": "Email is required."})

    @staticmethod
    def validate_student(data):
        """
        Validate the input data for a student.

        Args:
            data (dict): The input data to validate.

        Returns:
            dict: Validated data.

        Raises:
            ValidationError: If validation fails.
        """
        try:
            return StudentSchema().load(data)
        except ValidationError as err:
            # Log error details for debugging
            print(f"Validation error: {err.messages}")  # logging can be improved with a logging library
            raise err