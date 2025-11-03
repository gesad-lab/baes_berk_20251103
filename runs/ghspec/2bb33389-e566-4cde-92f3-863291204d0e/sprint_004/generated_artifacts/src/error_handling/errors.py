```python
# src/error_handling/errors.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models import Student, Course

def validate_student_id(student_id: int, db: Session) -> None:
    """
    Validates that the given student_id exists in the database.

    Args:
        student_id (int): The ID of the student.
        db (Session): Database session for querying.

    Raises:
        HTTPException: If the student ID does not exist, with a 400 Bad Request status.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E001", "message": "Invalid student ID provided."}},
        )

def validate_course_id(course_id: int, db: Session) -> None:
    """
    Validates that the given course_id exists in the database.

    Args:
        course_id (int): The ID of the course.
        db (Session): Database session for querying.

    Raises:
        HTTPException: If the course ID does not exist, with a 400 Bad Request status.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(
            status_code=400,
            detail={"error": {"code": "E002", "message": "Invalid course ID provided."}},
        )
```