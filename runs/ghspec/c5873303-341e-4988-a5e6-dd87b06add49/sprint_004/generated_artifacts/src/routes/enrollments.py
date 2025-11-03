from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter()

@router.post("/students/{student_id}/enroll", response_model=schemas.EnrollmentResponse)
def enroll_student_in_courses(student_id: int, enrollment_request: schemas.EnrollmentRequest, db: Session = Depends(get_db)):
    """
    Enroll a student in multiple courses.

    Parameters:
    - student_id: The ID of the student.
    - enrollment_request: Contains the list of course IDs for enrollment.

    Returns:
    - EnrollmentResponse: Confirmation of successful enrollment.
    """
    # Verify that the student exists
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    # Verify valid courses and enroll the student
    invalid_courses = []
    for course_id in enrollment_request.course_ids:
        course = db.query(models.Course).filter(models.Course.id == course_id).first()
        if course:
            # Add the enrollment
            student_course = models.StudentCourse(student_id=student_id, course_id=course_id)
            db.add(student_course)
        else:
            invalid_courses.append(course_id)

    db.commit()

    if invalid_courses:
        raise HTTPException(status_code=400, detail={"error": "Invalid courses", "invalid_ids": invalid_courses})

    return {"message": "Student enrolled successfully", "enrollment_status": enrollment_request.course_ids}

@router.get("/students/{student_id}/courses", response_model=List[schemas.CourseResponse])
def get_student_courses(student_id: int, db: Session = Depends(get_db)):
    """
    Retrieve the courses that a student is enrolled in.

    Parameters:
    - student_id: The ID of the student.

    Returns:
    - List[CourseResponse]: A list of courses the student is enrolled in.
    """
    student = db.query(models.Student).filter(models.Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    enrolled_courses = db.query(models.Course).join(models.StudentCourse).filter(models.StudentCourse.student_id == student_id).all()

    return enrolled_courses