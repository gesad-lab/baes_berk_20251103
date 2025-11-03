```python
from fastapi import FastAPI, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.models.enrollment import Enrollment
from src.models.student import Student
from src.models.course import Course
from src.schemas.enrollment import EnrollmentCreate, EnrollmentResponse
from src.services.enrollment_service import EnrollmentService

app = FastAPI()

enrollment_service = EnrollmentService()

@app.post("/students/{id}/enroll", response_model=EnrollmentResponse)
def enroll_student(id: int, enrollment: EnrollmentCreate, db: Session = Depends(get_db)):
    """
    Enroll a student in a specific course.

    Args:
        id (int): The student ID.
        enrollment (EnrollmentCreate): The enrollment data containing the course ID.
        db (Session): The database session.

    Returns:
        EnrollmentResponse: The enrollment details.
    """
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    # Call service to create an enrollment record
    result = enrollment_service.enroll_student(student_id=id, course_id=enrollment.course_id, db=db)
    return result

@app.get("/students/{id}/courses", response_model=list[EnrollmentResponse])
def get_student_courses(id: int, db: Session = Depends(get_db)):
    """
    Retrieve all courses a student is enrolled in.

    Args:
        id (int): The student ID.
        db (Session): The database session.

    Returns:
        list[EnrollmentResponse]: List of courses the student is enrolled in.
    """
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    courses = enrollment_service.get_courses_by_student(student_id=id, db=db)
    return courses

@app.delete("/students/{studentId}/courses/{courseId}", status_code=status.HTTP_204_NO_CONTENT)
def unenroll_student(studentId: int, courseId: int, db: Session = Depends(get_db)):
    """
    De-enroll a student from a specific course.

    Args:
        studentId (int): The student ID.
        courseId (int): The course ID.

    Returns:
        HTTP status: 204 No Content if successful.
    """
    student = db.query(Student).filter(Student.id == studentId).first()
    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    course = db.query(Course).filter(Course.id == courseId).first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")

    enrollment_service.unenroll_student(student_id=studentId, course_id=courseId, db=db)
```
