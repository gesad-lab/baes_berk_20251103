```python
# src/services/student_service.py

from typing import List, Dict
from sqlalchemy.exc import IntegrityError
from src.models.student import Student
from src.models.course import Course
from app import db

def enroll_student_in_courses(student_id: int, course_ids: List[int]) -> Dict[str, str]:
    """Enroll a student in one or more courses.
    
    Args:
        student_id (int): The ID of the student to enroll.
        course_ids (List[int]): A list of course IDs to enroll the student in.

    Returns:
        Dict[str, str]: A success or error message indicating the outcome.
    """
    student = Student.query.get(student_id)
    courses = Course.query.filter(Course.id.in_(course_ids)).all()

    if not student:
        return {"error": "Student not found."}

    if not courses:
        return {"error": "No valid courses found."}

    # Associate student with courses
    try:
        for course in courses:
            student.courses.append(course)  # Assuming a many-to-many relationship exists
        db.session.commit()
        return {"message": "Student enrolled in courses successfully."}
    except IntegrityError:
        db.session.rollback()  # Rollback on error to prevent data inconsistency
        return {"error": "Failed to enroll student in courses."}


def remove_student_from_course(student_id: int, course_id: int) -> Dict[str, str]:
    """Remove a student from a specific course.
    
    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course to remove the student from.

    Returns:
        Dict[str, str]: A success or error message indicating the outcome.
    """
    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student:
        return {"error": "Student not found."}
    
    if not course:
        return {"error": "Course not found."}

    # Disassociate student from course
    if course in student.courses:
        student.courses.remove(course)
        db.session.commit()
        return {"message": "Student removed from course successfully."}
    else:
        return {"error": "Student is not enrolled in this course."}
```