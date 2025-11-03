```python
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Course  # Assuming Course is defined in src/models.py

def get_course_by_id(db: Session, course_id: int) -> Course:
    """Retrieve a course by its ID.

    Args:
        db (Session): The database session.
        course_id (int): The ID of the course to retrieve.

    Returns:
        Course: The course object if found.

    Raises:
        HTTPException: If the course with the given ID does not exist.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")
    return course
```