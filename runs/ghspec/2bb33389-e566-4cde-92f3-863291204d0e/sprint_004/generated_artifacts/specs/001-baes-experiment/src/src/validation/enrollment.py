```python
# src/validation/enrollment.py

from fastapi import HTTPException
from src.models import Student, Course  # Assuming these models are defined in src/models.py


def validate_student_id(student_id: int):
    """Validate that the student ID exists in the database."""
    if student_id is None or student_id <= 0:
        raise HTTPException(status_code=400, detail="E001: Invalid student ID. Must be a positive integer.")
    
    # Check existence of student in the database
    student = Student.query.filter_by(id=student_id).first()
    if not student:
        raise HTTPException(status_code=400, detail="E002: Student ID does not exist.")


def validate_course_id(course_id: int):
    """Validate that the course ID exists in the database."""
    if course_id is None or course_id <= 0:
        raise HTTPException(status_code=400, detail="E003: Invalid course ID. Must be a positive integer.")
    
    # Check existence of course in the database
    course = Course.query.filter_by(id=course_id).first()
    if not course:
        raise HTTPException(status_code=400, detail="E004: Course ID does not exist.")


def validate_enrollment_data(student_id: int, course_id: int):
    """Validate the enrollment data for student and course IDs."""
    validate_student_id(student_id)
    validate_course_id(course_id)
```