```python
from fastapi import HTTPException
from sqlalchemy.orm import Session
from .models import Course, Teacher  # Ensure we import our models

def assign_teacher_service(course_id: int, teacher_id: int, session: Session):
    """Assign a Teacher to a Course.

    Args:
        course_id (int): The ID of the Course to which the Teacher is assigned.
        teacher_id (int): The ID of the Teacher being assigned to the Course.
        session (Session): The SQLAlchemy session for database interaction.

    Returns:
        Course: The updated Course object after assignment.

    Raises:
        HTTPException: If the Course is not found (404).
    """
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    course.teacher_id = teacher_id
    session.commit()  # Save changes to the database
    return course


def get_course_detail_service(course_id: int, session: Session):
    """Retrieve the details of a Course including assigned Teacher's information.

    Args:
        course_id (int): The ID of the Course to retrieve.
        session (Session): The SQLAlchemy session for database interaction.

    Returns:
        dict: A dictionary containing the Course details and Teacher information.

    Raises:
        HTTPException: If the Course is not found (404).
    """
    course = session.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Constructing course detail response
    return {
        "id": course.id,
        "title": course.title,
        "description": course.description,
        "teacher": {
            "id": course.teacher.id if course.teacher else None,  # Fetch teacher ID if exists
            "name": course.teacher.name if course.teacher else None  # Fetch teacher name if exists
        }
    }
```