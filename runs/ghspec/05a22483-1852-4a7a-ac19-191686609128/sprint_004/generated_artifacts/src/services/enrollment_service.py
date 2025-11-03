```python
# src/services/enrollment_service.py

from src.models import Enrollment, Student, Course  # Import necessary models
from your_app import db  # Ensure we have access to the database session
from flask import abort

def enroll_student_in_course(student_id: int, course_id: int) -> dict:
    """Enroll a student in a course.

    Args:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.

    Returns:
        dict: Enrollment confirmation details.

    Raises:
        ValueError: If the student or course does not exist.
    """
    student = Student.query.get(student_id)
    course = Course.query.get(course_id)

    if not student:
        abort(400, description=f"E001: Invalid student ID {student_id}.")
    if not course:
        abort(400, description=f"E002: Invalid course ID {course_id}.")

    enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.session.add(enrollment)
    db.session.commit()

    return {
        "message": "Enrollment successful.",
        "student_id": student_id,
        "course_id": course_id
    }


def get_courses_for_student(student_id: int) -> list:
    """Retrieve the list of courses for a given student.

    Args:
        student_id (int): The ID of the student.

    Returns:
        list: A list of course names the student is enrolled in.

    Raises:
        ValueError: If the student does not exist.
    """
    student = Student.query.get(student_id)

    if not student:
        abort(404, description=f"E003: Student with ID {student_id} not found.")

    # Retrieve the courses associated with the student
    courses = Course.query.join(Enrollment).filter(Enrollment.student_id == student_id).all()

    return [course.name for course in courses]  # Return a list of course names
```