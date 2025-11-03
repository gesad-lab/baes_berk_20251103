```python
# src/validation/student_validation.py

from typing import Dict, Union

class StudentValidationError(Exception):
    """Custom exception raised for student validation errors."""
    pass

def validate_student_name(name: str) -> Union[None, Dict[str, str]]:
    """
    Validate the name of a student.
    
    :param name: The name of the student to validate. Must be a non-empty string.
    :return: None if valid, or a dictionary with error details if invalid.
    :raises StudentValidationError: Raised if unexpected issues occur during validation.
    
    Validation rules:
    - Name must be a non-empty string.
    - Name must not exceed 100 characters in length.
    """
    try:
        # Check if name is empty
        if not name:
            return {"code": "E001", "message": "Name cannot be empty."}
        
        # Check if name exceeds maximum length
        if len(name) > 100:
            return {"code": "E002", "message": "Name must not exceed 100 characters."}
        
        # Validation passed
        return None
    except Exception as e:
        # Raise a StudentValidationError if something unexpected happens
        raise StudentValidationError(f"Validation error occurred: {str(e)}")
```