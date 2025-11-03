```python
# File: services/course_service.py

from models import db, Course, Teacher
from sqlalchemy.exc import IntegrityError

def assign_teacher_to_course(course_id: int, teacher_id: int) -> str:
    """Assign a teacher to an existing course.

    Args:
        course_id (int): The ID of the course to assign the teacher to.
        teacher_id (int): The ID of the teacher to assign to the course.

    Returns:
        str: A confirmation message upon successful assignment.

    Raises:
        ValueError: If the course or teacher does not exist.
    """
    course = Course.query.get(course_id)
    teacher = Teacher.query.get(teacher_id)
    
    if course is None:
        raise ValueError(f"E001: Course with ID {course_id} does not exist.")
    if teacher is None:
        raise ValueError(f"E002: Teacher with ID {teacher_id} does not exist.")
    
    course.teacher_id = teacher_id  # Assign teacher to course

    try:
        db.session.commit()  # Save changes to the database
    except IntegrityError:
        db.session.rollback()  # Rollback in case of integrity exception
        raise ValueError("Failed to assign the teacher due to a database error.")
    
    return f"Teacher with ID {teacher_id} has been successfully assigned to Course ID {course_id}."


def retrieve_course_with_teacher(course_id: int) -> dict:
    """Retrieve course details along with teacher information.

    Args:
        course_id (int): The ID of the course to retrieve.

    Returns:
        dict: A dictionary containing course details and assigned teacher's name.

    Raises:
        ValueError: If the course does not exist.
    """
    course = Course.query.get(course_id)
    
    if course is None:
        raise ValueError(f"E001: Course with ID {course_id} does not exist.")

    # Prepare course details with teacher info
    course_details = {
        "course_id": course.id,
        "course_name": course.name,
        "teacher_id": course.teacher_id,
        "teacher_name": course.teacher.name if course.teacher else None  # Include teacher name if assigned
    }
    
    return course_details
```