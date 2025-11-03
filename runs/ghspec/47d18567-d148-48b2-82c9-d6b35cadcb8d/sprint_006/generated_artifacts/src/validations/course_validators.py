```python
# src/validations/course_validators.py
from fastapi import HTTPException
from src.db.models import Teacher  # Import Teacher model for validation

def validate_teacher_id(teacher_id: int):
    """
    Validates the provided teacher_id to ensure it corresponds to an existing teacher.

    Args:
        teacher_id (int): The ID of the teacher to validate.

    Raises:
        HTTPException: If the teacher_id does not correspond to an existing teacher,
                       raises a 400 Bad Request error with a descriptive message.
    """
    # Check if the teacher exists in the database
    exists = Teacher.query.filter(Teacher.id == teacher_id).first() is not None
    if not exists:
        raise HTTPException(
            status_code=400,
            detail={"code": "E001", "message": f"Invalid teacher_id: {teacher_id}. Teacher not found."}
        )

# You can add other validation functions here, preserving the existing code structure and functionality.
```