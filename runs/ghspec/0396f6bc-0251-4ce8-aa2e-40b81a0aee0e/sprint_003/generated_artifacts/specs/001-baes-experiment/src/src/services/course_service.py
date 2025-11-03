```python
# src/services/course_service.py

from typing import Optional
from sqlalchemy.orm import Session
from models import Course  # Assuming Course model is already defined
from fastapi import HTTPException

def create_course(name: str, level: str, db: Session) -> Course:
    """
    Create a course record in the database.

    Args:
        name (str): The name of the course.
        level (str): The level of the course.
        db (Session): SQLAlchemy database session.

    Returns:
        Course: The created Course object.

    Raises:
        HTTPException: If the name or level is missing.
    """
    if not name:
        raise HTTPException(status_code=400, detail="E001: Course name is required")
    if not level:
        raise HTTPException(status_code=400, detail="E002: Course level is required")

    # Create a new Course instance
    new_course = Course(name=name, level=level)

    # Add the new course to the session and commit
    db.add(new_course)
    db.commit()
    db.refresh(new_course)  # Refresh the instance to get the updated data

    return new_course

def get_course_by_id(course_id: int, db: Session) -> Optional[Course]:
    """
    Retrieve a course by ID from the database.

    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): SQLAlchemy database session.

    Returns:
        Optional[Course]: The Course object if found, or None if not found.

    Raises:
        HTTPException: If the course ID is invalid or the course does not exist.
    """
    if course_id <= 0:
        raise HTTPException(status_code=400, detail="E003: Invalid course ID")

    # Query the course by ID
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="E004: Course not found")

    return course
```