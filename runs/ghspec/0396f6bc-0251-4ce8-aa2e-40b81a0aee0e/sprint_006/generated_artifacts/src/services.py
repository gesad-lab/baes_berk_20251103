```python
# src/services.py

from sqlalchemy.orm import Session
from models import Course, Teacher  # Import Course and Teacher models
from fastapi import HTTPException

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session) -> Course:
    """
    Assign a teacher to a course.

    Parameters:
        course_id (int): The ID of the course to which the teacher will be assigned.
        teacher_id (int): The ID of the teacher being assigned to the course.
        db (Session): The database session.

    Returns:
        Course: The updated Course object with the assigned teacher.

    Raises:
        HTTPException: If the course or teacher is not found or if the assignment fails.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")

    teacher = db.query(Teacher).filter(Teacher.id == teacher_id).first()
    if not teacher:
        raise HTTPException(status_code=404, detail="Teacher not found.")

    # Assign the teacher to the course
    course.teacher_id = teacher_id
    db.commit()
    db.refresh(course)  # Refresh the course instance to include the updated teacher_id
    return course

def get_course_details(course_id: int, db: Session) -> Course:
    """
    Retrieve detailed information about a course.

    Parameters:
        course_id (int): The ID of the course to retrieve.
        db (Session): The database session.

    Returns:
        Course: The Course object with complete details.

    Raises:
        HTTPException: If the course is not found.
    """
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found.")
    
    return course
```