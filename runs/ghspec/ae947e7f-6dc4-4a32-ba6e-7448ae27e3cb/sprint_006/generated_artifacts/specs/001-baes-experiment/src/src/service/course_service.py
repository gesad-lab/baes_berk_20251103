```python
# src/service/course_service.py

from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.model.course import Course  # Import the Course model
from src.model.teacher import Teacher  # Import the Teacher model


def dissociate_teacher(course_id: int, db: Session):
    """Dissociates a teacher from a course by setting the teacher_id to None.

    Args:
        course_id (int): The ID of the course from which to dissociate the teacher.
        db (Session): The database session to execute the query.

    Raises:
        HTTPException: If the course does not exist or if the teacher is not associated with the course.

    Returns:
        dict: A message confirming the teacher has been dissociated from the course.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    
    # Validate if course exists
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    # Check if a teacher is already associated
    if course.teacher_id is None:
        raise HTTPException(status_code=400, detail="No teacher is currently associated with this course.")

    # Dissociate the teacher
    course.teacher_id = None
    db.commit()  # Commit the changes to the database

    return {"message": "Teacher dissociated successfully."}
```