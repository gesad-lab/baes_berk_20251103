```python
# src/services/enrollment_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.enrollment import Enrollment  # Import the Enrollment model
from src.models.student import Student  # Import the Student model
from src.models.course import Course  # Import the Course model
from src.schemas.enrollment import EnrollmentCreate, EnrollmentResponse  # Import schemas for validation

def enroll_student(db: Session, student_id: int, enrollment: EnrollmentCreate) -> EnrollmentResponse:
    """
    Enroll a student in a course.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student.
        enrollment (EnrollmentCreate): Schema containing the course ID to enroll.

    Returns:
        EnrollmentResponse: The response schema containing enrollment details.

    Raises:
        HTTPException: If the student or course does not exist or if the enrollment fails.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create the enrollment record
    new_enrollment = Enrollment(student_id=student.id, course_id=course.id)
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    
    # Create and return the response object
    return EnrollmentResponse(student_id=new_enrollment.student_id, course_id=new_enrollment.course_id)

def get_student_courses(db: Session, student_id: int):
    """
    Retrieve all courses a student is enrolled in.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student.

    Returns:
        List[Course]: List of courses the student is enrolled in.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Retrieve courses associated with the student
    courses = db.query(Course).join(Enrollment).filter(Enrollment.student_id == student.id).all()
    return courses

def unenroll_student(db: Session, student_id: int, course_id: int):
    """
    De-enroll a student from a specific course.

    Args:
        db (Session): The database session.
        student_id (int): The ID of the student.
        course_id (int): The ID of the course.

    Raises:
        HTTPException: If the enrollment record does not exist.
    """
    # Check if the student is enrolled in the specific course
    enrollment = db.query(Enrollment).filter(Enrollment.student_id == student_id, Enrollment.course_id == course_id).first()
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment record not found")

    # Delete the enrollment record
    db.delete(enrollment)
    db.commit()
```