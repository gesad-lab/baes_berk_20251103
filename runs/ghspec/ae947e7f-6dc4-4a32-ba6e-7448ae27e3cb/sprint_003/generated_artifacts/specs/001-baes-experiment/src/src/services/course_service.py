```python
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.model.course import Course  # Assuming the Course model will be defined in the model folder
from typing import Optional

def create_course(name: str, level: str, db: Session) -> Course:
    """
    Creates a new course entity.

    Args:
        name (str): The name of the course.
        level (str): The level of the course.
        db (Session): The database session to use for the operation.

    Returns:
        Course: The created course entity.

    Raises:
        HTTPException: If the name or level is not provided.
    """
    # Validate inputs
    if not name:
        raise HTTPException(status_code=400, detail="Course name is required.")
    if not level:
        raise HTTPException(status_code=400, detail="Course level is required.")

    # Create new course entity
    new_course = Course(name=name, level=level)
    
    # Add the course to the database
    db.add(new_course)
    db.commit()
    db.refresh(new_course)  # Refresh instance to get the newly assigned ID

    return new_course


def get_course_by_id(course_id: int, db: Session) -> Optional[Course]:
    """
    Retrieves a course by its ID.

    Args:
        course_id (int): The ID of the course to retrieve.
        db (Session): The database session to use for the operation.

    Returns:
        Course: The course entity if found.

    Raises:
        HTTPException: If the course with the given ID does not exist.
    """
    # Retrieve the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return course
```