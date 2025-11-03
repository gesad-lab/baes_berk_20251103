```python
# src/validations.py

from flask_sqlalchemy import SQLAlchemy
from yourapp.models import Course, Teacher
from yourapp.errors import ValidationError

db = SQLAlchemy()

def validate_teacher_assignment(course_id: int, teacher_id: int) -> None:
    """
    Validate that the provided teacher_id corresponds to a valid Teacher entry 
    and that the course exists.
    
    Parameters:
        course_id (int): The ID of the course being updated.
        teacher_id (int): The ID of the teacher to assign to the course.

    Raises:
        ValidationError: If the teacher_id is invalid or if the course does not exist.
    """
    # Check if course exists
    course = Course.query.get(course_id)
    if course is None:
        raise ValidationError(f"Course ID {course_id} does not exist.")

    # If teacher_id is provided, validate it corresponds to a valid Teacher
    if teacher_id is not None:
        teacher = Teacher.query.get(teacher_id)
        if teacher is None:
            raise ValidationError(f"Teacher ID {teacher_id} does not exist.")
        
        # Additional logic to handle the relationship can be implemented here
        # For example, we could check if the teacher is active or qualified for assignment

def validate_teacher_removal(course_id: int) -> None:
    """
    Validate that a teacher can be removed from a course.

    Parameters:
        course_id (int): The ID of the course.

    Raises:
        ValidationError: If the course does not exist or if 
        there is an issue with the removal.
    """
    # Check if course exists
    course = Course.query.get(course_id)
    if course is None:
        raise ValidationError(f"Course ID {course_id} does not exist.")

    # You may want to add logic here to handle specific cases related
    # to teacher removal, e.g., if the course has students enrolled.

```
