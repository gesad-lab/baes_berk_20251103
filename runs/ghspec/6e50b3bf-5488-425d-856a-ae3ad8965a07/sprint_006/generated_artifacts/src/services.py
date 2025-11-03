```python
# src/services.py

from sqlalchemy.orm import Session
from src.models import Course, Teacher  # Importing necessary models
from sqlalchemy.exc import NoResultFound

def assign_teacher_to_course(course_id: int, teacher_id: int, session: Session):
    """
    Assign a teacher to a course.

    Parameters:
    - course_id: The ID of the course to which the teacher will be assigned.
    - teacher_id: The ID of the teacher to assign to the course.
    - session: The SQLAlchemy session for database operations.

    Raises:
    - ValueError: If the course or teacher does not exist.

    Returns:
    - Course: The updated course object with the assigned teacher.
    """
    # Fetch the course and teacher using their IDs
    course = session.query(Course).filter(Course.id == course_id).one_or_none()
    teacher = session.query(Teacher).filter(Teacher.id == teacher_id).one_or_none()

    # Validate existence of course and teacher
    if course is None:
        raise ValueError(f"E001: Course with ID {course_id} does not exist.")
    if teacher is None:
        raise ValueError(f"E002: Teacher with ID {teacher_id} does not exist.")

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    
    # Commit the change to the database
    session.commit()

    return course

def get_course_with_teacher(course_id: int, session: Session):
    """
    Retrieve a course along with its assigned teacher by course ID.

    Parameters:
    - course_id: The ID of the course to retrieve.

    Returns:
    - Course: The course object with its teacher populated.

    Raises:
    - ValueError: If the course does not exist.
    """
    course = session.query(Course).filter(Course.id == course_id).one_or_none()

    if course is None:
        raise ValueError(f"E001: Course with ID {course_id} does not exist.")

    return course
```