```python
from pydantic import BaseModel, Field, ValidationError


class StudentCreateValidator(BaseModel):
    """Validator for creating a new Student."""
    name: str = Field(..., min_length=1, description="The name of the student. Must be a non-empty string.")

    @classmethod
    def validate_student_creation(cls, student_data):
        """
        Validate the incoming student creation data.

        Args:
            student_data (dict): The incoming data for creating a student.

        Raises:
            ValueError: If the input validation fails.
        """
        try:
            # Validate input by creating an instance of the StudentCreateValidator
            cls(**student_data)
        except ValidationError as e:
            # Extract the first error message to return
            raise ValueError(f"Invalid input for creating a student: {e.errors()}") from e


# Example usage of the validator:
if __name__ == "__main__":
    input_data = {"name": "John Doe"}
    try:
        StudentCreateValidator.validate_student_creation(input_data)
        print("Validation succeeded.")
    except ValueError as ve:
        print(ve)
```