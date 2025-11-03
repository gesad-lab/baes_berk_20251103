```python
# src/validation/validators.py

from models import Student, Course  # Assuming these models are defined in models.py
from fastapi import HTTPException, status
from typing import List

class ValidationError(Exception):
    """Custom exception for validation errors."""
    def __init__(self, detail: str):
        self.detail = detail


def validate_student(student_id: int) -> None:
    """Validate if the given student ID corresponds to an existing student.

    Args:
        student_id (int): The ID of the student to validate.

    Raises:
        HTTPException: If the student does not exist.
    """
    student = Student.query.get(student_id)  # Assume SQLAlchemy ORM is used.
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with ID {student_id} does not exist."
        )


def validate_courses(course_ids: List[int]) -> None:
    """Validate if all the given course IDs correspond to existing courses.

    Args:
        course_ids (List[int]): A list of course IDs to validate.

    Raises:
        HTTPException: If any of the course IDs do not exist.
    """
    for course_id in course_ids:
        course = Course.query.get(course_id)  # Assume SQLAlchemy ORM is used.
        if not course:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Course with ID {course_id} does not exist."
            )


def validate_course_assignment(student_id: int, course_ids: List[int]) -> None:
    """Validate the student and course assignment parameters.

    Args:
        student_id (int): The ID of the student to assign the courses to.
        course_ids (List[int]): The list of course IDs to assign.

    Raises:
        ValidationError: If validation for student or courses fails.
    """
    validate_student(student_id)
    validate_courses(course_ids)
```