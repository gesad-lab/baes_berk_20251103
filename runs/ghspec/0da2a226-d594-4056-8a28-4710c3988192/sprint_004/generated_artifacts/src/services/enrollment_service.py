```python
# File: src/services/enrollment_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from models import Student, Course, Enrollment

def enroll_student(student_id: int, course_id: int, db: Session) -> str:
    """
    Enroll a student in a specified course.

    Args:
        student_id (int): The ID of the student to enroll.
        course_id (int): The ID of the course to enroll the student in.
        db (Session): The database session.

    Returns:
        str: A success message indicating enrollment completion.

    Raises:
        HTTPException: If the student is already enrolled in the course or if the course does not exist.
    """
    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="E001: Course not found")

    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="E002: Student not found")

    # Check if the student is already enrolled in the course
    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.course_id == course_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="E003: Student is already enrolled in this course")

    # Enroll the student in the course
    new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(new_enrollment)
    db.commit()

    return "Enrollment successful"

def get_student_courses(student_id: int, db: Session) -> list:
    """
    Retrieve all courses associated with a given student.

    Args:
        student_id (int): The ID of the student whose courses to retrieve.
        db (Session): The database session.

    Returns:
        list: A list of courses that the student is enrolled in.

    Raises:
        HTTPException: If the student does not exist.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="E002: Student not found")

    # Retrieve courses enrolled by the student
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student_id).all()

    return [{"name": course.name, "level": course.level} for course in courses]
```