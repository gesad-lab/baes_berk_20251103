```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from models import Course  # Import the Course model
from fastapi import HTTPException, status

# Define acceptable levels for the course
VALID_LEVELS = {"Beginner", "Intermediate", "Advanced"}

def create_course(db: Session, name: str, level: str) -> Course:
    """Create a new course in the database.

    Args:
        db (Session): The database session for making queries.
        name (str): The name of the course.
        level (str): The level of the course (must be one of the predefined values).

    Returns:
        Course: The newly created course.

    Raises:
        HTTPException: If the level is invalid or if required fields are missing.
    """
    # Validate input
    if not name or not level:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Both 'name' and 'level' are required."
        )
    
    if level not in VALID_LEVELS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid level. Expected one of: {', '.join(VALID_LEVELS)}."
        )

    # Create a new course instance
    new_course = Course(name=name, level=level)

    # Add the new course to the session and commit
    db.add(new_course)
    db.commit()
    db.refresh(new_course)  # Refresh to get the updated instance with ID

    return new_course


def get_course(db: Session, course_id: int) -> Course:
    """Retrieve a course by its ID.

    Args:
        db (Session): The database session for making queries.
        course_id (int): The ID of the course to retrieve.

    Returns:
        Course: The course with the specified ID.

    Raises:
        HTTPException: If the course is not found.
    """
    # Attempt to fetch the course by its ID
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if course is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Course not found."
        )
    
    return course
```