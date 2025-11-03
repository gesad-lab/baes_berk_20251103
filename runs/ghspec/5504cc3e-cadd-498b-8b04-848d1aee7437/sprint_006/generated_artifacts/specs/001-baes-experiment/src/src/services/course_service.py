```python
from flask import jsonify
from src.models.course import Course
from src.models.teacher import Teacher
from app import db

def assign_teacher_to_course(course_id: int, teacher_id: int) -> bool:
    """
    Assign a Teacher to a Course by updating the teacher_id in the Course record.

    Parameters:
    - course_id (int): The ID of the Course to which the Teacher will be assigned.
    - teacher_id (int): The ID of the Teacher to assign to the Course.

    Returns:
    - bool: True if the assignment was successful, False otherwise.
    """
    course = db.session.query(Course).filter(Course.id == course_id).first()
    if not course:
        return False  # Course does not exist

    course.teacher_id = teacher_id
    db.session.commit()
    return True


def get_course_details(course_id: int):
    """
    Retrieve detailed information about a Course, including the assigned Teacher's name.

    Parameters:
    - course_id (int): The ID of the Course to retrieve.

    Returns:
    - dict: A dictionary containing course details and the teacher's name, or None if not found.
    """
    course = db.session.query(Course).filter(Course.id == course_id).first()
    if not course:
        return None  # Course does not exist

    # Build response structure including course details and teacher information
    course_details = {
        'id': course.id,
        'name': course.name,
        'description': course.description,
        'teacher_name': course.teacher.name if course.teacher else None  # Include teacher's name if exists
    }
    return course_details
```