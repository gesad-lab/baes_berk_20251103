```python
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models import Student, Course, Enrollment  # Ensure these are defined in models.py

def validate_enrollment_input(student_id: int, course_id: int, db: Session) -> None:
    """
    Validate the input for enrolling a student in a course.
    
    Parameters:
    - student_id (int): ID of the student to be enrolled.
    - course_id (int): ID of the course for enrollment.
    - db (Session): Database session for querying.

    Raises:
    - HTTPException: If the student or course does not exist, or if the student is already enrolled in the course.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found.")

    # Check if the student is already enrolled in the course
    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.student_id == student_id,
        Enrollment.course_id == course_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student is already enrolled in this course.")

def enroll_student(student_id: int, course_id: int, db: Session) -> None:
    """
    Enroll a student in a course after validating input.

    Parameters:
    - student_id (int): ID of the student to enroll.
    - course_id (int): ID of the course in which to enroll the student.
    - db (Session): Database session for handling queries and updates.
    """
    # Validate the input before proceeding
    validate_enrollment_input(student_id, course_id, db)
    
    # Proceed with enrollment
    new_enrollment = Enrollment(student_id=student_id, course_id=course_id)
    db.add(new_enrollment)
    db.commit()
```
