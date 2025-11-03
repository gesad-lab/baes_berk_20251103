from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from src.models import Student, Course, StudentCourse
from src.database import get_db
from pydantic import BaseModel

router = APIRouter()

class UnenrollRequest(BaseModel):
    student_id: int
    course_id: int

@router.delete("/students/unenroll", response_model=None, status_code=204)
def unenroll_student_from_course(unenroll_request: UnenrollRequest, db: Session = Depends(get_db)):
    """
    Unenroll a student from a course.
    
    Parameters:
    - unenroll_request: An object containing student_id and course_id.
    - db: Database session.

    Returns:
    - 204: Successfully unenrolled.
    - 404: If student or course does not exist.
    """

    # Validate existence of student
    student = db.query(Student).filter(Student.id == unenroll_request.student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate existence of course
    course = db.query(Course).filter(Course.id == unenroll_request.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")

    # Remove the relationship record
    record = db.query(StudentCourse).filter(
        StudentCourse.student_id == unenroll_request.student_id,
        StudentCourse.course_id == unenroll_request.course_id
    ).first()

    if not record:
        raise HTTPException(status_code=404, detail="Enrollment record not found")

    db.delete(record)
    db.commit()  # Commit the transaction
    return None  # Return 204 No Content on successful unenrollment