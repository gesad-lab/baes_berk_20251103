```python
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.enrollment import Enrollment
from src.models.student import Student
from src.models.course import Course
from src.schemas.enrollment import EnrollmentCreate, EnrollmentResponse
from src.services.enrollment_service import enroll_student, get_student_courses, de_enroll_student

router = APIRouter()

@router.post("/students/{student_id}/enroll", response_model=EnrollmentResponse)
def enroll(student_id: int, enrollment_data: EnrollmentCreate, db: Session = Depends(get_db)):
    """
    Enroll a student in a course.

    Parameters:
        student_id (int): The ID of the student to enroll.
        enrollment_data (EnrollmentCreate): Enrollment payload containing course ID.

    Returns:
        EnrollmentResponse: The details of the enrollment.

    Raises:
        HTTPException: If the student or course does not exist.
    """
    # Check if the student exists
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    # Check if the course exists
    course = db.query(Course).filter(Course.id == enrollment_data.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {enrollment_data.course_id} not found.")

    # Attempt to enroll the student
    try:
        enrollment = enroll_student(student_id, enrollment_data.course_id, db)
        return enrollment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/students/{student_id}/courses", response_model=list[EnrollmentResponse])
def get_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses a student is enrolled in.

    Parameters:
        student_id (int): The ID of the student.

    Returns:
        list[EnrollmentResponse]: A list of courses the student is enrolled in.

    Raises:
        HTTPException: If the student does not exist.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    courses = get_student_courses(student_id, db)
    return courses


@router.delete("/students/{student_id}/courses/{course_id}", response_model=EnrollmentResponse)
def de_enroll(student_id: int, course_id: int, db: Session = Depends(get_db)):
    """
    De-enroll a student from a specific course.

    Parameters:
        student_id (int): The ID of the student.
        course_id (int): The ID of the course to de-enroll from.

    Returns:
        EnrollmentResponse: The details of the de-enrollment.

    Raises:
        HTTPException: If the student or course does not exist, or de-enrollment fails.
    """
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail=f"Student with ID {student_id} not found.")

    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail=f"Course with ID {course_id} not found.")

    try:
        enrollment = de_enroll_student(student_id, course_id, db)
        return enrollment
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```