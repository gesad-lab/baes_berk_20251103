```python
# File: src/services/course_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models import Course, Teacher

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session) -> None:
    """
    Assign a teacher to an existing course.

    Args:
    - course_id: The ID of the course to which the teacher will be assigned.
    - teacher_id: The ID of the teacher to be assigned to the course.
    - db: Database session.

    Raises:
    - HTTPException: If the course or teacher does not exist.
    """
    # Retrieve the course by its ID
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if course is None:
        raise HTTPException(status_code=404, detail="Course not found")  # Return 404 if course doesn't exist
    
    # Retrieve the teacher by its ID
    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    
    if teacher is None:
        raise HTTPException(status_code=400, detail="Teacher not found")  # Return 400 if teacher doesn't exist

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    
    try:
        db.commit()  # Commit the changes to the database
    except Exception as e:
        db.rollback()  # Roll back in case of an error
        raise HTTPException(status_code=500, detail="Failed to assign teacher") from e  # Raise an error for any issues
```