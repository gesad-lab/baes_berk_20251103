```python
from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models import Course  # Assuming the Course model is defined in models
from src.database import get_db  # Assuming a function to get the database session

router = APIRouter()

@router.post("/courses", response_model=Course)  # Response model should conform to course model
def create_course(course: Course, db: Session = next(get_db())):
    """
    Create a new course.

    Args:
        course (Course): Course data containing name and level.
        db (Session, optional): Database session. Defaults to next(get_db()).

    Raises:
        HTTPException: If required fields are missing.

    Returns:
        Course: The created course details including ID, name, and level.
    """
    # Validate that both name and level exist
    if not course.name or not course.level:
        raise HTTPException(
            status_code=400,
            detail={"errors": {
                "name": "Field 'name' is required." if not course.name else None,
                "level": "Field 'level' is required." if not course.level else None
            }}
        )

    # Add the course to the session and commit
    db.add(course)
    db.commit()
    db.refresh(course)  # Reload the instance from the database

    return course  # Return the created course

@router.get("/courses", response_model=list[Course])  # Assuming an appropriate list response model
def get_all_courses(db: Session = next(get_db())):
    """
    Retrieve all courses.

    Args:
        db (Session, optional): Database session. Defaults to next(get_db()).

    Returns:
        list[Course]: List of all courses in the database.
    """
    return db.query(Course).all()  # Return all courses from the database
```