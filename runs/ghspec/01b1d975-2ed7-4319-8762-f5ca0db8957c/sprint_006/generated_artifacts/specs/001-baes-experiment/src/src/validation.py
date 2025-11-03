```python
# src/validation.py

from src.models import db, Course, Teacher  # Importing necessary models for validation
from sqlalchemy.exc import NoResultFound

def validate_course_exists(course_id: int) -> bool:
    """Check if a course exists in the database.

    Args:
        course_id (int): The ID of the course to check.

    Returns:
        bool: True if the course exists, else False.
    """
    return db.session.query(Course).filter(Course.id == course_id).count() > 0

def validate_teacher_exists(teacher_id: int) -> bool:
    """Check if a teacher exists in the database.

    Args:
        teacher_id (int): The ID of the teacher to check.

    Returns:
        bool: True if the teacher exists, else False.
    """
    return db.session.query(Teacher).filter(Teacher.id == teacher_id).count() > 0

def validate_teacher_assignment(course_id: int, teacher_id: int) -> str:
    """Validate the assignment of a teacher to a course.

    Args:
        course_id (int): The ID of the course.
        teacher_id (int): The ID of the teacher.

    Returns:
        str: Error message if validation fails, or success message if all checks pass.
    """
    if not validate_course_exists(course_id):
        return f"Validation Error: Course ID {course_id} does not exist."
    
    if not validate_teacher_exists(teacher_id):
        return f"Validation Error: Teacher ID {teacher_id} does not exist."
    
    return "Validation Successful: Teacher can be assigned to the course."
```