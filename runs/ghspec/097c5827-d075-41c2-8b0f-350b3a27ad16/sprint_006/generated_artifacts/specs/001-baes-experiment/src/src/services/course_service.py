```python
# src/services/course_service.py

from sqlalchemy.orm import Session
from src.models import Course, Teacher
from typing import Optional, Dict, Any
from flask import jsonify

def get_course_details(course_id: int, db_session: Session) -> Optional[Dict[str, Any]]:
    """Retrieve course details by course ID, including assigned teacher information.
    
    Args:
        course_id (int): The ID of the course to retrieve.
        db_session (Session): The database session for querying.

    Returns:
        Optional[Dict[str, Any]]: Course details including teacher info if exists, else None.
    """
    course = db_session.query(Course).filter_by(id=course_id).first()
    
    # Check if the course exists
    if not course:
        return None

    # Prepare course details
    course_details = {
        'courseId': course.id,
        'courseName': course.name,
        'level': course.level,
        'teacher': None  # Default to None if no teacher is assigned
    }

    # Include teacher information if assigned
    if course.teacher_id:
        teacher = db_session.query(Teacher).filter_by(id=course.teacher_id).first()
        if teacher:
            course_details['teacher'] = {
                'id': teacher.id,
                'name': teacher.name,
                'email': teacher.email
            }
    
    return course_details

def assign_teacher_to_course(course_id: int, teacher_id: int, db_session: Session) -> bool:
    """Assign a teacher to a course.
    
    Args:
        course_id (int): The ID of the course.
        teacher_id (int): The ID of the teacher to assign.
        db_session (Session): The database session for committing changes.

    Returns:
        bool: True if teacher assigned successfully, False otherwise.
    """
    course = db_session.query(Course).filter_by(id=course_id).first()
    teacher = db_session.query(Teacher).filter_by(id=teacher_id).first()

    # Validate course and teacher existence
    if not course or not teacher:
        return False
    
    # Assign teacher to course
    course.teacher_id = teacher.id  # Assuming `teacher_id` is the column in Course model
    db_session.commit()
    return True
```