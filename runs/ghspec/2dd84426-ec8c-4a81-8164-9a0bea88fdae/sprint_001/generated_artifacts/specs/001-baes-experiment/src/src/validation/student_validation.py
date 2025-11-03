```python
# src/validation/student_validation.py

from typing import Dict, Any

class StudentValidationError(Exception):
    """Custom exception for student validation errors."""
    def __init__(self, message: str):
        super().__init__(message)

def validate_student_creation(data: Dict[str, Any]) -> None:
    """Validates the input data for creating a student.
    
    Args:
        data (Dict[str, Any]): The input data to validate.
    
    Raises:
        StudentValidationError: If the input data is invalid.
    """
    # Check if the 'name' field is present and is a non-empty string
    if 'name' not in data:
        raise StudentValidationError("E001: Name field is required.")
    
    if not isinstance(data['name'], str) or not data['name'].strip():
        raise StudentValidationError("E002: Name must be a non-empty string.")
    
    # Add additional valid input checks if necessary
    # Currently, only checks for the `name` field as per the specifications
```