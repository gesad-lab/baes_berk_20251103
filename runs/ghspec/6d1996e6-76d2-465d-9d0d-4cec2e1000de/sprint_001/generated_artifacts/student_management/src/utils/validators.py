```python
# student_management/src/utils/validators.py

from typing import Tuple, Union

class ValidationError(Exception):
    """Custom exception for handling validation errors."""
    pass

def validate_student_name(name: str) -> None:
    """Validate the student name.

    Args:
        name (str): The name of the student.

    Raises:
        ValidationError: If the name is empty or invalid.
    """
    if not isinstance(name, str):
        raise ValidationError("E001: Name must be a string")
    
    if not name.strip():
        raise ValidationError("E002: Name cannot be empty or whitespace")

def validate_student_id(student_id: Union[int, str]) -> None:
    """Validate the student ID.

    Args:
        student_id (Union[int, str]): The ID of the student.

    Raises:
        ValidationError: If the ID is not an integer or is negative.
    """
    if not isinstance(student_id, (int, str)):
        raise ValidationError("E003: Student ID must be an integer or string")
    if isinstance(student_id, str) and not student_id.isdigit():
        raise ValidationError("E004: Student ID must be a positive integer")
    if isinstance(student_id, int) and student_id < 1:
        raise ValidationError("E005: Student ID must be a positive integer")
```
