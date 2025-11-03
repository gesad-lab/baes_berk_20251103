```python
# src/api/dependencies.py

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from models import Course, Teacher
from database import get_db

def get_courses_with_teachers(db: Session):
    """
    Retrieve all courses along with their associated teachers.

    Args:
        db: Database session.

    Returns:
        List of Course models including teacher information.
    """
    # Retrieve all courses with their associated teacher
    courses = db.query(Course).options(Course.teacher).all()
    return courses

def assign_teacher_to_course(course_id: int, teacher_id: int, db: Session):
    """
    Assign a teacher to a specific course.

    Args:
        course_id: ID of the course to be updated.
        teacher_id: ID of the teacher to be assigned.
        db: Database session.

    Raises:
        HTTPException: If the course does not exist.
    """
    # Retrieve the course by ID
    course = db.query(Course).filter(Course.id == course_id).first()
    
    if not course:
        # Raise error if course is not found
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Assign teacher to the course
    course.teacher_id = teacher_id
    db.commit()

def get_course_with_teacher(course_id: int, db: Session):
    """
    Retrieve a specific course along with its assigned teacher.

    Args:
        course_id: ID of the course to be retrieved.
        db: Database session.
    
    Returns:
        Course model including teacher information.
    
    Raises:
        HTTPException: If the course does not exist.
    """
    # Retrieve specific course with associated teacher
    course = db.query(Course).options(Course.teacher).filter(Course.id == course_id).first()
    
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    return course
```