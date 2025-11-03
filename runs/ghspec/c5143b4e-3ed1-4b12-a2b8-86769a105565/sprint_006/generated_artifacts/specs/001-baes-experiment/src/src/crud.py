```python
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.models import Course, Teacher
from fastapi import HTTPException, status

def remove_teacher_from_course(course_id: str, db: Session):
    """
    Removes a teacher assignment from a course identified by course_id.
    
    Parameters:
    - course_id: The ID of the course from which the teacher will be removed.
    - db: The database session for interacting with the database.

    Returns:
    - The updated Course object without the assigned teacher.

    Raises:
    - HTTPException: If the course does not exist or if the teacher is not assigned.
    """
    # Retrieve the course from the database
    course = db.query(Course).filter(Course.id == course_id).first()

    if not course:
        # Course not found, raise a 404 error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    if not course.teacher_id:
        # If no teacher is assigned, raise a 400 error
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No teacher assigned to this course")

    # Removed the teacher assignment
    course.teacher_id = None
    db.commit()  # Commit the changes to the database

    return course  # Return the updated course object
```