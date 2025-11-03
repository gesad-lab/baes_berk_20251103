```python
# File: src/api/validators.py

from flask import jsonify
from your_application import db  # Adjust import based on your actual application structure
from models import Student, Course  # Import existing models for validation

def validate_enrollment(student_id: int, course_id: int) -> (bool, str):
    """
    Validate the student ID and course ID for enrollment.

    Args:
        student_id (int): The ID of the student to enroll.
        course_id (int): The ID of the course to enroll into.

    Returns:
        Tuple[bool, str]: A tuple where the first element indicates if validation passed,
                          and the second element is an error message if validation fails.
    """
    # Check if student exists
    student = db.session.query(Student).filter_by(id=student_id).first()
    if not student:
        return False, f"E001: Invalid student ID {student_id}. Student does not exist."

    # Check if course exists
    course = db.session.query(Course).filter_by(id=course_id).first()
    if not course:
        return False, f"E002: Invalid course ID {course_id}. Course does not exist."

    # Validation passed
    return True, "Valid enrollment parameters."

def validate_student_courses_request(student_id: int) -> (bool, str):
    """
    Validate the student ID for retrieving courses.

    Args:
        student_id (int): The ID of the student whose courses are to be retrieved.

    Returns:
        Tuple[bool, str]: A tuple where the first element indicates if validation passed,
                          and the second element is an error message if validation fails.
    """
    # Check if student exists
    student = db.session.query(Student).filter_by(id=student_id).first()
    if not student:
        return False, f"E001: Invalid student ID {student_id}. Student does not exist."

    # Validation passed
    return True, "Valid student ID for retrieving courses."
```