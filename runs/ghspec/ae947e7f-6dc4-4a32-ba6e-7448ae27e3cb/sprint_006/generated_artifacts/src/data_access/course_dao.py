```python
# File: src/data_access/course_dao.py

from typing import Dict
from sqlalchemy.orm import Session
from src.model.course import Course  # Import the Course model
from src.model.teacher import Teacher  # Import the Teacher model
from fastapi import HTTPException

def dissociate_teacher(course_id: int, db: Session) -> None:
    """Removes the teacher association from a course.

    Args:
        course_id (int): The ID of the course from which to dissociate the teacher.
        db (Session): The database session for committing changes.

    Raises:
        HTTPException: If the course does not exist or if no teacher is associated.
    """
    # Retrieve the course based on the course_id
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found.")  # Fail if course does not exist
    
    if course.teacher_id is None:
        raise HTTPException(status_code=400, detail="No teacher is associated with this course.")  # Fail if no teacher is associated
    
    # Dissociate the teacher by setting teacher_id to None
    course.teacher_id = None
    
    try:
        db.commit()  # Commit the changes to the database
    except Exception as e:
        db.rollback()  # Rollback in case of failure
        raise HTTPException(status_code=500, detail="Failed to dissociate teacher due to an internal error.") from e
```
