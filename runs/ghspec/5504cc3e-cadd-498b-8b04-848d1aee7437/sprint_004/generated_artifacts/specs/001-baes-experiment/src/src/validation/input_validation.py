```python
# src/validation/input_validation.py

from werkzeug.exceptions import BadRequest

def validate_student_id(student_id: int) -> None:
    """Validate the given student ID.
    
    Args:
        student_id (int): The ID of the student to validate.

    Raises:
        BadRequest: If the student ID is not a positive integer.
    """
    if not isinstance(student_id, int) or student_id <= 0:
        raise BadRequest(f"E001: Invalid student ID. Received: {student_id}. Must be a positive integer.")

def validate_course_id(course_id: int) -> None:
    """Validate the given course ID.
    
    Args:
        course_id (int): The ID of the course to validate.

    Raises:
        BadRequest: If the course ID is not a positive integer.
    """
    if not isinstance(course_id, int) or course_id <= 0:
        raise BadRequest(f"E002: Invalid course ID. Received: {course_id}. Must be a positive integer.")
```
