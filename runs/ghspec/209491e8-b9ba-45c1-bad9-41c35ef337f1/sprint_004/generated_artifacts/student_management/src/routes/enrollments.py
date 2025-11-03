from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/students/{student_id}/courses", response_model=schemas.Course)
def enroll_student_in_course(student_id: int, course: schemas.CourseCreate, db: Session = Depends(get_db)):
    """
    Enroll a student in a course.

    Parameters:
    - student_id: The ID of the student to enroll.
    - course: The course details from the request body.

    Returns:
    - The created Course object with the enrollment details.

    Raises:
    - HTTPException: If the student or course does not exist.
    """
    # Validate if the student exists
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Validate if the course exists
    course_from_db = db.query(models.Course).filter(models.Course.id == course.id).first()
    if not course_from_db:
        raise HTTPException(status_code=404, detail="Course not found")

    # Create an enrollment record in the join table
    enrollment = models.StudentCourse(student_id=student_id, course_id=course.id)
    db.add(enrollment)
    db.commit()
    db.refresh(enrollment)

    return course_from_db

@router.get("/students/{student_id}/courses", response_model=List[schemas.Course])
def get_enrolled_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the list of courses a student is enrolled in.

    Parameters:
    - student_id: The ID of the student.

    Returns:
    - A list of Course objects the student is enrolled in.

    Raises:
    - HTTPException: If the student does not exist.
    """
    # Validate if the student exists
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Fetch the courses for the student
    courses = db.query(models.Course).join(models.StudentCourse).filter(models.StudentCourse.student_id == student_id).all()
    return courses
