```python
# src/validation/course_validation.py

from fastapi import HTTPException
from models import Course, Teacher
from sqlalchemy.orm import Session

def validate_course_exists(course_id: int, db: Session) -> Course:
    """Validate the existence of a course by its ID.

    Args:
        course_id (int): The ID of the course to validate.
        db (Session): The database session.

    Raises:
        HTTPException: If the course does not exist.

    Returns:
        Course: The course entity if found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="E001: Course not found.")
    return course

def validate_teacher_exists(teacher_id: int, db: Session) -> Teacher:
    """Validate the existence of a teacher by their ID.

    Args:
        teacher_id (int): The ID of the teacher to validate.
        db (Session): The database session.

    Raises:
        HTTPException: If the teacher does not exist.

    Returns:
        Teacher: The teacher entity if found.
    """
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if teacher is None:
        raise HTTPException(status_code=404, detail="E002: Teacher not found.")
    return teacher

def validate_teacher_assignment(course_id: int, teacher_id: int, db: Session) -> None:
    """Validate the assignment of a teacher to a course.

    Args:
        course_id (int): The ID of the course.
        teacher_id (int): The ID of the teacher.
        db (Session): The database session.

    Raises:
        HTTPException: If the course or teacher do not exist.
    """
    validate_course_exists(course_id, db)
    validate_teacher_exists(teacher_id, db)
```
