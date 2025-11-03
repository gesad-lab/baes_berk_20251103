```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from models import Course  # Importing the Course model for interaction with the database
from fastapi import HTTPException

def assign_teacher_to_course(db: Session, course_id: int, teacher_id: int):
    """
    Assign a Teacher to a Course.
    
    Parameters:
    - db: The database session to use for the operation.
    - course_id: The ID of the Course to which the Teacher will be assigned.
    - teacher_id: The ID of the Teacher to be assigned to the Course.
    
    Raises:
    - HTTPException: If the Course does not exist, a 404 error is raised.
    
    Returns:
    - dict: A success message upon successful assignment of the Teacher.
    """
    # Verify if the course exists in the database
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        # If course does not exist, raise an HTTP exception with a 404 Not Found status
        raise HTTPException(status_code=404, detail={
            "error": {
                "code": "E002",
                "message": "Course not found."
            }
        })
    
    # Logic to assign teacher to course (assuming there is an attribute `teacher_id` in Course)
    course.teacher_id = teacher_id  # Assigning teacher_id to the course
    db.commit()  # Commit the changes to the database
    
    return {"message": "Teacher assigned to Course successfully."}
```