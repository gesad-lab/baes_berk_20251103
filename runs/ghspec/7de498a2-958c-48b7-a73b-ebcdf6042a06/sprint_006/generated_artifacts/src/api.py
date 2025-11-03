```python
# src/services.py

from sqlalchemy.orm import Session
from src.models import Course  # Assuming Course model is located here
from fastapi import HTTPException

def remove_teacher_from_course(course_id: int, db: Session) -> Course:
    """
    Remove the teacher from a specific course by setting the teacher_id to None.

    Args:
        course_id (int): The ID of the course from which to remove the teacher.
        db (Session): Database session object.

    Returns:
        Course: The updated Course object without the teacher.

    Raises:
        HTTPException: If the course is not found or if an error occurs during the update.
    """

    # Fetch the course
    course = db.query(Course).filter(Course.id == course_id).first()
    
    # If course doesn't exist, raise a 404 error
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Remove the teacher by setting teacher_id to None
    course.teacher_id = None

    # Save changes to the database
    try:
        db.commit()
    except Exception as e:
        db.rollback()  # Rollback in case of error
        raise HTTPException(status_code=500, detail="Error removing teacher from course")

    return course
```